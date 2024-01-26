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

from nuvolos_client_api.models.api_node_pool import APINodePool

class TestAPINodePool(unittest.TestCase):
    """APINodePool unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> APINodePool:
        """Test APINodePool
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `APINodePool`
        """
        model = APINodePool()
        if include_optional:
            return APINodePool(
                slug = '',
                description = '',
                credits_per_hour = 1.337,
                cpu = 56,
                memory = 56,
                ssd = 56,
                vram = 56,
                gpu_type = '',
                available_in_teaching_spaces = True
            )
        else:
            return APINodePool(
        )
        """

    def testAPINodePool(self):
        """Test APINodePool"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()