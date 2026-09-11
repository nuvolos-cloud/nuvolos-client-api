# InstanceInvitationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from nuvolos_client_api.models.instance_invitation_request import InstanceInvitationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceInvitationRequest from a JSON string
instance_invitation_request_instance = InstanceInvitationRequest.from_json(json)
# print the JSON string representation of the object
print(InstanceInvitationRequest.to_json())

# convert the object into a dict
instance_invitation_request_dict = instance_invitation_request_instance.to_dict()
# create an instance of InstanceInvitationRequest from a dict
instance_invitation_request_from_dict = InstanceInvitationRequest.from_dict(instance_invitation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


