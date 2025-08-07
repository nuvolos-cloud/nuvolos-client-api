# nuvolos_client_api.TablesV1Api

All URIs are relative to *https://api.nuvolos.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_table**](TablesV1Api.md#delete_table) | **DELETE** /tables/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/snapshot/{snapshot_slug}/table/{table_slug} | 
[**get_schema_ddl**](TablesV1Api.md#get_schema_ddl) | **GET** /tables/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/snapshot/{snapshot_slug}/get_ddl | 
[**get_table_columns**](TablesV1Api.md#get_table_columns) | **GET** /tables/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/snapshot/{snapshot_slug}/table/{table_slug}/columns | 
[**get_table_ddl**](TablesV1Api.md#get_table_ddl) | **GET** /tables/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/snapshot/{snapshot_slug}/table/{table_slug}/get_ddl | 
[**get_tables**](TablesV1Api.md#get_tables) | **GET** /tables/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/snapshot/{snapshot_slug} | 
[**rename_table**](TablesV1Api.md#rename_table) | **PATCH** /tables/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/snapshot/{snapshot_slug}/table/{table_slug} | 


# **delete_table**
> delete_table(org_slug, space_slug, instance_slug, snapshot_slug, table_slug)

Deletes a table in the specified snapshot.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
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
    api_instance = nuvolos_client_api.TablesV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    snapshot_slug = 'snapshot_slug_example' # str | 
    table_slug = 'table_slug_example' # str | 

    try:
        api_instance.delete_table(org_slug, space_slug, instance_slug, snapshot_slug, table_slug)
    except Exception as e:
        print("Exception when calling TablesV1Api->delete_table: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **instance_slug** | **str**|  | 
 **snapshot_slug** | **str**|  | 
 **table_slug** | **str**|  | 

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
**403** | Access to Nuvolos resource is forbidden |  -  |
**404** | Nuvolos object not found |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema_ddl**
> DDL get_schema_ddl(org_slug, space_slug, instance_slug, snapshot_slug)

Returns the DDL of the database schema corresponding to the specified snapshot in Nuvolos.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.ddl import DDL
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
    api_instance = nuvolos_client_api.TablesV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    snapshot_slug = 'snapshot_slug_example' # str | 

    try:
        api_response = api_instance.get_schema_ddl(org_slug, space_slug, instance_slug, snapshot_slug)
        print("The response of TablesV1Api->get_schema_ddl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TablesV1Api->get_schema_ddl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **instance_slug** | **str**|  | 
 **snapshot_slug** | **str**|  | 

### Return type

[**DDL**](DDL.md)

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

# **get_table_columns**
> List[ColumnPublic] get_table_columns(org_slug, space_slug, instance_slug, snapshot_slug, table_slug)

Returns the columns of a table in the specified snapshot.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.column_public import ColumnPublic
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
    api_instance = nuvolos_client_api.TablesV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    snapshot_slug = 'snapshot_slug_example' # str | 
    table_slug = 'table_slug_example' # str | 

    try:
        api_response = api_instance.get_table_columns(org_slug, space_slug, instance_slug, snapshot_slug, table_slug)
        print("The response of TablesV1Api->get_table_columns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TablesV1Api->get_table_columns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **instance_slug** | **str**|  | 
 **snapshot_slug** | **str**|  | 
 **table_slug** | **str**|  | 

### Return type

[**List[ColumnPublic]**](ColumnPublic.md)

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

# **get_table_ddl**
> DDL get_table_ddl(org_slug, space_slug, instance_slug, snapshot_slug, table_slug)

Returns the DDL of a table in the specified snapshot.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.ddl import DDL
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
    api_instance = nuvolos_client_api.TablesV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    snapshot_slug = 'snapshot_slug_example' # str | 
    table_slug = 'table_slug_example' # str | 

    try:
        api_response = api_instance.get_table_ddl(org_slug, space_slug, instance_slug, snapshot_slug, table_slug)
        print("The response of TablesV1Api->get_table_ddl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TablesV1Api->get_table_ddl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **instance_slug** | **str**|  | 
 **snapshot_slug** | **str**|  | 
 **table_slug** | **str**|  | 

### Return type

[**DDL**](DDL.md)

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

# **get_tables**
> List[Table] get_tables(org_slug, space_slug, instance_slug, snapshot_slug)

Returns the tables in the specified snapshot.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.table import Table
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
    api_instance = nuvolos_client_api.TablesV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    snapshot_slug = 'snapshot_slug_example' # str | 

    try:
        api_response = api_instance.get_tables(org_slug, space_slug, instance_slug, snapshot_slug)
        print("The response of TablesV1Api->get_tables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TablesV1Api->get_tables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **instance_slug** | **str**|  | 
 **snapshot_slug** | **str**|  | 

### Return type

[**List[Table]**](Table.md)

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

# **rename_table**
> Table rename_table(org_slug, space_slug, instance_slug, snapshot_slug, table_slug, table_update=table_update)

Renames a table in the specified snapshot.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import nuvolos_client_api
from nuvolos_client_api.models.table import Table
from nuvolos_client_api.models.table_update import TableUpdate
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
    api_instance = nuvolos_client_api.TablesV1Api(api_client)
    org_slug = 'org_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 
    snapshot_slug = 'snapshot_slug_example' # str | 
    table_slug = 'table_slug_example' # str | 
    table_update = nuvolos_client_api.TableUpdate() # TableUpdate |  (optional)

    try:
        api_response = api_instance.rename_table(org_slug, space_slug, instance_slug, snapshot_slug, table_slug, table_update=table_update)
        print("The response of TablesV1Api->rename_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TablesV1Api->rename_table: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_slug** | **str**|  | 
 **space_slug** | **str**|  | 
 **instance_slug** | **str**|  | 
 **snapshot_slug** | **str**|  | 
 **table_slug** | **str**|  | 
 **table_update** | [**TableUpdate**](TableUpdate.md)|  | [optional] 

### Return type

[**Table**](Table.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update succeeded |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Access to Nuvolos resource is forbidden |  -  |
**404** | Nuvolos object not found |  -  |
**409** | Conflict with Nuvolos object |  -  |
**410** | Nuvolos object no longer available |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

