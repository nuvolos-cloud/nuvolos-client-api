# AppCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**long_id** | **str** |  | 
**imid** | **int** |  | 
**pars** | **str** |  | [optional] [default to '{}']
**description** | **str** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.app_create import AppCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AppCreate from a JSON string
app_create_instance = AppCreate.from_json(json)
# print the JSON string representation of the object
print(AppCreate.to_json())

# convert the object into a dict
app_create_dict = app_create_instance.to_dict()
# create an instance of AppCreate from a dict
app_create_from_dict = AppCreate.from_dict(app_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


