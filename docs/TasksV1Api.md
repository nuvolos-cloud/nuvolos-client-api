# nuvolos_client_api.TasksV1Api

All URIs are relative to *https://api.nuvolos.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_task**](TasksV1Api.md#get_task) | **GET** /tasks/v1/{tkid} | 


# **get_task**
> Task1 get_task(tkid)

Returns the task object with the specified id. Only callable by the task submitter.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.task1 import Task1
from nuvolos_client_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nuvolos.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = nuvolos_client_api.Configuration(
    host = "https://api.nuvolos.cloud"
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
    api_instance = nuvolos_client_api.TasksV1Api(api_client)
    tkid = 56 # int | 

    try:
        api_response = api_instance.get_task(tkid)
        print("The response of TasksV1Api->get_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksV1Api->get_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tkid** | **int**|  | 

### Return type

[**Task1**](Task1.md)

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
**403** | Access to Nuvolos resource is forbidden |  -  |
**404** | Nuvolos object not found |  -  |
**408** | Request Timeout - task not finished yet and only_finished&#x3D;true was specified |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |
**418** | I&#39;m a teapot - task failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

