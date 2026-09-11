# SpaceMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 
**active** | **bool** |  | 
**space_role** | **str** |  | [optional] 
**instance_roles** | [**List[SpaceInstanceRole]**](SpaceInstanceRole.md) |  | 

## Example

```python
from nuvolos_client_api.models.space_member import SpaceMember

# TODO update the JSON string below
json = "{}"
# create an instance of SpaceMember from a JSON string
space_member_instance = SpaceMember.from_json(json)
# print the JSON string representation of the object
print(SpaceMember.to_json())

# convert the object into a dict
space_member_dict = space_member_instance.to_dict()
# create an instance of SpaceMember from a dict
space_member_from_dict = SpaceMember.from_dict(space_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


