# InstanceCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.instance_create_request import InstanceCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceCreateRequest from a JSON string
instance_create_request_instance = InstanceCreateRequest.from_json(json)
# print the JSON string representation of the object
print(InstanceCreateRequest.to_json())

# convert the object into a dict
instance_create_request_dict = instance_create_request_instance.to_dict()
# create an instance of InstanceCreateRequest from a dict
instance_create_request_from_dict = InstanceCreateRequest.from_dict(instance_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


