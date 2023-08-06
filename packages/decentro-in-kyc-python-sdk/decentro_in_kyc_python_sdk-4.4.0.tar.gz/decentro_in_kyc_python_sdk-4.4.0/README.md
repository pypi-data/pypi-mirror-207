# decentro-in-kyc-python-sdk@4.4.0
KYC & Onboarding


## Requirements

Python >=3.7

## Installing

```sh
pip install decentro-in-kyc-python-sdk==4.4.0
```

## Getting Started

```python
from pprint import pprint
from decentro_in_kyc_client import Decentro, ApiException

decentro = Decentro(
    # Defining the host is optional and defaults to https://in.staging.decentro.tech
    # See configuration.py for a list of all supported configuration parameters.
    host="https://in.staging.decentro.tech",
    # Configure API key authorization: client_id
    client_id="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'client_id': 'Bearer'},
    # Configure API key authorization: client_secret
    client_secret="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'client_secret': 'Bearer'},
    # Configure API key authorization: module_secret
    module_secret="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'module_secret': 'Bearer'},
)

try:
    # Image Quality Check
    check_image_quality_response = decentro.kyc.check_image_quality(
        reference_id="ABCDEF12345",  # required
        consent=False,  # required
        consent_purpose="For Testing Purpose Only",  # required
        image=open("/path/to/file", "rb"),  # optional
        quality_parameter="all",  # optional
        image_url="string_example",  # optional
    )
    pprint(check_image_quality_response.body)
    pprint(check_image_quality_response.body["decentroTxnId"])
    pprint(check_image_quality_response.body["status"])
    pprint(check_image_quality_response.body["responseCode"])
    pprint(check_image_quality_response.body["message"])
    pprint(check_image_quality_response.body["data"])
    pprint(check_image_quality_response.headers)
    pprint(check_image_quality_response.status)
    pprint(check_image_quality_response.round_trip_time)
except ApiException as e:
    print("Exception when calling KYCApi.check_image_quality: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["decentroTxnId"])
        pprint(e.body["status"])
        pprint(e.body["responseCode"])
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Documentation for API Endpoints

All URIs are relative to *https://in.staging.decentro.tech*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*KYCApi* | [**check_image_quality**](docs/apis/tags/KYCApi.md#check_image_quality) | **post** /v2/kyc/forensics/image_quality | Image Quality Check
*KYCApi* | [**check_photocopy**](docs/apis/tags/KYCApi.md#check_photocopy) | **post** /v2/kyc/forensics/photocopy_check | Photocopy Check
*KYCApi* | [**check_video_liveness**](docs/apis/tags/KYCApi.md#check_video_liveness) | **post** /v2/kyc/forensics/video_liveness | Liveness Check
*KYCApi* | [**classify_document**](docs/apis/tags/KYCApi.md#classify_document) | **post** /v2/kyc/document_classification | ID Classification
*KYCApi* | [**extract_text**](docs/apis/tags/KYCApi.md#extract_text) | **post** /kyc/scan_extract/ocr | Scan &amp; Extract
*KYCApi* | [**mask_aadhaar_uid**](docs/apis/tags/KYCApi.md#mask_aadhaar_uid) | **post** /v2/kyc/identities/mask_aadhaar_uid | Aadhaar Masking
*KYCApi* | [**match_face**](docs/apis/tags/KYCApi.md#match_face) | **post** /v2/kyc/forensics/face_match | Face Match
*KYCApi* | [**validate**](docs/apis/tags/KYCApi.md#validate) | **post** /kyc/public_registry/validate | Validate

## Documentation For Models

 - [CheckImageQuality400Response](docs/models/CheckImageQuality400Response.md)
 - [CheckImageQualityRequest](docs/models/CheckImageQualityRequest.md)
 - [CheckImageQualityResponse](docs/models/CheckImageQualityResponse.md)
 - [CheckPhotocopy400Response](docs/models/CheckPhotocopy400Response.md)
 - [CheckPhotocopyRequest](docs/models/CheckPhotocopyRequest.md)
 - [CheckPhotocopyResponse](docs/models/CheckPhotocopyResponse.md)
 - [CheckVideoLiveness400Response](docs/models/CheckVideoLiveness400Response.md)
 - [CheckVideoLivenessRequest](docs/models/CheckVideoLivenessRequest.md)
 - [CheckVideoLivenessResponse](docs/models/CheckVideoLivenessResponse.md)
 - [ClassifyDocument400Response](docs/models/ClassifyDocument400Response.md)
 - [ClassifyDocumentRequest](docs/models/ClassifyDocumentRequest.md)
 - [ClassifyDocumentResponse](docs/models/ClassifyDocumentResponse.md)
 - [ExtractText400Response](docs/models/ExtractText400Response.md)
 - [ExtractTextRequest](docs/models/ExtractTextRequest.md)
 - [ExtractTextResponse](docs/models/ExtractTextResponse.md)
 - [MaskAadhaarRequest](docs/models/MaskAadhaarRequest.md)
 - [MaskAadhaarUid400Response](docs/models/MaskAadhaarUid400Response.md)
 - [MaskAadhaarUidResponse](docs/models/MaskAadhaarUidResponse.md)
 - [MatchFace400Response](docs/models/MatchFace400Response.md)
 - [MatchFaceRequest](docs/models/MatchFaceRequest.md)
 - [MatchFaceResponse](docs/models/MatchFaceResponse.md)
 - [Validate400Response](docs/models/Validate400Response.md)
 - [ValidateRequest](docs/models/ValidateRequest.md)
 - [ValidateResponse](docs/models/ValidateResponse.md)


