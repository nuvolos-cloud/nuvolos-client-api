import inspect

import pytest
from pydantic import ValidationError

from nuvolos_client_api import (
    ApiClient,
    GroupInstanceCreateRequest,
    InstancesV1Api,
    InstanceInvitationRequest,
    SpacesV1Api,
    SpaceInvitationRequest,
)


def _public_parameters(method):
    return [
        parameter
        for parameter in inspect.signature(method).parameters
        if not parameter.startswith("_")
    ]


def test_group_instance_request_requires_at_least_one_editor():
    request = GroupInstanceCreateRequest(
        name="Team Alpha",
        slug="team_alpha",
        editor_emails=["alice@example.org"],
    )

    assert request.to_dict()["editor_emails"] == ["alice@example.org"]
    with pytest.raises(ValidationError):
        GroupInstanceCreateRequest(
            name="Team Alpha",
            slug="team_alpha",
            editor_emails=[],
        )


def test_group_instance_request_serializes_slug_path_and_body():
    api = InstancesV1Api(ApiClient())
    request = GroupInstanceCreateRequest(
        name="Team Alpha",
        slug="team_alpha",
        editor_emails=["alice@example.org"],
    )

    method, url, _, body, _ = api._create_group_instance_serialize(
        "research",
        "course",
        request,
        None,
        None,
        None,
        0,
    )

    assert method == "POST"
    assert url.endswith("/instances/v1/org/research/space/course/group")
    assert body == {
        "name": "Team Alpha",
        "slug": "team_alpha",
        "editor_emails": ["alice@example.org"],
    }


def test_generated_instance_api_preserves_slug_parameter_order():
    assert _public_parameters(InstancesV1Api.create_group_instance) == [
        "self",
        "org_slug",
        "space_slug",
        "group_instance_create_request",
    ]
    assert _public_parameters(InstancesV1Api.get_instance_members) == [
        "self",
        "org_slug",
        "space_slug",
        "instance_slug",
    ]
    assert _public_parameters(InstancesV1Api.invite_instance_member) == [
        "self",
        "org_slug",
        "space_slug",
        "instance_slug",
        "instance_invitation_request",
    ]


def test_generated_space_api_preserves_slug_parameter_order():
    assert _public_parameters(SpacesV1Api.get_space_members) == [
        "self",
        "org_slug",
        "space_slug",
    ]
    assert _public_parameters(SpacesV1Api.invite_space_member) == [
        "self",
        "org_slug",
        "space_slug",
        "space_invitation_request",
    ]


def test_generated_invitation_models_expose_supported_roles():
    instance_request = InstanceInvitationRequest(
        email="member@example.org",
        role="EDITOR",
    )
    space_request = SpaceInvitationRequest(
        email="admin@example.org",
        role="SPACE_ADMIN",
    )

    assert instance_request.to_dict() == {
        "email": "member@example.org",
        "role": "EDITOR",
    }
    assert space_request.to_dict() == {
        "email": "admin@example.org",
        "role": "SPACE_ADMIN",
    }
