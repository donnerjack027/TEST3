import pytest
import logging as log
from lxml import html
import os


log.basicConfig(filename="test_suite_001_log.log", level=log.INFO, filemode="w")
os.chdir('../../')
class TestSuite_001:

    def test_case_001(self):
        log.debug("Running TestSuite_001, test_case_001, address_to_coordinates")
        from test_suites.test_suite_001.test_cases.test_case_001_address_to_coordinates \
            import TestCase_001_address_to_coordinates as TestCase_001

        with open('address_to_coordinates.xml') as xml_file:
            xml = xml_file.read()
        xml_file.close()
        root = html.fromstring(xml.encode('utf-8'))
        count = 0
        while count < len(root.xpath('.//set')):
            Address = str(root.xpath('.//set/@address')[count])
            lat = float(root.xpath('.//set/@standard_lat')[count])
            lon = float(root.xpath('.//set/@standard_lon')[count])
            request_params = {'q': Address, 'format': 'xml'}
            TestCase_001.test_run(self, request_params, lat, lon)
            count = count+1

    def test_case_002(self):
        log.debug("Running TestSuite_001, test_case_002, coordinates_to_address")
        from test_suites.test_suite_001.test_cases.test_case_002_coordinates_to_address \
            import TestCase_002_coordinates_to_address as TestCase_002

        with open('coordinates_to_address.xml') as xml_file:
            xml = xml_file.read()
        xml_file.close()
        root = html.fromstring(xml.encode('utf-8'))
        count = 0
        while count < len(root.xpath('.//set')):
            Address = str(root.xpath('.//set/@standard_address')[count])
            lat = float(root.xpath('.//set/@lat')[count])
            lon = float(root.xpath('.//set/@lon')[count])
            request_params = {'format': 'xml', 'lat': lat, 'lon': lon, 'accept-language': 'english'}
            TestCase_002.test_run(self, request_params, Address)
            count = count+1
