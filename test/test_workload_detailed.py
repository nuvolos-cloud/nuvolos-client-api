# coding: utf-8

"""
    Nuvolos

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: prod
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from nuvolos_client_api.models.workload_detailed import WorkloadDetailed

class TestWorkloadDetailed(unittest.TestCase):
    """WorkloadDetailed unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkloadDetailed:
        """Test WorkloadDetailed
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkloadDetailed`
        """
        model = WorkloadDetailed()
        if include_optional:
            return WorkloadDetailed(
                slug = '',
                name = '',
                status = '',
                org_slug = '',
                space_slug = '',
                instance_slug = '',
                session_id = '',
                creation_timestamp = '',
                shared = '',
                compute_units = '',
                addons_compute_units = '',
                gpu = '',
                current_cpu = '',
                current_memory = '',
                node_pool = '',
                max_cpu = '',
                max_memory = ''
            )
        else:
            return WorkloadDetailed(
        )
        """

    def testWorkloadDetailed(self):
        """Test WorkloadDetailed"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
