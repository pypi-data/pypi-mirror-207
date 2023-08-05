"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from speakeasy.models import operations, shared
from typing import Optional

class APIEndpoints:
    r"""REST APIs for managing ApiEndpoint entities"""
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    
    def delete_api_endpoint(self, request: operations.DeleteAPIEndpointRequest) -> operations.DeleteAPIEndpointResponse:
        r"""Delete an ApiEndpoint.
        Delete an ApiEndpoint. This will also delete all associated Request Logs (if using a Postgres datastore).
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteAPIEndpointRequest, base_url, '/v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID}', request)
        
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteAPIEndpointResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    
    def find_api_endpoint(self, request: operations.FindAPIEndpointRequest) -> operations.FindAPIEndpointResponse:
        r"""Find an ApiEndpoint via its displayName.
        Find an ApiEndpoint via its displayName (set by operationId from a registered OpenAPI schema).
        This is useful for finding the ID of an ApiEndpoint to use in the /v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID} endpoints.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.FindAPIEndpointRequest, base_url, '/v1/apis/{apiID}/version/{versionID}/api_endpoints/find/{displayName}', request)
        
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.FindAPIEndpointResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIEndpoint])
                res.api_endpoint = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    
    def generate_open_api_spec_for_api_endpoint(self, request: operations.GenerateOpenAPISpecForAPIEndpointRequest) -> operations.GenerateOpenAPISpecForAPIEndpointResponse:
        r"""Generate an OpenAPI specification for a particular ApiEndpoint.
        This endpoint will generate a new operation in any registered OpenAPI document if the operation does not already exist in the document.
        Returns the original document and the newly generated document allowing a diff to be performed to see what has changed.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GenerateOpenAPISpecForAPIEndpointRequest, base_url, '/v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID}/generate/openapi', request)
        
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GenerateOpenAPISpecForAPIEndpointResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GenerateOpenAPISpecDiff])
                res.generate_open_api_spec_diff = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    
    def generate_postman_collection_for_api_endpoint(self, request: operations.GeneratePostmanCollectionForAPIEndpointRequest) -> operations.GeneratePostmanCollectionForAPIEndpointResponse:
        r"""Generate a Postman collection for a particular ApiEndpoint.
        Generates a postman collection that allows the endpoint to be called from postman variables produced for any path/query/header parameters included in the OpenAPI document.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GeneratePostmanCollectionForAPIEndpointRequest, base_url, '/v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID}/generate/postman', request)
        
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GeneratePostmanCollectionForAPIEndpointResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/octet-stream'):
                res.postman_collection = http_res.content
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_all_api_endpoints(self, request: operations.GetAllAPIEndpointsRequest) -> operations.GetAllAPIEndpointsResponse:
        r"""Get all Api endpoints for a particular apiID."""
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetAllAPIEndpointsRequest, base_url, '/v1/apis/{apiID}/api_endpoints', request)
        
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAllAPIEndpointsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.APIEndpoint]])
                res.api_endpoints = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_all_for_version_api_endpoints(self, request: operations.GetAllForVersionAPIEndpointsRequest) -> operations.GetAllForVersionAPIEndpointsResponse:
        r"""Get all ApiEndpoints for a particular apiID and versionID."""
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetAllForVersionAPIEndpointsRequest, base_url, '/v1/apis/{apiID}/version/{versionID}/api_endpoints', request)
        
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAllForVersionAPIEndpointsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.APIEndpoint]])
                res.api_endpoints = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    
    def get_api_endpoint(self, request: operations.GetAPIEndpointRequest) -> operations.GetAPIEndpointResponse:
        r"""Get an ApiEndpoint."""
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetAPIEndpointRequest, base_url, '/v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID}', request)
        
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAPIEndpointResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIEndpoint])
                res.api_endpoint = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    
    def upsert_api_endpoint(self, request: operations.UpsertAPIEndpointRequest) -> operations.UpsertAPIEndpointResponse:
        r"""Upsert an ApiEndpoint.
        Upsert an ApiEndpoint. If the ApiEndpoint does not exist it will be created, otherwise it will be updated.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpsertAPIEndpointRequest, base_url, '/v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID}', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "api_endpoint_input", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpsertAPIEndpointResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIEndpoint])
                res.api_endpoint = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Error])
                res.error = out

        return res

    