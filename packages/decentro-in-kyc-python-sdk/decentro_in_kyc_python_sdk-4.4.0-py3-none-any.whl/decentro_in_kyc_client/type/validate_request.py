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


RequiredValidateRequest = TypedDict("RequiredValidateRequest", {
    "reference_id": str,

    "document_type": str,

    "id_number": str,

    "consent": str,

    "consent_purpose": str,
    })

OptionalValidateRequest = TypedDict("OptionalValidateRequest", {
    "dob": str,

    "name": str,
    }, total=False)

class ValidateRequest(RequiredValidateRequest, OptionalValidateRequest):
    pass
