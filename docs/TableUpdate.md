# TableUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**bytes** | **int** |  | [optional] 
**row_count** | **int** |  | [optional] 
**delete_timestamp** | **str** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.table_update import TableUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TableUpdate from a JSON string
table_update_instance = TableUpdate.from_json(json)
# print the JSON string representation of the object
print(TableUpdate.to_json())

# convert the object into a dict
table_update_dict = table_update_instance.to_dict()
# create an instance of TableUpdate from a dict
table_update_from_dict = TableUpdate.from_dict(table_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


