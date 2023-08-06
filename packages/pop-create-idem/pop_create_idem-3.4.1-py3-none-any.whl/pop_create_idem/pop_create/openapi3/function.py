"""Parse function related data from swagger"""
from typing import Any
from typing import Dict

import openapi3


def parse(
    hub,
    ctx,
    request_type: str,
    path: str,
    resource_name: str,
    func: openapi3.paths.Operation,
    all_schemas: dict,
) -> Dict[str, Any]:
    params = {}

    # Parse all query, path, header parameters
    for p in func.parameters:
        params[p.name] = hub.pop_create.openapi3.params.parse_non_schema_members(p)

    # Parse request body if available
    (
        request_body_params,
        request_mappings,
    ) = hub.pop_create.openapi3.function.parse_request_body(func, all_schemas)
    params.update(request_body_params)

    if "name" in params:
        # The template already adds name by default
        params.pop("name")

    deprecated_text = "\nDEPRECATED" if func.deprecated else ""

    return {
        "doc": f"{func.summary}\n    {func.description}    {deprecated_text}".strip(),
        "params": params,
        "hardcoded": {
            "method": request_type,
            "path": path.split(" ")[0],
            "service_name": ctx.service_name,
            "resource_name": resource_name,
            "request_mappings": request_mappings,
            "response_mappings": hub.pop_create.openapi3.function.parse_response_mappings(
                func, all_schemas
            ),
        },
    }


def parse_request_body(
    hub,
    func: openapi3.paths.Operation,
    all_schemas: dict,
):
    # Usually put, post, patch should have request_body
    request_body_params = {}
    request_mappings = ""
    request_body: openapi3.paths.RequestBody = func.requestBody
    try:
        if request_body:
            # application/json is preferable always
            # An example would be ->
            #   "application/json": {
            #       "schema": {
            #         "$ref": "#/components/schemas/User"
            #       }
            #   }
            schema = request_body.content.raw_element.get("application/json")
            if not schema:
                # Take the first one for now
                # e.g. #/components/schemas/StoreOrder
                schema = list(request_body.content.raw_element.values()).pop()

            schema_ref = schema.get("schema", {}).get("$ref")
            hub.pop_create.openapi3.params.parse_schema_members(
                request_body_params, schema_ref, all_schemas
            )

            request_mappings = (
                hub.pop_create.openapi3.params.parse_resource_to_request_input_mappings(
                    schema_ref, all_schemas
                )
            )
    except Exception as e:
        hub.log.debug(f"Failed to parse request body: {e.__class__.__name__}: {e}")

    return request_body_params, request_mappings


def parse_response_mappings(
    hub,
    func: openapi3.paths.Operation,
    all_schemas: dict,
):
    responses: openapi3.paths.Response = func.responses
    response_mappings = {}
    try:
        if responses:
            for status, response in responses.raw_element.items():
                # For now, we support 200 only for mapping into "present" format
                if status == "200" and "content" in response:
                    schema = response.get("content", {}).get("application/json")
                    if not schema:
                        # Take the first one for now
                        schema = list(response.get("content", {}).values()).pop()

                    schema_ref = schema.get("schema", {}).get("$ref")

                    response_mappings = (
                        hub.pop_create.openapi3.params.parse_response_mappings(
                            schema_ref, all_schemas
                        )
                    )
    except Exception as e:
        hub.log.debug(f"Failed to parse response mapping: {e.__class__.__name__}: {e}")

    return response_mappings
