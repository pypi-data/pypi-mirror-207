# coding: utf-8

"""
    decentro-in-kyc

    KYC & Onboarding

    The version of the OpenAPI document: 1.0.0
    Contact: admin@decentro.tech
    Created by: https://decentro.tech
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal


RequiredExtractTextResponse = TypedDict("RequiredExtractTextResponse", {
    })

OptionalExtractTextResponse = TypedDict("OptionalExtractTextResponse", {
    "ocrStatus": str,

    "status": str,

    "message": str,

    "ocrResult": typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],

    "responseCode": str,

    "requestTimestamp": str,

    "responseTimestamp": str,

    "decentroTxnId": str,
    }, total=False)

class ExtractTextResponse(RequiredExtractTextResponse, OptionalExtractTextResponse):
    pass
