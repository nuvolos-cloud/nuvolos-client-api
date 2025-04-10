# nuvolos_client_api.SpacesV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_spaces**](SpacesV1Api.md#get_spaces) | **GET** /spaces/v1/org/{slug} | 


# **get_spaces**
> List[Space] get_spaces(slug)

Returns the spaces the user is affiliated with in the selected org. 

### Example


```python
import nuvolos_client_api
from nuvolos_client_api.models.space import Space
from nuvolos_client_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = nuvolos_client_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with nuvolos_client_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuvolos_client_api.SpacesV1Api(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.get_spaces(slug)
        print("The response of SpacesV1Api->get_spaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpacesV1Api->get_spaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**List[Space]**](Space.md)

### Authorization

No authorization required

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

