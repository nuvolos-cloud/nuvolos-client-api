# ExecuteCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** |  | 

## Example

```python
from nuvolos_client_api.models.execute_command import ExecuteCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteCommand from a JSON string
execute_command_instance = ExecuteCommand.from_json(json)
# print the JSON string representation of the object
print(ExecuteCommand.to_json())

# convert the object into a dict
execute_command_dict = execute_command_instance.to_dict()
# create an instance of ExecuteCommand from a dict
execute_command_form_dict = execute_command.from_dict(execute_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


