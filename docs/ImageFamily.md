# ImageFamily


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ifid** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**icon_url** | **str** |  | [optional] 
**groups** | **List[str]** |  | [optional] 
**priority** | **float** |  | [optional] 
**disabled_reason** | **int** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.image_family import ImageFamily

# TODO update the JSON string below
json = "{}"
# create an instance of ImageFamily from a JSON string
image_family_instance = ImageFamily.from_json(json)
# print the JSON string representation of the object
print(ImageFamily.to_json())

# convert the object into a dict
image_family_dict = image_family_instance.to_dict()
# create an instance of ImageFamily from a dict
image_family_from_dict = ImageFamily.from_dict(image_family_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


