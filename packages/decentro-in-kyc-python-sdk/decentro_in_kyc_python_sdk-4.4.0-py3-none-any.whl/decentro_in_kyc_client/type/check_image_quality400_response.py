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


RequiredCheckImageQuality400Response = TypedDict("RequiredCheckImageQuality400Response", {
    })

OptionalCheckImageQuality400Response = TypedDict("OptionalCheckImageQuality400Response", {
    "decentroTxnId": str,

    "status": str,

    "responseCode": str,

    "message": str,
    }, total=False)

class CheckImageQuality400Response(RequiredCheckImageQuality400Response, OptionalCheckImageQuality400Response):
    pass
