# nuvolos_client_api.LFSV1Api

All URIs are relative to *https://api.eu1.nuvolos.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cleanup_lfs_share**](LFSV1Api.md#cleanup_lfs_share) | **POST** /lfs/v1/org/{org_slug}/space/{space_slug}/shares/{afsid}/cleanup | 
[**list_lfs_shares**](LFSV1Api.md#list_lfs_shares) | **GET** /lfs/v1/org/{org_slug}/space/{space_slug}/shares | 


# **cleanup_lfs_share**
> Task cleanup_lfs_share(org_slug, space_slug, afsid)

Remove incomplete multipart uploads to an LFS

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.task import Task
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
    api_instance = nuvolos_client_api.LFSV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    afsid = 56 # int | 

    try:
        api_response = api_instance.cleanup_lfs_share(org_slug, space_slug, afsid)
        print("The response of LFSV1Api->cleanup_lfs_share:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LFSV1Api->cleanup_lfs_share: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **afsid** | **int**|  | 

### Return type

[**Task**](Task.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Cleanup task accepted |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**404** | Nuvolos object not found |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_lfs_shares**
> List[LFSShare] list_lfs_shares(org_slug, space_slug)

List active LFS shares attached to a space.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.lfs_share import LFSShare
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
    api_instance = nuvolos_client_api.LFSV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 

    try:
        api_response = api_instance.list_lfs_shares(org_slug, space_slug)
        print("The response of LFSV1Api->list_lfs_shares:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LFSV1Api->list_lfs_shares: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 

### Return type

[**List[LFSShare]**](LFSShare.md)

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

