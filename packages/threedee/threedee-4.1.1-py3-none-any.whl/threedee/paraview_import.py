
#from pyjsparser import PyJsParser
#import esprima

#import xml.etree.ElementTree as ET
import bs4
from bs4 import BeautifulSoup

import json, re, base64, struct

from django.core.files.base import ContentFile


class ParaviewWebGLContent(object):

    def __init__(self, base64_object_streams, metadata):
        self.base64_object_streams = base64_object_streams
        self.object_streams = []
        self.metadata = metadata

        for b64_stream in self.base64_object_streams:
            self.object_streams.append(base64.b64decode(b64_stream))

    def save(self, storage, path):

        metadata_json = json.dumps(self.metadata).encode("utf-8")
        metadata_json_file = ContentFile(metadata_json)
        storage.save(path + "metadata.json", metadata_json_file)

        binary_data = b''

        for stream in self.object_streams:
            binary_data += struct.pack("<I", len(stream) + 4)
            binary_data += stream

        object_streams_file = ContentFile(binary_data)
        storage.save(path + "object_streams.bin", object_streams_file)


def parse_paraview_webgl_content_html_file(file):

    # tree = ET.parse(path)
    # html = tree.getroot()

    html = BeautifulSoup(file, "html5lib")
    return parse_paraview_webgl_content_html_tree(html)


def parse_paraview_webgl_content_html_text(text):

    #html = ET.fromstring(text.decode("utf-8"))

    html = BeautifulSoup(text, "html5lib")
    return parse_paraview_webgl_content_html_tree(html)


def filter_paraview_webgl_content_script(node, data_object_matches, metadata_matches):

    if node.type != "VariableDeclaration":
        return

    if node.declarations[0].id.name == "metadata" and \
        node.declarations[0].id.type == "Identifier":

        metadata_content = json.loads(node.declarations[0].init.value)

        metadata_matches.append(metadata_content)
        return

    if node.declarations[0].id.name == "object" and \
            node.declarations[0].id.type == "Identifier" and \
            node.declarations[0].init.type == "ArrayExpression":

        elements = [x.value for x in node.declarations[0].init.elements if x.type == "Literal"]
        data_object_matches.append(elements)
        return


def parse_paraview_webgl_content_html_tree(html):

    paraview_script_tag = html.find('script')

    if paraview_script_tag is None:
        return ParaviewWebGLContent([], {})

    paraview_script_text = paraview_script_tag.get_text(types=[bs4.element.NavigableString,
                                                               bs4.element.Script])

    return parse_paraview_webgl_content_script(paraview_script_text)


PARAVIEW_RE = re.compile("(var[\s]+metadata[\s]+=[\s]+'(([^']|\\\\')*)';)|(var[\s]+object[\s]+=[\s]+\[([^]]*)];)", re.UNICODE + re.MULTILINE)


def parse_paraview_webgl_content_script(script_text):

    metadata_matches = []
    data_object_matches = []

    #script_parser = esprima.parseScript
    #script_parser(script_text, {}, lambda node, metadata: filter_paraview_webgl_content_script(node, data_object_matches, metadata_matches))
    #result = ParaviewWebGLContent(data_object_matches[0], metadata_matches[0])

    pos = 0

    while pos < len(script_text):

        match = PARAVIEW_RE.search(script_text, pos=pos)

        if match is None:
            break

        if match.group(1):
            metadata_match = match.group(2)
            metadata_matches.append(json.loads(metadata_match))
        elif match.group(4):

            data_object_match = match.group(5)
            data_object_match = '"'.join(data_object_match.split("'"))

            data_object_match = '{ "elements":[' + data_object_match + ']}'
            data_object = json.loads(data_object_match)
            data_object_matches.append(data_object['elements'])

        pos += match.end()

    result = None

    if data_object_matches and metadata_matches:
        result = ParaviewWebGLContent(data_object_matches[0], metadata_matches[0])

    return result

