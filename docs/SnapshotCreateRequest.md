# SnapshotCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**email_once_finished** | **bool** |  | [optional] [default to False]
**name** | **str** |  | 
**slug** | **str** |  | 

## Example

```python
from nuvolos_client_api.models.snapshot_create_request import SnapshotCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotCreateRequest from a JSON string
snapshot_create_request_instance = SnapshotCreateRequest.from_json(json)
# print the JSON string representation of the object
print(SnapshotCreateRequest.to_json())

# convert the object into a dict
snapshot_create_request_dict = snapshot_create_request_instance.to_dict()
# create an instance of SnapshotCreateRequest from a dict
snapshot_create_request_from_dict = SnapshotCreateRequest.from_dict(snapshot_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


