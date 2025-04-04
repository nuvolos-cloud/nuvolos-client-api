# WorkloadDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addons_compute_units** | **str** |  | [optional] 
**compute_units** | **str** |  | [optional] 
**creation_timestamp** | **str** |  | [optional] 
**current_cpu** | **str** |  | [optional] 
**current_memory** | **str** |  | [optional] 
**gpu** | **str** |  | [optional] 
**instance_slug** | **str** |  | [optional] 
**max_cpu** | **str** |  | [optional] 
**max_memory** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**node_pool** | **str** |  | [optional] 
**org_slug** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**shared** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**space_slug** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.workload_detailed import WorkloadDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadDetailed from a JSON string
workload_detailed_instance = WorkloadDetailed.from_json(json)
# print the JSON string representation of the object
print(WorkloadDetailed.to_json())

# convert the object into a dict
workload_detailed_dict = workload_detailed_instance.to_dict()
# create an instance of WorkloadDetailed from a dict
workload_detailed_from_dict = WorkloadDetailed.from_dict(workload_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


