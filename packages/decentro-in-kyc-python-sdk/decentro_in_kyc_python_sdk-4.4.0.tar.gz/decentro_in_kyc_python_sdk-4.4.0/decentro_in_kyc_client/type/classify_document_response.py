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


RequiredClassifyDocumentResponse = TypedDict("RequiredClassifyDocumentResponse", {
    })

OptionalClassifyDocumentResponse = TypedDict("OptionalClassifyDocumentResponse", {
    "data": typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],

    "decentroTxnId": str,

    "message": str,

    "responseCode": str,

    "status": str,
    }, total=False)

class ClassifyDocumentResponse(RequiredClassifyDocumentResponse, OptionalClassifyDocumentResponse):
    pass
