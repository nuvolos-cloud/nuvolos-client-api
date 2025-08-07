# Application


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**status** | **str** |  | 
**storage_used** | **int** |  | 
**shared** | **bool** |  | 
**exportable** | **bool** |  | 
**aoid** | **int** |  | 

## Example

```python
from nuvolos_client_api.models.application import Application

# TODO update the JSON string below
json = "{}"
# create an instance of Application from a JSON string
application_instance = Application.from_json(json)
# print the JSON string representation of the object
print(Application.to_json())

# convert the object into a dict
application_dict = application_instance.to_dict()
# create an instance of Application from a dict
application_from_dict = Application.from_dict(application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


