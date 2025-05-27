# Task1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**result** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**started** | **datetime** |  | [optional] 
**finished** | **datetime** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.task1 import Task1

# TODO update the JSON string below
json = "{}"
# create an instance of Task1 from a JSON string
task1_instance = Task1.from_json(json)
# print the JSON string representation of the object
print(Task1.to_json())

# convert the object into a dict
task1_dict = task1_instance.to_dict()
# create an instance of Task1 from a dict
task1_from_dict = Task1.from_dict(task1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


