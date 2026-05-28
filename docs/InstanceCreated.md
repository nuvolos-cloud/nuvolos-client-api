# InstanceCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**creation_timestamp** | **datetime** |  | [optional] 
**archival_timestamp** | **datetime** |  | [optional] 
**rearchive_after_timestamp** | **datetime** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.instance_created import InstanceCreated

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceCreated from a JSON string
instance_created_instance = InstanceCreated.from_json(json)
# print the JSON string representation of the object
print(InstanceCreated.to_json())

# convert the object into a dict
instance_created_dict = instance_created_instance.to_dict()
# create an instance of InstanceCreated from a dict
instance_created_from_dict = InstanceCreated.from_dict(instance_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


