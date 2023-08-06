# coding: utf-8

"""
    decentro-in-kyc

    KYC & Onboarding

    The version of the OpenAPI document: 1.0.0
    Contact: admin@decentro.tech
    Created by: https://decentro.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
import json
from urllib3._collections import HTTPHeaderDict

from decentro_in_kyc_client.api_response import AsyncGeneratorResponse
from decentro_in_kyc_client import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from decentro_in_kyc_client import schemas  # noqa: F401

from decentro_in_kyc_client.model.extract_text400_response import ExtractText400Response as ExtractText400ResponseSchema
from decentro_in_kyc_client.model.extract_text_request import ExtractTextRequest as ExtractTextRequestSchema
from decentro_in_kyc_client.model.extract_text_response import ExtractTextResponse as ExtractTextResponseSchema

from decentro_in_kyc_client.type.extract_text400_response import ExtractText400Response
from decentro_in_kyc_client.type.extract_text_response import ExtractTextResponse
from decentro_in_kyc_client.type.extract_text_request import ExtractTextRequest

from . import path

# body param
SchemaForRequestBodyMultipartFormData = ExtractTextRequestSchema


request_body_extract_text_request = api_client.RequestBody(
    content={
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
    },
    required=True,
)
_auth = [
    'client_id',
    'client_secret',
    'module_secret',
]
ContentLengthSchema = schemas.IntSchema
content_length_parameter = api_client.HeaderParameter(
    name="Content-Length",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ContentLengthSchema,
)
ConnectionSchema = schemas.StrSchema
connection_parameter = api_client.HeaderParameter(
    name="Connection",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ConnectionSchema,
)
DateSchema = schemas.StrSchema
date_parameter = api_client.HeaderParameter(
    name="Date",
    style=api_client.ParameterStyle.SIMPLE,
    schema=DateSchema,
)
XDECENTROURNSchema = schemas.StrSchema
x_decentro_urn_parameter = api_client.HeaderParameter(
    name="X-DECENTRO-URN",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XDECENTROURNSchema,
)
ExpectCTSchema = schemas.StrSchema
expect_ct_parameter = api_client.HeaderParameter(
    name="Expect-CT",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ExpectCTSchema,
)
XPermittedCrossDomainPoliciesSchema = schemas.StrSchema
x_permitted_cross_domain_policies_parameter = api_client.HeaderParameter(
    name="X-Permitted-Cross-Domain-Policies",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XPermittedCrossDomainPoliciesSchema,
)
XFrameOptionsSchema = schemas.StrSchema
x_frame_options_parameter = api_client.HeaderParameter(
    name="X-Frame-Options",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XFrameOptionsSchema,
)
XXSSProtectionSchema = schemas.StrSchema
x_xss_protection_parameter = api_client.HeaderParameter(
    name="X-XSS-Protection",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XXSSProtectionSchema,
)
XContentTypeOptionsSchema = schemas.StrSchema
x_content_type_options_parameter = api_client.HeaderParameter(
    name="X-Content-Type-Options",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XContentTypeOptionsSchema,
)
ContentSecurityPolicySchema = schemas.StrSchema
content_security_policy_parameter = api_client.HeaderParameter(
    name="Content-Security-Policy",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ContentSecurityPolicySchema,
)
XContentSecurityPolicySchema = schemas.StrSchema
x_content_security_policy_parameter = api_client.HeaderParameter(
    name="X-Content-Security-Policy",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XContentSecurityPolicySchema,
)
StrictTransportSecuritySchema = schemas.StrSchema
strict_transport_security_parameter = api_client.HeaderParameter(
    name="Strict-Transport-Security",
    style=api_client.ParameterStyle.SIMPLE,
    schema=StrictTransportSecuritySchema,
)
ReferrerPolicySchema = schemas.StrSchema
referrer_policy_parameter = api_client.HeaderParameter(
    name="Referrer-Policy",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ReferrerPolicySchema,
)
VarySchema = schemas.StrSchema
vary_parameter = api_client.HeaderParameter(
    name="vary",
    style=api_client.ParameterStyle.SIMPLE,
    schema=VarySchema,
)
SchemaFor200ResponseBodyApplicationJson = ExtractTextResponseSchema
ResponseHeadersFor200 = typing_extensions.TypedDict(
    'ResponseHeadersFor200',
    {
        'Content-Length': ContentLengthSchema,
        'Connection': ConnectionSchema,
        'Date': DateSchema,
        'X-DECENTRO-URN': XDECENTROURNSchema,
        'Expect-CT': ExpectCTSchema,
        'X-Permitted-Cross-Domain-Policies': XPermittedCrossDomainPoliciesSchema,
        'X-Frame-Options': XFrameOptionsSchema,
        'X-XSS-Protection': XXSSProtectionSchema,
        'X-Content-Type-Options': XContentTypeOptionsSchema,
        'Content-Security-Policy': ContentSecurityPolicySchema,
        'X-Content-Security-Policy': XContentSecurityPolicySchema,
        'Strict-Transport-Security': StrictTransportSecuritySchema,
        'Referrer-Policy': ReferrerPolicySchema,
        'vary': VarySchema,
    }
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ExtractTextResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ExtractTextResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
    headers=[
        content_length_parameter,
        connection_parameter,
        date_parameter,
        x_decentro_urn_parameter,
        expect_ct_parameter,
        x_permitted_cross_domain_policies_parameter,
        x_frame_options_parameter,
        x_xss_protection_parameter,
        x_content_type_options_parameter,
        content_security_policy_parameter,
        x_content_security_policy_parameter,
        strict_transport_security_parameter,
        referrer_policy_parameter,
        vary_parameter,
    ]
)
SchemaFor400ResponseBodyApplicationJson = ExtractText400ResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ExtractText400Response


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ExtractText400Response


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _extract_text_mapped_args(
        self,
        body: typing.Optional[ExtractTextRequest] = None,
        reference_id: typing.Optional[str] = None,
        document_type: typing.Optional[str] = None,
        consent: typing.Optional[str] = None,
        consent_purpose: typing.Optional[str] = None,
        kyc_validate: typing.Optional[int] = None,
        document: typing.Optional[typing.IO] = None,
        document_url: typing.Optional[str] = None,
        document_back: typing.Optional[typing.IO] = None,
        document_back_url: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        query_params = {}
        header_params = {}
        path_params = {}
        cookie_params = {}
        _body = {}
        if reference_id is not None:
            _body["reference_id"] = reference_id
        if document_type is not None:
            _body["document_type"] = document_type
        if consent is not None:
            _body["consent"] = consent
        if consent_purpose is not None:
            _body["consent_purpose"] = consent_purpose
        if kyc_validate is not None:
            _body["kyc_validate"] = kyc_validate
        if document is not None:
            _body["document"] = document
        if document_url is not None:
            _body["document_url"] = document_url
        if document_back is not None:
            _body["document_back"] = document_back
        if document_back_url is not None:
            _body["document_back_url"] = document_back_url
        args.body = body if body is not None else _body
        args.query = query_params
        args.header = header_params
        args.path = path_params
        args.cookie = cookie_params
        return args

    async def _aextract_text_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'multipart/form-data',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Scan &amp; Extract
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        serialized_data = request_body_extract_text_request.serialize(body, content_type)
        _headers.add('Content-Type', content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method='post'.upper(),
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
        
        if stream:
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response

    def _extract_text_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'multipart/form-data',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Scan &amp; Extract
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        serialized_data = request_body_extract_text_request.serialize(body, content_type)
        _headers.add('Content-Type', content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']    
        response = self.api_client.call_api(
            resource_path=used_path,
            method='post'.upper(),
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response

class ExtractText(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aextract_text(
        self,
        body: typing.Optional[ExtractTextRequest] = None,
        reference_id: typing.Optional[str] = None,
        document_type: typing.Optional[str] = None,
        consent: typing.Optional[str] = None,
        consent_purpose: typing.Optional[str] = None,
        kyc_validate: typing.Optional[int] = None,
        document: typing.Optional[typing.IO] = None,
        document_url: typing.Optional[str] = None,
        document_back: typing.Optional[typing.IO] = None,
        document_back_url: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._extract_text_mapped_args(
            body=body,
            reference_id=reference_id,
            document_type=document_type,
            consent=consent,
            consent_purpose=consent_purpose,
            kyc_validate=kyc_validate,
            document=document,
            document_url=document_url,
            document_back=document_back,
            document_back_url=document_back_url,
        )
        return await self._aextract_text_oapg(
            body=args.body,
        )
    
    def extract_text(
        self,
        body: typing.Optional[ExtractTextRequest] = None,
        reference_id: typing.Optional[str] = None,
        document_type: typing.Optional[str] = None,
        consent: typing.Optional[str] = None,
        consent_purpose: typing.Optional[str] = None,
        kyc_validate: typing.Optional[int] = None,
        document: typing.Optional[typing.IO] = None,
        document_url: typing.Optional[str] = None,
        document_back: typing.Optional[typing.IO] = None,
        document_back_url: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._extract_text_mapped_args(
            body=body,
            reference_id=reference_id,
            document_type=document_type,
            consent=consent,
            consent_purpose=consent_purpose,
            kyc_validate=kyc_validate,
            document=document,
            document_url=document_url,
            document_back=document_back,
            document_back_url=document_back_url,
        )
        return self._extract_text_oapg(
            body=args.body,
        )

class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        body: typing.Optional[ExtractTextRequest] = None,
        reference_id: typing.Optional[str] = None,
        document_type: typing.Optional[str] = None,
        consent: typing.Optional[str] = None,
        consent_purpose: typing.Optional[str] = None,
        kyc_validate: typing.Optional[int] = None,
        document: typing.Optional[typing.IO] = None,
        document_url: typing.Optional[str] = None,
        document_back: typing.Optional[typing.IO] = None,
        document_back_url: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._extract_text_mapped_args(
            body=body,
            reference_id=reference_id,
            document_type=document_type,
            consent=consent,
            consent_purpose=consent_purpose,
            kyc_validate=kyc_validate,
            document=document,
            document_url=document_url,
            document_back=document_back,
            document_back_url=document_back_url,
        )
        return await self._aextract_text_oapg(
            body=args.body,
        )
    
    def post(
        self,
        body: typing.Optional[ExtractTextRequest] = None,
        reference_id: typing.Optional[str] = None,
        document_type: typing.Optional[str] = None,
        consent: typing.Optional[str] = None,
        consent_purpose: typing.Optional[str] = None,
        kyc_validate: typing.Optional[int] = None,
        document: typing.Optional[typing.IO] = None,
        document_url: typing.Optional[str] = None,
        document_back: typing.Optional[typing.IO] = None,
        document_back_url: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._extract_text_mapped_args(
            body=body,
            reference_id=reference_id,
            document_type=document_type,
            consent=consent,
            consent_purpose=consent_purpose,
            kyc_validate=kyc_validate,
            document=document,
            document_url=document_url,
            document_back=document_back,
            document_back_url=document_back_url,
        )
        return self._extract_text_oapg(
            body=args.body,
        )

