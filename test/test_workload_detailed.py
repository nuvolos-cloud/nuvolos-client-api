# coding: utf-8

"""
    Nuvolos

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: dev
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from nuvolos_client_api.models.workload_detailed import WorkloadDetailed

class TestWorkloadDetailed(unittest.TestCase):
    """WorkloadDetailed unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkloadDetailed:
        """Test WorkloadDetailed
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkloadDetailed`
        """
        model = WorkloadDetailed()
        if include_optional:
            return WorkloadDetailed(
                addons_compute_units = '',
                compute_units = '',
                creation_timestamp = '',
                current_cpu = '',
                current_memory = '',
                gpu = '',
                instance_slug = '',
                max_cpu = '',
                max_memory = '',
                name = '',
                node_pool = '',
                org_slug = '',
                session_id = '',
                shared = '',
                slug = '',
                space_slug = '',
                status = ''
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
