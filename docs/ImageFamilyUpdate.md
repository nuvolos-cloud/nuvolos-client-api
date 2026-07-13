# ImageFamilyUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**disabled_reason** | **int** |  | [optional] 
**groups** | **List[str]** |  | [optional] 
**icon_url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**priority** | **float** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.image_family_update import ImageFamilyUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ImageFamilyUpdate from a JSON string
image_family_update_instance = ImageFamilyUpdate.from_json(json)
# print the JSON string representation of the object
print(ImageFamilyUpdate.to_json())

# convert the object into a dict
image_family_update_dict = image_family_update_instance.to_dict()
# create an instance of ImageFamilyUpdate from a dict
image_family_update_from_dict = ImageFamilyUpdate.from_dict(image_family_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


