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


RequiredCheckVideoLivenessRequest = TypedDict("RequiredCheckVideoLivenessRequest", {
    "reference_id": str,

    "consent": str,

    "consent_purpose": str,
    })

OptionalCheckVideoLivenessRequest = TypedDict("OptionalCheckVideoLivenessRequest", {
    "video": typing.IO,

    "video_url": str,
    }, total=False)

class CheckVideoLivenessRequest(RequiredCheckVideoLivenessRequest, OptionalCheckVideoLivenessRequest):
    pass
