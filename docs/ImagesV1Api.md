# nuvolos_client_api.ImagesV1Api

All URIs are relative to *https://api.eu1.nuvolos.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_image**](ImagesV1Api.md#create_image) | **PUT** /images/v1 | 
[**get_images**](ImagesV1Api.md#get_images) | **GET** /images/v1 | 
[**update_image**](ImagesV1Api.md#update_image) | **PATCH** /images/v1/{imid} | 


# **create_image**
> ImageResponse create_image(image_create=image_create)

Creates a new image record along with image_link and image_family_link records. org_slug and space_slug can be omitted only for account managers (globally available image). If both are specified, the space must belong to the org and the user must be a Space Admin. If only org_slug is specified, the user must be an Org Admin for that org.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.image_create import ImageCreate
from nuvolos_client_api.models.image_response import ImageResponse
from nuvolos_client_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.eu1.nuvolos.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = nuvolos_client_api.Configuration(
    host = "https://api.eu1.nuvolos.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with nuvolos_client_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuvolos_client_api.ImagesV1Api(api_client)
    image_create = nuvolos_client_api.ImageCreate() # ImageCreate |  (optional)

    try:
        api_response = api_instance.create_image(image_create=image_create)
        print("The response of ImagesV1Api->create_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesV1Api->create_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_create** | [**ImageCreate**](ImageCreate.md)|  | [optional] 

### Return type

[**ImageResponse**](ImageResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Image created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**404** | Nuvolos object not found |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images**
> List[Image] get_images()

Lists image records accessible to the authenticated user.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.image import Image
from nuvolos_client_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.eu1.nuvolos.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = nuvolos_client_api.Configuration(
    host = "https://api.eu1.nuvolos.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with nuvolos_client_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuvolos_client_api.ImagesV1Api(api_client)

    try:
        api_response = api_instance.get_images()
        print("The response of ImagesV1Api->get_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesV1Api->get_images: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Image]**](Image.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation succeeded |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**404** | Nuvolos object not found |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_image**
> Image update_image(imid, image_update=image_update)

Updates fields of an existing image record accessible to the authenticated user. All fields are optional; only provided fields are updated. release_date is always set to the current date on a successful update. Updatable fields: name, description, docker_image_url, configuration, app_type, description_md, complexity, tags, public, public_description.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.image import Image
from nuvolos_client_api.models.image_update import ImageUpdate
from nuvolos_client_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.eu1.nuvolos.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = nuvolos_client_api.Configuration(
    host = "https://api.eu1.nuvolos.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with nuvolos_client_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuvolos_client_api.ImagesV1Api(api_client)
    imid = 56 # int | 
    image_update = nuvolos_client_api.ImageUpdate() # ImageUpdate |  (optional)

    try:
        api_response = api_instance.update_image(imid, image_update=image_update)
        print("The response of ImagesV1Api->update_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesV1Api->update_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imid** | **int**|  | 
 **image_update** | [**ImageUpdate**](ImageUpdate.md)|  | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image updated |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**404** | Nuvolos object not found |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

