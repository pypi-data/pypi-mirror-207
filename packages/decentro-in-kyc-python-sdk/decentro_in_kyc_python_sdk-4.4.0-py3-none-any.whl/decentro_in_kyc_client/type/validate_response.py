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


RequiredValidateResponse = TypedDict("RequiredValidateResponse", {
    })

OptionalValidateResponse = TypedDict("OptionalValidateResponse", {
    "kycStatus": str,

    "status": str,

    "message": str,

    "kycResult": typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],

    "responseCode": str,

    "requestTimestamp": str,

    "responseTimestamp": str,

    "decentroTxnId": str,

    "error": typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],
    }, total=False)

class ValidateResponse(RequiredValidateResponse, OptionalValidateResponse):
    pass
