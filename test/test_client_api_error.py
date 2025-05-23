# coding: utf-8

"""
    Nuvolos

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: prod
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from nuvolos_client_api.models.client_api_error import ClientApiError

class TestClientApiError(unittest.TestCase):
    """ClientApiError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientApiError:
        """Test ClientApiError
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientApiError`
        """
        model = ClientApiError()
        if include_optional:
            return ClientApiError(
                ctxid = None,
                err = None,
                incident_id = None,
                msg = None
            )
        else:
            return ClientApiError(
        )
        """

    def testClientApiError(self):
        """Test ClientApiError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
