# StartApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dpi** | **int** |  | [optional] [default to 96]
**node_pool** | **str** |  | [optional] 
**screen_height** | **int** |  | [optional] [default to 768]
**screen_width** | **int** |  | [optional] [default to 1024]

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
start_app_from_dict = StartApp.from_dict(start_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


