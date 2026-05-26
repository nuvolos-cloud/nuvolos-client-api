# ImageUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**docker_image_url** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**description_md** | **str** |  | [optional] 
**public** | **bool** |  | [optional] 
**public_description** | **str** |  | [optional] 
**app_type** | **str** |  | [optional] 
**configuration** | **Dict[str, object]** |  | [optional] 
**complexity** | **int** |  | [optional] 
**tags** | **Dict[str, object]** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.image_update import ImageUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ImageUpdate from a JSON string
image_update_instance = ImageUpdate.from_json(json)
# print the JSON string representation of the object
print(ImageUpdate.to_json())

# convert the object into a dict
image_update_dict = image_update_instance.to_dict()
# create an instance of ImageUpdate from a dict
image_update_from_dict = ImageUpdate.from_dict(image_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


