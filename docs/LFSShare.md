# LFSShare


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**afsid** | **int** |  | 
**name** | **str** |  | 
**quota_gib** | **int** |  | 
**subresource** | **str** |  | 
**mount_path** | **str** |  | [optional] 
**read_only** | **bool** |  | [optional] 
**slug** | **str** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.lfs_share import LFSShare

# TODO update the JSON string below
json = "{}"
# create an instance of LFSShare from a JSON string
lfs_share_instance = LFSShare.from_json(json)
# print the JSON string representation of the object
print(LFSShare.to_json())

# convert the object into a dict
lfs_share_dict = lfs_share_instance.to_dict()
# create an instance of LFSShare from a dict
lfs_share_from_dict = LFSShare.from_dict(lfs_share_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


