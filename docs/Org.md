# Org


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | 
**name** | **str** |  | 
**role** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**tables_enabled** | **bool** |  | [optional] 
**hpc_enabled** | **bool** |  | [optional] 
**creation_timestamp** | **datetime** |  | [optional] 
**video_library_enabled** | **bool** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.org import Org

# TODO update the JSON string below
json = "{}"
# create an instance of Org from a JSON string
org_instance = Org.from_json(json)
# print the JSON string representation of the object
print Org.to_json()

# convert the object into a dict
org_dict = org_instance.to_dict()
# create an instance of Org from a dict
org_form_dict = org.from_dict(org_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


