# GroupInstanceCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**slug** | **str** |  | 
**description** | **str** |  | [optional] 
**editor_emails** | **List[str]** |  | 

## Example

```python
from nuvolos_client_api.models.group_instance_create_request import GroupInstanceCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupInstanceCreateRequest from a JSON string
group_instance_create_request_instance = GroupInstanceCreateRequest.from_json(json)
# print the JSON string representation of the object
print(GroupInstanceCreateRequest.to_json())

# convert the object into a dict
group_instance_create_request_dict = group_instance_create_request_instance.to_dict()
# create an instance of GroupInstanceCreateRequest from a dict
group_instance_create_request_from_dict = GroupInstanceCreateRequest.from_dict(group_instance_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


