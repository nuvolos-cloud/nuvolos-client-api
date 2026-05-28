# ImageCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**docker_image_url** | **str** |  | 
**description_md** | **str** |  | 
**ifid** | **int** |  | 
**description** | **str** |  | [optional] 
**public** | **bool** |  | [optional] [default to False]
**public_description** | **str** |  | [optional] 
**org_slug** | **str** |  | [optional] 
**space_slug** | **str** |  | [optional] 
**app_type** | **str** |  | [optional] 
**configuration** | **Dict[str, object]** |  | [optional] 
**has_tables** | **bool** |  | [optional] 
**complexity** | **int** |  | [optional] 
**tags** | **Dict[str, object]** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.image_create import ImageCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ImageCreate from a JSON string
image_create_instance = ImageCreate.from_json(json)
# print the JSON string representation of the object
print(ImageCreate.to_json())

# convert the object into a dict
image_create_dict = image_create_instance.to_dict()
# create an instance of ImageCreate from a dict
image_create_from_dict = ImageCreate.from_dict(image_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


