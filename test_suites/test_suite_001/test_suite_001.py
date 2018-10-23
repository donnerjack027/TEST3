import pytest
import logging as log
import os
from library.file_parser import File_parser

log.basicConfig(filename="test_suite_001_log.log", level=log.INFO, filemode="w")


"""Раскомментировать при непосредственном ручном запуске test_suite_001.py"""
"""os.chdir('../../')"""


class TestSuite_001:

    @pytest.mark.parametrize("param", File_parser.parser('address_to_coordinates.xml'))
    def test_case_001(self, param):
        log.debug("Running TestSuite_001, test_case_001, address_to_coordinates")
        from test_suites.test_suite_001.test_cases.test_case_001_address_to_coordinates \
            import TestCase_001_address_to_coordinates as TestCase_001
        request_params = {'q': param[0], 'format': 'xml'}
        TestCase_001.test_run(self, request_params, param[1], param[2])

    @pytest.mark.parametrize("param", File_parser.parser('coordinates_to_address.xml'))
    def test_case_002(self, param):
        log.debug("Running TestSuite_001, test_case_002, coordinates_to_address")
        from test_suites.test_suite_001.test_cases.test_case_002_coordinates_to_address \
            import TestCase_002_coordinates_to_address as TestCase_002
        request_params = {'format': 'xml', 'lat': param[1], 'lon': param[2], 'accept-language': 'english'}
        TestCase_002.test_run(self, request_params, param[0])
