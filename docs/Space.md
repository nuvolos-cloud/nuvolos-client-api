# Space


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | 
**name** | **str** |  | 
**role** | **str** |  | [optional] 
**type** | **str** |  | 
**visibility_type** | **str** |  | 
**description** | **str** |  | [optional] 
**database_tables_enabled** | **bool** |  | [optional] 
**archival_timestamp** | **datetime** |  | [optional] 
**archive_by_date** | **date** |  | [optional] 
**creation_timestamp** | **datetime** |  | [optional] 
**video_library_enabled** | **bool** |  | 
**last_modified_timestamp** | **datetime** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.space import Space

# TODO update the JSON string below
json = "{}"
# create an instance of Space from a JSON string
space_instance = Space.from_json(json)
# print the JSON string representation of the object
print Space.to_json()

# convert the object into a dict
space_dict = space_instance.to_dict()
# create an instance of Space from a dict
space_form_dict = space.from_dict(space_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


