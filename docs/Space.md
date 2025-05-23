# Space


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_timestamp** | **datetime** |  | [optional] 
**archive_by_date** | **date** |  | [optional] 
**creation_timestamp** | **datetime** |  | [optional] 
**database_tables_enabled** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**last_modified_timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**role** | **str** |  | [optional] 
**slug** | **str** |  | 
**type** | **str** |  | 
**video_library_enabled** | **bool** |  | 
**visibility_type** | **str** |  | 

## Example

```python
from nuvolos_client_api.models.space import Space

# TODO update the JSON string below
json = "{}"
# create an instance of Space from a JSON string
space_instance = Space.from_json(json)
# print the JSON string representation of the object
print(Space.to_json())

# convert the object into a dict
space_dict = space_instance.to_dict()
# create an instance of Space from a dict
space_from_dict = Space.from_dict(space_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


