# coding: utf-8

"""
    Nuvolos

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: prod
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from nuvolos_client_api.models.execute_command_response import ExecuteCommandResponse

class TestExecuteCommandResponse(unittest.TestCase):
    """ExecuteCommandResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExecuteCommandResponse:
        """Test ExecuteCommandResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExecuteCommandResponse`
        """
        model = ExecuteCommandResponse()
        if include_optional:
            return ExecuteCommandResponse(
                error_path = '',
                metadata_path = '',
                output_path = '',
                reqid = ''
            )
        else:
            return ExecuteCommandResponse(
        )
        """

    def testExecuteCommandResponse(self):
        """Test ExecuteCommandResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
