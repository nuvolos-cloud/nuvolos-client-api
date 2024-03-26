# ClientApiError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incident_id** | **object** |  | [optional] 
**ctxid** | **object** |  | [optional] 
**err** | **object** |  | [optional] 
**msg** | **object** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.client_api_error import ClientApiError

# TODO update the JSON string below
json = "{}"
# create an instance of ClientApiError from a JSON string
client_api_error_instance = ClientApiError.from_json(json)
# print the JSON string representation of the object
print ClientApiError.to_json()

# convert the object into a dict
client_api_error_dict = client_api_error_instance.to_dict()
# create an instance of ClientApiError from a dict
client_api_error_form_dict = client_api_error.from_dict(client_api_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


