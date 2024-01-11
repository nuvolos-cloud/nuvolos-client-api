# nuvolos_client_api.OrganizationsV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_org_options**](OrganizationsV1Api.md#list_org_options) | **OPTIONS** /orgs/v1 | 
[**list_orgs**](OrganizationsV1Api.md#list_orgs) | **GET** /orgs/v1 | 


# **list_org_options**
> List[Org] list_org_options()



Lists all Nuvolos organizations the user is affiliated with

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import nuvolos_client_api
from nuvolos_client_api.models.org import Org
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
    api_instance = nuvolos_client_api.OrganizationsV1Api(api_client)

    try:
        api_response = api_instance.list_org_options()
        print("The response of OrganizationsV1Api->list_org_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsV1Api->list_org_options: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Org]**](Org.md)

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

# **list_orgs**
> List[Org] list_orgs()



Lists all Nuvolos organizations the user is affiliated with

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import nuvolos_client_api
from nuvolos_client_api.models.org import Org
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
    api_instance = nuvolos_client_api.OrganizationsV1Api(api_client)

    try:
        api_response = api_instance.list_orgs()
        print("The response of OrganizationsV1Api->list_orgs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsV1Api->list_orgs: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Org]**](Org.md)

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

