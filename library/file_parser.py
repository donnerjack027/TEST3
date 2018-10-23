import logging as log
from lxml import html
from library import exceptions


class File_parser:

    @staticmethod
    def parser(filename):
        log.debug("Executing parse file %s" % filename)
        try:
            param = list()
            with open(filename) as xml_file:
                xml = xml_file.read()
            xml_file.close()
            root = html.fromstring(xml.encode('utf-8'))
            count = 0

            while count < len(root.xpath('.//set')):
                temp_list = list()
                temp_list.append(str(root.xpath('.//set/@address')[count]))
                temp_list.append(float(root.xpath('.//set/@lat')[count]))
                temp_list.append(float(root.xpath('.//set/@lon')[count]))
                param.append(temp_list)
                count = count + 1

            return param

        except exceptions.ParseError:
            log.error('Error while parse file')




