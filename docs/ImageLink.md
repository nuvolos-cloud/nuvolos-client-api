# ImageLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imid** | **int** |  | 
**linkid** | **int** |  | 
**org_slug** | **str** |  | [optional] 
**space_slug** | **str** |  | [optional] 
**priority** | **int** |  | [optional] 
**space_type** | **int** |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.image_link import ImageLink

# TODO update the JSON string below
json = "{}"
# create an instance of ImageLink from a JSON string
image_link_instance = ImageLink.from_json(json)
# print the JSON string representation of the object
print(ImageLink.to_json())

# convert the object into a dict
image_link_dict = image_link_instance.to_dict()
# create an instance of ImageLink from a dict
image_link_from_dict = ImageLink.from_dict(image_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


