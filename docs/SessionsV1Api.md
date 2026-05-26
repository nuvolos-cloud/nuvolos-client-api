# nuvolos_client_api.SessionsV1Api

All URIs are relative to *https://api.eu1.nuvolos.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_session_logs**](SessionsV1Api.md#get_session_logs) | **GET** /sessions/v1/{session_id}/container/{container_name}/logs | 
[**get_sessions**](SessionsV1Api.md#get_sessions) | **GET** /sessions/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/app/{app_slug} | 


# **get_session_logs**
> get_session_logs(session_id, container_name, max_lines=max_lines, from_start=from_start)

Returns logs for the given session and container.

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
    api_instance = nuvolos_client_api.SessionsV1Api(api_client)
    session_id = 'session_id_example' # str | 
    container_name = 'container_name_example' # str | 
    max_lines = 100 # int |  (optional) (default to 100)
    from_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_instance.get_session_logs(session_id, container_name, max_lines=max_lines, from_start=from_start)
    except Exception as e:
        print("Exception when calling SessionsV1Api->get_session_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **container_name** | **str**|  | 
 **max_lines** | **int**|  | [optional] [default to 100]
 **from_start** | **datetime**|  | [optional] 

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
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**404** | Nuvolos object not found |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sessions**
> List[Session] get_sessions(org_slug, space_slug, instance_slug, app_slug, page=page, per_page=per_page, metadata=metadata, order_by=order_by, session_id=session_id, sort=sort)

Returns sessions for the given Nuvolos application.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.session import Session
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
    api_instance = nuvolos_client_api.SessionsV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    app_slug = 'app_slug_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    per_page = 100 # int |  (optional) (default to 100)
    metadata = False # bool |  (optional) (default to False)
    order_by = 'order_by_example' # str |  (optional)
    session_id = 'session_id_example' # str |  (optional)
    sort = desc # str |  (optional) (default to desc)

    try:
        api_response = api_instance.get_sessions(org_slug, space_slug, instance_slug, app_slug, page=page, per_page=per_page, metadata=metadata, order_by=order_by, session_id=session_id, sort=sort)
        print("The response of SessionsV1Api->get_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsV1Api->get_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **instance_slug** | **str**|  | 
 **app_slug** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 100]
 **metadata** | **bool**|  | [optional] [default to False]
 **order_by** | **str**|  | [optional] 
 **session_id** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] [default to desc]

### Return type

[**List[Session]**](Session.md)

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

