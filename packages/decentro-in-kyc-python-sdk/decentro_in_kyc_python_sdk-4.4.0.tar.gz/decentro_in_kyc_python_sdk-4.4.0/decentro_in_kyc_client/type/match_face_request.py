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


RequiredMatchFaceRequest = TypedDict("RequiredMatchFaceRequest", {
    "reference_id": str,

    "consent": str,

    "consent_purpose": str,
    })

OptionalMatchFaceRequest = TypedDict("OptionalMatchFaceRequest", {
    "image1": typing.IO,

    "image2": typing.IO,

    "threshold": int,

    "image1_url": str,

    "image2_url": str,
    }, total=False)

class MatchFaceRequest(RequiredMatchFaceRequest, OptionalMatchFaceRequest):
    pass
