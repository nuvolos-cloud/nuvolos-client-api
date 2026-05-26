# Session


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | 
**start_time** | **datetime** |  | 
**stop_time** | **datetime** |  | [optional] 
**start_uid** | **int** |  | 
**start_uid_full_name** | **str** |  | 
**stop_uid** | **int** |  | [optional] 
**stop_uid_full_name** | **str** |  | [optional] 
**runtime_seconds** | **int** |  | [optional] 
**ncu** | **int** |  | [optional] 
**ncu_hours_used** | **float** |  | [optional] 
**ncu_sidecars_total** | **float** |  | [optional] 
**credits_spent** | **float** |  | [optional] 
**node_pool** | **str** |  | [optional] 
**active_resource** | **str** |  | [optional] 
**can_read_logs** | **bool** |  | [optional] 
**logging_containers** | **List[str]** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.session import Session

# TODO update the JSON string below
json = "{}"
# create an instance of Session from a JSON string
session_instance = Session.from_json(json)
# print the JSON string representation of the object
print(Session.to_json())

# convert the object into a dict
session_dict = session_instance.to_dict()
# create an instance of Session from a dict
session_from_dict = Session.from_dict(session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


