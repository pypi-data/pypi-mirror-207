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


RequiredClassifyDocumentRequest = TypedDict("RequiredClassifyDocumentRequest", {
    "reference_id": str,

    "document_type": str,

    "consent": bool,

    "consent_purpose": str,
    })

OptionalClassifyDocumentRequest = TypedDict("OptionalClassifyDocumentRequest", {
    "document": typing.IO,

    "document_url": str,
    }, total=False)

class ClassifyDocumentRequest(RequiredClassifyDocumentRequest, OptionalClassifyDocumentRequest):
    pass
