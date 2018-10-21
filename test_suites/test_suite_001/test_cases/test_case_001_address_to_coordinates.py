from test_suites.common.ITestCase import ITestCase
from library.request import Request
import requests
import logging as log
from lxml import html
from library import exceptions


class TestCase_001_address_to_coordinates(ITestCase):

    def __init__(self):
        super().__init__()

    def test_run(self, request_params, lat, lon):
        log.info("Running test case %s" % TestCase_001_address_to_coordinates.__name__)
        log.info("Input params: %s" % request_params)
        log.debug("Standart_lat: %s" % lat)
        log.debug("Standart_lon: %s" % lon)
        try:
            http_request_name = 'search'
            response = Request.prepare_request(http_request_name, request_params)
            if response != requests.exceptions.ReadTimeout and response.status_code != 200:
                raise exceptions.Error(
                    "Error execute request. Status code %s Request: %s, error text: %s " %
                    (response.status_code, response.url, html.fromstring(response.text).xpath('.//errormessage/text()')))

            parsed_body = html.fromstring(response.content)
            log.debug("HTTP response: %s" % response.text)
            response_lat = float(parsed_body.xpath('.//place/@lat')[0])
            response_lon = float(parsed_body.xpath('.//place/@lon')[0])
            log.debug("Response_lat: %s" % response_lat)
            log.debug("Response_lon: %s" % response_lon)

            assert response_lat == lat, \
                "Latitude from file doesn't match with latitude from HTTP response"
            assert response_lon == lon, \
                "Longitude from file doesn't match with longitude from HTTP response"

        except IndexError:
            log.error('Index error, status code %s, error message: \n %s' % (
                response.status_code, html.fromstring(response.content).xpath('.//error/text()')))
            assert False, 'Index error, status code %s, error message: \n %s' % \
                          (response.status_code, html.fromstring(response.content).xpath('.//error/text()'))

        except AttributeError:
            log.error('Attribute \ timeout error')
            assert False, 'Attribute \ timeout error'