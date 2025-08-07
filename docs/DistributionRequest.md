# DistributionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_instances** | **List[Dict[str, object]]** | List of target instances with org_slug, space_slug, instance_slug. Objects will be distributed to the development snapshot of the target instance. | 
**source_applications** | **List[str]** | List of application slugs to distribute. | [optional] [default to []]
**source_files** | **List[str]** | List of file OS paths to distribute. These are the actual paths in the file system, not slugs. | [optional] [default to []]
**source_tables** | **List[str]** | List of table names to distribute. These are the actual table names, not slugs. | [optional] [default to []]
**auto_snapshot** | **bool** | Whether to create a snapshot of the target instance before distributing. | [optional] [default to False]
**notify_target_users** | **bool** | Whether to notify target users when the distribution is complete. | [optional] [default to False]
**custom_email_message** | **str** | Message to send when the distribution is complete. | [optional] 

## Example

```python
from nuvolos_client_api.models.distribution_request import DistributionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DistributionRequest from a JSON string
distribution_request_instance = DistributionRequest.from_json(json)
# print the JSON string representation of the object
print(DistributionRequest.to_json())

# convert the object into a dict
distribution_request_dict = distribution_request_instance.to_dict()
# create an instance of DistributionRequest from a dict
distribution_request_from_dict = DistributionRequest.from_dict(distribution_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


