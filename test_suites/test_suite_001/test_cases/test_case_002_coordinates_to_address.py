from test_suites.common.ITestCase import ITestCase
from library.request import Request
import requests
import logging as log
from lxml import html
from library import exceptions


class TestCase_002_coordinates_to_address(ITestCase):

    def __init__(self):
        super().__init__()

    def test_run(self, request_params, Address):
        log.info("Running test case %s" % TestCase_002_coordinates_to_address.__name__)
        log.info("Input params: %s" % request_params)
        log.debug("Standart_address: %s" % Address)
        try:
            http_request_name = 'reverse'
            response = Request.prepare_request(http_request_name, request_params)
            if response != requests.exceptions.ReadTimeout and response.status_code != 200:
                raise exceptions.Error(
                    "Error execute request. Status code %s Request: %s, error text: %s " %
                    (response.status_code, response.url, html.fromstring(response.text).xpath('.//errormessage/text()')))

            parsed_body = html.fromstring(response.content)
            log.debug("HTTP response: %s" % response.text)
            response_Address = str(parsed_body.xpath('.//result/text()')[0])
            log.debug("Response_Address: %s" % response_Address)

            assert response_Address == Address, \
                "Address from file doesn't match with address from HTTP response"

        except IndexError:
            log.error('Index error, status code %s, error message: \n %s' % (
                response.status_code, html.fromstring(response.content).xpath('.//error/text()')))
            assert False, 'Index error, status code %s, error message: \n %s' % \
                          (response.status_code, html.fromstring(response.content).xpath('.//error/text()'))

        except AttributeError:
            log.error('Attribute \ timeout error')
            assert False, 'Attribute \ timeout error'