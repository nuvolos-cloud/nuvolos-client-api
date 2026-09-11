# SpaceInvitationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from nuvolos_client_api.models.space_invitation_request import SpaceInvitationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SpaceInvitationRequest from a JSON string
space_invitation_request_instance = SpaceInvitationRequest.from_json(json)
# print the JSON string representation of the object
print(SpaceInvitationRequest.to_json())

# convert the object into a dict
space_invitation_request_dict = space_invitation_request_instance.to_dict()
# create an instance of SpaceInvitationRequest from a dict
space_invitation_request_from_dict = SpaceInvitationRequest.from_dict(space_invitation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


