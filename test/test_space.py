# coding: utf-8

"""
    Nuvolos

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: prod
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from nuvolos_client_api.models.space import Space

class TestSpace(unittest.TestCase):
    """Space unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Space:
        """Test Space
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Space`
        """
        model = Space()
        if include_optional:
            return Space(
                archival_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                archive_by_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                database_tables_enabled = True,
                description = '',
                last_modified_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                role = '',
                slug = '',
                type = '',
                video_library_enabled = True,
                visibility_type = ''
            )
        else:
            return Space(
                name = '',
                slug = '',
                type = '',
                video_library_enabled = True,
                visibility_type = '',
        )
        """

    def testSpace(self):
        """Test Space"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
