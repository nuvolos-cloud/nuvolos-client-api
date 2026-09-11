# nuvolos_client_api.SpacesV1Api

All URIs are relative to *https://api.eu1.nuvolos.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_space_members**](SpacesV1Api.md#get_space_members) | **GET** /spaces/v1/org/{org_slug}/space/{space_slug}/members | Spaces V1 List Members
[**get_spaces**](SpacesV1Api.md#get_spaces) | **GET** /spaces/v1/org/{slug} | Spaces V1 List Spaces
[**invite_space_member**](SpacesV1Api.md#invite_space_member) | **POST** /spaces/v1/org/{org_slug}/space/{space_slug}/invitations | Spaces V1 Invite Member


# **get_space_members**
> List[SpaceMember] get_space_members(org_slug, space_slug)

Spaces V1 List Members

Returns space administrators and users with instance roles in the specified space.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.space_member import SpaceMember
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
    api_instance = nuvolos_client_api.SpacesV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 

    try:
        # Spaces V1 List Members
        api_response = api_instance.get_space_members(org_slug, space_slug)
        print("The response of SpacesV1Api->get_space_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpacesV1Api->get_space_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 

### Return type

[**List[SpaceMember]**](SpaceMember.md)

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

# **get_spaces**
> List[Space] get_spaces(slug)

Spaces V1 List Spaces

Returns the spaces the user is affiliated with in the selected org. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.space import Space
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
    api_instance = nuvolos_client_api.SpacesV1Api(api_client)
    slug = 'slug_example' # str | 

    try:
        # Spaces V1 List Spaces
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

# **invite_space_member**
> SpaceInvitationSummary invite_space_member(org_slug, space_slug, space_invitation_request=space_invitation_request)

Spaces V1 Invite Member

Invites a user to administer the specified space.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.space_invitation_request import SpaceInvitationRequest
from nuvolos_client_api.models.space_invitation_summary import SpaceInvitationSummary
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
    api_instance = nuvolos_client_api.SpacesV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    space_invitation_request = nuvolos_client_api.SpaceInvitationRequest() # SpaceInvitationRequest |  (optional)

    try:
        # Spaces V1 Invite Member
        api_response = api_instance.invite_space_member(org_slug, space_slug, space_invitation_request=space_invitation_request)
        print("The response of SpacesV1Api->invite_space_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpacesV1Api->invite_space_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **space_invitation_request** | [**SpaceInvitationRequest**](SpaceInvitationRequest.md)|  | [optional] 

### Return type

[**SpaceInvitationSummary**](SpaceInvitationSummary.md)

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

