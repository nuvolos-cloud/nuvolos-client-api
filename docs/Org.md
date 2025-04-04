# Org


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_timestamp** | **none_type** |  | [optional] 
**description** | **str** |  | [optional] 
**hpc_enabled** | **bool** |  | [optional] 
**name** | **str** |  | 
**role** | **str** |  | [optional] 
**slug** | **str** |  | 
**tables_enabled** | **bool** |  | [optional] 
**video_library_enabled** | **bool** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.org import Org

# TODO update the JSON string below
json = "{}"
# create an instance of Org from a JSON string
org_instance = Org.from_json(json)
# print the JSON string representation of the object
print(Org.to_json())

# convert the object into a dict
org_dict = org_instance.to_dict()
# create an instance of Org from a dict
org_from_dict = Org.from_dict(org_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


