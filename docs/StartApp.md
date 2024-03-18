# StartApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dpi** | **int** |  | [optional] 
**screen_width** | **int** |  | [optional] 
**screen_height** | **int** |  | [optional] 
**node_pool** | **str** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.start_app import StartApp

# TODO update the JSON string below
json = "{}"
# create an instance of StartApp from a JSON string
start_app_instance = StartApp.from_json(json)
# print the JSON string representation of the object
print(StartApp.to_json())

# convert the object into a dict
start_app_dict = start_app_instance.to_dict()
# create an instance of StartApp from a dict
start_app_form_dict = start_app.from_dict(start_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


