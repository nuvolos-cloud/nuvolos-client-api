# InvitationSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**role** | **str** |  | 
**status** | **str** |  | 
**validity_timestamp** | **datetime** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.invitation_summary import InvitationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationSummary from a JSON string
invitation_summary_instance = InvitationSummary.from_json(json)
# print the JSON string representation of the object
print(InvitationSummary.to_json())

# convert the object into a dict
invitation_summary_dict = invitation_summary_instance.to_dict()
# create an instance of InvitationSummary from a dict
invitation_summary_from_dict = InvitationSummary.from_dict(invitation_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


