# nuvolos_client_api.WorkloadsV1Api

All URIs are relative to *https://api.eu1.nuvolos.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workload**](WorkloadsV1Api.md#create_workload) | **POST** /workloads/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/app/{app_slug} | Workloads V1 Start App
[**delete_workload**](WorkloadsV1Api.md#delete_workload) | **DELETE** /workloads/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/app/{app_slug} | Workloads V1 Stop App
[**execute_command**](WorkloadsV1Api.md#execute_command) | **POST** /workloads/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/app/{app_slug}/execute | Workloads V1 Execute Command
[**get_nodepools**](WorkloadsV1Api.md#get_nodepools) | **GET** /workloads/v1/org/{org_slug}/space/{space_slug}/nodepools | Workloads V1 List Nodepools
[**get_workloads**](WorkloadsV1Api.md#get_workloads) | **GET** /workloads/v1 | Workloads V1 List All Running
[**get_workloads_for_app**](WorkloadsV1Api.md#get_workloads_for_app) | **GET** /workloads/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/app/{app_slug} | Workloads V1 List Workloads For App


# **create_workload**
> Task create_workload(org_slug, space_slug, instance_slug, app_slug, start_app=start_app)

Workloads V1 Start App

Creates a new workload by starting a Nuvolos application.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.start_app import StartApp
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
    api_instance = nuvolos_client_api.WorkloadsV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    app_slug = 'app_slug_example' # str | 
    start_app = nuvolos_client_api.StartApp() # StartApp |  (optional)

    try:
        # Workloads V1 Start App
        api_response = api_instance.create_workload(org_slug, space_slug, instance_slug, app_slug, start_app=start_app)
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
 **start_app** | [**StartApp**](StartApp.md)|  | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request accepted |  -  |
**422** | Validation error |  -  |
**404** | Nuvolos object not found |  -  |
**400** | Bad request |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |
**500** | Internal server error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workload**
> delete_workload(org_slug, space_slug, instance_slug, app_slug)

Workloads V1 Stop App

Deletes a workload by stopping a Nuvolos application.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
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
    api_instance = nuvolos_client_api.WorkloadsV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    app_slug = 'app_slug_example' # str | 

    try:
        # Workloads V1 Stop App
        api_instance.delete_workload(org_slug, space_slug, instance_slug, app_slug)
    except Exception as e:
        print("Exception when calling WorkloadsV1Api->delete_workload: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Nuvolos object not found |  -  |
**400** | Bad request |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |
**500** | Internal server error |  -  |
**204** | Deletion succeeded |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_command**
> ExecuteCommandResponse execute_command(org_slug, space_slug, instance_slug, app_slug, execute_command=execute_command)

Workloads V1 Execute Command

Executes a custom command in a selected workload.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.execute_command import ExecuteCommand
from nuvolos_client_api.models.execute_command_response import ExecuteCommandResponse
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
    api_instance = nuvolos_client_api.WorkloadsV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    app_slug = 'app_slug_example' # str | 
    execute_command = nuvolos_client_api.ExecuteCommand() # ExecuteCommand |  (optional)

    try:
        # Workloads V1 Execute Command
        api_response = api_instance.execute_command(org_slug, space_slug, instance_slug, app_slug, execute_command=execute_command)
        print("The response of WorkloadsV1Api->execute_command:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkloadsV1Api->execute_command: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **instance_slug** | **str**|  | 
 **app_slug** | **str**|  | 
 **execute_command** | [**ExecuteCommand**](ExecuteCommand.md)|  | [optional] 

### Return type

[**ExecuteCommandResponse**](ExecuteCommandResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request accepted |  -  |
**422** | Validation error |  -  |
**404** | Nuvolos object not found |  -  |
**400** | Bad request |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |
**500** | Internal server error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodepools**
> List[APINodePool] get_nodepools(org_slug, space_slug)

Workloads V1 List Nodepools

Returns the Virtual Machines available for scaled workloads in the given org/space context.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.api_node_pool import APINodePool
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
    api_instance = nuvolos_client_api.WorkloadsV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 

    try:
        # Workloads V1 List Nodepools
        api_response = api_instance.get_nodepools(org_slug, space_slug)
        print("The response of WorkloadsV1Api->get_nodepools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkloadsV1Api->get_nodepools: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 

### Return type

[**List[APINodePool]**](APINodePool.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation succeeded |  -  |
**404** | Nuvolos object not found |  -  |
**400** | Bad request |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |
**500** | Internal server error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workloads**
> List[WorkloadDetailed] get_workloads()

Workloads V1 List All Running

Returns the workloads currently run by the user.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.workload_detailed import WorkloadDetailed
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
    api_instance = nuvolos_client_api.WorkloadsV1Api(api_client)

    try:
        # Workloads V1 List All Running
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation succeeded |  -  |
**400** | Bad request |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**404** | Nuvolos object not found |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |
**500** | Internal server error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workloads_for_app**
> List[WorkloadDetailed] get_workloads_for_app(org_slug, space_slug, instance_slug, app_slug)

Workloads V1 List Workloads For App

Returns the workloads available for the user of a given Nuvolos application.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.workload_detailed import WorkloadDetailed
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
    api_instance = nuvolos_client_api.WorkloadsV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    app_slug = 'app_slug_example' # str | 

    try:
        # Workloads V1 List Workloads For App
        api_response = api_instance.get_workloads_for_app(org_slug, space_slug, instance_slug, app_slug)
        print("The response of WorkloadsV1Api->get_workloads_for_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkloadsV1Api->get_workloads_for_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **instance_slug** | **str**|  | 
 **app_slug** | **str**|  | 

### Return type

[**List[WorkloadDetailed]**](WorkloadDetailed.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation succeeded |  -  |
**404** | Nuvolos object not found |  -  |
**400** | Bad request |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |
**500** | Internal server error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

