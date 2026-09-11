# nuvolos_client_api.InstancesV1Api

All URIs are relative to *https://api.eu1.nuvolos.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group_instance**](InstancesV1Api.md#create_group_instance) | **POST** /instances/v1/org/{org_slug}/space/{space_slug}/group | Instances V1 Create Group Instance
[**create_instance**](InstancesV1Api.md#create_instance) | **POST** /instances/v1/org/{org_slug}/space/{space_slug} | Instances V1 Create Instance
[**create_snapshot**](InstancesV1Api.md#create_snapshot) | **POST** /instances/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/snapshots | Instances V1 Create Snapshot
[**get_instance_members**](InstancesV1Api.md#get_instance_members) | **GET** /instances/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/members | Instances V1 List Members
[**get_instances**](InstancesV1Api.md#get_instances) | **GET** /instances/v1/org/{org_slug}/space/{space_slug} | Instances V1 List Instances
[**invite_instance_member**](InstancesV1Api.md#invite_instance_member) | **POST** /instances/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/invitations | Instances V1 Invite Member


# **create_group_instance**
> Task create_group_instance(org_slug, space_slug, group_instance_create_request=group_instance_create_request)

Instances V1 Create Group Instance

Creates a group instance and invites the supplied users as editors asynchronously.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.group_instance_create_request import GroupInstanceCreateRequest
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
    api_instance = nuvolos_client_api.InstancesV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    group_instance_create_request = nuvolos_client_api.GroupInstanceCreateRequest() # GroupInstanceCreateRequest |  (optional)

    try:
        # Instances V1 Create Group Instance
        api_response = api_instance.create_group_instance(org_slug, space_slug, group_instance_create_request=group_instance_create_request)
        print("The response of InstancesV1Api->create_group_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesV1Api->create_group_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **group_instance_create_request** | [**GroupInstanceCreateRequest**](GroupInstanceCreateRequest.md)|  | [optional] 

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

# **create_instance**
> InstanceCreated create_instance(org_slug, space_slug, instance_create_request=instance_create_request)

Instances V1 Create Instance

Creates a new instance in the specified org and space.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.instance_create_request import InstanceCreateRequest
from nuvolos_client_api.models.instance_created import InstanceCreated
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
    api_instance = nuvolos_client_api.InstancesV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_create_request = nuvolos_client_api.InstanceCreateRequest() # InstanceCreateRequest |  (optional)

    try:
        # Instances V1 Create Instance
        api_response = api_instance.create_instance(org_slug, space_slug, instance_create_request=instance_create_request)
        print("The response of InstancesV1Api->create_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesV1Api->create_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **instance_create_request** | [**InstanceCreateRequest**](InstanceCreateRequest.md)|  | [optional] 

### Return type

[**InstanceCreated**](InstanceCreated.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creation succeeded |  -  |
**422** | Validation error |  -  |
**404** | Nuvolos object not found |  -  |
**400** | Bad request |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |
**500** | Internal server error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snapshot**
> Task create_snapshot(org_slug, space_slug, instance_slug, snapshot_create_request=snapshot_create_request)

Instances V1 Create Snapshot

Creates a snapshot in the specified instance asynchronously

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.snapshot_create_request import SnapshotCreateRequest
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
    api_instance = nuvolos_client_api.InstancesV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    snapshot_create_request = nuvolos_client_api.SnapshotCreateRequest() # SnapshotCreateRequest |  (optional)

    try:
        # Instances V1 Create Snapshot
        api_response = api_instance.create_snapshot(org_slug, space_slug, instance_slug, snapshot_create_request=snapshot_create_request)
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
 **snapshot_create_request** | [**SnapshotCreateRequest**](SnapshotCreateRequest.md)|  | [optional] 

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
**201** | Creation succeeded |  -  |
**422** | Validation error |  -  |
**404** | Nuvolos object not found |  -  |
**400** | Bad request |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |
**500** | Internal server error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance_members**
> List[InstanceMember] get_instance_members(org_slug, space_slug, instance_slug)

Instances V1 List Members

Returns explicit and inherited members of the specified instance.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.instance_member import InstanceMember
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
    api_instance = nuvolos_client_api.InstancesV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 

    try:
        # Instances V1 List Members
        api_response = api_instance.get_instance_members(org_slug, space_slug, instance_slug)
        print("The response of InstancesV1Api->get_instance_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesV1Api->get_instance_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **instance_slug** | **str**|  | 

### Return type

[**List[InstanceMember]**](InstanceMember.md)

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

# **get_instances**
> List[Instance] get_instances(org_slug, space_slug)

Instances V1 List Instances

Returns the instances the user has access to in the selected org and space.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.instance import Instance
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
    api_instance = nuvolos_client_api.InstancesV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 

    try:
        # Instances V1 List Instances
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

# **invite_instance_member**
> InvitationSummary invite_instance_member(org_slug, space_slug, instance_slug, instance_invitation_request=instance_invitation_request)

Instances V1 Invite Member

Invites a user to the specified instance with the requested role.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.instance_invitation_request import InstanceInvitationRequest
from nuvolos_client_api.models.invitation_summary import InvitationSummary
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
    api_instance = nuvolos_client_api.InstancesV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    instance_invitation_request = nuvolos_client_api.InstanceInvitationRequest() # InstanceInvitationRequest |  (optional)

    try:
        # Instances V1 Invite Member
        api_response = api_instance.invite_instance_member(org_slug, space_slug, instance_slug, instance_invitation_request=instance_invitation_request)
        print("The response of InstancesV1Api->invite_instance_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesV1Api->invite_instance_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **instance_slug** | **str**|  | 
 **instance_invitation_request** | [**InstanceInvitationRequest**](InstanceInvitationRequest.md)|  | [optional] 

### Return type

[**InvitationSummary**](InvitationSummary.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Invitation created |  -  |
**422** | Validation error |  -  |
**404** | Nuvolos object not found |  -  |
**400** | Bad request |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |
**500** | Internal server error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

