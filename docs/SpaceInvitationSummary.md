# SpaceInvitationSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**role** | **str** |  | 
**status** | **str** |  | 
**validity_timestamp** | **datetime** |  | [optional] 

## Example

```python
from nuvolos_client_api.models.space_invitation_summary import SpaceInvitationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SpaceInvitationSummary from a JSON string
space_invitation_summary_instance = SpaceInvitationSummary.from_json(json)
# print the JSON string representation of the object
print(SpaceInvitationSummary.to_json())

# convert the object into a dict
space_invitation_summary_dict = space_invitation_summary_instance.to_dict()
# create an instance of SpaceInvitationSummary from a dict
space_invitation_summary_from_dict = SpaceInvitationSummary.from_dict(space_invitation_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


