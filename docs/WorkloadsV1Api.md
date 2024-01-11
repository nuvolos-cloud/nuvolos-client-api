# nuvolos_client_api.WorkloadsV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workload**](WorkloadsV1Api.md#create_workload) | **POST** /workloads/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/app/{app_slug} | 
[**delete_workload_options**](WorkloadsV1Api.md#delete_workload_options) | **OPTIONS** /workloads/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/app/{app_slug} | 
[**get_workloads**](WorkloadsV1Api.md#get_workloads) | **GET** /workloads/v1 | 
[**get_workloads_options**](WorkloadsV1Api.md#get_workloads_options) | **OPTIONS** /workloads/v1 | 
[**stop_workload**](WorkloadsV1Api.md#stop_workload) | **DELETE** /workloads/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/app/{app_slug} | 


# **create_workload**
> Task create_workload(org_slug, space_slug, instance_slug, app_slug, body=body)



Creates a new workload by starting a Nuvolos application.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import nuvolos_client_api
from nuvolos_client_api.models.start_app import StartApp
from nuvolos_client_api.models.task import Task
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
    api_instance = nuvolos_client_api.WorkloadsV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    app_slug = 'app_slug_example' # str | 
    body = nuvolos_client_api.StartApp() # StartApp |  (optional)

    try:
        api_response = api_instance.create_workload(org_slug, space_slug, instance_slug, app_slug, body=body)
        print("The response of WorkloadsV1Api->create_workload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkloadsV1Api->create_workload: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **instance_slug** | **str**|  | 
 **app_slug** | **str**|  | 
 **body** | [**StartApp**](StartApp.md)|  | [optional] 

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
**202** | Request accepted |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**404** | Nuvolos object not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workload_options**
> delete_workload_options(org_slug, space_slug, instance_slug, app_slug)



Deletes a workload by stopping a Nuvolos application.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import nuvolos_client_api
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
    api_instance = nuvolos_client_api.WorkloadsV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    app_slug = 'app_slug_example' # str | 

    try:
        api_instance.delete_workload_options(org_slug, space_slug, instance_slug, app_slug)
    except Exception as e:
        print("Exception when calling WorkloadsV1Api->delete_workload_options: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **instance_slug** | **str**|  | 
 **app_slug** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deletion succeeded |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**404** | Nuvolos object not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workloads**
> List[WorkloadDetailed] get_workloads()



Returns the workloads currently run by the user.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import nuvolos_client_api
from nuvolos_client_api.models.workload_detailed import WorkloadDetailed
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
    api_instance = nuvolos_client_api.WorkloadsV1Api(api_client)

    try:
        api_response = api_instance.get_workloads()
        print("The response of WorkloadsV1Api->get_workloads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkloadsV1Api->get_workloads: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[WorkloadDetailed]**](WorkloadDetailed.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workloads_options**
> List[WorkloadDetailed] get_workloads_options()



Returns the workloads currently run by the user.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import nuvolos_client_api
from nuvolos_client_api.models.workload_detailed import WorkloadDetailed
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
    api_instance = nuvolos_client_api.WorkloadsV1Api(api_client)

    try:
        api_response = api_instance.get_workloads_options()
        print("The response of WorkloadsV1Api->get_workloads_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkloadsV1Api->get_workloads_options: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[WorkloadDetailed]**](WorkloadDetailed.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_workload**
> stop_workload(org_slug, space_slug, instance_slug, app_slug)



Deletes a workload by stopping a Nuvolos application.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import nuvolos_client_api
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
    api_instance = nuvolos_client_api.WorkloadsV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    app_slug = 'app_slug_example' # str | 

    try:
        api_instance.stop_workload(org_slug, space_slug, instance_slug, app_slug)
    except Exception as e:
        print("Exception when calling WorkloadsV1Api->stop_workload: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **instance_slug** | **str**|  | 
 **app_slug** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deletion succeeded |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**404** | Nuvolos object not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

