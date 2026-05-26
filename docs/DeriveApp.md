# DeriveApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_tag** | **str** |  | [optional] 
**email_once_finished** | **bool** |  | [optional] [default to True]

## Example

```python
from nuvolos_client_api.models.derive_app import DeriveApp

# TODO update the JSON string below
json = "{}"
# create an instance of DeriveApp from a JSON string
derive_app_instance = DeriveApp.from_json(json)
# print the JSON string representation of the object
print(DeriveApp.to_json())

# convert the object into a dict
derive_app_dict = derive_app_instance.to_dict()
# create an instance of DeriveApp from a dict
derive_app_from_dict = DeriveApp.from_dict(derive_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


