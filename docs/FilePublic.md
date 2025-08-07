# FilePublic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fid** | **str** |  | 
**short_id** | **str** |  | 
**local_path** | **str** |  | 
**os_path** | **str** |  | [optional] 
**area** | **str** |  | 
**type** | **str** |  | 
**size** | **int** |  | [optional] 
**is_video** | **bool** |  | [optional] 
**snapshot_slug** | **str** |  | [optional] 
**creation_timestamp** | **str** |  | [optional] 
**last_modified_timestamp** | **str** |  | [optional] 
**status** | **Dict[str, object]** |  | [optional] 
**history** | **Dict[str, object]** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.file_public import FilePublic

# TODO update the JSON string below
json = "{}"
# create an instance of FilePublic from a JSON string
file_public_instance = FilePublic.from_json(json)
# print the JSON string representation of the object
print(FilePublic.to_json())

# convert the object into a dict
file_public_dict = file_public_instance.to_dict()
# create an instance of FilePublic from a dict
file_public_from_dict = FilePublic.from_dict(file_public_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


