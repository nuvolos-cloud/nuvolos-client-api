# nuvolos_client_api.AppsV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_apps**](AppsV1Api.md#get_apps) | **GET** /apps/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/snapshot/{snapshot_slug} | 


# **get_apps**
> List[Application] get_apps(snapshot_slug, space_slug, instance_slug, org_slug)



Returns the apps in the given snapshot.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import nuvolos_client_api
from nuvolos_client_api.models.application import Application
from nuvolos_client_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = nuvolos_client_api.Configuration(
    host = "http://localhost"
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
    api_instance = nuvolos_client_api.AppsV1Api(api_client)
    snapshot_slug = 'snapshot_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    org_slug = 'org_slug_example' # str | 

    try:
        api_response = api_instance.get_apps(snapshot_slug, space_slug, instance_slug, org_slug)
        print("The response of AppsV1Api->get_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsV1Api->get_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **instance_slug** | **str**|  | 
 **org_slug** | **str**|  | 

### Return type

[**List[Application]**](Application.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**500** | Internal server error |  -  |
**404** | Nuvolos object not found |  -  |
**200** | Operation succeeded |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

