# coding: utf-8

"""
    Stable Diffusion

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.default_api import DefaultApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_txt2img(self):
        """Test case for txt2img

        Generate an image using a text prompt  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()