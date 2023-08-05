"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from typing import Optional
from vesselapi.models import operations

class Connections:
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
        
    
    def delete(self, request: operations.DeleteConnectionRequestBody, security: operations.DeleteConnectionSecurity) -> operations.DeleteConnectionResponse:
        r"""Delete Connection
        Remove a connection for a given `connectionId`. Removing a connection disconnects the user's CRM so they'll need to re-authenticate should they want to re-connect their CRM.
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/connection/connection'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('DELETE', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteConnectionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    
    def find(self, request: operations.GetOneConnectionRequest) -> operations.GetOneConnectionResponse:
        r"""Get Connection
        Get info about a connection for a given accessToken.
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/connection/connection'
        
        query_params = utils.get_query_params(operations.GetOneConnectionRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOneConnectionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetOneConnectionResponseBody])
                res.response_body = out

        return res

    
    def list(self) -> operations.GetAllCrmConnectionsResponse:
        r"""Get All Connections
        List all established connections for a workspace
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/connection/connections'
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAllCrmConnectionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetAllCrmConnectionsResponseBody])
                res.response_body = out

        return res

    