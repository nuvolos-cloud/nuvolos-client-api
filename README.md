# Nuvolos Client API
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: staging
- Package version: 0.9.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import nuvolos_client_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import nuvolos_client_api
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
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
    api_instance = nuvolos_client_api.AppsV1Api(api_client)
    snapshot_slug = 'snapshot_slug_example' # str | 
    space_slug = 'space_slug_example' # str | 
    org_slug = 'org_slug_example' # str | 
    instance_slug = 'instance_slug_example' # str | 

    try:
        api_response = api_instance.get_apps(snapshot_slug, space_slug, org_slug, instance_slug)
        print("The response of AppsV1Api->get_apps:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsV1Api->get_apps: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AppsV1Api* | [**get_apps**](docs/AppsV1Api.md#get_apps) | **GET** /apps/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/snapshot/{snapshot_slug} | 
*InstancesV1Api* | [**get_instances**](docs/InstancesV1Api.md#get_instances) | **GET** /instances/v1/org/{org_slug}/space/{space_slug} | 
*OrganizationsV1Api* | [**get_orgs**](docs/OrganizationsV1Api.md#get_orgs) | **GET** /orgs/v1 | 
*SnapshotsV1Api* | [**get_snapshots**](docs/SnapshotsV1Api.md#get_snapshots) | **GET** /snapshots/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug} | 
*SpacesV1Api* | [**get_spaces**](docs/SpacesV1Api.md#get_spaces) | **GET** /spaces/v1/org/{slug} | 
*WorkloadsV1Api* | [**create_workload**](docs/WorkloadsV1Api.md#create_workload) | **POST** /workloads/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/app/{app_slug} | 
*WorkloadsV1Api* | [**delete_workload**](docs/WorkloadsV1Api.md#delete_workload) | **DELETE** /workloads/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/app/{app_slug} | 
*WorkloadsV1Api* | [**execute_command**](docs/WorkloadsV1Api.md#execute_command) | **POST** /workloads/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/app/{app_slug}/execute | 
*WorkloadsV1Api* | [**get_nodepools**](docs/WorkloadsV1Api.md#get_nodepools) | **GET** /workloads/v1/nodepools | 
*WorkloadsV1Api* | [**get_workloads**](docs/WorkloadsV1Api.md#get_workloads) | **GET** /workloads/v1 | 
*WorkloadsV1Api* | [**get_workloads_for_app**](docs/WorkloadsV1Api.md#get_workloads_for_app) | **GET** /workloads/v1/org/{org_slug}/space/{space_slug}/instance/{instance_slug}/app/{app_slug} | 


## Documentation For Models

 - [APINodePool](docs/APINodePool.md)
 - [Application](docs/Application.md)
 - [ClientApiError](docs/ClientApiError.md)
 - [ExecuteCommand](docs/ExecuteCommand.md)
 - [ExecuteCommandResponse](docs/ExecuteCommandResponse.md)
 - [Instance](docs/Instance.md)
 - [Org](docs/Org.md)
 - [Snapshot](docs/Snapshot.md)
 - [Space](docs/Space.md)
 - [StartApp](docs/StartApp.md)
 - [Task](docs/Task.md)
 - [WorkloadDetailed](docs/WorkloadDetailed.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




