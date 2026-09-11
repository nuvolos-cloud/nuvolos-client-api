# SpaceInstanceRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_slug** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from nuvolos_client_api.models.space_instance_role import SpaceInstanceRole

# TODO update the JSON string below
json = "{}"
# create an instance of SpaceInstanceRole from a JSON string
space_instance_role_instance = SpaceInstanceRole.from_json(json)
# print the JSON string representation of the object
print(SpaceInstanceRole.to_json())

# convert the object into a dict
space_instance_role_dict = space_instance_role_instance.to_dict()
# create an instance of SpaceInstanceRole from a dict
space_instance_role_from_dict = SpaceInstanceRole.from_dict(space_instance_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


