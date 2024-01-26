import os
import nuvolos_client_api
from nuvolos_client_api.rest import ApiException
from pprint import pprint
import logging
from http.client import HTTPConnection


def debug_requests_on():
    """Switches on logging of the requests module."""
    HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)


# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = nuvolos_client_api.Configuration(
    host="https://api.nuvolos.cloud/",
    api_key={"ApiKeyAuth": os.getenv("NUVOLOS_API_KEY")},
    api_key_prefix={"ApiKeyAuth": "basic"},
)


# Enter a context with an instance of the API client
with nuvolos_client_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nuvolos_client_api.OrganizationsV1Api(api_client)
    debug_requests_on()

    try:
        api_response = api_instance.get_orgs()
        print("The response of OrganizationsApi->orgs_v1_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrganizationsApi->orgs_v1_get: %s\n" % e)
