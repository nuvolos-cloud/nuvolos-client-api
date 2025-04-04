# nuvolos_client_api.SnapshotsV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_snapshot**](SnapshotsV1Api.md#delete_snapshot) | **DELETE** /snapshots/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/snapshot/{snapshot_slug} | 
[**get_snapshots**](SnapshotsV1Api.md#get_snapshots) | **GET** /snapshots/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug} | 


# **delete_snapshot**
> Task delete_snapshot(snapshot_slug, space_slug, instance_slug, org_slug)

Deletes a snapshot in the specified instance asynchronously

### Example


```python
import nuvolos_client_api
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
    api_instance = nuvolos_client_api.SnapshotsV1Api(api_client)
    snapshot_slug = 'snapshot_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    org_slug = 'org_slug_example' # str | 

    try:
        api_response = api_instance.delete_snapshot(snapshot_slug, space_slug, instance_slug, org_slug)
        print("The response of SnapshotsV1Api->delete_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsV1Api->delete_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **instance_slug** | **str**|  | 
 **org_slug** | **str**|  | 

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
**201** | Deletion initiated |  -  |
**400** | Bad request |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**404** | Nuvolos object not found |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshots**
> List[Snapshot] get_snapshots(space_slug, instance_slug, org_slug)

Returns the snapshots the user has access to in the specified org, space and instance.

### Example


```python
import nuvolos_client_api
from nuvolos_client_api.models.snapshot import Snapshot
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
    api_instance = nuvolos_client_api.SnapshotsV1Api(api_client)
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    org_slug = 'org_slug_example' # str | 

    try:
        api_response = api_instance.get_snapshots(space_slug, instance_slug, org_slug)
        print("The response of SnapshotsV1Api->get_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsV1Api->get_snapshots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_slug** | **str**|  | 
 **instance_slug** | **str**|  | 
 **org_slug** | **str**|  | 

### Return type

[**List[Snapshot]**](Snapshot.md)

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

