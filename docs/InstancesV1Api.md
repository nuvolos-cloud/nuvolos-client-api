# nuvolos_client_api.InstancesV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_snapshot**](InstancesV1Api.md#create_snapshot) | **POST** /instances/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/snapshots | 
[**get_instances**](InstancesV1Api.md#get_instances) | **GET** /instances/v1/org/{org_slug}/space/{space_slug} | 


# **create_snapshot**
> Task create_snapshot(org_slug, space_slug, instance_slug, body=body)

Creates a snapshot in the specified instance asynchronously

### Example


```python
import nuvolos_client_api
from nuvolos_client_api.models.snapshot_create_request import SnapshotCreateRequest
from nuvolos_client_api.models.task import Task
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
    api_instance = nuvolos_client_api.InstancesV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    body = nuvolos_client_api.SnapshotCreateRequest() # SnapshotCreateRequest |  (optional)

    try:
        api_response = api_instance.create_snapshot(org_slug, space_slug, instance_slug, body=body)
        print("The response of InstancesV1Api->create_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesV1Api->create_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **instance_slug** | **str**|  | 
 **body** | [**SnapshotCreateRequest**](SnapshotCreateRequest.md)|  | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creation succeeded |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**404** | Nuvolos object not found |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instances**
> List[Instance] get_instances(org_slug, space_slug)

Returns the instances the user has access to in the selected org and space.

### Example


```python
import nuvolos_client_api
from nuvolos_client_api.models.instance import Instance
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
    api_instance = nuvolos_client_api.InstancesV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 

    try:
        api_response = api_instance.get_instances(org_slug, space_slug)
        print("The response of InstancesV1Api->get_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesV1Api->get_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 

### Return type

[**List[Instance]**](Instance.md)

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

