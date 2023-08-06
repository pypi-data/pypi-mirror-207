# coding: utf-8
"""
    decentro-in-kyc

    KYC & Onboarding

    The version of the OpenAPI document: 1.0.0
    Contact: admin@decentro.tech
    Created by: https://decentro.tech
"""

import typing
import inspect
from datetime import date, datetime
from decentro_in_kyc_client.client_custom import ClientCustom
from decentro_in_kyc_client.configuration import Configuration
from decentro_in_kyc_client.api_client import ApiClient
from decentro_in_kyc_client.type_util import copy_signature
from decentro_in_kyc_client.apis.tags.kyc_api import KYCApi



class Decentro(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.kyc = KYCApi(api_client)
