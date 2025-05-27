# ExecuteCommandResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reqid** | **str** |  | [optional] 
**output_path** | **str** |  | [optional] 
**error_path** | **str** |  | [optional] 
**metadata_path** | **str** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.execute_command_response import ExecuteCommandResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteCommandResponse from a JSON string
execute_command_response_instance = ExecuteCommandResponse.from_json(json)
# print the JSON string representation of the object
print(ExecuteCommandResponse.to_json())

# convert the object into a dict
execute_command_response_dict = execute_command_response_instance.to_dict()
# create an instance of ExecuteCommandResponse from a dict
execute_command_response_from_dict = ExecuteCommandResponse.from_dict(execute_command_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


