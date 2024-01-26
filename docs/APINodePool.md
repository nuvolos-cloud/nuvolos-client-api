# APINodePool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**credits_per_hour** | **float** |  | [optional] 
**cpu** | **int** |  | [optional] 
**memory** | **int** |  | [optional] 
**ssd** | **int** |  | [optional] 
**vram** | **int** |  | [optional] 
**gpu_type** | **str** |  | [optional] 
**available_in_teaching_spaces** | **bool** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.api_node_pool import APINodePool

# TODO update the JSON string below
json = "{}"
# create an instance of APINodePool from a JSON string
api_node_pool_instance = APINodePool.from_json(json)
# print the JSON string representation of the object
print APINodePool.to_json()

# convert the object into a dict
api_node_pool_dict = api_node_pool_instance.to_dict()
# create an instance of APINodePool from a dict
api_node_pool_form_dict = api_node_pool.from_dict(api_node_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


