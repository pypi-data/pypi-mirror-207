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


RequiredExtractText400Response = TypedDict("RequiredExtractText400Response", {
    })

OptionalExtractText400Response = TypedDict("OptionalExtractText400Response", {
    "status": str,

    "ocrStatus": str,

    "kycStatus": str,

    "error": typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],

    "requestTimestamp": str,

    "responseTimestamp": str,

    "decentroTxnId": str,
    }, total=False)

class ExtractText400Response(RequiredExtractText400Response, OptionalExtractText400Response):
    pass
