# ImageFamilyCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**icon_url** | **str** |  | 
**description** | **str** |  | [optional] 
**groups** | **List[str]** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.image_family_create import ImageFamilyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ImageFamilyCreate from a JSON string
image_family_create_instance = ImageFamilyCreate.from_json(json)
# print the JSON string representation of the object
print(ImageFamilyCreate.to_json())

# convert the object into a dict
image_family_create_dict = image_family_create_instance.to_dict()
# create an instance of ImageFamilyCreate from a dict
image_family_create_from_dict = ImageFamilyCreate.from_dict(image_family_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


