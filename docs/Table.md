# Table


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**database** | **str** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**bytes** | **int** |  | 
**row_count** | **int** |  | 
**delete_timestamp** | **str** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.table import Table

# TODO update the JSON string below
json = "{}"
# create an instance of Table from a JSON string
table_instance = Table.from_json(json)
# print the JSON string representation of the object
print(Table.to_json())

# convert the object into a dict
table_dict = table_instance.to_dict()
# create an instance of Table from a dict
table_from_dict = Table.from_dict(table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


