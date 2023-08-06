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

from decentro_in_kyc_client.model.check_photocopy_response import CheckPhotocopyResponse as CheckPhotocopyResponseSchema
from decentro_in_kyc_client.model.check_photocopy400_response import CheckPhotocopy400Response as CheckPhotocopy400ResponseSchema
from decentro_in_kyc_client.model.check_photocopy_request import CheckPhotocopyRequest as CheckPhotocopyRequestSchema

from decentro_in_kyc_client.type.check_photocopy400_response import CheckPhotocopy400Response
from decentro_in_kyc_client.type.check_photocopy_request import CheckPhotocopyRequest
from decentro_in_kyc_client.type.check_photocopy_response import CheckPhotocopyResponse

# body param
SchemaForRequestBodyMultipartFormData = CheckPhotocopyRequestSchema


request_body_check_photocopy_request = api_client.RequestBody(
    content={
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
    },
    required=True,
)
ContentLengthSchema = schemas.IntSchema
ConnectionSchema = schemas.StrSchema
DateSchema = schemas.StrSchema
XDECENTROURNSchema = schemas.StrSchema
ExpectCTSchema = schemas.StrSchema
XPermittedCrossDomainPoliciesSchema = schemas.StrSchema
XFrameOptionsSchema = schemas.StrSchema
XXSSProtectionSchema = schemas.StrSchema
XContentTypeOptionsSchema = schemas.StrSchema
ContentSecurityPolicySchema = schemas.StrSchema
XContentSecurityPolicySchema = schemas.StrSchema
StrictTransportSecuritySchema = schemas.StrSchema
ReferrerPolicySchema = schemas.StrSchema
VarySchema = schemas.StrSchema
SchemaFor200ResponseBodyApplicationJson = CheckPhotocopyResponseSchema
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
    body: CheckPhotocopyResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CheckPhotocopyResponse


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
SchemaFor400ResponseBodyApplicationJson = CheckPhotocopy400ResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: CheckPhotocopy400Response


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: CheckPhotocopy400Response


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _check_photocopy_mapped_args(
        self,
        body: typing.Optional[CheckPhotocopyRequest] = None,
        reference_id: typing.Optional[str] = None,
        consent: typing.Optional[bool] = None,
        consent_purpose: typing.Optional[str] = None,
        image: typing.Optional[typing.IO] = None,
        image_url: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        query_params = {}
        header_params = {}
        path_params = {}
        cookie_params = {}
        _body = {}
        if reference_id is not None:
            _body["reference_id"] = reference_id
        if consent is not None:
            _body["consent"] = consent
        if consent_purpose is not None:
            _body["consent_purpose"] = consent_purpose
        if image is not None:
            _body["image"] = image
        if image_url is not None:
            _body["image_url"] = image_url
        args.body = body if body is not None else _body
        args.query = query_params
        args.header = header_params
        args.path = path_params
        args.cookie = cookie_params
        return args

    async def _acheck_photocopy_oapg(
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
        Photocopy Check
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
        serialized_data = request_body_check_photocopy_request.serialize(body, content_type)
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

    def _check_photocopy_oapg(
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
        Photocopy Check
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
        serialized_data = request_body_check_photocopy_request.serialize(body, content_type)
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

class CheckPhotocopy(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acheck_photocopy(
        self,
        body: typing.Optional[CheckPhotocopyRequest] = None,
        reference_id: typing.Optional[str] = None,
        consent: typing.Optional[bool] = None,
        consent_purpose: typing.Optional[str] = None,
        image: typing.Optional[typing.IO] = None,
        image_url: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._check_photocopy_mapped_args(
            body=body,
            reference_id=reference_id,
            consent=consent,
            consent_purpose=consent_purpose,
            image=image,
            image_url=image_url,
        )
        return await self._acheck_photocopy_oapg(
            body=args.body,
        )
    
    def check_photocopy(
        self,
        body: typing.Optional[CheckPhotocopyRequest] = None,
        reference_id: typing.Optional[str] = None,
        consent: typing.Optional[bool] = None,
        consent_purpose: typing.Optional[str] = None,
        image: typing.Optional[typing.IO] = None,
        image_url: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._check_photocopy_mapped_args(
            body=body,
            reference_id=reference_id,
            consent=consent,
            consent_purpose=consent_purpose,
            image=image,
            image_url=image_url,
        )
        return self._check_photocopy_oapg(
            body=args.body,
        )

class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        body: typing.Optional[CheckPhotocopyRequest] = None,
        reference_id: typing.Optional[str] = None,
        consent: typing.Optional[bool] = None,
        consent_purpose: typing.Optional[str] = None,
        image: typing.Optional[typing.IO] = None,
        image_url: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._check_photocopy_mapped_args(
            body=body,
            reference_id=reference_id,
            consent=consent,
            consent_purpose=consent_purpose,
            image=image,
            image_url=image_url,
        )
        return await self._acheck_photocopy_oapg(
            body=args.body,
        )
    
    def post(
        self,
        body: typing.Optional[CheckPhotocopyRequest] = None,
        reference_id: typing.Optional[str] = None,
        consent: typing.Optional[bool] = None,
        consent_purpose: typing.Optional[str] = None,
        image: typing.Optional[typing.IO] = None,
        image_url: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._check_photocopy_mapped_args(
            body=body,
            reference_id=reference_id,
            consent=consent,
            consent_purpose=consent_purpose,
            image=image,
            image_url=image_url,
        )
        return self._check_photocopy_oapg(
            body=args.body,
        )

