# coding: utf-8

"""
    Nuvolos

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: staging
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from nuvolos_client_api.models.org import Org

class TestOrg(unittest.TestCase):
    """Org unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Org:
        """Test Org
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Org`
        """
        model = Org()
        if include_optional:
            return Org(
                slug = '',
                name = '',
                role = '',
                description = '',
                tables_enabled = True,
                hpc_enabled = True,
                creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                video_library_enabled = True
            )
        else:
            return Org(
                slug = '',
                name = '',
        )
        """

    def testOrg(self):
        """Test Org"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
