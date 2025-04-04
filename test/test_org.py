# coding: utf-8

"""
    Nuvolos

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: dev
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from nuvolos_client_api.models.org import Org

class TestOrg(unittest.TestCase):
    """Org unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Org:
        """Test Org
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Org`
        """
        model = Org()
        if include_optional:
            return Org(
                creation_timestamp = 'null',
                description = '',
                hpc_enabled = True,
                name = '',
                role = '',
                slug = '',
                tables_enabled = True,
                video_library_enabled = True
            )
        else:
            return Org(
                name = '',
                slug = '',
        )
        """

    def testOrg(self):
        """Test Org"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
