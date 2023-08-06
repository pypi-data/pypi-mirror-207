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


RequiredCheckPhotocopyRequest = TypedDict("RequiredCheckPhotocopyRequest", {
    "reference_id": str,

    "consent": bool,

    "consent_purpose": str,
    })

OptionalCheckPhotocopyRequest = TypedDict("OptionalCheckPhotocopyRequest", {
    "image": typing.IO,

    "image_url": str,
    }, total=False)

class CheckPhotocopyRequest(RequiredCheckPhotocopyRequest, OptionalCheckPhotocopyRequest):
    pass
