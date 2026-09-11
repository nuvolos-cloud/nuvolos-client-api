# InstanceMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 
**active** | **bool** |  | 
**role** | **str** |  | 
**role_source** | **str** |  | 

## Example

```python
from nuvolos_client_api.models.instance_member import InstanceMember

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceMember from a JSON string
instance_member_instance = InstanceMember.from_json(json)
# print the JSON string representation of the object
print(InstanceMember.to_json())

# convert the object into a dict
instance_member_dict = instance_member_instance.to_dict()
# create an instance of InstanceMember from a dict
instance_member_from_dict = InstanceMember.from_dict(instance_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


