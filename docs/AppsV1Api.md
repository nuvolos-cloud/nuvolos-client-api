# nuvolos_client_api.AppsV1Api

All URIs are relative to *https://api.eu1.nuvolos.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app**](AppsV1Api.md#create_app) | **POST** /apps/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/applications | 
[**derive_app**](AppsV1Api.md#derive_app) | **POST** /apps/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/app/{app_slug}/derived_images | 
[**get_apps**](AppsV1Api.md#get_apps) | **GET** /apps/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/snapshot/{snapshot_slug} | 


# **create_app**
> AppCreated create_app(org_slug, space_slug, instance_slug, app_create=app_create)

Creates a new application in the development snapshot of the specified instance.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.app_create import AppCreate
from nuvolos_client_api.models.app_created import AppCreated
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
    api_instance = nuvolos_client_api.AppsV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    app_create = nuvolos_client_api.AppCreate() # AppCreate |  (optional)

    try:
        api_response = api_instance.create_app(org_slug, space_slug, instance_slug, app_create=app_create)
        print("The response of AppsV1Api->create_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsV1Api->create_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **instance_slug** | **str**|  | 
 **app_create** | [**AppCreate**](AppCreate.md)|  | [optional] 

### Return type

[**AppCreated**](AppCreated.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Application created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**404** | Nuvolos object not found |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **derive_app**
> Task derive_app(org_slug, space_slug, instance_slug, app_slug, derive_app=derive_app)

Creates a derived image from an existing Nuvolos application

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.derive_app import DeriveApp
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
    api_instance = nuvolos_client_api.AppsV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    app_slug = 'app_slug_example' # str | 
    derive_app = nuvolos_client_api.DeriveApp() # DeriveApp |  (optional)

    try:
        api_response = api_instance.derive_app(org_slug, space_slug, instance_slug, app_slug, derive_app=derive_app)
        print("The response of AppsV1Api->derive_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsV1Api->derive_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **instance_slug** | **str**|  | 
 **app_slug** | **str**|  | 
 **derive_app** | [**DeriveApp**](DeriveApp.md)|  | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request accepted |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**404** | Nuvolos object not found |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_apps**
> List[Application] get_apps(org_slug, space_slug, instance_slug, snapshot_slug)

Returns the apps in the given snapshot.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.application import Application
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
    api_instance = nuvolos_client_api.AppsV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    snapshot_slug = 'snapshot_slug_example' # str | 

    try:
        api_response = api_instance.get_apps(org_slug, space_slug, instance_slug, snapshot_slug)
        print("The response of AppsV1Api->get_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsV1Api->get_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **instance_slug** | **str**|  | 
 **snapshot_slug** | **str**|  | 

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
**200** | Operation succeeded |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**404** | Nuvolos object not found |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

