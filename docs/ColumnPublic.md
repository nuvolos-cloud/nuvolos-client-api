# ColumnPublic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_slug** | **str** |  | [optional] 
**short_id** | **str** |  | 
**long_id** | **str** |  | 
**coltype** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.column_public import ColumnPublic

# TODO update the JSON string below
json = "{}"
# create an instance of ColumnPublic from a JSON string
column_public_instance = ColumnPublic.from_json(json)
# print the JSON string representation of the object
print(ColumnPublic.to_json())

# convert the object into a dict
column_public_dict = column_public_instance.to_dict()
# create an instance of ColumnPublic from a dict
column_public_from_dict = ColumnPublic.from_dict(column_public_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


