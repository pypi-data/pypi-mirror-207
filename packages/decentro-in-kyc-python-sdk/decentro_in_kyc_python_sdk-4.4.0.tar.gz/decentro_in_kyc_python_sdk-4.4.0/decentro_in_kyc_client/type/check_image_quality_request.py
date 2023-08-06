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


RequiredCheckImageQualityRequest = TypedDict("RequiredCheckImageQualityRequest", {
    "reference_id": str,

    "consent": bool,

    "consent_purpose": str,
    })

OptionalCheckImageQualityRequest = TypedDict("OptionalCheckImageQualityRequest", {
    "image": typing.IO,

    "quality_parameter": str,

    "image_url": str,
    }, total=False)

class CheckImageQualityRequest(RequiredCheckImageQualityRequest, OptionalCheckImageQualityRequest):
    pass
