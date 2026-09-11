# ValidationErrorDetailLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **List[str]** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.validation_error_detail_location import ValidationErrorDetailLocation

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorDetailLocation from a JSON string
validation_error_detail_location_instance = ValidationErrorDetailLocation.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorDetailLocation.to_json())

# convert the object into a dict
validation_error_detail_location_dict = validation_error_detail_location_instance.to_dict()
# create an instance of ValidationErrorDetailLocation from a dict
validation_error_detail_location_from_dict = ValidationErrorDetailLocation.from_dict(validation_error_detail_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


