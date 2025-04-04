# Snapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_timestamp** | **datetime** |  | [optional] 
**database_tables_enabled** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | 
**slug** | **str** |  | 
**snapshot_timestamp** | **datetime** |  | [optional] 
**snapshot_type** | **str** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.snapshot import Snapshot

# TODO update the JSON string below
json = "{}"
# create an instance of Snapshot from a JSON string
snapshot_instance = Snapshot.from_json(json)
# print the JSON string representation of the object
print(Snapshot.to_json())

# convert the object into a dict
snapshot_dict = snapshot_instance.to_dict()
# create an instance of Snapshot from a dict
snapshot_from_dict = Snapshot.from_dict(snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


