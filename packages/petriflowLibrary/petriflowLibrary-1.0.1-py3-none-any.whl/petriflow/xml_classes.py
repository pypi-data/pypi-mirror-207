#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Generated Fri Dec 16 21:03:57 2022 by generateDS.py version 2.41.1.
# Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)]
#
# Command line options:
#   ('-o', 'xml_classes.py')
#   ('-s', 'xml_subclasses.py')
#   ('--super', 'xml_classes')
#   ('--member-specs', 'dict')
#
# Command line arguments:
#   xsd_scheme/petriflow.schema.xsd
#
# Command line:
#   D:/PyCharm Projects/petriflowLibrary/venv/Scripts/generateDS.py -o "xml_classes.py" -s "xml_subclasses.py" --super="xml_classes" --member-specs="dict" resources/petriflow.schema.xsd
#
# Current working directory (os.getcwd()):
#   petriflowLibrary
#

import sys
from six.moves import zip_longest
from urllib.request import urlopen
import os
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_

try:
    from lxml import etree as etree_
except ImportError:
    from xml.etree import ElementTree as etree_

Validate_simpletypes_ = True
SaveElementTreeNode = True
TagNamePrefix = ""


def parse_xml_(infile, parser=None, **kwargs):
    """
    First, using the ElementTree API, we get a parser, thanks to which we then analyze the document file object.
    :param infile: document file object, usually file system path
        The ``infile`` can be any of the following:

            - a file name/path
            - a file object
            - a file-like object

    :param parser: If no parser is provided as second argument, the default parser is used.
    :return: An ElementTree object loaded with source elements.
    """
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        # if infile is type of object implementing the os.PathLike protocol (representing a file system path)
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc


def parse_xml_string_(instring, parser=None, **kwargs):
    """

    :param instring: can be a URL using the HTTP or FTP protocol, because return value from URL is not xml, but string
    :param parser: If no parser is provided as second argument, the default parser is used.
    :return: The root node (or the result returned by a parser target).
    """
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element


def set_namespace_defs(root_node, root_tag="document"):
    """
    Get all name space prefix definitions required in this XML doc including attributes
    :param root_node: node representing the root element of this tree
    :param root_tag: usually has a value of root element tag , for example "document"
    :return:
    """
    ns_map = {
        prefix: uri
        for node in root_node.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespace_defs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in ns_map.items()
    ])

    ns_string = ""
    for node in root_node.iter():
        if node.tag == root_tag:
            for key in node.attrib.keys():
                if node.nsmap.get("xsi") is not None:
                    ns_string += " xsi:"
                    ns_string += key.split('}')[-1]
                    ns_string += "="
                    ns_string += '\"' + node.attrib.get(key) + '\"'
    dict_ = {root_tag: namespace_defs + ns_string}
    GenerateDSNamespaceDefs_.clear()
    GenerateDSNamespaceDefs_.update(dict_)


def set_boolean_value(input_data):
    if input_data is True or input_data is False:
        if input_data is True:
            return 'true'
        return 'false'
    elif isinstance(input_data, str):
        if input_data.lower() in ('true', '1'):
            return 'true'
        elif input_data.lower() in ('false', '0'):
            return 'false'
        else:
            raise TypeError("Requires boolean value")
    elif isinstance(input_data, int):
        if input_data == 1:
            return 'true'
        elif input_data == 0:
            return 'false'
        else:
            raise TypeError("Requires boolean value")
    else:
        raise TypeError("Requires boolean value")


#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the _exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ImportError:
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ImportError:
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ImportError:

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))

#
# The super-class for enum types
#

try:
    from enum import Enum
except ImportError:
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError as exp:
    try:
        from generatedssupersuper import GeneratedsSuperSuper
    except ImportError as exp:
        class GeneratedsSuperSuper(object):
            pass


    class GeneratedsSuper(GeneratedsSuperSuper):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')

        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name

            def utcoffset(self, dt):
                return self.__offset

            def tzname(self, dt):
                return self.__name

            def dst(self, dt):
                return None

        def __str__(self):
            settings = {
                'str_pretty_print': True,
                'str_indent_level': 0,
                'str_namespaceprefix': '',
                'str_name': self.__class__.__name__,
                'str_namespacedefs': '',
            }
            for n in settings:
                if hasattr(self, n):
                    settings[n] = getattr(self, n)
            from io import StringIO
            output = StringIO()
            self.export(
                output,
                settings['str_indent_level'],
                pretty_print=settings['str_pretty_print'],
                namespaceprefix_=settings['str_namespaceprefix'],
                name_=settings['str_name'],
                namespacedef_=settings['str_namespacedefs']
            )
            strval = output.getvalue()
            output.close()
            return strval

        def gds_format_string(self, input_data, input_name=''):
            return input_data

        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data

        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data

        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data).decode('ascii')

        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data

        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % int(input_data)

        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival

        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value

        def gds_format_integer_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], str):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)

        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer values')
            return values

        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % float(input_data)).rstrip('0')

        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_

        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value

        def gds_format_float_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], str):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)

        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values

        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value

        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value

        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value

        def gds_format_decimal_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], str):
                input_data = [str(s) for s in input_data]
            return ' '.join([self.gds_format_decimal(item) for item in input_data])

        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values

        def gds_format_double(self, input_data, input_name=''):
            return '%s' % input_data

        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_

        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value

        def gds_format_double_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], str):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)

        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values

        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()

        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            input_data = input_data.strip()
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval

        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0,):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data

        def gds_format_boolean_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], str):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)

        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                value = self.gds_parse_boolean(value, node, input_name)
                if value not in (True, 1, False, 0,):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values

        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data

        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue

        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"),)
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt

        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data

        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue

        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()

        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data

        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue

        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            target = str(target)
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1

        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()

        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None:
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))

        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))

        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))

        def gds_str_lower(self, instring):
            return instring.lower()

        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path

        Tag_strip_pattern_ = re_.compile(r'\{.*\}')

        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)

        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1

        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content

        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))

        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring

        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring,
                                                            str):  # unicode has changed to bytes , bytes to str
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result

        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')

            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))

        def __ne__(self, other):
            return not self.__eq__(other)

        # Django ETL transform hooks. zbytocne
        def gds_djo_etl_transform(self):
            pass

        # zbytocne
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass

        # SQLAlchemy ETL transform hooks. zbytocne
        def gds_sqa_etl_transform(self):
            return 0, None

        # zbytocne
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass

        # zbytocne
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""


    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None

#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None


#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, str) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, str) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    s1 = s1.replace('\n', '&#10;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        if prefix == 'xml':
            namespace = 'http://www.w3.org/XML/1998/namespace'
        else:
            namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name,))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline,)
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8

    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value

    def getCategory(self):
        return self.category

    def getContenttype(self, content_type):
        return self.content_type

    def getValue(self):
        return self.value

    def getName(self):
        return self.name

    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:  # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)

    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))

    def to_etree(self, element, mapping_=None, reverse_mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:  # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)

    def to_etree_simple(self, mapping_=None, reverse_mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
              self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
              self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text

    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:  # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
                 optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_data_type(self, data_type):
        self.data_type = data_type

    def get_data_type_chain(self):
        return self.data_type

    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type

    def set_container(self, container):
        self.container = container

    def get_container(self):
        return self.container

    def set_child_attrs(self, child_attrs):
        self.child_attrs = child_attrs

    def get_child_attrs(self):
        return self.child_attrs

    def set_choice(self, choice):
        self.choice = choice

    def get_choice(self):
        return self.choice

    def set_optional(self, optional):
        self.optional = optional

    def get_optional(self):
        return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)


#
# Data representation classes.
#


class appearance(str, Enum):
    STANDARD = 'standard'
    OUTLINE = 'outline'
    FILL = 'fill'
    LEGACY = 'legacy'


class arc_type(str, Enum):
    REGULAR = 'regular'
    RESET = 'reset'
    INHIBITOR = 'inhibitor'
    READ = 'read'
    VARIABLE = 'variable'


class assignPolicy(str, Enum):
    AUTO = 'auto'
    MANUAL = 'manual'


class behavior(str, Enum):
    FORBIDDEN = 'forbidden'
    HIDDEN = 'hidden'
    VISIBLE = 'visible'
    EDITABLE = 'editable'
    REQUIRED = 'required'
    IMMEDIATE = 'immediate'
    OPTIONAL = 'optional'


class buttonTypeType(str, Enum):
    STANDARD = 'standard'
    RAISED = 'raised'
    STROKED = 'stroked'
    FLAT = 'flat'
    ICON = 'icon'
    FAB = 'fab'
    MINIFAB = 'minifab'


class caseEventType(str, Enum):
    CREATE = 'create'
    DELETE = 'delete'


class compactDirection(str, Enum):
    NONE = 'none'
    UP = 'up'


class dataEventType(str, Enum):
    SET = 'set'
    GET = 'get'


class dataFocusPolicy(str, Enum):
    MANUAL = 'manual'
    AUTO_EMPTY_REQUIRED = 'auto_empty_required'


class dataGroupAlignment(str, Enum):
    START = 'start'
    CENTER = 'center'
    END = 'end'
    LEFT = 'left'


class data_type(str, Enum):
    NUMBER = 'number'
    TEXT = 'text'
    ENUMERATION = 'enumeration'
    ENUMERATION_MAP = 'enumeration_map'
    MULTICHOICE = 'multichoice'
    MULTICHOICE_MAP = 'multichoice_map'
    BOOLEAN = 'boolean'
    DATE = 'date'
    FILE = 'file'
    FILE_LIST = 'fileList'
    USER = 'user'
    USER_LIST = 'userList'
    DATE_TIME = 'dateTime'
    BUTTON = 'button'
    TASK_REF = 'taskRef'
    CASE_REF = 'caseRef'
    FILTER = 'filter'
    I_18_N = 'i18n'


class empty(str, Enum):
    _ = ''


class eventPhaseType(str, Enum):
    PRE = 'pre'
    POST = 'post'


class eventType(str, Enum):
    ASSIGN = 'assign'
    CANCEL = 'cancel'
    FINISH = 'finish'
    DELEGATE = 'delegate'


class fieldAlignment(str, Enum):
    TOP = 'top'
    CENTER = 'center'
    BOTTOM = 'bottom'


class finishPolicy(str, Enum):
    AUTO_NO_DATA = 'auto_no_data'
    MANUAL = 'manual'


class hideEmptyRows(str, Enum):
    ALL = 'all'
    COMPACTED = 'compacted'
    NONE = 'none'


class iconType(str, Enum):
    MATERIAL = 'material'
    SVG = 'svg'


class layoutType(str, Enum):
    FLOW = 'flow'
    GRID = 'grid'
    LEGACY = 'legacy'


class processEventType(str, Enum):
    UPLOAD = 'upload'


class scope(str, Enum):
    NAMESPACE = 'namespace'
    PROCESS = 'process'


class template(str, Enum):
    MATERIAL = 'material'
    NETGRIF = 'netgrif'


class triggerType(str, Enum):
    AUTO = 'auto'
    USER = 'user'
    TIME = 'time'


class transaction(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'id': MemberSpec_('id', 'xs:string', 0, 0, {'name': 'id', 'type': 'xs:string'}, None),
        'title': MemberSpec_('title', 'i18nStringType', 0, 0, {'name': 'title', 'type': 'i18nStringType'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, id=None, title=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = id
        self.id_nsprefix_ = None
        self.title = title
        self.title_nsprefix_ = None

    #
    def factory(*args_, **kwargs_):
        """
        Create a document object
        :param args_:
        :param kwargs_:
        :return:
        """
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, transaction)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if transaction.subclass:
            return transaction.subclass(*args_, **kwargs_)
        else:
            return transaction(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_id(self):
        return self.id

    def set_id(self, id_):
        if type(id_) is str:
            self.id = id_
        else:
            raise TypeError("Requires str value")

    def get_title(self):
        return self.title

    def set_title(self, title):
        if type(title) is i18nStringType:
            self.title = title
        else:
            raise TypeError("Requires i18nStringType value")

    def _hasContent(self):
        if (
                self.id is not None or
                self.title is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='transaction', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('transaction')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'transaction':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='transaction')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='transaction',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='transaction'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='transaction',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.id is not None:
            namespaceprefix_ = self.id_nsprefix_ + ':' if (UseCapturedNS_ and self.id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sid>%s</%sid>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.id), input_name='id')),
                namespaceprefix_, eol_))
        if self.title is not None:
            namespaceprefix_ = self.title_nsprefix_ + ':' if (UseCapturedNS_ and self.title_nsprefix_) else ''
            self.title.export(outfile, level, namespaceprefix_, namespacedef_='', name_='title',
                              pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):  # , gds_collector_=None
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_,
                                gds_collector_=gds_collector_)  # , gds_collector_=gds_collector_
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'id')
            value_ = self.gds_validate_string(value_, node, 'id')
            self.id = value_
            self.id_nsprefix_ = child_.prefix
        elif nodeName_ == 'title':
            class_obj_ = self.get_class_obj_(child_, i18nStringType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.title = obj_
            obj_.original_tagname_ = 'title'


# end class transaction


class data(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'type_': MemberSpec_('type_', 'data_type', 0, 0, {'use': 'required', 'name': 'type_'}),
        'immediate': MemberSpec_('immediate', 'xs:boolean', 0, 1, {'use': 'optional', 'name': 'immediate'}),
        'id': MemberSpec_('id', 'xs:string', 0, 0, {'name': 'id', 'type': 'xs:string'}, None),
        'title': MemberSpec_('title', 'i18nStringType', 0, 0, {'name': 'title', 'type': 'i18nStringType'}, None),
        'placeholder': MemberSpec_('placeholder', 'i18nStringType', 0, 1,
                                   {'minOccurs': '0', 'name': 'placeholder', 'type': 'i18nStringType'}, None),
        'desc': MemberSpec_('desc', 'i18nStringType', 0, 1,
                            {'minOccurs': '0', 'name': 'desc', 'type': 'i18nStringType'}, None),
        'values': MemberSpec_('values', 'i18nStringTypeWithExpression', 1, 1,
                              {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'values',
                               'type': 'i18nStringTypeWithExpression'}, 1),
        'options': MemberSpec_('options', 'options', 0, 1, {'minOccurs': '0', 'name': 'options', 'type': 'options'}, 1),
        'valid': MemberSpec_('valid', 'valid', 1, 1,
                             {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'valid', 'type': 'valid'}, 2),
        'validations': MemberSpec_('validations', 'validations', 0, 1,
                                   {'minOccurs': '0', 'name': 'validations', 'type': 'validations'}, 2),
        'init': MemberSpec_('init', 'init', 0, 1, {'minOccurs': '0', 'name': 'init', 'type': 'init'}, 3),
        'inits': MemberSpec_('inits', 'inits', 0, 1, {'minOccurs': '0', 'name': 'inits', 'type': 'inits'}, 3),
        'format': MemberSpec_('format', 'format', 0, 1, {'minOccurs': '0', 'name': 'format', 'type': 'format'}, None),
        'view': MemberSpec_('view', 'fieldView', 0, 1, {'minOccurs': '0', 'name': 'view', 'type': 'fieldView'}, 4),
        'component': MemberSpec_('component', 'component', 0, 1,
                                 {'minOccurs': '0', 'name': 'component', 'type': 'component'}, None),
        'encryption': MemberSpec_('encryption', 'encryption', 0, 1,
                                  {'minOccurs': '0', 'name': 'encryption', 'type': 'encryption'}, None),
        'action': MemberSpec_('action', 'action', 1, 1,
                              {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'action', 'type': 'action'}, 5),
        'event': MemberSpec_('event', 'event', 1, 1,
                             {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'event', 'type': 'dataEvent'}, 5),
        'actionRef': MemberSpec_('actionRef', 'actionRef', 1, 1,
                                 {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'actionRef', 'type': 'actionRef'},
                                 None),
        'documentRef': MemberSpec_('documentRef', 'documentRef', 0, 1,
                                   {'minOccurs': '0', 'name': 'documentRef', 'type': 'documentRef'}, None),
        'remote': MemberSpec_('remote', ['remote', 'xs:string'], 0, 1,
                              {'minOccurs': '0', 'name': 'remote', 'type': 'xs:string'}, None),
        'length': MemberSpec_('length', 'xs:int', 0, 1, {'minOccurs': '0', 'name': 'length', 'type': 'xs:int'}, None),
        'allowedNets': MemberSpec_('allowedNets', 'allowedNets', 0, 1,
                                   {'minOccurs': '0', 'name': 'allowedNets', 'type': 'allowedNets'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, type_=None, immediate=None, id=None, title=None, placeholder=None, desc=None, values=None,
                 options=None, valid=None, validations=None, init=None, inits=None, format=None, view=None,
                 component=None, encryption=None, action=None, event=None, actionRef=None, documentRef=None,
                 remote=None, length=None, allowedNets=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
        self.immediate = _cast(bool, immediate)
        self.immediate_nsprefix_ = None
        self.id = id
        self.id_nsprefix_ = None
        self.title = title
        self.title_nsprefix_ = None
        self.placeholder = placeholder
        self.placeholder_nsprefix_ = None
        self.desc = desc
        self.desc_nsprefix_ = None
        if values is None:
            self.values = []
        else:
            self.values = values
        self.values_nsprefix_ = None
        self.options = options
        self.options_nsprefix_ = None
        if valid is None:
            self.valid = []
        else:
            self.valid = valid
        self.valid_nsprefix_ = None
        self.validations = validations
        self.validations_nsprefix_ = None
        self.init = init
        self.init_nsprefix_ = None
        self.inits = inits
        self.inits_nsprefix_ = None
        self.format = format
        self.format_nsprefix_ = None
        self.view = view
        self.view_nsprefix_ = None
        self.component = component
        self.component_nsprefix_ = None
        self.encryption = encryption
        self.encryption_nsprefix_ = None
        if action is None:
            self.action = []
        else:
            self.action = action
        self.action_nsprefix_ = None
        if event is None:
            self.event = []
        else:
            self.event = event
        self.event_nsprefix_ = None
        if actionRef is None:
            self.actionRef = []
        else:
            self.actionRef = actionRef
        self.actionRef_nsprefix_ = None
        self.documentRef = documentRef
        self.documentRef_nsprefix_ = None
        self.remote = remote
        self.validate_remote(self.remote)
        self.remote_nsprefix_ = None
        self.length = length
        self.length_nsprefix_ = None
        self.allowedNets = allowedNets
        self.allowedNets_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, data)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if data.subclass:
            return data.subclass(*args_, **kwargs_)
        else:
            return data(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_id(self):
        return self.id

    def set_id(self, id_, doc):
        if type(id_) is str:
            if all(x.id != id_ for x in doc.data):
                self.id = id_
            else:
                raise ValueError("Requires unique id value")
        else:
            raise TypeError("Requires str value")

    def get_title(self):
        return self.title

    def set_title(self, title):
        if type(title) is i18nStringType:
            self.title = title
        else:
            raise TypeError("Requires i18nStringType value")

    def get_placeholder(self):
        return self.placeholder

    def set_placeholder(self, placeholder):
        if type(placeholder) is i18nStringType:
            self.placeholder = placeholder
        else:
            raise TypeError("Requires i18nStringType value")

    def get_desc(self):
        return self.desc

    def set_desc(self, desc):
        if type(desc) is i18nStringType:
            self.desc = desc
        else:
            raise TypeError("Requires i18nStringType value")

    def get_values(self):
        return self.values

    def set_values(self, values_):
        if self.options is None:
            if all(isinstance(x, i18nStringTypeWithExpression) for x in values_):
                self.values = values_
            else:
                raise TypeError("Requires i18nStringTypeWithExpression values inside an array")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'options' element.")

    def add_values(self, value):
        if self.options is None:
            if type(value) is i18nStringTypeWithExpression:
                self.values.append(value)
            else:
                raise TypeError("Requires i18nStringTypeWithExpression value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'options' element.")

    def insert_values_at(self, index, value):
        if self.options is None:
            if 0 <= index <= len(self.values):
                if type(value) is i18nStringTypeWithExpression:
                    self.values.insert(index, value)
                else:
                    raise TypeError("Requires only i18nStringTypeWithExpression value inside an array")
            else:
                raise IndexError("Invalid index value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'options' element.")

    def replace_values_at(self, index, value):
        if self.options is None:
            if 0 <= index < len(self.values):
                if self.values[index]:
                    if type(value) is i18nStringTypeWithExpression:
                        self.values[index] = value
                    else:
                        raise TypeError("Requires i18nStringTypeWithExpression value")
                else:
                    raise Exception("Invalid index value")
            else:
                raise IndexError("Index out of range")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'options' element.")

    def get_options(self):
        return self.options

    def set_options(self, options_):
        if not self.values:
            if type(options_) is options:
                self.options = options_
            else:
                raise TypeError("Requires options value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'values' element.")

    def get_valid(self):
        return self.valid

    def set_valid(self, valid_):
        if self.validations is None:
            if all(isinstance(x, valid) for x in valid_):
                self.valid = valid_
            else:
                raise TypeError("Requires only i18nStringTypeWithExpression values inside an array")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'validations' element.")

    def add_valid(self, value):
        if self.validations is None:
            if type(value) is valid:
                self.valid.append(value)
            else:
                raise TypeError("Requires valid value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'validations' element.")

    def insert_valid_at(self, index, value):
        if self.validations is None:
            if 0 <= index <= len(self.valid):
                if type(value) is valid:
                    self.valid.insert(index, value)
                else:
                    raise TypeError("Requires valid value")
            else:
                raise IndexError("Invalid index value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'validations' element.")

    def replace_valid_at(self, index, value):
        if self.validations is None:
            if 0 <= index < len(self.valid):
                if self.valid[index]:
                    if type(value) is valid:
                        self.valid[index] = value
                    else:
                        raise TypeError("Requires valid value")
                else:
                    raise Exception("Invalid index value")
            else:
                raise IndexError("Index out of range")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'validations' element.")

    def get_validations(self):
        return self.validations

    def set_validations(self, validations_):
        if not self.valid:
            if type(validations_) is validations:
                self.validations = validations_
            else:
                raise TypeError("Requires validations value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'valid' element.")

    def get_init(self):
        return self.init

    def set_init(self, init_):
        if not self.inits:
            if type(init_) is init:
                self.init = init_
            else:
                raise TypeError("Requires init value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'inits' element.")

    def get_inits(self):
        return self.inits

    def set_inits(self, inits_):
        if not self.init:
            if type(inits_) is inits:
                self.inits = inits_
            else:
                raise TypeError("Requires inits value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'init' element.")

    def get_format(self):
        return self.format

    def set_format(self, format_):
        if type(format_) is format:
            self.format = format_
        else:
            raise TypeError("Requires format value")

    def get_view(self):
        return self.view

    def set_view(self, view):
        if type(view) is fieldView:
            self.view = view
        else:
            raise TypeError("Requires fieldView value")

    def get_component(self):
        return self.component

    def set_component(self, component_):
        if type(component_) is component:
            self.component = component_
        else:
            raise TypeError("Requires component value")

    def get_encryption(self):
        return self.encryption

    def set_encryption(self, encryption_):
        if type(encryption_) is encryption:
            self.encryption = encryption_
        else:
            raise TypeError("Requires encryption value")

    def get_action(self):
        return self.action

    def set_action(self, action_):
        if not self.event:
            if all(isinstance(x, action) for x in action_):
                self.action = action_
            else:
                raise TypeError("Requires only action values inside an array")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'event' element.")

    def add_action(self, value):
        if not self.event:
            if type(value) is action:
                self.action.append(value)
            else:
                raise TypeError("Requires action value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'event' element.")

    def insert_action_at(self, index, value):
        if not self.event:
            if 0 <= index <= len(self.action):
                if type(value) is action:
                    self.action.insert(index, value)
                else:
                    raise TypeError("Requires action value")
            else:
                raise IndexError("Invalid index value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'event' element.")

    def replace_action_at(self, index, value):
        if not self.event:
            if 0 <= index < len(self.action):
                if self.action[index]:
                    if type(value) is action:
                        self.action[index] = value
                    else:
                        raise TypeError("Requires action value")
                else:
                    raise Exception("Invalid index value")
            else:
                raise IndexError("Index out of range")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'event' element.")

    def get_event(self):
        return self.event

    # if you want your own specific event list , else it is an empty list
    def set_event(self, event_):
        if not self.action:
            if all(isinstance(x, dataEvent) for x in event_):
                self.event = event_
            else:
                raise TypeError("Requires only dataEvent values inside an array")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'action' element.")

    def add_event(self, value):
        if not self.action:
            if type(value) is dataEvent:
                self.event.append(value)
            else:
                raise TypeError("Requires dataEvent value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'action' element.")

    def insert_event_at(self, index, value):
        if not self.action:
            if 0 <= index <= len(self.event):
                if type(value) is dataEvent:
                    self.event.insert(index, value)
                else:
                    raise TypeError("Requires dataEvent value")
            else:
                raise IndexError("Invalid index value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'action' element.")

    def replace_event_at(self, index, value):
        if not self.action:
            if 0 <= index < len(self.event):
                if self.event[index]:
                    if type(value) is dataEvent:
                        self.event[index] = value
                    else:
                        raise TypeError("Requires dataEvent value")
                else:
                    raise Exception("Invalid index value")
            else:
                raise IndexError("Index out of range")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'action' element.")

    def get_actionRef(self):
        return self.actionRef

    def set_actionRef(self, actionRef_):
        if all(isinstance(x, actionRef) for x in actionRef_):
            self.actionRef = actionRef_
        else:
            raise TypeError("Requires only actionRef values inside an array")

    def add_actionRef(self, value):
        if type(value) is actionRef:
            self.actionRef.append(value)
        else:
            raise TypeError("Requires actionRef value")

    def insert_actionRef_at(self, index, value):
        if 0 <= index <= len(self.actionRef):
            if type(value) is actionRef:
                self.actionRef.insert(index, value)
            else:
                raise TypeError("Requires actionRef value")
        else:
            raise IndexError("Invalid index value")

    def replace_actionRef_at(self, index, value):
        if 0 <= index < len(self.actionRef):
            if self.actionRef[index]:
                if type(value) is actionRef:
                    self.actionRef[index] = value
                else:
                    raise TypeError("Requires actionRef value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_documentRef(self):
        return self.documentRef

    def set_documentRef(self, documentRef_):
        if type(documentRef_) is documentRef:
            self.documentRef = documentRef_
        else:
            raise TypeError("Requires documentRef value")

    def get_remote(self):
        return self.remote

    def set_remote(self, remote):
        if len(remote) > 0:
            raise ValueError("The 'remote' element can only contain an empty string.")
        else:
            self.remote = remote

    def get_length(self):
        return self.length

    def set_length(self, length):
        if type(length) is int:
            self.length = length
        else:
            raise TypeError("Requires int value")

    def get_allowedNets(self):
        return self.allowedNets

    def set_allowedNets(self, allowedNets_):
        if type(allowedNets_) is allowedNets:
            self.allowedNets = allowedNets_
        else:
            raise TypeError("Requires allowedNets_ value")

    def get_type(self):
        return self.type_

    def set_type_(self, type_):
        if type(type_) is data_type:
            self.type_ = type_
        else:
            raise TypeError("Requires data_type value")

    def get_immediate(self):
        return self.immediate

    def set_immediate(self, immediate):
        self.immediate = set_boolean_value(immediate)

    def validate_remote(self, value):
        result = True
        # Validate type remote, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            if len(value) > 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on remote' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
        return result

    def validate_data_type(self, value):
        # Validate type data_type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['number', 'text', 'enumeration', 'enumeration_map', 'multichoice', 'multichoice_map',
                            'boolean', 'date', 'file', 'fileList', 'user', 'userList', 'dateTime', 'button', 'taskRef',
                            'caseRef', 'filter', 'i18n']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on data_type' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False

    def _hasContent(self):
        if (
                self.id is not None or
                self.title is not None or
                self.placeholder is not None or
                self.desc is not None or
                self.values or
                self.options is not None or
                self.valid or
                self.validations is not None or
                self.init is not None or
                self.inits is not None or
                self.format is not None or
                self.view is not None or
                self.component is not None or
                self.encryption is not None or
                self.action or
                self.event or
                self.actionRef or
                self.documentRef is not None or
                self.remote is not None or
                self.length is not None or
                self.allowedNets is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='data', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('data')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'data':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='data')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='data',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='data'):
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(
                ' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')),))
        if self.immediate is not None and 'immediate' not in already_processed:
            already_processed.add('immediate')
            outfile.write(' immediate="%s"' % self.gds_format_boolean(self.immediate, input_name='immediate'))

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='data', fromsubclass_=False,
                        pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.id is not None:
            namespaceprefix_ = self.id_nsprefix_ + ':' if (UseCapturedNS_ and self.id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sid>%s</%sid>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.id), input_name='id')),
                namespaceprefix_, eol_))
        if self.title is not None:
            namespaceprefix_ = self.title_nsprefix_ + ':' if (UseCapturedNS_ and self.title_nsprefix_) else ''
            self.title.export(outfile, level, namespaceprefix_, namespacedef_='', name_='title',
                              pretty_print=pretty_print)
        if self.placeholder is not None:
            namespaceprefix_ = self.placeholder_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.placeholder_nsprefix_) else ''
            self.placeholder.export(outfile, level, namespaceprefix_, namespacedef_='', name_='placeholder',
                                    pretty_print=pretty_print)
        if self.desc is not None:
            namespaceprefix_ = self.desc_nsprefix_ + ':' if (UseCapturedNS_ and self.desc_nsprefix_) else ''
            self.desc.export(outfile, level, namespaceprefix_, namespacedef_='', name_='desc',
                             pretty_print=pretty_print)
        for values_ in self.values:
            namespaceprefix_ = self.values_nsprefix_ + ':' if (UseCapturedNS_ and self.values_nsprefix_) else ''
            values_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='values',
                           pretty_print=pretty_print)
        if self.options is not None:
            namespaceprefix_ = self.options_nsprefix_ + ':' if (UseCapturedNS_ and self.options_nsprefix_) else ''
            self.options.export(outfile, level, namespaceprefix_, namespacedef_='', name_='options',
                                pretty_print=pretty_print)
        for valid_ in self.valid:
            namespaceprefix_ = self.valid_nsprefix_ + ':' if (UseCapturedNS_ and self.valid_nsprefix_) else ''
            valid_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='valid', pretty_print=pretty_print)
        if self.validations is not None:
            namespaceprefix_ = self.validations_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.validations_nsprefix_) else ''
            self.validations.export(outfile, level, namespaceprefix_, namespacedef_='', name_='validations',
                                    pretty_print=pretty_print)
        if self.init is not None:
            namespaceprefix_ = self.init_nsprefix_ + ':' if (UseCapturedNS_ and self.init_nsprefix_) else ''
            self.init.export(outfile, level, namespaceprefix_, namespacedef_='', name_='init',
                             pretty_print=pretty_print)
        if self.inits is not None:
            namespaceprefix_ = self.inits_nsprefix_ + ':' if (UseCapturedNS_ and self.inits_nsprefix_) else ''
            self.inits.export(outfile, level, namespaceprefix_, namespacedef_='', name_='inits',
                              pretty_print=pretty_print)
        if self.format is not None:
            namespaceprefix_ = self.format_nsprefix_ + ':' if (UseCapturedNS_ and self.format_nsprefix_) else ''
            self.format.export(outfile, level, namespaceprefix_, namespacedef_='', name_='format',
                               pretty_print=pretty_print)
        if self.view is not None:
            namespaceprefix_ = self.view_nsprefix_ + ':' if (UseCapturedNS_ and self.view_nsprefix_) else ''
            self.view.export(outfile, level, namespaceprefix_, namespacedef_='', name_='view',
                             pretty_print=pretty_print)
        if self.component is not None:
            namespaceprefix_ = self.component_nsprefix_ + ':' if (UseCapturedNS_ and self.component_nsprefix_) else ''
            self.component.export(outfile, level, namespaceprefix_, namespacedef_='', name_='component',
                                  pretty_print=pretty_print)
        if self.encryption is not None:
            namespaceprefix_ = self.encryption_nsprefix_ + ':' if (UseCapturedNS_ and self.encryption_nsprefix_) else ''
            self.encryption.export(outfile, level, namespaceprefix_, namespacedef_='', name_='encryption',
                                   pretty_print=pretty_print)
        for action_ in self.action:
            namespaceprefix_ = self.action_nsprefix_ + ':' if (UseCapturedNS_ and self.action_nsprefix_) else ''
            action_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='action',
                           pretty_print=pretty_print)
        for event_ in self.event:
            namespaceprefix_ = self.event_nsprefix_ + ':' if (UseCapturedNS_ and self.event_nsprefix_) else ''
            event_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='event', pretty_print=pretty_print)
        for actionRef_ in self.actionRef:
            namespaceprefix_ = self.actionRef_nsprefix_ + ':' if (UseCapturedNS_ and self.actionRef_nsprefix_) else ''
            actionRef_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='actionRef',
                              pretty_print=pretty_print)
        if self.documentRef is not None:
            namespaceprefix_ = self.documentRef_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.documentRef_nsprefix_) else ''
            self.documentRef.export(outfile, level, namespaceprefix_, namespacedef_='', name_='documentRef',
                                    pretty_print=pretty_print)
        if self.remote is not None:
            namespaceprefix_ = self.remote_nsprefix_ + ':' if (UseCapturedNS_ and self.remote_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sremote>%s</%sremote>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.remote), input_name='remote')),
                namespaceprefix_, eol_))
        if self.length is not None:
            namespaceprefix_ = self.length_nsprefix_ + ':' if (UseCapturedNS_ and self.length_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slength>%s</%slength>%s' % (
                namespaceprefix_, self.gds_format_integer(self.length, input_name='length'), namespaceprefix_, eol_))
        if self.allowedNets is not None:
            namespaceprefix_ = self.allowedNets_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.allowedNets_nsprefix_) else ''
            self.allowedNets.export(outfile, level, namespaceprefix_, namespacedef_='', name_='allowedNets',
                                    pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.validate_data_type(self.type_)  # validate type data_type
        value = find_attr_value_('immediate', node)
        if value is not None and 'immediate' not in already_processed:
            already_processed.add('immediate')
            if value in ('true', '1'):
                self.immediate = True
            elif value in ('false', '0'):
                self.immediate = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'id')
            value_ = self.gds_validate_string(value_, node, 'id')
            self.id = value_
            self.id_nsprefix_ = child_.prefix
        elif nodeName_ == 'title':
            class_obj_ = self.get_class_obj_(child_, i18nStringType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.title = obj_
            obj_.original_tagname_ = 'title'
        elif nodeName_ == 'placeholder':
            class_obj_ = self.get_class_obj_(child_, i18nStringType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.placeholder = obj_
            obj_.original_tagname_ = 'placeholder'
        elif nodeName_ == 'desc':
            class_obj_ = self.get_class_obj_(child_, i18nStringType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.desc = obj_
            obj_.original_tagname_ = 'desc'
        elif nodeName_ == 'values':
            class_obj_ = self.get_class_obj_(child_, i18nStringTypeWithExpression)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.values.append(obj_)
            obj_.original_tagname_ = 'values'
        elif nodeName_ == 'options':
            obj_ = options.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.options = obj_
            obj_.original_tagname_ = 'options'
        elif nodeName_ == 'valid':
            obj_ = valid.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.valid.append(obj_)
            obj_.original_tagname_ = 'valid'
        elif nodeName_ == 'validations':
            obj_ = validations.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.validations = obj_
            obj_.original_tagname_ = 'validations'
        elif nodeName_ == 'init':
            obj_ = init.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.init = obj_
            obj_.original_tagname_ = 'init'
        elif nodeName_ == 'inits':
            obj_ = inits.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.inits = obj_
            obj_.original_tagname_ = 'inits'
        elif nodeName_ == 'format':
            obj_ = format.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.format = obj_
            obj_.original_tagname_ = 'format'
        elif nodeName_ == 'view':
            obj_ = fieldView.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.view = obj_
            obj_.original_tagname_ = 'view'
        elif nodeName_ == 'component':
            obj_ = component.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.component = obj_
            obj_.original_tagname_ = 'component'
        elif nodeName_ == 'encryption':
            obj_ = encryption.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.encryption = obj_
            obj_.original_tagname_ = 'encryption'
        elif nodeName_ == 'action':
            obj_ = action.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.action.append(obj_)
            obj_.original_tagname_ = 'action'
        elif nodeName_ == 'event':
            obj_ = dataEvent.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.event.append(obj_)
            obj_.original_tagname_ = 'event'
        elif nodeName_ == 'actionRef':
            obj_ = actionRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.actionRef.append(obj_)
            obj_.original_tagname_ = 'actionRef'
        elif nodeName_ == 'documentRef':
            obj_ = documentRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.documentRef = obj_
            obj_.original_tagname_ = 'documentRef'
        elif nodeName_ == 'remote':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'remote')
            value_ = self.gds_validate_string(value_, node, 'remote')
            self.remote = value_
            self.remote_nsprefix_ = child_.prefix
            # validate type remote
            self.validate_remote(self.remote)
        elif nodeName_ == 'length' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'length')
            ival_ = self.gds_validate_integer(ival_, node, 'length')
            self.length = ival_
            self.length_nsprefix_ = child_.prefix
        elif nodeName_ == 'allowedNets':
            obj_ = allowedNets.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.allowedNets = obj_
            obj_.original_tagname_ = 'allowedNets'


# end class data


class function(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'scope': MemberSpec_('scope', 'scope', 0, 0, {'use': 'required', 'name': 'scope'}),
        'name': MemberSpec_('name', 'xs:string', 0, 0, {'use': 'required', 'name': 'name'}),
        'valueOf_': MemberSpec_('valueOf_', 'xs:string', 0),
    }
    subclass = None
    superclass = None

    def __init__(self, scope=None, name=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.scope = _cast(None, scope)
        self.scope_nsprefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.valueOf_ = valueOf_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, function)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if function.subclass:
            return function.subclass(*args_, **kwargs_)
        else:
            return function(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_scope(self):
        return self.scope

    def set_scope(self, scope_):
        if type(scope_) is scope:
            self.scope = scope_
        else:
            raise TypeError("Requires scope value")

    def get_name(self):
        return self.name

    def set_name(self, name):
        if type(name) is str:
            self.name = name
        else:
            raise TypeError("Requires str value")

    def get_valueOf_(self):
        return self.valueOf_

    def set_valueOf_(self, valueOf_):
        if type(valueOf_) is str:
            self.valueOf_ = valueOf_
        else:
            raise TypeError("Requires str value")

    def validate_scope(self, value):
        # Validate type scope, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['namespace', 'process']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on scope' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False

    def _hasContent(self):
        if (
                (1 if type(self.valueOf_) in [int, float] else self.valueOf_)
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='function', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('function')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'function':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='function')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='function',
                                 pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='function'):
        if self.scope is not None and 'scope' not in already_processed:
            already_processed.add('scope')
            outfile.write(
                ' scope=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.scope), input_name='scope')),))
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(
                ' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')),))

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='function',
                        fromsubclass_=False, pretty_print=True):
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('scope', node)
        if value is not None and 'scope' not in already_processed:
            already_processed.add('scope')
            self.scope = value
            self.validate_scope(self.scope)  # validate type scope
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass


# end class function


class role(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'id': MemberSpec_('id', 'xs:string', 0, 0, {'name': 'id', 'type': 'xs:string'}, None),
        'title': MemberSpec_('title', 'i18nStringType', 0, 0, {'name': 'title', 'type': 'i18nStringType'}, 6),
        'name': MemberSpec_('name', 'i18nStringType', 0, 0, {'name': 'name', 'type': 'i18nStringType'}, 6),
        'event': MemberSpec_('event', 'event', 1, 1,
                             {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'event', 'type': 'event'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, id=None, title=None, name=None, event=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = id
        self.id_nsprefix_ = None
        self.title = title
        self.title_nsprefix_ = None
        self.name = name
        self.name_nsprefix_ = None
        if event is None:
            self.event = []
        else:
            self.event = event
        self.event_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, role)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if role.subclass:
            return role.subclass(*args_, **kwargs_)
        else:
            return role(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_id(self):
        return self.id

    def set_id(self, id_, doc):
        if type(id_) is str:
            if all(x.id != id_ for x in doc.role):
                self.id = id_
            else:
                raise ValueError("Requires unique id value")
        else:
            raise TypeError("Requires str value")

    def get_title(self):
        return self.title

    def set_title(self, title):
        if self.name is None:
            if type(title) is i18nStringType:
                self.title = title
            else:
                raise TypeError("Requires i18nStringType value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'name' element.")

    def get_name(self):
        return self.name

    def set_name(self, name):
        if self.title is None:
            if type(name) is i18nStringType:
                self.name = name
            else:
                raise TypeError("Requires i18nStringType value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'title' element.")

    def get_event(self):
        return self.event

    # if you want your own specific event list , else it is an empty list
    def set_event(self, event_):
        if all(isinstance(x, event) for x in event_):
            self.event = event_
        else:
            raise TypeError("Requires only event values inside an array")

    def add_event(self, value):
        if type(value) is event:
            self.event.append(value)
        else:
            raise TypeError("Requires event value")

    def insert_event_at(self, index, value):
        if 0 <= index <= len(self.event):
            if type(value) is event:
                self.event.insert(index, value)
            else:
                raise TypeError("Requires event value")
        else:
            raise IndexError("Invalid index value")

    def replace_event_at(self, index, value):
        if 0 <= index < len(self.event):
            if self.event[index]:
                if type(value) is event:
                    self.event[index] = value
                else:
                    raise TypeError("Requires event value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def _hasContent(self):
        if (
                self.id is not None or
                self.title is not None or
                self.name is not None or
                self.event
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='role', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('role')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'role':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='role')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='role',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='role'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='role', fromsubclass_=False,
                        pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.id is not None:
            namespaceprefix_ = self.id_nsprefix_ + ':' if (UseCapturedNS_ and self.id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sid>%s</%sid>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.id), input_name='id')),
                namespaceprefix_, eol_))
        if self.title is not None:
            namespaceprefix_ = self.title_nsprefix_ + ':' if (UseCapturedNS_ and self.title_nsprefix_) else ''
            self.title.export(outfile, level, namespaceprefix_, namespacedef_='', name_='title',
                              pretty_print=pretty_print)
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            self.name.export(outfile, level, namespaceprefix_, namespacedef_='', name_='name',
                             pretty_print=pretty_print)
        for event_ in self.event:
            namespaceprefix_ = self.event_nsprefix_ + ':' if (UseCapturedNS_ and self.event_nsprefix_) else ''
            event_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='event', pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'id')
            value_ = self.gds_validate_string(value_, node, 'id')
            self.id = value_
            self.id_nsprefix_ = child_.prefix
        elif nodeName_ == 'title':
            class_obj_ = self.get_class_obj_(child_, i18nStringType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.title = obj_
            obj_.original_tagname_ = 'title'
        elif nodeName_ == 'name':
            class_obj_ = self.get_class_obj_(child_, i18nStringType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'event':
            obj_ = event.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.event.append(obj_)
            obj_.original_tagname_ = 'event'


# end class role


class mapping(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'id': MemberSpec_('id', 'xs:string', 0, 0, {'name': 'id', 'type': 'xs:string'}, None),
        'transitionRef': MemberSpec_('transitionRef', 'xs:string', 0, 0, {'name': 'transitionRef', 'type': 'xs:string'},
                                     None),
        'roleRef': MemberSpec_('roleRef', 'roleRef', 1, 1,
                               {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'roleRef', 'type': 'roleRef'},
                               None),
        'dataRef': MemberSpec_('dataRef', 'dataRef', 1, 1,
                               {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'dataRef', 'type': 'dataRef'},
                               None),
        'dataGroup': MemberSpec_('dataGroup', 'dataGroup', 1, 1,
                                 {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'dataGroup', 'type': 'dataGroup'},
                                 None),
        'trigger': MemberSpec_('trigger', 'trigger', 1, 1,
                               {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'trigger', 'type': 'trigger'},
                               None),
    }
    subclass = None
    superclass = None

    def __init__(self, id=None, transitionRef=None, roleRef=None, dataRef=None, dataGroup=None, trigger=None,
                 gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = id
        self.id_nsprefix_ = None
        self.transitionRef = transitionRef
        self.transitionRef_nsprefix_ = None
        if roleRef is None:
            self.roleRef = []
        else:
            self.roleRef = roleRef
        self.roleRef_nsprefix_ = None
        if dataRef is None:
            self.dataRef = []
        else:
            self.dataRef = dataRef
        self.dataRef_nsprefix_ = None
        if dataGroup is None:
            self.dataGroup = []
        else:
            self.dataGroup = dataGroup
        self.dataGroup_nsprefix_ = None
        if trigger is None:
            self.trigger = []
        else:
            self.trigger = trigger
        self.trigger_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, mapping)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if mapping.subclass:
            return mapping.subclass(*args_, **kwargs_)
        else:
            return mapping(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_id(self):
        return self.id

    def set_id(self, id_, doc):
        if type(id_) is str:
            if all(x.id != id_ for x in doc.mapping):
                self.id = id_
            else:
                raise ValueError("Requires unique id value")
        else:
            raise TypeError("Requires str value")

    def get_transitionRef(self):
        return self.transitionRef

    def set_transitionRef(self, transitionRef):
        if type(transitionRef) is str:
            self.transitionRef = transitionRef
        else:
            raise TypeError("Requires str value")

    def get_roleRef(self):
        return self.roleRef

    def set_roleRef(self, roleRef_):
        if all(isinstance(x, roleRef) for x in roleRef_):
            self.roleRef = roleRef_
        else:
            raise TypeError("Requires only roleRef values inside an array")

    def add_roleRef(self, value):
        if type(value) is roleRef:
            self.roleRef.append(value)
        else:
            raise TypeError("Requires roleRef value")

    def insert_roleRef_at(self, index, value):
        if 0 <= index <= len(self.roleRef):
            if type(value) is roleRef:
                self.roleRef.insert(index, value)
            else:
                raise TypeError("Requires roleRef value")
        else:
            raise IndexError("Invalid index value")

    def replace_roleRef_at(self, index, value):
        if 0 <= index < len(self.roleRef):
            if self.roleRef[index]:
                if type(value) is roleRef:
                    self.roleRef[index] = value
                else:
                    raise TypeError("Requires roleRef value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_dataRef(self):
        return self.dataRef

    def set_dataRef(self, dataRef_):
        if all(isinstance(x, dataRef) for x in dataRef_):
            self.dataRef = dataRef_
        else:
            raise TypeError("Requires only dataRef values inside an array")

    def add_dataRef(self, value):
        if type(value) is dataRef:
            self.dataRef.append(value)
        else:
            raise TypeError("Requires dataRef value")

    def insert_dataRef_at(self, index, value):
        if 0 <= index <= len(self.dataRef):
            if type(value) is dataRef:
                self.dataRef.insert(index, value)
            else:
                raise TypeError("Requires dataRef value")
        else:
            raise IndexError("Invalid index value")

    def replace_dataRef_at(self, index, value):
        if 0 <= index < len(self.dataRef):
            if self.dataRef[index]:
                if type(value) is dataRef:
                    self.dataRef[index] = value
                else:
                    raise TypeError("Requires dataRef value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_dataGroup(self):
        return self.dataGroup

    def set_dataGroup(self, dataGroup_):
        if all(isinstance(x, dataGroup) for x in dataGroup_):
            self.dataGroup = dataGroup_
        else:
            raise TypeError("Requires only dataGroup values inside an array")

    def add_dataGroup(self, value):
        if type(value) is dataGroup:
            self.dataGroup.append(value)
        else:
            raise TypeError("Requires dataGroup value")

    def insert_dataGroup_at(self, index, value):
        if 0 <= index <= len(self.dataGroup):
            if type(value) is dataGroup:
                self.dataGroup.insert(index, value)
            else:
                raise TypeError("Requires dataGroup value")
        else:
            raise IndexError("Invalid index value")

    def replace_dataGroup_at(self, index, value):
        if 0 <= index < len(self.dataGroup):
            if self.dataGroup[index]:
                if type(value) is dataGroup:
                    self.dataGroup[index] = value
                else:
                    raise TypeError("Requires dataGroup value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_trigger(self):
        return self.trigger

    def set_trigger(self, trigger_):
        if all(isinstance(x, trigger) for x in trigger_):
            self.trigger = trigger_
        else:
            raise TypeError("Requires only trigger values inside an array")

    def add_trigger(self, value):
        if type(value) is trigger:
            self.trigger.append(value)
        else:
            raise TypeError("Requires trigger value")

    def insert_trigger_at(self, index, value):
        if 0 <= index <= len(self.trigger):
            if type(value) is trigger:
                self.trigger.insert(index, value)
            else:
                raise TypeError("Requires trigger value")
        else:
            raise IndexError("Invalid index value")

    def replace_trigger_at(self, index, value):
        if 0 <= index < len(self.trigger):
            if self.trigger[index]:
                if type(value) is trigger:
                    self.trigger[index] = value
                else:
                    raise TypeError("Requires trigger value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def _hasContent(self):
        if (
                self.id is not None or
                self.transitionRef is not None or
                self.roleRef or
                self.dataRef or
                self.dataGroup or
                self.trigger
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='mapping', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('mapping')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'mapping':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='mapping')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='mapping',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='mapping'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='mapping',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.id is not None:
            namespaceprefix_ = self.id_nsprefix_ + ':' if (UseCapturedNS_ and self.id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sid>%s</%sid>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.id), input_name='id')),
                namespaceprefix_, eol_))
        if self.transitionRef is not None:
            namespaceprefix_ = self.transitionRef_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.transitionRef_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stransitionRef>%s</%stransitionRef>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.transitionRef), input_name='transitionRef')), namespaceprefix_,
                                                                       eol_))
        for roleRef_ in self.roleRef:
            namespaceprefix_ = self.roleRef_nsprefix_ + ':' if (UseCapturedNS_ and self.roleRef_nsprefix_) else ''
            roleRef_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='roleRef',
                            pretty_print=pretty_print)
        for dataRef_ in self.dataRef:
            namespaceprefix_ = self.dataRef_nsprefix_ + ':' if (UseCapturedNS_ and self.dataRef_nsprefix_) else ''
            dataRef_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='dataRef',
                            pretty_print=pretty_print)
        for dataGroup_ in self.dataGroup:
            namespaceprefix_ = self.dataGroup_nsprefix_ + ':' if (UseCapturedNS_ and self.dataGroup_nsprefix_) else ''
            dataGroup_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='dataGroup',
                              pretty_print=pretty_print)
        for trigger_ in self.trigger:
            namespaceprefix_ = self.trigger_nsprefix_ + ':' if (UseCapturedNS_ and self.trigger_nsprefix_) else ''
            trigger_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='trigger',
                            pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'id')
            value_ = self.gds_validate_string(value_, node, 'id')
            self.id = value_
            self.id_nsprefix_ = child_.prefix
        elif nodeName_ == 'transitionRef':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'transitionRef')
            value_ = self.gds_validate_string(value_, node, 'transitionRef')
            self.transitionRef = value_
            self.transitionRef_nsprefix_ = child_.prefix
        elif nodeName_ == 'roleRef':
            obj_ = roleRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.roleRef.append(obj_)
            obj_.original_tagname_ = 'roleRef'
        elif nodeName_ == 'dataRef':
            obj_ = dataRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dataRef.append(obj_)
            obj_.original_tagname_ = 'dataRef'
        elif nodeName_ == 'dataGroup':
            obj_ = dataGroup.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dataGroup.append(obj_)
            obj_.original_tagname_ = 'dataGroup'
        elif nodeName_ == 'trigger':
            obj_ = trigger.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.trigger.append(obj_)
            obj_.original_tagname_ = 'trigger'


# end class mapping


class transition(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'id': MemberSpec_('id', 'xs:string', 0, 0, {'name': 'id', 'type': 'xs:string'}, None),
        'x': MemberSpec_('x', ['nonNegativeInteger', 'xs:int'], 0, 0, {'name': 'x', 'type': 'xs:int'}, None),
        'y': MemberSpec_('y', ['nonNegativeInteger', 'xs:int'], 0, 0, {'name': 'y', 'type': 'xs:int'}, None),
        'label': MemberSpec_('label', 'i18nStringType', 0, 0, {'name': 'label', 'type': 'i18nStringType'}, None),
        'layout': MemberSpec_('layout', 'layout', 0, 1,
                              {'minOccurs': '0', 'name': 'layout', 'type': 'transitionLayout'}, None),
        'icon': MemberSpec_('icon', 'icon', 0, 1, {'minOccurs': '0', 'name': 'icon', 'type': 'xs:string'}, None),
        'priority': MemberSpec_('priority', ['nonNegativeInteger', 'xs:int'], 0, 1,
                                {'minOccurs': '0', 'name': 'priority', 'type': 'xs:int'}, None),
        'assignPolicy': MemberSpec_('assignPolicy', ['assignPolicy', 'xs:string'], 0, 1,
                                    {'minOccurs': '0', 'name': 'assignPolicy', 'type': 'xs:string'}, None),
        'dataFocusPolicy': MemberSpec_('dataFocusPolicy', ['dataFocusPolicy', 'xs:string'], 0, 1,
                                       {'minOccurs': '0', 'name': 'dataFocusPolicy', 'type': 'xs:string'}, None),
        'finishPolicy': MemberSpec_('finishPolicy', ['finishPolicy', 'xs:string'], 0, 1,
                                    {'minOccurs': '0', 'name': 'finishPolicy', 'type': 'xs:string'}, None),
        'trigger': MemberSpec_('trigger', 'trigger', 1, 1,
                               {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'trigger', 'type': 'trigger'},
                               None),
        'transactionRef': MemberSpec_('transactionRef', 'transactionRef', 0, 1,
                                      {'minOccurs': '0', 'name': 'transactionRef', 'type': 'transactionRef'}, None),
        'roleRef': MemberSpec_('roleRef', 'roleRef', 1, 1,
                               {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'roleRef', 'type': 'roleRef'},
                               None),
        'usersRef': MemberSpec_('usersRef', 'userRef', 1, 1,
                                {'maxOccurs': 'unbounded', 'name': 'usersRef', 'type': 'userRef'}, 7),
        'userRef': MemberSpec_('userRef', 'userRef', 1, 1,
                               {'maxOccurs': 'unbounded', 'name': 'userRef', 'type': 'userRef'}, 7),
        'assignedUser': MemberSpec_('assignedUser', 'assignedUser', 0, 1,
                                    {'minOccurs': '0', 'name': 'assignedUser', 'type': 'assignedUser'}, None),
        'dataRef': MemberSpec_('dataRef', 'dataRef', 1, 1,
                               {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'dataRef', 'type': 'dataRef'},
                               None),
        'dataGroup': MemberSpec_('dataGroup', 'dataGroup', 1, 1,
                                 {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'dataGroup', 'type': 'dataGroup'},
                                 None),
        'event': MemberSpec_('event', 'event', 1, 1,
                             {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'event', 'type': 'event'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, id=None, x=None, y=None, label=None, layout=None, icon=None, priority=None, assignPolicy=None,
                 dataFocusPolicy=None, finishPolicy=None, trigger=None, transactionRef=None, roleRef=None,
                 usersRef=None, userRef=None, assignedUser=None, dataRef=None, dataGroup=None, event=None,
                 gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = id
        self.id_nsprefix_ = None
        self.x = x
        self.validate_nonNegativeInteger(self.x)
        self.x_nsprefix_ = None
        self.y = y
        self.validate_nonNegativeInteger(self.y)
        self.y_nsprefix_ = None
        self.label = label
        self.label_nsprefix_ = None
        self.layout = layout
        self.layout_nsprefix_ = None
        self.icon = icon
        self.icon_nsprefix_ = None
        self.priority = priority
        self.validate_nonNegativeInteger(self.priority)
        self.priority_nsprefix_ = None
        self.assignPolicy = assignPolicy
        self.validate_assignPolicy(self.assignPolicy)
        self.assignPolicy_nsprefix_ = None
        self.dataFocusPolicy = dataFocusPolicy
        self.validate_dataFocusPolicy(self.dataFocusPolicy)
        self.dataFocusPolicy_nsprefix_ = None
        self.finishPolicy = finishPolicy
        self.validate_finishPolicy(self.finishPolicy)
        self.finishPolicy_nsprefix_ = None
        if trigger is None:
            self.trigger = []
        else:
            self.trigger = trigger
        self.trigger_nsprefix_ = None
        self.transactionRef = transactionRef
        self.transactionRef_nsprefix_ = None
        if roleRef is None:
            self.roleRef = []
        else:
            self.roleRef = roleRef
        self.roleRef_nsprefix_ = None
        if usersRef is None:
            self.usersRef = []
        else:
            self.usersRef = usersRef
        self.usersRef_nsprefix_ = None
        if userRef is None:
            self.userRef = []
        else:
            self.userRef = userRef
        self.userRef_nsprefix_ = None
        self.assignedUser = assignedUser
        self.assignedUser_nsprefix_ = None
        if dataRef is None:
            self.dataRef = []
        else:
            self.dataRef = dataRef
        self.dataRef_nsprefix_ = None
        if dataGroup is None:
            self.dataGroup = []
        else:
            self.dataGroup = dataGroup
        self.dataGroup_nsprefix_ = None
        if event is None:
            self.event = []
        else:
            self.event = event
        self.event_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, transition)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if transition.subclass:
            return transition.subclass(*args_, **kwargs_)
        else:
            return transition(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_id(self):
        return self.id

    def set_id(self, id_, doc):
        if type(id_) is str:
            if all(x.id != id_ for x in doc.transition):
                self.id = id_
            else:
                raise ValueError("Requires unique id value")
        else:
            raise TypeError("Requires str value")

    def get_x(self):
        return self.x

    def set_x(self, x):
        if type(x) is int:
            if x < 0:
                raise ValueError("The 'x' element has to be nonNegativeInteger")
            else:
                self.x = x
        else:
            raise TypeError("Requires int value")

    def get_y(self):
        return self.y

    def set_y(self, y):
        if type(y) is int:
            if y < 0:
                raise ValueError("The 'y' element has to be nonNegativeInteger")
            else:
                self.y = y
        else:
            raise TypeError("Requires int value")

    def get_label(self):
        return self.label

    def set_label(self, label):
        if type(label) is i18nStringType:
            self.label = label
        else:
            raise TypeError("Requires i18nStringType value")

    def get_layout(self):
        return self.layout

    def set_layout(self, layout_):
        if type(layout_) is transitionLayout:
            self.layout = layout_
        else:
            raise TypeError("Requires transitionLayout value")

    def get_icon(self):
        return self.icon

    def set_icon(self, icon_):
        if type(icon_) is str:
            self.icon = icon_
        else:
            raise TypeError("Requires str value")

    def get_priority(self):
        return self.priority

    def set_priority(self, priority):
        if type(priority) is int:
            if priority < 0:
                raise ValueError("The 'priority' element has to be nonNegativeInteger")
            else:
                self.priority = priority
        else:
            raise TypeError("Requires int value")

    def get_assignPolicy(self):
        return self.assignPolicy

    def set_assignPolicy(self, assignPolicy_):
        if type(assignPolicy_) is assignPolicy:
            self.assignPolicy = assignPolicy_
        else:
            raise TypeError("Requires assignPolicy value")

    def get_dataFocusPolicy(self):
        return self.dataFocusPolicy

    def set_dataFocusPolicy(self, dataFocusPolicy_):
        if type(dataFocusPolicy_) is dataFocusPolicy:
            self.dataFocusPolicy = dataFocusPolicy_
        else:
            raise TypeError("Requires dataFocusPolicy value")

    def get_finishPolicy(self):
        return self.finishPolicy

    def set_finishPolicy(self, finishPolicy_):
        if type(finishPolicy_) is finishPolicy:
            self.finishPolicy = finishPolicy_
        else:
            raise TypeError("Requires finishPolicy value")

    def get_trigger(self):
        return self.trigger

    def set_trigger(self, trigger_):
        if all(isinstance(x, trigger) for x in trigger_):
            self.trigger = trigger_
        else:
            raise TypeError("Requires only trigger values inside an array")

    def add_trigger(self, value):
        if type(value) is trigger:
            self.trigger.append(value)
        else:
            raise TypeError("Requires trigger value")

    def insert_trigger_at(self, index, value):
        if 0 <= index <= len(self.trigger):
            if type(value) is trigger:
                self.trigger.insert(index, value)
            else:
                raise TypeError("Requires trigger value")
        else:
            raise IndexError("Invalid index value")

    def replace_trigger_at(self, index, value):
        if 0 <= index < len(self.trigger):
            if self.trigger[index]:
                if type(value) is trigger:
                    self.trigger[index] = value
                else:
                    raise TypeError("Requires trigger value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_transactionRef(self):
        return self.transactionRef

    def set_transactionRef(self, transactionRef_):
        if type(transactionRef_) is transactionRef:
            self.transactionRef = transactionRef_
        else:
            raise TypeError("Requires transactionRef value")

    def get_roleRef(self):
        return self.roleRef

    def set_roleRef(self, roleRef_):
        if all(isinstance(x, roleRef) for x in roleRef_):
            self.roleRef = roleRef_
        else:
            raise TypeError("Requires only roleRef values inside an array")

    def add_roleRef(self, value):
        if type(value) is roleRef:
            self.roleRef.append(value)
        else:
            raise TypeError("Requires roleRef value")

    def insert_roleRef_at(self, index, value):
        if 0 <= index <= len(self.roleRef):
            if type(value) is roleRef:
                self.roleRef.insert(index, value)
            else:
                raise TypeError("Requires roleRef value")
        else:
            raise IndexError("Invalid index value")

    def replace_roleRef_at(self, index, value):
        if 0 <= index < len(self.roleRef):
            if self.roleRef[index]:
                if type(value) is roleRef:
                    self.roleRef[index] = value
                else:
                    raise TypeError("Requires roleRef value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_usersRef(self):
        return self.usersRef

    def set_usersRef(self, usersRef):
        if not self.userRef:
            if all(isinstance(x, userRef) for x in usersRef):
                self.usersRef = usersRef
            else:
                raise TypeError("Requires only userRef values inside an array")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'userRef' element.")

    def add_usersRef(self, value):
        if not self.userRef:
            if type(value) is userRef:
                self.usersRef.append(value)
            else:
                raise TypeError("Requires userRef value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'userRef' element.")

    def insert_usersRef_at(self, index, value):
        if not self.userRef:
            if 0 <= index <= len(self.usersRef):
                if type(value) is userRef:
                    self.usersRef.insert(index, value)
                else:
                    raise TypeError("Requires userRef value")
            else:
                raise IndexError("Invalid index value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'userRef' element.")

    def replace_usersRef_at(self, index, value):
        if not self.userRef:
            if 0 <= index < len(self.usersRef):
                if self.usersRef[index]:
                    if type(value) is userRef:
                        self.usersRef[index] = value
                    else:
                        raise TypeError("Requires userRef value")
                else:
                    raise Exception("Invalid index value")
            else:
                raise IndexError("Index out of range")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'userRef' element.")

    def get_userRef(self):
        return self.userRef

    def set_userRef(self, userRef_):
        if not self.usersRef:
            if all(isinstance(x, userRef) for x in userRef_):
                self.userRef = userRef_
            else:
                raise TypeError("Requires only userRef values inside an array")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'usersRef' element.")

    def add_userRef(self, value):
        if not self.usersRef:
            if type(value) is userRef:
                self.userRef.append(value)
            else:
                raise TypeError("Requires userRef value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'usersRef' element.")

    def insert_userRef_at(self, index, value):
        if not self.usersRef:
            if 0 <= index <= len(self.userRef):
                if type(value) is userRef:
                    self.userRef.insert(index, value)
                else:
                    raise TypeError("Requires userRef value")
            else:
                raise IndexError("Invalid index value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'usersRef' element.")

    def replace_userRef_at(self, index, value):
        if not self.usersRef:
            if 0 <= index < len(self.userRef):
                if self.userRef[index]:
                    if type(value) is userRef:
                        self.userRef[index] = value
                    else:
                        raise TypeError("Requires userRef value")
                else:
                    raise Exception("Invalid index value")
            else:
                raise IndexError("Index out of range")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'usersRef' element.")

    def get_assignedUser(self):
        return self.assignedUser

    def set_assignedUser(self, assignedUser_):
        if type(assignedUser_) is assignedUser:
            self.assignedUser = assignedUser_
        else:
            raise TypeError("Requires assignedUser value")

    def get_dataRef(self):
        return self.dataRef

    def set_dataRef(self, dataRef_):
        if all(isinstance(x, dataRef) for x in dataRef_):
            self.dataRef = dataRef_
        else:
            raise TypeError("Requires only dataRef values inside an array")

    def add_dataRef(self, value):
        if type(value) is dataRef:
            self.dataRef.append(value)
        else:
            raise TypeError("Requires dataRef value")

    def insert_dataRef_at(self, index, value):
        if 0 <= index <= len(self.dataRef):
            if type(value) is dataRef:
                self.dataRef.insert(index, value)
            else:
                raise TypeError("Requires dataRef value")
        else:
            raise IndexError("Invalid index value")

    def replace_dataRef_at(self, index, value):
        if 0 <= index < len(self.dataRef):
            if self.dataRef[index]:
                if type(value) is dataRef:
                    self.dataRef[index] = value
                else:
                    raise TypeError("Requires dataRef value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_dataGroup(self):
        return self.dataGroup

    def set_dataGroup(self, dataGroup_):
        if all(isinstance(x, dataGroup) for x in dataGroup_):
            self.dataGroup = dataGroup_
        else:
            raise TypeError("Requires only dataGroup values inside an array")

    def add_dataGroup(self, value):
        if type(value) is dataGroup:
            self.dataGroup.append(value)
        else:
            raise TypeError("Requires dataGroup value")

    def insert_dataGroup_at(self, index, value):
        if 0 <= index <= len(self.dataGroup):
            if type(value) is dataGroup:
                self.dataGroup.insert(index, value)
            else:
                raise TypeError("Requires dataGroup value")
        else:
            raise IndexError("Invalid index value")

    def replace_dataGroup_at(self, index, value):
        if 0 <= index < len(self.dataGroup):
            if self.dataGroup[index]:
                if type(value) is dataGroup:
                    self.dataGroup[index] = value
                else:
                    raise TypeError("Requires dataGroup value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_event(self):
        return self.event

    # if you want your own specific event list , else it is an empty list
    def set_event(self, event_):
        if all(isinstance(x, event) for x in event_):
            self.event = event_
        else:
            raise TypeError("Requires only event values inside an array")

    def add_event(self, value):
        if type(value) is event:
            self.event.append(value)
        else:
            raise TypeError("Requires event value")

    def insert_event_at(self, index, value):
        if 0 <= index <= len(self.event):
            if type(value) is event:
                self.event.insert(index, value)
            else:
                raise TypeError("Requires event value")
        else:
            raise IndexError("Invalid index value")

    def replace_event_at(self, index, value):
        if 0 <= index < len(self.event):
            if self.event[index]:
                if type(value) is event:
                    self.event[index] = value
                else:
                    raise TypeError("Requires event value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def validate_nonNegativeInteger(self, value):
        result = True
        # Validate type nonNegativeInteger, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on nonNegativeInteger' % {
                        "value": value, "lineno": lineno})
                result = False
        return result

    def validate_assignPolicy(self, value):
        result = True
        # Validate type assignPolicy, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['auto', 'manual']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on assignPolicy' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
        return result

    def validate_dataFocusPolicy(self, value):
        result = True
        # Validate type dataFocusPolicy, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['manual', 'auto_empty_required']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on dataFocusPolicy' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
        return result

    def validate_finishPolicy(self, value):
        result = True
        # Validate type finishPolicy, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['auto_no_data', 'manual']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on finishPolicy' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
        return result

    def _hasContent(self):
        if (
                self.id is not None or
                self.x is not None or
                self.y is not None or
                self.label is not None or
                self.layout is not None or
                self.icon is not None or
                self.priority is not None or
                self.assignPolicy is not None or
                self.dataFocusPolicy is not None or
                self.finishPolicy is not None or
                self.trigger or
                self.transactionRef is not None or
                self.roleRef or
                self.usersRef or
                self.userRef or
                self.assignedUser is not None or
                self.dataRef or
                self.dataGroup or
                self.event
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='transition', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('transition')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'transition':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='transition')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='transition',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='transition'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='transition',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.id is not None:
            namespaceprefix_ = self.id_nsprefix_ + ':' if (UseCapturedNS_ and self.id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sid>%s</%sid>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.id), input_name='id')),
                namespaceprefix_, eol_))
        if self.x is not None:
            namespaceprefix_ = self.x_nsprefix_ + ':' if (UseCapturedNS_ and self.x_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sx>%s</%sx>%s' % (
                namespaceprefix_, self.gds_format_integer(self.x, input_name='x'), namespaceprefix_, eol_))
        if self.y is not None:
            namespaceprefix_ = self.y_nsprefix_ + ':' if (UseCapturedNS_ and self.y_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sy>%s</%sy>%s' % (
                namespaceprefix_, self.gds_format_integer(self.y, input_name='y'), namespaceprefix_, eol_))
        if self.label is not None:
            namespaceprefix_ = self.label_nsprefix_ + ':' if (UseCapturedNS_ and self.label_nsprefix_) else ''
            self.label.export(outfile, level, namespaceprefix_, namespacedef_='', name_='label',
                              pretty_print=pretty_print)
        if self.layout is not None:
            namespaceprefix_ = self.layout_nsprefix_ + ':' if (UseCapturedNS_ and self.layout_nsprefix_) else ''
            self.layout.export(outfile, level, namespaceprefix_, namespacedef_='', name_='layout',
                               pretty_print=pretty_print)
        if self.icon is not None:
            namespaceprefix_ = self.icon_nsprefix_ + ':' if (UseCapturedNS_ and self.icon_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sicon>%s</%sicon>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.icon), input_name='icon')),
                namespaceprefix_, eol_))
        if self.priority is not None:
            namespaceprefix_ = self.priority_nsprefix_ + ':' if (UseCapturedNS_ and self.priority_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spriority>%s</%spriority>%s' % (
                namespaceprefix_, self.gds_format_integer(self.priority, input_name='priority'), namespaceprefix_,
                eol_))
        if self.assignPolicy is not None:
            namespaceprefix_ = self.assignPolicy_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.assignPolicy_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sassignPolicy>%s</%sassignPolicy>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.assignPolicy), input_name='assignPolicy')), namespaceprefix_,
                                                                     eol_))
        if self.dataFocusPolicy is not None:
            namespaceprefix_ = self.dataFocusPolicy_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.dataFocusPolicy_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdataFocusPolicy>%s</%sdataFocusPolicy>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.dataFocusPolicy), input_name='dataFocusPolicy')),
                                                                           namespaceprefix_, eol_))
        if self.finishPolicy is not None:
            namespaceprefix_ = self.finishPolicy_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.finishPolicy_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfinishPolicy>%s</%sfinishPolicy>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.finishPolicy), input_name='finishPolicy')), namespaceprefix_,
                                                                     eol_))
        for trigger_ in self.trigger:
            namespaceprefix_ = self.trigger_nsprefix_ + ':' if (UseCapturedNS_ and self.trigger_nsprefix_) else ''
            trigger_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='trigger',
                            pretty_print=pretty_print)
        if self.transactionRef is not None:
            namespaceprefix_ = self.transactionRef_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.transactionRef_nsprefix_) else ''
            self.transactionRef.export(outfile, level, namespaceprefix_, namespacedef_='', name_='transactionRef',
                                       pretty_print=pretty_print)
        for roleRef_ in self.roleRef:
            namespaceprefix_ = self.roleRef_nsprefix_ + ':' if (UseCapturedNS_ and self.roleRef_nsprefix_) else ''
            roleRef_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='roleRef',
                            pretty_print=pretty_print)
        for usersRef_ in self.usersRef:
            namespaceprefix_ = self.usersRef_nsprefix_ + ':' if (UseCapturedNS_ and self.usersRef_nsprefix_) else ''
            usersRef_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='usersRef',
                             pretty_print=pretty_print)
        for userRef_ in self.userRef:
            namespaceprefix_ = self.userRef_nsprefix_ + ':' if (UseCapturedNS_ and self.userRef_nsprefix_) else ''
            userRef_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='userRef',
                            pretty_print=pretty_print)
        if self.assignedUser is not None:
            namespaceprefix_ = self.assignedUser_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.assignedUser_nsprefix_) else ''
            self.assignedUser.export(outfile, level, namespaceprefix_, namespacedef_='', name_='assignedUser',
                                     pretty_print=pretty_print)
        for dataRef_ in self.dataRef:
            namespaceprefix_ = self.dataRef_nsprefix_ + ':' if (UseCapturedNS_ and self.dataRef_nsprefix_) else ''
            dataRef_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='dataRef',
                            pretty_print=pretty_print)
        for dataGroup_ in self.dataGroup:
            namespaceprefix_ = self.dataGroup_nsprefix_ + ':' if (UseCapturedNS_ and self.dataGroup_nsprefix_) else ''
            dataGroup_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='dataGroup',
                              pretty_print=pretty_print)
        for event_ in self.event:
            namespaceprefix_ = self.event_nsprefix_ + ':' if (UseCapturedNS_ and self.event_nsprefix_) else ''
            event_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='event', pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'id')
            value_ = self.gds_validate_string(value_, node, 'id')
            self.id = value_
            self.id_nsprefix_ = child_.prefix
        elif nodeName_ == 'x' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'x')
            ival_ = self.gds_validate_integer(ival_, node, 'x')
            self.x = ival_
            self.x_nsprefix_ = child_.prefix
            # validate type nonNegativeInteger
            self.validate_nonNegativeInteger(self.x)
        elif nodeName_ == 'y' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'y')
            ival_ = self.gds_validate_integer(ival_, node, 'y')
            self.y = ival_
            self.y_nsprefix_ = child_.prefix
            # validate type nonNegativeInteger
            self.validate_nonNegativeInteger(self.y)
        elif nodeName_ == 'label':
            class_obj_ = self.get_class_obj_(child_, i18nStringType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.label = obj_
            obj_.original_tagname_ = 'label'
        elif nodeName_ == 'layout':
            obj_ = transitionLayout.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.layout = obj_
            obj_.original_tagname_ = 'layout'
        elif nodeName_ == 'icon':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'icon')
            value_ = self.gds_validate_string(value_, node, 'icon')
            self.icon = value_
            self.icon_nsprefix_ = child_.prefix
        elif nodeName_ == 'priority' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'priority')
            ival_ = self.gds_validate_integer(ival_, node, 'priority')
            self.priority = ival_
            self.priority_nsprefix_ = child_.prefix
            # validate type nonNegativeInteger
            self.validate_nonNegativeInteger(self.priority)
        elif nodeName_ == 'assignPolicy':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'assignPolicy')
            value_ = self.gds_validate_string(value_, node, 'assignPolicy')
            self.assignPolicy = value_
            self.assignPolicy_nsprefix_ = child_.prefix
            # validate type assignPolicy
            self.validate_assignPolicy(self.assignPolicy)
        elif nodeName_ == 'dataFocusPolicy':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'dataFocusPolicy')
            value_ = self.gds_validate_string(value_, node, 'dataFocusPolicy')
            self.dataFocusPolicy = value_
            self.dataFocusPolicy_nsprefix_ = child_.prefix
            # validate type dataFocusPolicy
            self.validate_dataFocusPolicy(self.dataFocusPolicy)
        elif nodeName_ == 'finishPolicy':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'finishPolicy')
            value_ = self.gds_validate_string(value_, node, 'finishPolicy')
            self.finishPolicy = value_
            self.finishPolicy_nsprefix_ = child_.prefix
            # validate type finishPolicy
            self.validate_finishPolicy(self.finishPolicy)
        elif nodeName_ == 'trigger':
            obj_ = trigger.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.trigger.append(obj_)
            obj_.original_tagname_ = 'trigger'
        elif nodeName_ == 'transactionRef':
            obj_ = transactionRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.transactionRef = obj_
            obj_.original_tagname_ = 'transactionRef'
        elif nodeName_ == 'roleRef':
            obj_ = roleRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.roleRef.append(obj_)
            obj_.original_tagname_ = 'roleRef'
        elif nodeName_ == 'usersRef':
            obj_ = userRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.usersRef.append(obj_)
            obj_.original_tagname_ = 'usersRef'
        elif nodeName_ == 'userRef':
            obj_ = userRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.userRef.append(obj_)
            obj_.original_tagname_ = 'userRef'
        elif nodeName_ == 'assignedUser':
            obj_ = assignedUser.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.assignedUser = obj_
            obj_.original_tagname_ = 'assignedUser'
        elif nodeName_ == 'dataRef':
            obj_ = dataRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dataRef.append(obj_)
            obj_.original_tagname_ = 'dataRef'
        elif nodeName_ == 'dataGroup':
            obj_ = dataGroup.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dataGroup.append(obj_)
            obj_.original_tagname_ = 'dataGroup'
        elif nodeName_ == 'event':
            obj_ = event.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.event.append(obj_)
            obj_.original_tagname_ = 'event'


# end class transition


class transitionLayout(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'type_': MemberSpec_('type_', 'layoutType', 0, 1, {'use': 'optional', 'name': 'type_'}),
        'cols': MemberSpec_('cols', ['nonNegativeInteger', 'xs:int'], 0, 1,
                            {'minOccurs': '0', 'name': 'cols', 'type': 'xs:int'}, None),
        'rows': MemberSpec_('rows', ['nonNegativeInteger', 'xs:int'], 0, 1,
                            {'minOccurs': '0', 'name': 'rows', 'type': 'xs:int'}, None),
        'offset': MemberSpec_('offset', ['nonNegativeInteger', 'xs:int'], 0, 1,
                              {'minOccurs': '0', 'name': 'offset', 'type': 'xs:int'}, None),
        'fieldAlignment': MemberSpec_('fieldAlignment', ['fieldAlignment', 'xs:string'], 0, 1,
                                      {'minOccurs': '0', 'name': 'fieldAlignment', 'type': 'xs:string'}, None),
        'hideEmptyRows': MemberSpec_('hideEmptyRows', ['hideEmptyRows', 'xs:string'], 0, 1,
                                     {'minOccurs': '0', 'name': 'hideEmptyRows', 'type': 'xs:string'}, None),
        'compactDirection': MemberSpec_('compactDirection', ['compactDirection', 'xs:string'], 0, 1,
                                        {'minOccurs': '0', 'name': 'compactDirection', 'type': 'xs:string'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, type_=None, cols=None, rows=None, offset=None, fieldAlignment=None, hideEmptyRows=None,
                 compactDirection=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
        self.cols = cols
        self.validate_nonNegativeInteger(self.cols)
        self.cols_nsprefix_ = None
        self.rows = rows
        self.validate_nonNegativeInteger(self.rows)
        self.rows_nsprefix_ = None
        self.offset = offset
        self.validate_nonNegativeInteger(self.offset)
        self.offset_nsprefix_ = None
        self.fieldAlignment = fieldAlignment
        self.validate_fieldAlignment(self.fieldAlignment)
        self.fieldAlignment_nsprefix_ = None
        self.hideEmptyRows = hideEmptyRows
        self.validate_hideEmptyRows(self.hideEmptyRows)
        self.hideEmptyRows_nsprefix_ = None
        self.compactDirection = compactDirection
        self.validate_compactDirection(self.compactDirection)
        self.compactDirection_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, transitionLayout)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if transitionLayout.subclass:
            return transitionLayout.subclass(*args_, **kwargs_)
        else:
            return transitionLayout(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_cols(self):
        return self.cols

    def set_cols(self, cols):
        if type(cols) is int:
            if cols < 0:
                raise ValueError("The 'cols' element has to be nonNegativeInteger")
            else:
                self.cols = cols
        else:
            raise TypeError("Requires int value")

    def get_rows(self):
        return self.rows

    def set_rows(self, rows):
        if type(rows) is int:
            if rows < 0:
                raise ValueError("The 'rows' element has to be nonNegativeInteger")
            else:
                self.rows = rows
        else:
            raise TypeError("Requires int value")

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        if type(offset) is int:
            if offset < 0:
                raise ValueError("The 'offset' element has to be nonNegativeInteger")
            else:
                self.offset = offset
        else:
            raise TypeError("Requires int value")

    def get_fieldAlignment(self):
        return self.fieldAlignment

    def set_fieldAlignment(self, fieldAlignment_):
        if type(fieldAlignment_) is fieldAlignment:
            self.fieldAlignment = fieldAlignment_
        else:
            raise TypeError("Requires fieldAlignment value")

    def get_hideEmptyRows(self):
        return self.hideEmptyRows

    def set_hideEmptyRows(self, hideEmptyRows_):
        if type(hideEmptyRows_) is hideEmptyRows:
            self.hideEmptyRows = hideEmptyRows_
        else:
            raise TypeError("Requires hideEmptyRows value")

    def get_compactDirection(self):
        return self.compactDirection

    def set_compactDirection(self, compactDirection_):
        if type(compactDirection_) is compactDirection:
            self.compactDirection = compactDirection_
        else:
            raise TypeError("Requires compactDirection value")

    def get_type(self):
        return self.type_

    def set_type_(self, type_):
        if type(type_) is layoutType:
            self.type_ = type_
        else:
            raise TypeError("Requires layoutType value")

    def validate_nonNegativeInteger(self, value):
        result = True
        # Validate type nonNegativeInteger, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on nonNegativeInteger' % {
                        "value": value, "lineno": lineno})
                result = False
        return result

    def validate_fieldAlignment(self, value):
        result = True
        # Validate type fieldAlignment, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['top', 'center', 'bottom']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on fieldAlignment' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
        return result

    def validate_hideEmptyRows(self, value):
        result = True
        # Validate type hideEmptyRows, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['all', 'compacted', 'none']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on hideEmptyRows' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
        return result

    def validate_compactDirection(self, value):
        result = True
        # Validate type compactDirection, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['none', 'up']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on compactDirection' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
        return result

    def validate_layoutType(self, value):
        # Validate type layoutType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['flow', 'grid', 'legacy']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on layoutType' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False

    def _hasContent(self):
        if (
                self.cols is not None or
                self.rows is not None or
                self.offset is not None or
                self.fieldAlignment is not None or
                self.hideEmptyRows is not None or
                self.compactDirection is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='transitionLayout',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('transitionLayout')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'transitionLayout':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='transitionLayout')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='transitionLayout',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='transitionLayout'):
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(
                ' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')),))

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='transitionLayout',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.cols is not None:
            namespaceprefix_ = self.cols_nsprefix_ + ':' if (UseCapturedNS_ and self.cols_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scols>%s</%scols>%s' % (
                namespaceprefix_, self.gds_format_integer(self.cols, input_name='cols'), namespaceprefix_, eol_))
        if self.rows is not None:
            namespaceprefix_ = self.rows_nsprefix_ + ':' if (UseCapturedNS_ and self.rows_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srows>%s</%srows>%s' % (
                namespaceprefix_, self.gds_format_integer(self.rows, input_name='rows'), namespaceprefix_, eol_))
        if self.offset is not None:
            namespaceprefix_ = self.offset_nsprefix_ + ':' if (UseCapturedNS_ and self.offset_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soffset>%s</%soffset>%s' % (
                namespaceprefix_, self.gds_format_integer(self.offset, input_name='offset'), namespaceprefix_, eol_))
        if self.fieldAlignment is not None:
            namespaceprefix_ = self.fieldAlignment_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.fieldAlignment_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfieldAlignment>%s</%sfieldAlignment>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.fieldAlignment), input_name='fieldAlignment')), namespaceprefix_,
                                                                         eol_))
        if self.hideEmptyRows is not None:
            namespaceprefix_ = self.hideEmptyRows_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.hideEmptyRows_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%shideEmptyRows>%s</%shideEmptyRows>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.hideEmptyRows), input_name='hideEmptyRows')), namespaceprefix_,
                                                                       eol_))
        if self.compactDirection is not None:
            namespaceprefix_ = self.compactDirection_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.compactDirection_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scompactDirection>%s</%scompactDirection>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.compactDirection), input_name='compactDirection')),
                                                                             namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.validate_layoutType(self.type_)  # validate type layoutType

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'cols' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'cols')
            ival_ = self.gds_validate_integer(ival_, node, 'cols')
            self.cols = ival_
            self.cols_nsprefix_ = child_.prefix
            # validate type nonNegativeInteger
            self.validate_nonNegativeInteger(self.cols)
        elif nodeName_ == 'rows' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'rows')
            ival_ = self.gds_validate_integer(ival_, node, 'rows')
            self.rows = ival_
            self.rows_nsprefix_ = child_.prefix
            # validate type nonNegativeInteger
            self.validate_nonNegativeInteger(self.rows)
        elif nodeName_ == 'offset' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'offset')
            ival_ = self.gds_validate_integer(ival_, node, 'offset')
            self.offset = ival_
            self.offset_nsprefix_ = child_.prefix
            # validate type nonNegativeInteger
            self.validate_nonNegativeInteger(self.offset)
        elif nodeName_ == 'fieldAlignment':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'fieldAlignment')
            value_ = self.gds_validate_string(value_, node, 'fieldAlignment')
            self.fieldAlignment = value_
            self.fieldAlignment_nsprefix_ = child_.prefix
            # validate type fieldAlignment
            self.validate_fieldAlignment(self.fieldAlignment)
        elif nodeName_ == 'hideEmptyRows':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'hideEmptyRows')
            value_ = self.gds_validate_string(value_, node, 'hideEmptyRows')
            self.hideEmptyRows = value_
            self.hideEmptyRows_nsprefix_ = child_.prefix
            # validate type hideEmptyRows
            self.validate_hideEmptyRows(self.hideEmptyRows)
        elif nodeName_ == 'compactDirection':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'compactDirection')
            value_ = self.gds_validate_string(value_, node, 'compactDirection')
            self.compactDirection = value_
            self.compactDirection_nsprefix_ = child_.prefix
            # validate type compactDirection
            self.validate_compactDirection(self.compactDirection)


# end class transitionLayout


class place(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'id': MemberSpec_('id', 'xs:string', 0, 0, {'name': 'id', 'type': 'xs:string'}, None),
        'x': MemberSpec_('x', ['nonNegativeInteger', 'xs:int'], 0, 0, {'name': 'x', 'type': 'xs:int'}, None),
        'y': MemberSpec_('y', ['nonNegativeInteger', 'xs:int'], 0, 0, {'name': 'y', 'type': 'xs:int'}, None),
        'label': MemberSpec_('label', 'i18nStringType', 0, 0, {'name': 'label', 'type': 'i18nStringType'}, None),
        'tokens': MemberSpec_('tokens', ['nonNegativeInteger', 'xs:int'], 0, 0, {'name': 'tokens', 'type': 'xs:int'},
                              None),
        'isStatic': MemberSpec_('isStatic', 'xs:boolean', 0, 0, {'name': 'isStatic', 'type': 'xs:boolean'}, 8),
        'static': MemberSpec_('static', 'xs:boolean', 0, 0, {'name': 'static', 'type': 'xs:boolean'}, 8),
    }
    subclass = None
    superclass = None

    def __init__(self, id=None, x=None, y=None, label=None, tokens=None, isStatic=None, static=None,
                 gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = id
        self.id_nsprefix_ = None
        self.x = x
        self.validate_nonNegativeInteger(self.x)
        self.x_nsprefix_ = None
        self.y = y
        self.validate_nonNegativeInteger(self.y)
        self.y_nsprefix_ = None
        self.label = label
        self.label_nsprefix_ = None
        self.tokens = tokens
        self.validate_nonNegativeInteger(self.tokens)
        self.tokens_nsprefix_ = None
        self.isStatic = isStatic
        self.isStatic_nsprefix_ = None
        self.static = static
        self.static_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, place)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if place.subclass:
            return place.subclass(*args_, **kwargs_)
        else:
            return place(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_id(self):
        return self.id

    def set_id(self, id_, doc):
        if type(id_) is str:
            if all(x.id != id_ for x in doc.place):
                self.id = id_
            else:
                raise ValueError("Requires unique id value")
        else:
            raise TypeError("Requires str value")

    def get_x(self):
        return self.x

    def set_x(self, x):
        if type(x) is int:
            if x < 0:
                raise ValueError("The 'x' element has to be nonNegativeInteger")
            else:
                self.x = x
        else:
            raise TypeError("Requires int value")

    def get_y(self):
        return self.y

    def set_y(self, y):
        if type(y) is int:
            if y < 0:
                raise ValueError("The 'y' element has to be nonNegativeInteger")
            else:
                self.y = y
        else:
            raise TypeError("Requires int value")

    def get_label(self):
        return self.label

    def set_label(self, label):
        if type(label) is i18nStringType:
            self.label = label
        else:
            raise TypeError("Requires i18nStringType value")

    def get_tokens(self):
        return self.tokens

    def set_tokens(self, tokens):
        if type(tokens) is int:
            if tokens < 0:
                raise ValueError("The 'tokens' element has to be nonNegativeInteger")
            else:
                self.tokens = tokens
        else:
            raise TypeError("Requires int value")

    def get_isStatic(self):
        return self.isStatic

    def set_isStatic(self, isStatic):
        if self.static is None:
            self.isStatic = set_boolean_value(isStatic)
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'static' element.")

    def get_static(self):
        return self.static

    def set_static(self, static):
        if self.isStatic is None:
            self.static = set_boolean_value(static)
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'isStatic' element.")

    def validate_nonNegativeInteger(self, value):
        result = True
        # Validate type nonNegativeInteger, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on nonNegativeInteger' % {
                        "value": value, "lineno": lineno})
                result = False
        return result

    def _hasContent(self):
        if (
                self.id is not None or
                self.x is not None or
                self.y is not None or
                self.label is not None or
                self.tokens is not None or
                self.isStatic is not None or
                self.static is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='place', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('place')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'place':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='place')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='place',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='place'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='place', fromsubclass_=False,
                        pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.id is not None:
            namespaceprefix_ = self.id_nsprefix_ + ':' if (UseCapturedNS_ and self.id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sid>%s</%sid>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.id), input_name='id')),
                namespaceprefix_, eol_))
        if self.x is not None:
            namespaceprefix_ = self.x_nsprefix_ + ':' if (UseCapturedNS_ and self.x_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sx>%s</%sx>%s' % (
                namespaceprefix_, self.gds_format_integer(self.x, input_name='x'), namespaceprefix_, eol_))
        if self.y is not None:
            namespaceprefix_ = self.y_nsprefix_ + ':' if (UseCapturedNS_ and self.y_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sy>%s</%sy>%s' % (
                namespaceprefix_, self.gds_format_integer(self.y, input_name='y'), namespaceprefix_, eol_))
        if self.label is not None:
            namespaceprefix_ = self.label_nsprefix_ + ':' if (UseCapturedNS_ and self.label_nsprefix_) else ''
            self.label.export(outfile, level, namespaceprefix_, namespacedef_='', name_='label',
                              pretty_print=pretty_print)
        if self.tokens is not None:
            namespaceprefix_ = self.tokens_nsprefix_ + ':' if (UseCapturedNS_ and self.tokens_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stokens>%s</%stokens>%s' % (
                namespaceprefix_, self.gds_format_integer(self.tokens, input_name='tokens'), namespaceprefix_, eol_))
        if self.isStatic is not None:
            namespaceprefix_ = self.isStatic_nsprefix_ + ':' if (UseCapturedNS_ and self.isStatic_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sisStatic>%s</%sisStatic>%s' % (
                namespaceprefix_, self.gds_format_boolean(self.isStatic, input_name='isStatic'), namespaceprefix_,
                eol_))
        if self.static is not None:
            namespaceprefix_ = self.static_nsprefix_ + ':' if (UseCapturedNS_ and self.static_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstatic>%s</%sstatic>%s' % (
                namespaceprefix_, self.gds_format_boolean(self.static, input_name='static'), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'id')
            value_ = self.gds_validate_string(value_, node, 'id')
            self.id = value_
            self.id_nsprefix_ = child_.prefix
        elif nodeName_ == 'x' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'x')
            ival_ = self.gds_validate_integer(ival_, node, 'x')
            self.x = ival_
            self.x_nsprefix_ = child_.prefix
            # validate type nonNegativeInteger
            self.validate_nonNegativeInteger(self.x)
        elif nodeName_ == 'y' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'y')
            ival_ = self.gds_validate_integer(ival_, node, 'y')
            self.y = ival_
            self.y_nsprefix_ = child_.prefix
            # validate type nonNegativeInteger
            self.validate_nonNegativeInteger(self.y)
        elif nodeName_ == 'label':
            class_obj_ = self.get_class_obj_(child_, i18nStringType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.label = obj_
            obj_.original_tagname_ = 'label'
        elif nodeName_ == 'tokens' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'tokens')
            ival_ = self.gds_validate_integer(ival_, node, 'tokens')
            self.tokens = ival_
            self.tokens_nsprefix_ = child_.prefix
            # validate type nonNegativeInteger
            self.validate_nonNegativeInteger(self.tokens)
        elif nodeName_ == 'isStatic':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'isStatic')
            ival_ = self.gds_validate_boolean(ival_, node, 'isStatic')
            self.isStatic = ival_
            self.isStatic_nsprefix_ = child_.prefix
        elif nodeName_ == 'static':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'static')
            ival_ = self.gds_validate_boolean(ival_, node, 'static')
            self.static = ival_
            self.static_nsprefix_ = child_.prefix


# end class place


class arc(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'id': MemberSpec_('id', 'xs:string', 0, 0, {'name': 'id', 'type': 'xs:string'}, None),
        'type_': MemberSpec_('type_', ['arc_type', 'xs:string'], 0, 0,
                             {'default': 'regular', 'name': 'type', 'type': 'xs:string'}, None),
        'sourceId': MemberSpec_('sourceId', 'xs:string', 0, 0, {'name': 'sourceId', 'type': 'xs:string'}, None),
        'destinationId': MemberSpec_('destinationId', 'xs:string', 0, 0, {'name': 'destinationId', 'type': 'xs:string'},
                                     None),
        'multiplicity': MemberSpec_('multiplicity', ['nonNegativeInteger', 'xs:int'], 0, 0,
                                    {'name': 'multiplicity', 'type': 'xs:int'}, None),
        'reference': MemberSpec_('reference', 'xs:string', 0, 1,
                                 {'minOccurs': '0', 'name': 'reference', 'type': 'xs:string'}, None),
        'breakpoint': MemberSpec_('breakpoint', 'breakpoint', 1, 1,
                                  {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'breakpoint',
                                   'type': 'breakpoint'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, id=None, type_='regular', sourceId=None, destinationId=None, multiplicity=None, reference=None,
                 breakpoint=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = id
        self.id_nsprefix_ = None
        self.type_ = type_
        self.validate_arc_type(self.type_)
        self.type__nsprefix_ = None
        self.sourceId = sourceId
        self.sourceId_nsprefix_ = None
        self.destinationId = destinationId
        self.destinationId_nsprefix_ = None
        self.multiplicity = multiplicity
        self.validate_nonNegativeInteger(self.multiplicity)
        self.multiplicity_nsprefix_ = None
        self.reference = reference
        self.reference_nsprefix_ = None
        if breakpoint is None:
            self.breakpoint = []
        else:
            self.breakpoint = breakpoint
        self.breakpoint_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, arc)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if arc.subclass:
            return arc.subclass(*args_, **kwargs_)
        else:
            return arc(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_id(self):
        return self.id

    def set_id(self, id_, doc):
        if type(id_) is str:
            if all(x.id != id_ for x in doc.arc):
                self.id = id_
            else:
                raise ValueError("Requires unique id value")
        else:
            raise TypeError("Requires str value")

    def get_type(self):
        return self.type_

    def set_type_(self, type_):
        if type(type_) is arc_type:
            self.type_ = type_
        else:
            raise TypeError("Requires arc_type value")

    def get_sourceId(self):
        return self.sourceId

    def set_sourceId(self, sourceId):
        if type(sourceId) is str:
            self.sourceId = sourceId
        else:
            raise TypeError("Requires str value")

    def get_destinationId(self):
        return self.destinationId

    def set_destinationId(self, destinationId):
        if type(destinationId) is str:
            self.destinationId = destinationId
        else:
            raise TypeError("Requires str value")

    def get_multiplicity(self):
        return self.multiplicity

    def set_multiplicity(self, multiplicity):
        if type(multiplicity) is int:
            if multiplicity < 0:
                raise ValueError("The 'multiplicity' element has to be nonNegativeInteger")
            else:
                self.multiplicity = multiplicity
        else:
            raise TypeError("Requires int value")

    def get_reference(self):
        return self.reference

    def set_reference(self, reference):
        if type(reference) is str:
            self.reference = reference
        else:
            raise TypeError("Requires str value")

    def get_breakpoint(self):
        return self.breakpoint

    def set_breakpoint(self, breakpoint_):
        if all(isinstance(x, breakpoint) for x in breakpoint_):
            self.breakpoint = breakpoint_
        else:
            raise TypeError("Requires only breakpoint values inside an array")

    def add_breakpoint(self, value):
        if type(value) is breakpoint:
            self.breakpoint.append(value)
        else:
            raise TypeError("Requires breakpoint value")

    def insert_breakpoint_at(self, index, value):
        if 0 <= index <= len(self.breakpoint):
            if type(value) is breakpoint:
                self.breakpoint.insert(index, value)
            else:
                raise TypeError("Requires breakpoint value")
        else:
            raise IndexError("Invalid index value")

    def replace_breakpoint_at(self, index, value):
        if 0 <= index < len(self.breakpoint):
            if self.breakpoint[index]:
                if type(value) is breakpoint:
                    self.breakpoint[index] = value
                else:
                    raise TypeError("Requires breakpoint value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def validate_arc_type(self, value):
        result = True
        # Validate type arc_type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['regular', 'reset', 'inhibitor', 'read', 'variable']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on arc_type' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
        return result

    def validate_nonNegativeInteger(self, value):
        result = True
        # Validate type nonNegativeInteger, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on nonNegativeInteger' % {
                        "value": value, "lineno": lineno})
                result = False
        return result

    def _hasContent(self):
        if (
                self.id is not None or
                self.type_ != "regular" or
                self.sourceId is not None or
                self.destinationId is not None or
                self.multiplicity is not None or
                self.reference is not None or
                self.breakpoint
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='arc', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('arc')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'arc':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='arc')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='arc',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='arc'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='arc', fromsubclass_=False,
                        pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.id is not None:
            namespaceprefix_ = self.id_nsprefix_ + ':' if (UseCapturedNS_ and self.id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sid>%s</%sid>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.id), input_name='id')),
                namespaceprefix_, eol_))
        if self.type_ is not None:
            namespaceprefix_ = self.type__nsprefix_ + ':' if (UseCapturedNS_ and self.type__nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stype>%s</%stype>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.type_), input_name='type')),
                namespaceprefix_, eol_))
        if self.type_ is None:
            namespaceprefix_ = self.type__nsprefix_ + ':' if (UseCapturedNS_ and self.type__nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stype>regular</%stype/>%s' % (namespaceprefix_, namespaceprefix_, eol_))
        if self.sourceId is not None:
            namespaceprefix_ = self.sourceId_nsprefix_ + ':' if (UseCapturedNS_ and self.sourceId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssourceId>%s</%ssourceId>%s' % (
                namespaceprefix_,
                self.gds_encode(self.gds_format_string(quote_xml(self.sourceId), input_name='sourceId')),
                namespaceprefix_, eol_))
        if self.destinationId is not None:
            namespaceprefix_ = self.destinationId_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.destinationId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdestinationId>%s</%sdestinationId>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.destinationId), input_name='destinationId')), namespaceprefix_,
                                                                       eol_))
        if self.multiplicity is not None:
            namespaceprefix_ = self.multiplicity_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.multiplicity_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smultiplicity>%s</%smultiplicity>%s' % (
                namespaceprefix_, self.gds_format_integer(self.multiplicity, input_name='multiplicity'),
                namespaceprefix_,
                eol_))
        if self.reference is not None:
            namespaceprefix_ = self.reference_nsprefix_ + ':' if (UseCapturedNS_ and self.reference_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sreference>%s</%sreference>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.reference), input_name='reference')), namespaceprefix_, eol_))
        for breakpoint_ in self.breakpoint:
            namespaceprefix_ = self.breakpoint_nsprefix_ + ':' if (UseCapturedNS_ and self.breakpoint_nsprefix_) else ''
            breakpoint_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='breakpoint',
                               pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'id')
            value_ = self.gds_validate_string(value_, node, 'id')
            self.id = value_
            self.id_nsprefix_ = child_.prefix
        elif nodeName_ == 'type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'type')
            value_ = self.gds_validate_string(value_, node, 'type')
            self.type_ = value_
            self.type_nsprefix_ = child_.prefix
            # validate type arc_type
            self.validate_arc_type(self.type_)
        elif nodeName_ == 'sourceId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'sourceId')
            value_ = self.gds_validate_string(value_, node, 'sourceId')
            self.sourceId = value_
            self.sourceId_nsprefix_ = child_.prefix
        elif nodeName_ == 'destinationId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'destinationId')
            value_ = self.gds_validate_string(value_, node, 'destinationId')
            self.destinationId = value_
            self.destinationId_nsprefix_ = child_.prefix
        elif nodeName_ == 'multiplicity' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'multiplicity')
            ival_ = self.gds_validate_integer(ival_, node, 'multiplicity')
            self.multiplicity = ival_
            self.multiplicity_nsprefix_ = child_.prefix
            # validate type nonNegativeInteger
            self.validate_nonNegativeInteger(self.multiplicity)
        elif nodeName_ == 'reference':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'reference')
            value_ = self.gds_validate_string(value_, node, 'reference')
            self.reference = value_
            self.reference_nsprefix_ = child_.prefix
        elif nodeName_ == 'breakpoint':
            obj_ = breakpoint.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.breakpoint.append(obj_)
            obj_.original_tagname_ = 'breakpoint'


# end class arc


class i18n(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'locale': MemberSpec_('locale', 'xs:string', 0, 1, {'use': 'optional', 'name': 'locale'}),
        'i18nString': MemberSpec_('i18nString', 'i18nStringType', 1, 1,
                                  {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'i18nString',
                                   'type': 'i18nStringType'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, locale=None, i18nString=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.locale = _cast(None, locale)
        self.locale_nsprefix_ = None
        if i18nString is None:
            self.i18nString = []
        else:
            self.i18nString = i18nString
        self.i18nString_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, i18n)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if i18n.subclass:
            return i18n.subclass(*args_, **kwargs_)
        else:
            return i18n(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_i18nString(self):
        return self.i18nString

    def set_i18nString(self, i18nString):
        if all(isinstance(x, i18nStringType) for x in i18nString):
            self.i18nString = i18nString
        else:
            raise TypeError("Requires only i18nStringType values inside an array")

    def add_i18nString(self, value):
        if type(value) is i18nStringType:
            self.i18nString.append(value)
        else:
            raise TypeError("Requires i18nStringType value")

    def insert_i18nString_at(self, index, value):
        if 0 <= index <= len(self.i18nString):
            if type(value) is i18nStringType:
                self.i18nString.insert(index, value)
            else:
                raise TypeError("Requires i18nStringType value")
        else:
            raise IndexError("Invalid index value")

    def replace_i18nString_at(self, index, value):
        if 0 <= index < len(self.i18nString):
            if self.i18nString[index]:
                if type(value) is i18nStringType:
                    self.i18nString[index] = value
                else:
                    raise TypeError("Requires i18nStringType value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_locale(self):
        return self.locale

    def set_locale(self, locale):
        if type(locale) is str:
            self.locale = locale
        else:
            raise TypeError("Requires str value")

    def _hasContent(self):
        if (
                self.i18nString
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='i18n', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('i18n')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'i18n':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='i18n')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='i18n',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='i18n'):
        if self.locale is not None and 'locale' not in already_processed:
            already_processed.add('locale')
            outfile.write(' locale=%s' % (
                self.gds_encode(self.gds_format_string(quote_attrib(self.locale), input_name='locale')),))

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='i18n', fromsubclass_=False,
                        pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for i18nString_ in self.i18nString:
            namespaceprefix_ = self.i18nString_nsprefix_ + ':' if (UseCapturedNS_ and self.i18nString_nsprefix_) else ''
            i18nString_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='i18nString',
                               pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('locale', node)
        if value is not None and 'locale' not in already_processed:
            already_processed.add('locale')
            self.locale = value

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'i18nString':
            class_obj_ = self.get_class_obj_(child_, i18nStringType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.i18nString.append(obj_)
            obj_.original_tagname_ = 'i18nString'


# end class i18n


class processEvents(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'event': MemberSpec_('event', 'event', 1, 1,
                             {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'event', 'type': 'processEvent'},
                             None),
    }
    subclass = None
    superclass = None

    def __init__(self, event=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if event is None:
            self.event = []
        else:
            self.event = event
        self.event_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, processEvents)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if processEvents.subclass:
            return processEvents.subclass(*args_, **kwargs_)
        else:
            return processEvents(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_event(self):
        return self.event

    # if you want your own specific event list , else it is an empty list
    def set_event(self, event_):
        if all(isinstance(x, processEvent) for x in event_):
            self.event = event_
        else:
            raise TypeError("Requires only processEvent values inside an array")

    def add_event(self, value):
        if type(value) is processEvent:
            self.event.append(value)
        else:
            raise TypeError("Requires processEvent value")

    def insert_event_at(self, index, value):
        if 0 <= index <= len(self.event):
            if type(value) is processEvent:
                self.event.insert(index, value)
            else:
                raise TypeError("Requires processEvent value")
        else:
            raise IndexError("Invalid index value")

    def replace_event_at(self, index, value):
        if 0 <= index < len(self.event):
            if self.event[index]:
                if type(value) is processEvent:
                    self.event[index] = value
                else:
                    raise TypeError("Requires processEvent value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def _hasContent(self):
        if (
                self.event
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='processEvents', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('processEvents')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'processEvents':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='processEvents')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='processEvents',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='processEvents'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='processEvents',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for event_ in self.event:
            namespaceprefix_ = self.event_nsprefix_ + ':' if (UseCapturedNS_ and self.event_nsprefix_) else ''
            event_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='event', pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'event':
            obj_ = processEvent.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.event.append(obj_)
            obj_.original_tagname_ = 'event'


# end class processEvents


class caseEvents(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'event': MemberSpec_('event', 'event', 1, 1,
                             {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'event', 'type': 'caseEvent'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, event=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if event is None:
            self.event = []
        else:
            self.event = event
        self.event_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, caseEvents)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if caseEvents.subclass:
            return caseEvents.subclass(*args_, **kwargs_)
        else:
            return caseEvents(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_event(self):
        return self.event

    # if you want your own specific event list , else it is an empty list
    def set_event(self, event_):
        if all(isinstance(x, caseEvent) for x in event_):
            self.event = event_
        else:
            raise TypeError("Requires only caseEvent values inside an array")

    def add_event(self, value):
        if type(value) is caseEvent:
            self.event.append(value)
        else:
            raise TypeError("Requires caseEvent value")

    def insert_event_at(self, index, value):
        if 0 <= index <= len(self.event):
            if type(value) is caseEvent:
                self.event.insert(index, value)
            else:
                raise TypeError("Requires caseEvent value")
        else:
            raise IndexError("Invalid index value")

    def replace_event_at(self, index, value):
        if 0 <= index < len(self.event):
            if self.event[index]:
                if type(value) is caseEvent:
                    self.event[index] = value
                else:
                    raise TypeError("Requires caseEvent value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def _hasContent(self):
        if (
                self.event
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='caseEvents', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('caseEvents')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'caseEvents':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='caseEvents')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='caseEvents',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='caseEvents'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='caseEvents',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for event_ in self.event:
            namespaceprefix_ = self.event_nsprefix_ + ':' if (UseCapturedNS_ and self.event_nsprefix_) else ''
            event_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='event', pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'event':
            obj_ = caseEvent.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.event.append(obj_)
            obj_.original_tagname_ = 'event'


# end class caseEvents


class documentType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'id': MemberSpec_('id', 'xs:string', 0, 0, {'name': 'id', 'type': 'xs:string'}, None),
        'version': MemberSpec_('version', 'xs:string', 0, 1, {'minOccurs': '0', 'name': 'version', 'type': 'xs:string'},
                               None),
        'initials': MemberSpec_('initials', ['initials', 'xs:string'], 0, 0, {'name': 'initials', 'type': 'xs:string'},
                                None),
        'title': MemberSpec_('title', 'i18nStringType', 0, 0, {'name': 'title', 'type': 'i18nStringType'}, None),
        'icon': MemberSpec_('icon', 'icon', 0, 1, {'minOccurs': '0', 'name': 'icon', 'type': 'xs:string'}, None),
        'defaultRole': MemberSpec_('defaultRole', 'xs:boolean', 0, 1,
                                   {'default': 'true', 'minOccurs': '0', 'name': 'defaultRole', 'type': 'xs:boolean'},
                                   None),
        'anonymousRole': MemberSpec_('anonymousRole', 'xs:boolean', 0, 1,
                                     {'default': 'true', 'minOccurs': '0', 'name': 'anonymousRole',
                                      'type': 'xs:boolean'}, None),
        'transitionRole': MemberSpec_('transitionRole', 'xs:boolean', 0, 1,
                                      {'default': 'true', 'minOccurs': '0', 'name': 'transitionRole',
                                       'type': 'xs:boolean'}, None),
        'caseName': MemberSpec_('caseName', 'i18nStringTypeWithExpression', 0, 1,
                                {'minOccurs': '0', 'name': 'caseName', 'type': 'i18nStringTypeWithExpression'}, None),
        'roleRef': MemberSpec_('roleRef', 'roleRef', 1, 1,
                               {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'roleRef', 'type': 'caseRoleRef'},
                               None),
        'usersRef': MemberSpec_('usersRef', 'caseUserRef', 1, 1,
                                {'maxOccurs': 'unbounded', 'name': 'usersRef', 'type': 'caseUserRef'}, 9),
        'userRef': MemberSpec_('userRef', 'userRef', 1, 1,
                               {'maxOccurs': 'unbounded', 'name': 'userRef', 'type': 'caseUserRef'}, 9),
        'processEvents': MemberSpec_('processEvents', 'processEvents', 0, 1,
                                     {'minOccurs': '0', 'name': 'processEvents', 'type': 'processEvents'}, None),
        'caseEvents': MemberSpec_('caseEvents', 'caseEvents', 0, 1,
                                  {'minOccurs': '0', 'name': 'caseEvents', 'type': 'caseEvents'}, None),
        'transaction': MemberSpec_('transaction', 'transaction', 1, 1,
                                   {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'transaction',
                                    'type': 'transaction'}, None),
        'role': MemberSpec_('role', 'role', 1, 1,
                            {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'role', 'type': 'role'}, None),
        'function': MemberSpec_('function', 'function', 1, 1,
                                {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'function', 'type': 'function'},
                                None),
        'data': MemberSpec_('data', 'data', 1, 1,
                            {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'data', 'type': 'data'}, None),
        'mapping': MemberSpec_('mapping', 'mapping', 1, 1,
                               {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'mapping', 'type': 'mapping'},
                               None),
        'i18n': MemberSpec_('i18n', 'i18n', 1, 1,
                            {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'i18n', 'type': 'i18n'}, None),
        'transition': MemberSpec_('transition', 'transition', 1, 0,
                                  {'maxOccurs': 'unbounded', 'name': 'transition', 'type': 'transition'}, None),
        'place': MemberSpec_('place', 'place', 1, 1,
                             {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'place', 'type': 'place'}, None),
        'arc': MemberSpec_('arc', 'arc', 1, 1,
                           {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'arc', 'type': 'arc'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, id=None, version=None, initials=None, title=None, icon=None, defaultRole=True,
                 anonymousRole=True, transitionRole=True, caseName=None, roleRef=None, usersRef=None, userRef=None,
                 processEvents=None, caseEvents=None, transaction=None, role=None, function=None, data=None,
                 mapping=None, i18n=None, transition=None, place=None, arc=None, extensiontype_=None,
                 gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = id
        self.id_nsprefix_ = None
        self.version = version
        self.version_nsprefix_ = None
        self.initials = initials
        self.validate_initials(self.initials)
        self.initials_nsprefix_ = None
        self.title = title
        self.title_nsprefix_ = None
        self.icon = icon
        self.icon_nsprefix_ = None
        self.defaultRole = defaultRole
        self.defaultRole_nsprefix_ = None
        self.anonymousRole = anonymousRole
        self.anonymousRole_nsprefix_ = None
        self.transitionRole = transitionRole
        self.transitionRole_nsprefix_ = None
        self.caseName = caseName
        self.caseName_nsprefix_ = None
        if roleRef is None:
            self.roleRef = []
        else:
            self.roleRef = roleRef
        self.roleRef_nsprefix_ = None
        if usersRef is None:
            self.usersRef = []
        else:
            self.usersRef = usersRef
        self.usersRef_nsprefix_ = None
        if userRef is None:
            self.userRef = []
        else:
            self.userRef = userRef
        self.userRef_nsprefix_ = None
        self.processEvents = processEvents
        self.processEvents_nsprefix_ = None
        self.caseEvents = caseEvents
        self.caseEvents_nsprefix_ = None
        if transaction is None:
            self.transaction = []
        else:
            self.transaction = transaction
        self.transaction_nsprefix_ = None
        if role is None:
            self.role = []
        else:
            self.role = role
        self.role_nsprefix_ = None
        if function is None:
            self.function = []
        else:
            self.function = function
        self.function_nsprefix_ = None
        if data is None:
            self.data = []
        else:
            self.data = data
        self.data_nsprefix_ = None
        if mapping is None:
            self.mapping = []
        else:
            self.mapping = mapping
        self.mapping_nsprefix_ = None
        if i18n is None:
            self.i18n = []
        else:
            self.i18n = i18n
        self.i18n_nsprefix_ = None
        if transition is None:
            self.transition = []
        else:
            self.transition = transition
        self.transition_nsprefix_ = None
        if place is None:
            self.place = []
        else:
            self.place = place
        self.place_nsprefix_ = None
        if arc is None:
            self.arc = []
        else:
            self.arc = arc
        self.arc_nsprefix_ = None
        self.extensiontype_ = extensiontype_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, documentType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if documentType.subclass:
            return documentType.subclass(*args_, **kwargs_)
        else:
            return documentType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_id(self):
        return self.id

    def set_id(self, id_):
        if type(id_) is str:
            self.id = id_
        else:
            raise TypeError("Requires str value")

    def get_version(self):
        return self.version

    def set_version(self, version):
        if type(version) is str:
            self.version = version
        else:
            raise TypeError("Requires str value")

    def get_initials(self):
        return self.initials

    def set_initials(self, initials):
        try:
            assert isinstance(initials, str), "Requires str value"
            assert len(
                initials) == 3, f"Element 'initials': [facet 'length'] The value has a length of '{len(initials)}'; this differs from the allowed length of '3'."
            self.initials = initials
        except AssertionError as e:
            print(type(e))
            raise Exception(str(e))

    def get_title(self):
        return self.title

    def set_title(self, title):
        if type(title) is i18nStringType:
            self.title = title
        else:
            raise TypeError("Requires i18nStringType value")

    def get_icon(self):
        return self.icon

    def set_icon(self, icon_):
        if type(icon_) is str:
            self.icon = icon_
        else:
            raise TypeError("Requires str value")

    def get_defaultRole(self):
        return self.defaultRole

    def set_defaultRole(self, defaultRole):
        self.defaultRole = set_boolean_value(defaultRole)

    def get_anonymousRole(self):
        return self.anonymousRole

    def set_anonymousRole(self, anonymousRole):
        self.anonymousRole = set_boolean_value(anonymousRole)

    def get_transitionRole(self):
        return self.transitionRole

    def set_transitionRole(self, transitionRole):
        self.transitionRole = set_boolean_value(transitionRole)

    def get_caseName(self):
        return self.caseName

    def set_caseName(self, caseName):
        if type(caseName) is i18nStringTypeWithExpression:
            self.caseName = caseName
        else:
            raise TypeError("Requires i18nStringTypeWithExpression value")

    def get_roleRef(self):
        return self.roleRef

    def set_roleRef(self, roleRef):
        if all(isinstance(x, caseRoleRef) for x in roleRef):
            self.roleRef = roleRef
        else:
            raise TypeError("Requires only caseRoleRef values inside an array")

    def add_roleRef(self, value):
        if type(value) is caseRoleRef:
            self.roleRef.append(value)
        else:
            raise TypeError("Requires caseRoleRef value")

    def insert_roleRef_at(self, index, value):
        if 0 <= index <= len(self.roleRef):
            if type(value) is caseRoleRef:
                self.roleRef.insert(index, value)
            else:
                raise TypeError("Requires caseRoleRef value")
        else:
            raise IndexError("Invalid index value")

    def replace_roleRef_at(self, index, value):
        if 0 <= index < len(self.roleRef):
            if self.roleRef[index]:
                if type(value) is caseRoleRef:
                    self.roleRef[index] = value
                else:
                    raise TypeError("Requires caseRoleRef value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_usersRef(self):
        return self.usersRef

    def set_usersRef(self, usersRef):
        if not self.userRef:
            if all(isinstance(x, caseUserRef) for x in usersRef):
                self.usersRef = usersRef
            else:
                raise TypeError("Requires only caseUserRef values inside an array")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'userRef' element.")

    def add_usersRef(self, value):
        if not self.userRef:
            if type(value) is caseUserRef:
                self.usersRef.append(value)
            else:
                raise TypeError("Requires caseUserRef value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'userRef' element.")

    def insert_usersRef_at(self, index, value):
        if not self.userRef:
            if 0 <= index <= len(self.usersRef):
                if type(value) is caseUserRef:
                    self.usersRef.insert(index, value)
                else:
                    raise TypeError("Requires caseUserRef value")
            else:
                raise IndexError("Invalid index value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'userRef' element.")

    def replace_usersRef_at(self, index, value):
        if not self.userRef:
            if 0 <= index < len(self.usersRef):
                if self.usersRef[index]:
                    if type(value) is caseUserRef:
                        self.usersRef[index] = value
                    else:
                        raise TypeError("Requires caseUserRef value")
                else:
                    raise Exception("Invalid index value")
            else:
                raise IndexError("Index out of range")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'userRef' element.")

    def get_userRef(self):
        return self.userRef

    def set_userRef(self, userRef):
        if not self.usersRef:
            if all(isinstance(x, caseUserRef) for x in userRef):
                self.userRef = userRef
            else:
                raise TypeError("Requires only caseUserRef values inside an array")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'usersRef' element.")

    def add_userRef(self, value):
        if not self.usersRef:
            if type(value) is caseUserRef:
                self.userRef.append(value)
            else:
                raise TypeError("Requires caseUserRef value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'usersRef' element.")

    def insert_userRef_at(self, index, value):
        if not self.usersRef:
            if 0 <= index <= len(self.userRef):
                if type(value) is caseUserRef:
                    self.userRef.insert(index, value)
                else:
                    raise TypeError("Requires caseUserRef value")
            else:
                raise IndexError("Invalid index value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'usersRef' element.")

    def replace_userRef_at(self, index, value):
        if not self.usersRef:
            if 0 <= index < len(self.userRef):
                if self.userRef[index]:
                    if type(value) is caseUserRef:
                        self.userRef[index] = value
                    else:
                        raise TypeError("Requires caseUserRef value")
                else:
                    raise Exception("Invalid index value")
            else:
                raise IndexError("Index out of range")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'usersRef' element.")

    def get_processEvents(self):
        return self.processEvents

    def set_processEvents(self, processEvents_):
        if type(processEvents_) is processEvents:
            self.processEvents = processEvents_
        else:
            raise TypeError("Requires processEvents value")

    def get_caseEvents(self):
        return self.caseEvents

    def set_caseEvents(self, caseEvents_):
        if type(caseEvents_) is caseEvents:
            self.caseEvents = caseEvents_
        else:
            raise TypeError("Requires caseEvents value")

    def get_transaction(self):
        return self.transaction

    def set_transaction(self, transaction_):
        if all(isinstance(x, transaction) for x in transaction_):
            self.transaction = transaction_
        else:
            raise TypeError("Requires only transaction values inside an array")

    def add_transaction(self, value):
        if type(value) is transaction:
            self.transaction.append(value)
        else:
            raise TypeError("Requires transaction value")

    def insert_transaction_at(self, index, value):
        if 0 <= index <= len(self.transaction):
            if type(value) is transaction:
                self.transaction.insert(index, value)
            else:
                raise TypeError("Requires transaction value")
        else:
            raise IndexError("Invalid index value")

    def replace_transaction_at(self, index, value):
        if 0 <= index < len(self.transaction):
            if self.transaction[index]:
                if type(value) is transaction:
                    self.transaction[index] = value
                else:
                    raise TypeError("Requires transaction value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_role(self):
        return self.role

    def set_role(self, role_):
        if all(isinstance(x, role) for x in role_):
            self.role = role_
        else:
            raise TypeError("Requires only role values inside an array")

    def add_role(self, value):
        if type(value) is role:
            self.role.append(value)
        else:
            raise TypeError("Requires role value")

    def insert_role_at(self, index, value):
        if 0 <= index <= len(self.role):
            if type(value) is role:
                self.role.insert(index, value)
            else:
                raise TypeError("Requires role value")
        else:
            raise IndexError("Invalid index value")

    def replace_role_at(self, index, value):
        if 0 <= index < len(self.role):
            if self.role[index]:
                if type(value) is role:
                    self.role[index] = value
                else:
                    raise TypeError("Requires role value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_function(self):
        return self.function

    def set_function(self, function_):
        if all(isinstance(x, function) for x in function_):
            self.function = function_
        else:
            raise TypeError("Requires only function values inside an array")

    def add_function(self, value):
        if type(value) is function:
            self.function.append(value)
        else:
            raise TypeError("Requires function value")

    def insert_function_at(self, index, value):
        if 0 <= index <= len(self.function):
            if type(value) is function:
                self.function.insert(index, value)
            else:
                raise TypeError("Requires function value")
        else:
            raise IndexError("Invalid index value")

    def replace_function_at(self, index, value):
        if 0 <= index < len(self.function):
            if self.function[index]:
                if type(value) is function:
                    self.function[index] = value
                else:
                    raise TypeError("Requires function value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_data(self):
        return self.data

    def set_data(self, data_):
        if all(isinstance(x, data) for x in data_):
            self.data = data_
        else:
            raise TypeError("Requires only data values inside an array")

    def add_data(self, value):
        if type(value) is data:
            self.data.append(value)
        else:
            raise TypeError("Requires data value")

    def insert_data_at(self, index, value):
        if 0 <= index <= len(self.data):
            if type(value) is data:
                self.data.insert(index, value)
            else:
                raise TypeError("Requires data value")
        else:
            raise IndexError("Invalid index value")

    def replace_data_at(self, index, value):
        if 0 <= index < len(self.data):
            if self.data[index]:
                if type(value) is data:
                    self.data[index] = value
                else:
                    raise TypeError("Requires data value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_mapping(self):
        return self.mapping

    def set_mapping(self, mapping_):
        if all(isinstance(x, mapping) for x in mapping_):
            self.mapping = mapping_
        else:
            raise TypeError("Requires only mapping values inside an array")

    def add_mapping(self, value):
        if type(value) is mapping:
            self.mapping.append(value)
        else:
            raise TypeError("Requires mapping value")

    def insert_mapping_at(self, index, value):
        if 0 <= index <= len(self.mapping):
            if type(value) is mapping:
                self.mapping.insert(index, value)
            else:
                raise TypeError("Requires mapping value")
        else:
            raise IndexError("Invalid index value")

    def replace_mapping_at(self, index, value):
        if 0 <= index < len(self.mapping):
            if self.mapping[index]:
                if type(value) is mapping:
                    self.mapping[index] = value
                else:
                    raise TypeError("Requires mapping value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_i18n(self):
        return self.i18n

    def set_i18n(self, i18n_):
        if all(isinstance(x, i18n) for x in i18n_):
            self.i18n = i18n_
        else:
            raise TypeError("Requires only i18n values inside an array")

    def add_i18n(self, value):
        if type(value) is i18n:
            self.i18n.append(value)
        else:
            raise TypeError("Requires i18n value")

    def insert_i18n_at(self, index, value):
        if 0 <= index <= len(self.i18n):
            if type(value) is i18n:
                self.i18n.insert(index, value)
            else:
                raise TypeError("Requires i18n value")
        else:
            raise IndexError("Invalid index value")

    def replace_i18n_at(self, index, value):
        if 0 <= index < len(self.i18n):
            if self.i18n[index]:
                if type(value) is i18n:
                    self.i18n[index] = value
                else:
                    raise TypeError("Requires i18n value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_transition(self):
        return self.transition

    def set_transition(self, transition_):
        if all(isinstance(x, transition) for x in transition_):
            self.transition = transition_
        else:
            raise TypeError("Requires only transition values inside an array")

    def add_transition(self, value):
        if type(value) is transition:
            self.transition.append(value)
        else:
            raise TypeError("Requires transition value")

    def insert_transition_at(self, index, value):
        if 0 <= index <= len(self.transition):
            if type(value) is transition:
                self.transition.insert(index, value)
            else:
                raise TypeError("Requires transition value")
        else:
            raise IndexError("Invalid index value")

    def replace_transition_at(self, index, value):
        if 0 <= index < len(self.transition):
            if self.transition[index]:
                if type(value) is transition:
                    self.transition[index] = value
                else:
                    raise TypeError("Requires transition value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_place(self):
        return self.place

    def set_place(self, place_):
        if all(isinstance(x, place) for x in place_):
            self.place = place_
        else:
            raise TypeError("Requires only place values inside an array")

    def add_place(self, value):
        if type(value) is place:
            self.place.append(value)
        else:
            raise TypeError("Requires place value")

    def insert_place_at(self, index, value):
        if 0 <= index <= len(self.place):
            if type(value) is place:
                self.place.insert(index, value)
            else:
                raise TypeError("Requires place value")
        else:
            raise IndexError("Invalid index value")

    def replace_place_at(self, index, value):
        if 0 <= index < len(self.place):
            if self.place[index]:
                if type(value) is place:
                    self.place[index] = value
                else:
                    raise TypeError("Requires place value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_arc(self):
        return self.arc

    def set_arc(self, arc_):
        if all(isinstance(x, arc) for x in arc_):
            self.arc = arc_
        else:
            raise TypeError("Requires only arc values inside an array")

    def add_arc(self, value):
        if type(value) is arc:
            self.arc.append(value)
        else:
            raise TypeError("Requires arc value")

    def insert_arc_at(self, index, value):
        if 0 <= index <= len(self.arc):
            if type(value) is arc:
                self.arc.insert(index, value)
            else:
                raise TypeError("Requires arc value")
        else:
            raise IndexError("Invalid index value")

    def replace_arc_at(self, index, value):
        if 0 <= index < len(self.arc):
            if self.arc[index]:
                if type(value) is arc:
                    self.arc[index] = value
                else:
                    raise TypeError("Requires arc value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_extensiontype_(self):
        return self.extensiontype_

    def set_extensiontype_(self, extensiontype_):
        self.extensiontype_ = extensiontype_

    def validate_initials(self, value):
        result = True
        # Validate type initials, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            if len(value) != 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd length restriction on initials' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
        return result

    def _hasContent(self):
        if (
                self.id is not None or
                self.version is not None or
                self.initials is not None or
                self.title is not None or
                self.icon is not None or
                self.defaultRole is not None or
                self.anonymousRole is not None or
                self.transitionRole is not None or
                self.caseName is not None or
                self.roleRef or
                self.usersRef or
                self.userRef or
                self.processEvents is not None or
                self.caseEvents is not None or
                self.transaction or
                self.role or
                self.function or
                self.data or
                self.mapping or
                self.i18n or
                self.transition or
                self.place or
                self.arc
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='documentType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('documentType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'documentType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='documentType')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='documentType',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='documentType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='documentType',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.id is not None:
            namespaceprefix_ = self.id_nsprefix_ + ':' if (UseCapturedNS_ and self.id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sid>%s</%sid>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.id), input_name='id')),
                namespaceprefix_, eol_))
        if self.version is not None:
            namespaceprefix_ = self.version_nsprefix_ + ':' if (UseCapturedNS_ and self.version_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sversion>%s</%sversion>%s' % (
                namespaceprefix_,
                self.gds_encode(self.gds_format_string(quote_xml(self.version), input_name='version')),
                namespaceprefix_, eol_))
        if self.initials is not None:
            namespaceprefix_ = self.initials_nsprefix_ + ':' if (UseCapturedNS_ and self.initials_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinitials>%s</%sinitials>%s' % (
                namespaceprefix_,
                self.gds_encode(self.gds_format_string(quote_xml(self.initials), input_name='initials')),
                namespaceprefix_, eol_))
        if self.title is not None:
            namespaceprefix_ = self.title_nsprefix_ + ':' if (UseCapturedNS_ and self.title_nsprefix_) else ''
            self.title.export(outfile, level, namespaceprefix_, namespacedef_='', name_='title',
                              pretty_print=pretty_print)
        if self.icon is not None:
            namespaceprefix_ = self.icon_nsprefix_ + ':' if (UseCapturedNS_ and self.icon_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sicon>%s</%sicon>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.icon), input_name='icon')),
                namespaceprefix_, eol_))

        if self.defaultRole is not None:
            namespaceprefix_ = self.defaultRole_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.defaultRole_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdefaultRole>%s</%sdefaultRole>%s' % (
                namespaceprefix_, self.gds_format_boolean(self.defaultRole, input_name='defaultRole'),
                namespaceprefix_, eol_))

        if self.anonymousRole is not None:
            namespaceprefix_ = self.anonymousRole_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.anonymousRole_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sanonymousRole>%s</%sanonymousRole>%s' % (
                namespaceprefix_, self.gds_format_boolean(self.anonymousRole, input_name='anonymousRole'),
                namespaceprefix_,
                eol_))
        if self.transitionRole is not None:
            namespaceprefix_ = self.transitionRole_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.transitionRole_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stransitionRole>%s</%stransitionRole>%s' % (
                namespaceprefix_, self.gds_format_boolean(self.transitionRole, input_name='transitionRole'),
                namespaceprefix_, eol_))
        if self.caseName is not None:
            namespaceprefix_ = self.caseName_nsprefix_ + ':' if (UseCapturedNS_ and self.caseName_nsprefix_) else ''
            self.caseName.export(outfile, level, namespaceprefix_, namespacedef_='', name_='caseName',
                                 pretty_print=pretty_print)
        for roleRef_ in self.roleRef:
            namespaceprefix_ = self.roleRef_nsprefix_ + ':' if (UseCapturedNS_ and self.roleRef_nsprefix_) else ''
            roleRef_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='roleRef',
                            pretty_print=pretty_print)
        for usersRef_ in self.usersRef:
            namespaceprefix_ = self.usersRef_nsprefix_ + ':' if (UseCapturedNS_ and self.usersRef_nsprefix_) else ''
            usersRef_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='usersRef',
                             pretty_print=pretty_print)
        for userRef_ in self.userRef:
            namespaceprefix_ = self.userRef_nsprefix_ + ':' if (UseCapturedNS_ and self.userRef_nsprefix_) else ''
            userRef_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='userRef',
                            pretty_print=pretty_print)
        if self.processEvents is not None:
            namespaceprefix_ = self.processEvents_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.processEvents_nsprefix_) else ''
            self.processEvents.export(outfile, level, namespaceprefix_, namespacedef_='', name_='processEvents',
                                      pretty_print=pretty_print)
        if self.caseEvents is not None:
            namespaceprefix_ = self.caseEvents_nsprefix_ + ':' if (UseCapturedNS_ and self.caseEvents_nsprefix_) else ''
            self.caseEvents.export(outfile, level, namespaceprefix_, namespacedef_='', name_='caseEvents',
                                   pretty_print=pretty_print)
        for transaction_ in self.transaction:
            namespaceprefix_ = self.transaction_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.transaction_nsprefix_) else ''
            transaction_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='transaction',
                                pretty_print=pretty_print)
        for role_ in self.role:
            namespaceprefix_ = self.role_nsprefix_ + ':' if (UseCapturedNS_ and self.role_nsprefix_) else ''
            role_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='role', pretty_print=pretty_print)
        for function_ in self.function:
            namespaceprefix_ = self.function_nsprefix_ + ':' if (UseCapturedNS_ and self.function_nsprefix_) else ''
            function_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='function',
                             pretty_print=pretty_print)
        for data_ in self.data:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            data_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
        for mapping_ in self.mapping:
            namespaceprefix_ = self.mapping_nsprefix_ + ':' if (UseCapturedNS_ and self.mapping_nsprefix_) else ''
            mapping_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='mapping',
                            pretty_print=pretty_print)
        for i18n_ in self.i18n:
            namespaceprefix_ = self.i18n_nsprefix_ + ':' if (UseCapturedNS_ and self.i18n_nsprefix_) else ''
            i18n_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='i18n', pretty_print=pretty_print)
        for transition_ in self.transition:
            namespaceprefix_ = self.transition_nsprefix_ + ':' if (UseCapturedNS_ and self.transition_nsprefix_) else ''
            transition_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='transition',
                               pretty_print=pretty_print)
        for place_ in self.place:
            namespaceprefix_ = self.place_nsprefix_ + ':' if (UseCapturedNS_ and self.place_nsprefix_) else ''
            place_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='place', pretty_print=pretty_print)
        for arc_ in self.arc:
            namespaceprefix_ = self.arc_nsprefix_ + ':' if (UseCapturedNS_ and self.arc_nsprefix_) else ''
            arc_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='arc', pretty_print=pretty_print)

    def build(self, node):  # , gds_collector_=None
        # self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_)  # , gds_collector_=gds_collector_
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'id')
            value_ = self.gds_validate_string(value_, node, 'id')
            self.id = value_
            self.id_nsprefix_ = child_.prefix
        elif nodeName_ == 'version':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'version')
            value_ = self.gds_validate_string(value_, node, 'version')
            self.version = value_
            self.version_nsprefix_ = child_.prefix
        elif nodeName_ == 'initials':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'initials')
            value_ = self.gds_validate_string(value_, node, 'initials')
            self.initials = value_
            self.initials_nsprefix_ = child_.prefix
            # validate type initials
            self.validate_initials(self.initials)
        elif nodeName_ == 'title':
            class_obj_ = self.get_class_obj_(child_, i18nStringType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.title = obj_
            obj_.original_tagname_ = 'title'
        elif nodeName_ == 'icon':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'icon')
            value_ = self.gds_validate_string(value_, node, 'icon')
            self.icon = value_
            self.icon_nsprefix_ = child_.prefix
        elif nodeName_ == 'defaultRole':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'defaultRole')
            ival_ = self.gds_validate_boolean(ival_, node, 'defaultRole')
            self.defaultRole = ival_
            self.defaultRole_nsprefix_ = child_.prefix
        elif nodeName_ == 'anonymousRole':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'anonymousRole')
            ival_ = self.gds_validate_boolean(ival_, node, 'anonymousRole')
            self.anonymousRole = ival_
            self.anonymousRole_nsprefix_ = child_.prefix
        elif nodeName_ == 'transitionRole':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'transitionRole')
            ival_ = self.gds_validate_boolean(ival_, node, 'transitionRole')
            self.transitionRole = ival_
            self.transitionRole_nsprefix_ = child_.prefix
        elif nodeName_ == 'caseName':
            class_obj_ = self.get_class_obj_(child_, i18nStringTypeWithExpression)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.caseName = obj_
            obj_.original_tagname_ = 'caseName'
        elif nodeName_ == 'roleRef':
            obj_ = caseRoleRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.roleRef.append(obj_)
            obj_.original_tagname_ = 'roleRef'
        elif nodeName_ == 'usersRef':
            obj_ = caseUserRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.usersRef.append(obj_)
            obj_.original_tagname_ = 'usersRef'
        elif nodeName_ == 'userRef':
            obj_ = caseUserRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.userRef.append(obj_)
            obj_.original_tagname_ = 'userRef'
        elif nodeName_ == 'processEvents':
            obj_ = processEvents.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.processEvents = obj_
            obj_.original_tagname_ = 'processEvents'
        elif nodeName_ == 'caseEvents':
            obj_ = caseEvents.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.caseEvents = obj_
            obj_.original_tagname_ = 'caseEvents'
        elif nodeName_ == 'transaction':
            obj_ = transaction.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.transaction.append(obj_)
            obj_.original_tagname_ = 'transaction'
        elif nodeName_ == 'role':
            obj_ = role.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.role.append(obj_)
            obj_.original_tagname_ = 'role'
        elif nodeName_ == 'function':
            obj_ = function.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.function.append(obj_)
            obj_.original_tagname_ = 'function'
        elif nodeName_ == 'data':
            obj_ = data.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data.append(obj_)
            obj_.original_tagname_ = 'data'
        elif nodeName_ == 'mapping':
            obj_ = mapping.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.mapping.append(obj_)
            obj_.original_tagname_ = 'mapping'
        elif nodeName_ == 'i18n':
            obj_ = i18n.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.i18n.append(obj_)
            obj_.original_tagname_ = 'i18n'
        elif nodeName_ == 'transition':
            obj_ = transition.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.transition.append(obj_)
            obj_.original_tagname_ = 'transition'
        elif nodeName_ == 'place':
            obj_ = place.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.place.append(obj_)
            obj_.original_tagname_ = 'place'
        elif nodeName_ == 'arc':
            obj_ = arc.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.arc.append(obj_)
            obj_.original_tagname_ = 'arc'


# end class documentType


class breakpoint(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'x': MemberSpec_('x', ['nonNegativeInteger', 'xs:int'], 0, 0, {'name': 'x', 'type': 'xs:int'}, None),
        'y': MemberSpec_('y', ['nonNegativeInteger', 'xs:int'], 0, 0, {'name': 'y', 'type': 'xs:int'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, x=None, y=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.x = x
        self.validate_nonNegativeInteger(self.x)
        self.x_nsprefix_ = None
        self.y = y
        self.validate_nonNegativeInteger(self.y)
        self.y_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, breakpoint)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if breakpoint.subclass:
            return breakpoint.subclass(*args_, **kwargs_)
        else:
            return breakpoint(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_x(self):
        return self.x

    def set_x(self, x):
        if type(x) is int:
            if x < 0:
                raise ValueError("The 'x' element has to be nonNegativeInteger")
            else:
                self.x = x
        else:
            raise TypeError("Requires int value")

    def get_y(self):
        return self.y

    def set_y(self, y):
        if type(y) is int:
            if y < 0:
                raise ValueError("The 'y' element has to be nonNegativeInteger")
            else:
                self.y = y
        else:
            raise TypeError("Requires int value")

    def validate_nonNegativeInteger(self, value):
        result = True
        # Validate type nonNegativeInteger, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on nonNegativeInteger' % {
                        "value": value, "lineno": lineno})
                result = False
        return result

    def _hasContent(self):
        if (
                self.x is not None or
                self.y is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='breakpoint', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('breakpoint')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'breakpoint':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='breakpoint')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='breakpoint',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='breakpoint'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='breakpoint',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.x is not None:
            namespaceprefix_ = self.x_nsprefix_ + ':' if (UseCapturedNS_ and self.x_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sx>%s</%sx>%s' % (
                namespaceprefix_, self.gds_format_integer(self.x, input_name='x'), namespaceprefix_, eol_))
        if self.y is not None:
            namespaceprefix_ = self.y_nsprefix_ + ':' if (UseCapturedNS_ and self.y_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sy>%s</%sy>%s' % (
                namespaceprefix_, self.gds_format_integer(self.y, input_name='y'), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'x' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'x')
            ival_ = self.gds_validate_integer(ival_, node, 'x')
            self.x = ival_
            self.x_nsprefix_ = child_.prefix
            # validate type nonNegativeInteger
            self.validate_nonNegativeInteger(self.x)
        elif nodeName_ == 'y' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'y')
            ival_ = self.gds_validate_integer(ival_, node, 'y')
            self.y = ival_
            self.y_nsprefix_ = child_.prefix
            # validate type nonNegativeInteger
            self.validate_nonNegativeInteger(self.y)


# end class breakpoint


class options(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'option': MemberSpec_('option', 'option', 1, 1,
                              {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'option', 'type': 'option'}, 10),
        'init': MemberSpec_('init', 'init', 0, 0, {'name': 'init', 'type': 'init'}, 10),
    }
    subclass = None
    superclass = None

    def __init__(self, option=None, init=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if option is None:
            self.option = []
        else:
            self.option = option
        self.option_nsprefix_ = None
        self.init = init
        self.init_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, options)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if options.subclass:
            return options.subclass(*args_, **kwargs_)
        else:
            return options(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_option(self):
        return self.option

    def set_option(self, option_):
        if self.init is None:
            if all(isinstance(x, option) for x in option_):
                self.option = option_
            else:
                raise TypeError("Requires only option values inside an array")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'init' element.")

    def add_option(self, value):
        if self.init is None:
            if type(value) is option:
                self.option.append(value)
            else:
                raise TypeError("Requires option value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'init' element.")

    def insert_option_at(self, index, value):
        if self.init is None:
            if 0 <= index <= len(self.option):
                if type(value) is option:
                    self.option.insert(index, value)
                else:
                    raise TypeError("Requires option value")
            else:
                raise IndexError("Invalid index value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'init' element.")

    def replace_option_at(self, index, value):
        if self.init is None:
            if 0 <= index < len(self.option):
                if self.option[index]:
                    if type(value) is option:
                        self.option[index] = value
                    else:
                        raise TypeError("Requires option value")
                else:
                    raise Exception("Invalid index value")
            else:
                raise IndexError("Index out of range")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'init' element.")

    def get_init(self):
        return self.init

    def set_init(self, init_):
        if not self.option:
            if type(init_) is init:
                self.init = init_
            else:
                raise TypeError("Requires init value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'option' element.")

    def _hasContent(self):
        if (
                self.option or
                self.init is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='options', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('options')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'options':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='options')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='options',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='options'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='options',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for option_ in self.option:
            namespaceprefix_ = self.option_nsprefix_ + ':' if (UseCapturedNS_ and self.option_nsprefix_) else ''
            option_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='option',
                           pretty_print=pretty_print)
        if self.init is not None:
            namespaceprefix_ = self.init_nsprefix_ + ':' if (UseCapturedNS_ and self.init_nsprefix_) else ''
            self.init.export(outfile, level, namespaceprefix_, namespacedef_='', name_='init',
                             pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'option':
            obj_ = option.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.option.append(obj_)
            obj_.original_tagname_ = 'option'
        elif nodeName_ == 'init':
            obj_ = init.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.init = obj_
            obj_.original_tagname_ = 'init'


# end class options


class inits(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'init': MemberSpec_('init', 'init', 1, 1,
                            {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'init', 'type': 'init'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, init=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if init is None:
            self.init = []
        else:
            self.init = init
        self.init_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, inits)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if inits.subclass:
            return inits.subclass(*args_, **kwargs_)
        else:
            return inits(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_init(self):
        return self.init

    def set_init(self, init_):
        if all(isinstance(x, init) for x in init_):
            self.init = init_
        else:
            raise TypeError("Requires only init values inside an array")

    def add_init(self, value):
        if type(value) is init:
            self.init.append(value)
        else:
            raise TypeError("Requires init value")

    def insert_init_at(self, index, value):
        if 0 <= index <= len(self.init):
            if type(value) is init:
                self.init.insert(index, value)
            else:
                raise TypeError("Requires init value")
        else:
            raise IndexError("Invalid index value")

    def replace_init_at(self, index, value):
        if 0 <= index < len(self.init):
            if self.init[index]:
                if type(value) is init:
                    self.init[index] = value
                else:
                    raise TypeError("Requires init value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def _hasContent(self):
        if (
                self.init
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='inits', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('inits')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'inits':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='inits')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='inits',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='inits'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='inits', fromsubclass_=False,
                        pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for init_ in self.init:
            namespaceprefix_ = self.init_nsprefix_ + ':' if (UseCapturedNS_ and self.init_nsprefix_) else ''
            init_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='init', pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'init':
            obj_ = init.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.init.append(obj_)
            obj_.original_tagname_ = 'init'


# end class inits


class expression(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'dynamic': MemberSpec_('dynamic', 'xs:boolean', 0, 1, {'use': 'optional', 'name': 'dynamic'}),
        'valueOf_': MemberSpec_('valueOf_', 'xs:string', 0),
    }
    subclass = None
    superclass = None

    def __init__(self, dynamic=False, valueOf_=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.dynamic = _cast(bool, dynamic)
        self.dynamic_nsprefix_ = None
        self.valueOf_ = valueOf_
        self.extensiontype_ = extensiontype_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, expression)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if expression.subclass:
            return expression.subclass(*args_, **kwargs_)
        else:
            return expression(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_dynamic(self):
        return self.dynamic

    def set_dynamic(self, dynamic):
        self.dynamic = set_boolean_value(dynamic)

    def get_valueOf_(self):
        return self.valueOf_

    def set_valueOf_(self, valueOf_):
        if type(valueOf_) is str:
            self.valueOf_ = valueOf_
        else:
            raise TypeError("Requires str value")

    def get_extensiontype_(self):
        return self.extensiontype_

    def set_extensiontype_(self, extensiontype_):
        self.extensiontype_ = extensiontype_

    def _hasContent(self):
        if (
                (1 if type(self.valueOf_) in [int, float] else self.valueOf_)
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='expression', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('expression')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'expression':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='expression')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='expression',
                                 pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='expression'):
        if self.dynamic and 'dynamic' not in already_processed:
            already_processed.add('dynamic')
            outfile.write(' dynamic="%s"' % self.gds_format_boolean(self.dynamic, input_name='dynamic'))
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='expression',
                        fromsubclass_=False, pretty_print=True):
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('dynamic', node)
        if value is not None and 'dynamic' not in already_processed:
            already_processed.add('dynamic')
            if value in ('true', '1'):
                self.dynamic = True
            elif value in ('false', '0'):
                self.dynamic = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass


# end class expression


class component(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'name': MemberSpec_('name', 'xs:string', 0, 0, {'name': 'name', 'type': 'xs:string'}, None),
        'property': MemberSpec_('property', 'property', 1, 1,
                                {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'property', 'type': 'property'},
                                11),
        'properties': MemberSpec_('properties', 'properties', 0, 0, {'name': 'properties', 'type': 'properties'}, 11),
    }
    subclass = None
    superclass = None

    def __init__(self, name=None, property=None, properties=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = name
        self.name_nsprefix_ = None
        if property is None:
            self.property = []
        else:
            self.property = property
        self.property_nsprefix_ = None
        self.properties = properties
        self.properties_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, component)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if component.subclass:
            return component.subclass(*args_, **kwargs_)
        else:
            return component(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_name(self):
        return self.name

    def set_name(self, name):
        if type(name) is str:
            self.name = name
        else:
            raise TypeError("Requires str value")

    def get_property(self):
        return self.property

    def set_property(self, property_):
        if self.properties is None:
            if all(isinstance(x, property) for x in property_):
                self.property = property_
            else:
                raise TypeError("Requires only property values inside an array")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'properties' element.")

    def add_property(self, value):
        if self.properties is None:
            if type(value) is property:
                self.property.append(value)
            else:
                raise TypeError("Requires property value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'properties' element.")

    def insert_property_at(self, index, value):
        if not self.properties:
            if 0 <= index <= len(self.property):
                if type(value) is property:
                    self.property.insert(index, value)
                else:
                    raise TypeError("Requires property value")
            else:
                raise IndexError("Invalid index value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'properties' element.")

    def replace_property_at(self, index, value):
        if not self.properties:
            if 0 <= index < len(self.property):
                if self.property[index]:
                    if type(value) is property:
                        self.property[index] = value
                    else:
                        raise TypeError("Requires property value")
                else:
                    raise Exception("Invalid index value")
            else:
                raise IndexError("Index out of range")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'properties' element.")

    def get_properties(self):
        return self.properties

    def set_properties(self, properties_):
        if not self.property:
            if type(properties_) is properties:
                self.properties = properties_
            else:
                raise TypeError("Requires properties value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'property' element.")

    def _hasContent(self):
        if (
                self.name is not None or
                self.property or
                self.properties is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='component', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('component')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'component':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='component')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='component',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='component'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='component',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sname>%s</%sname>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.name), input_name='name')),
                namespaceprefix_, eol_))
        for property_ in self.property:
            namespaceprefix_ = self.property_nsprefix_ + ':' if (UseCapturedNS_ and self.property_nsprefix_) else ''
            property_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='property',
                             pretty_print=pretty_print)
        if self.properties is not None:
            namespaceprefix_ = self.properties_nsprefix_ + ':' if (UseCapturedNS_ and self.properties_nsprefix_) else ''
            self.properties.export(outfile, level, namespaceprefix_, namespacedef_='', name_='properties',
                                   pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
        elif nodeName_ == 'property':
            obj_ = property.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.property.append(obj_)
            obj_.original_tagname_ = 'property'
        elif nodeName_ == 'properties':
            obj_ = properties.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.properties = obj_
            obj_.original_tagname_ = 'properties'


# end class component


class property(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'key': MemberSpec_('key', 'xs:string', 0, 0, {'use': 'required', 'name': 'key'}),
        'valueOf_': MemberSpec_('valueOf_', 'xs:string', 0),
    }
    subclass = None
    superclass = None

    def __init__(self, key=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.key = _cast(None, key)
        self.key_nsprefix_ = None
        self.valueOf_ = valueOf_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, property)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if property.subclass:
            return property.subclass(*args_, **kwargs_)
        else:
            return property(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_key(self):
        return self.key

    def set_key(self, key):
        if type(key) is str:
            self.key = key
        else:
            raise TypeError("Requires str value")

    def get_valueOf_(self):
        return self.valueOf_

    def set_valueOf_(self, valueOf_):
        if type(valueOf_) is str:
            self.valueOf_ = valueOf_
        else:
            raise TypeError("Requires str value")

    def _hasContent(self):
        if (
                (1 if type(self.valueOf_) in [int, float] else self.valueOf_)
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='property', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('property')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'property':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='property')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='property',
                                 pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='property'):
        if self.key is not None and 'key' not in already_processed:
            already_processed.add('key')
            outfile.write(
                ' key=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.key), input_name='key')),))

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='property',
                        fromsubclass_=False, pretty_print=True):
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('key', node)
        if value is not None and 'key' not in already_processed:
            already_processed.add('key')
            self.key = value

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass


# end class property


class properties(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'property': MemberSpec_('property', 'property', 1, 1,
                                {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'property', 'type': 'property'},
                                None),
        'option_icons': MemberSpec_('option_icons', 'icons', 0, 1,
                                    {'minOccurs': '0', 'name': 'option_icons', 'type': 'icons'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, property=None, option_icons=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if property is None:
            self.property = []
        else:
            self.property = property
        self.property_nsprefix_ = None
        self.option_icons = option_icons
        self.option_icons_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, properties)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if properties.subclass:
            return properties.subclass(*args_, **kwargs_)
        else:
            return properties(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_property(self):
        return self.property

    def set_property(self, property_):
        if all(isinstance(x, property) for x in property_):
            self.property = property_
        else:
            raise TypeError("Requires only property values inside an array")

    def add_property(self, value):
        if type(value) is property:
            self.property.append(value)
        else:
            raise TypeError("Requires property value")

    def insert_property_at(self, index, value):
        if 0 <= index <= len(self.property):
            if type(value) is property:
                self.property.insert(index, value)
            else:
                raise TypeError("Requires property value")
        else:
            raise IndexError("Invalid index value")

    def replace_property_at(self, index, value):
        if 0 <= index < len(self.property):
            if self.property[index]:
                if type(value) is property:
                    self.property[index] = value
                else:
                    raise TypeError("Requires property value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_option_icons(self):
        return self.option_icons

    def set_option_icons(self, option_icons):
        if type(option_icons) is icons:
            self.option_icons = option_icons
        else:
            raise TypeError("Requires icons value")

    def _hasContent(self):
        if (
                self.property or
                self.option_icons is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='properties', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('properties')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'properties':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='properties')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='properties',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='properties'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='properties',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for property_ in self.property:
            namespaceprefix_ = self.property_nsprefix_ + ':' if (UseCapturedNS_ and self.property_nsprefix_) else ''
            property_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='property',
                             pretty_print=pretty_print)
        if self.option_icons is not None:
            namespaceprefix_ = self.option_icons_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.option_icons_nsprefix_) else ''
            self.option_icons.export(outfile, level, namespaceprefix_, namespacedef_='', name_='option_icons',
                                     pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'property':
            obj_ = property.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.property.append(obj_)
            obj_.original_tagname_ = 'property'
        elif nodeName_ == 'option_icons':
            obj_ = icons.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.option_icons = obj_
            obj_.original_tagname_ = 'option_icons'


# end class properties


class icons(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'icon': MemberSpec_('icon', 'icon', 1, 1,
                            {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'icon', 'type': 'icon'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, icon=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if icon is None:
            self.icon = []
        else:
            self.icon = icon
        self.icon_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, icons)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if icons.subclass:
            return icons.subclass(*args_, **kwargs_)
        else:
            return icons(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_icon(self):
        return self.icon

    def set_icon(self, icon_):
        if all(isinstance(x, icon) for x in icon_):
            self.icon = icon_
        else:
            raise TypeError("Requires only icon values inside an array")

    def add_icon(self, value):
        if type(value) is icon:
            self.icon.append(value)
        else:
            raise TypeError("Requires icon value")

    def insert_icon_at(self, index, value):
        if 0 <= index <= len(self.icon):
            if type(value) is icon:
                self.icon.insert(index, value)
            else:
                raise TypeError("Requires icon value")
        else:
            raise IndexError("Invalid index value")

    def replace_icon_at(self, index, value):
        if 0 <= index < len(self.icon):
            if self.icon[index]:
                if type(value) is icon:
                    self.icon[index] = value
                else:
                    raise TypeError("Requires icon value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def _hasContent(self):
        if (
                self.icon
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='icons', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('icons')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'icons':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='icons')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='icons',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='icons'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='icons', fromsubclass_=False,
                        pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for icon_ in self.icon:
            namespaceprefix_ = self.icon_nsprefix_ + ':' if (UseCapturedNS_ and self.icon_nsprefix_) else ''
            icon_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='icon', pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'icon':
            obj_ = icon.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.icon.append(obj_)
            obj_.original_tagname_ = 'icon'


# end class icons


class icon(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'key': MemberSpec_('key', 'xs:string', 0, 1, {'use': 'optional', 'name': 'key'}),
        'type_': MemberSpec_('type_', 'iconType', 0, 1, {'use': 'optional', 'name': 'type_'}),
        'valueOf_': MemberSpec_('valueOf_', 'xs:string', 0),
    }
    subclass = None
    superclass = None

    def __init__(self, key=None, type_=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.key = _cast(None, key)
        self.key_nsprefix_ = None
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
        self.valueOf_ = valueOf_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, icon)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if icon.subclass:
            return icon.subclass(*args_, **kwargs_)
        else:
            return icon(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_key(self):
        return self.key

    def set_key(self, key):
        if type(key) is str:
            self.key = key
        else:
            raise TypeError("Requires str value")

    def get_type(self):
        return self.type_

    def set_type_(self, type_):
        if type(type_) is iconType:
            self.type_ = type_
        else:
            raise TypeError("Requires iconType value")

    def get_valueOf_(self):
        return self.valueOf_

    def set_valueOf_(self, valueOf_):
        if type(valueOf_) is str:
            self.valueOf_ = valueOf_
        else:
            raise TypeError("Requires str value")

    def validate_iconType(self, value):
        # Validate type iconType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['material', 'svg']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on iconType' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False

    def _hasContent(self):
        if (
                (1 if type(self.valueOf_) in [int, float] else self.valueOf_)
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='icon', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('icon')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'icon':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='icon')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='icon',
                                 pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='icon'):
        if self.key is not None and 'key' not in already_processed:
            already_processed.add('key')
            outfile.write(
                ' key=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.key), input_name='key')),))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(
                ' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')),))

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='icon', fromsubclass_=False,
                        pretty_print=True):
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('key', node)
        if value is not None and 'key' not in already_processed:
            already_processed.add('key')
            self.key = value
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.validate_iconType(self.type_)  # validate type iconType

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass


# end class icon


class allowedNets(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'allowedNet': MemberSpec_('allowedNet', 'xs:string', 1, 1,
                                  {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'allowedNet',
                                   'type': 'xs:string'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, allowedNet=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if allowedNet is None:
            self.allowedNet = []
        else:
            self.allowedNet = allowedNet
        self.allowedNet_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, allowedNets)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if allowedNets.subclass:
            return allowedNets.subclass(*args_, **kwargs_)
        else:
            return allowedNets(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_allowedNet(self):
        return self.allowedNet

    def set_allowedNet(self, allowedNet):
        if all(isinstance(x, str) for x in allowedNet):
            self.allowedNet = allowedNet
        else:
            raise TypeError("Requires only str values inside an array")

    def add_allowedNet(self, value):
        if type(value) is str:
            self.allowedNet.append(value)
        else:
            raise TypeError("Requires str value")

    def insert_allowedNet_at(self, index, value):
        if 0 <= index <= len(self.allowedNet):
            if type(value) is str:
                self.allowedNet.insert(index, value)
            else:
                raise TypeError("Requires str value")
        else:
            raise IndexError("Invalid index value")

    def replace_allowedNet_at(self, index, value):
        if 0 <= index < len(self.allowedNet):
            if self.allowedNet[index]:
                if type(value) is str:
                    self.allowedNet[index] = value
                else:
                    raise TypeError("Requires str value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def _hasContent(self):
        if (
                self.allowedNet
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='allowedNets', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('allowedNets')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'allowedNets':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='allowedNets')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='allowedNets',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='allowedNets'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='allowedNets',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for allowedNet_ in self.allowedNet:
            namespaceprefix_ = self.allowedNet_nsprefix_ + ':' if (UseCapturedNS_ and self.allowedNet_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sallowedNet>%s</%sallowedNet>%s' % (
                namespaceprefix_,
                self.gds_encode(self.gds_format_string(quote_xml(allowedNet_), input_name='allowedNet')),
                namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'allowedNet':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'allowedNet')
            value_ = self.gds_validate_string(value_, node, 'allowedNet')
            self.allowedNet.append(value_)
            self.allowedNet_nsprefix_ = child_.prefix


# end class allowedNets


class logic(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'perform': MemberSpec_('perform', 'xs:boolean', 0, 1,
                               {'minOccurs': '0', 'name': 'perform', 'type': 'xs:boolean'}, None),
        'delegate': MemberSpec_('delegate', 'xs:boolean', 0, 1,
                                {'minOccurs': '0', 'name': 'delegate', 'type': 'xs:boolean'}, None),
        'view': MemberSpec_('view', 'xs:boolean', 0, 1, {'minOccurs': '0', 'name': 'view', 'type': 'xs:boolean'}, None),
        'cancel': MemberSpec_('cancel', 'xs:boolean', 0, 1, {'minOccurs': '0', 'name': 'cancel', 'type': 'xs:boolean'},
                              None),
        'finish': MemberSpec_('finish', 'xs:boolean', 0, 1, {'minOccurs': '0', 'name': 'finish', 'type': 'xs:boolean'},
                              None),
        'assigned': MemberSpec_('assigned', 'xs:boolean', 0, 1, {'name': 'assigned', 'type': 'xs:boolean'}, 12),
        'assign': MemberSpec_('assign', 'xs:boolean', 0, 1, {'name': 'assign', 'type': 'xs:boolean'}, 12),
        'behavior': MemberSpec_('behavior', ['behavior', 'xs:string'], 1, 1,
                                {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'behavior', 'type': 'xs:string'},
                                None),
        'action': MemberSpec_('action', 'action', 1, 1,
                              {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'action', 'type': 'action'}, None),
        'actionRef': MemberSpec_('actionRef', 'actionRef', 1, 1,
                                 {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'actionRef', 'type': 'actionRef'},
                                 None),
    }
    subclass = None
    superclass = None

    def __init__(self, perform=None, delegate=None, view=None, cancel=None, finish=None, assigned=None, assign=None,
                 behavior=None, action=None, actionRef=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.perform = perform
        self.perform_nsprefix_ = None
        self.delegate = delegate
        self.delegate_nsprefix_ = None
        self.view = view
        self.view_nsprefix_ = None
        self.cancel = cancel
        self.cancel_nsprefix_ = None
        self.finish = finish
        self.finish_nsprefix_ = None
        self.assigned = assigned
        self.assigned_nsprefix_ = None
        self.assign = assign
        self.assign_nsprefix_ = None
        if behavior is None:
            self.behavior = []
        else:
            self.behavior = behavior
        self.behavior_nsprefix_ = None
        if action is None:
            self.action = []
        else:
            self.action = action
        self.action_nsprefix_ = None
        if actionRef is None:
            self.actionRef = []
        else:
            self.actionRef = actionRef
        self.actionRef_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, logic)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if logic.subclass:
            return logic.subclass(*args_, **kwargs_)
        else:
            return logic(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_perform(self):
        return self.perform

    def set_perform(self, perform):
        self.perform = set_boolean_value(perform)

    def get_delegate(self):
        return self.delegate

    def set_delegate(self, delegate):
        self.delegate = set_boolean_value(delegate)

    def get_view(self):
        return self.view

    def set_view(self, view):
        self.view = set_boolean_value(view)

    def get_cancel(self):
        return self.cancel

    def set_cancel(self, cancel):
        self.cancel = set_boolean_value(cancel)

    def get_finish(self):
        return self.finish

    def set_finish(self, finish):
        self.finish = set_boolean_value(finish)

    def get_assigned(self):
        return self.assigned

    def set_assigned(self, assigned):
        if self.assign is None:
            self.assigned = set_boolean_value(assigned)
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'assign' element.")

    def get_assign(self):
        return self.assign

    def set_assign(self, assign):
        if self.assigned is None:
            self.assign = set_boolean_value(assign)
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'assigned' element.")

    def get_behavior(self):
        return self.behavior

    def set_behavior(self, behavior_):
        if all(isinstance(x, behavior) for x in behavior_):
            self.behavior = behavior_
        else:
            raise TypeError("Requires only behavior values inside an array")

    def add_behavior(self, value):
        if type(value) is behavior:
            self.behavior.append(value)
        else:
            raise TypeError("Requires behavior value")

    def insert_behavior_at(self, index, value):
        if 0 <= index <= len(self.behavior):
            if type(value) is behavior:
                self.behavior.insert(index, value)
            else:
                raise TypeError("Requires behavior value")
        else:
            raise IndexError("Invalid index value")

    def replace_behavior_at(self, index, value):
        if 0 <= index < len(self.behavior):
            if self.behavior[index]:
                if type(value) is behavior:
                    self.behavior[index] = value
                else:
                    raise TypeError("Requires behavior value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_action(self):
        return self.action

    def set_action(self, action_):
        if all(isinstance(x, action) for x in action_):
            self.action = action_
        else:
            raise TypeError("Requires only action values inside an array")

    def add_action(self, value):
        if type(value) is action:
            self.action.append(value)
        else:
            raise TypeError("Requires action value")

    def insert_action_at(self, index, value):
        if 0 <= index <= len(self.action):
            if type(value) is action:
                self.action.insert(index, value)
            else:
                raise TypeError("Requires action value")
        else:
            raise IndexError("Invalid index value")

    def replace_action_at(self, index, value):
        if 0 <= index < len(self.action):
            if self.action[index]:
                if type(value) is action:
                    self.action[index] = value
                else:
                    raise TypeError("Requires action value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_actionRef(self):
        return self.actionRef

    def set_actionRef(self, actionRef_):
        if all(isinstance(x, actionRef) for x in actionRef_):
            self.actionRef = actionRef_
        else:
            raise TypeError("Requires only actionRef values inside an array")

    def add_actionRef(self, value):
        if type(value) is actionRef:
            self.actionRef.append(value)
        else:
            raise TypeError("Requires actionRef value")

    def insert_actionRef_at(self, index, value):
        if 0 <= index <= len(self.actionRef):
            if type(value) is actionRef:
                self.actionRef.insert(index, value)
            else:
                raise TypeError("Requires actionRef value")
        else:
            raise IndexError("Invalid index value")

    def replace_actionRef_at(self, index, value):
        if 0 <= index < len(self.actionRef):
            if self.actionRef[index]:
                if type(value) is actionRef:
                    self.actionRef[index] = value
                else:
                    raise TypeError("Requires actionRef value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def validate_behavior(self, value):
        result = True
        # Validate type behavior, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['forbidden', 'hidden', 'visible', 'editable', 'required', 'immediate', 'optional']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on behavior' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
        return result

    def _hasContent(self):
        if (
                self.perform is not None or
                self.delegate is not None or
                self.view is not None or
                self.cancel is not None or
                self.finish is not None or
                self.assigned is not None or
                self.assign is not None or
                self.behavior or
                self.action or
                self.actionRef
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='logic', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('logic')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'logic':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='logic')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='logic',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='logic'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='logic', fromsubclass_=False,
                        pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.perform is not None:
            namespaceprefix_ = self.perform_nsprefix_ + ':' if (UseCapturedNS_ and self.perform_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sperform>%s</%sperform>%s' % (
                namespaceprefix_, self.gds_format_boolean(self.perform, input_name='perform'), namespaceprefix_, eol_))
        if self.delegate is not None:
            namespaceprefix_ = self.delegate_nsprefix_ + ':' if (UseCapturedNS_ and self.delegate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdelegate>%s</%sdelegate>%s' % (
                namespaceprefix_, self.gds_format_boolean(self.delegate, input_name='delegate'), namespaceprefix_,
                eol_))
        if self.view is not None:
            namespaceprefix_ = self.view_nsprefix_ + ':' if (UseCapturedNS_ and self.view_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sview>%s</%sview>%s' % (
                namespaceprefix_, self.gds_format_boolean(self.view, input_name='view'), namespaceprefix_, eol_))
        if self.cancel is not None:
            namespaceprefix_ = self.cancel_nsprefix_ + ':' if (UseCapturedNS_ and self.cancel_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scancel>%s</%scancel>%s' % (
                namespaceprefix_, self.gds_format_boolean(self.cancel, input_name='cancel'), namespaceprefix_, eol_))
        if self.finish is not None:
            namespaceprefix_ = self.finish_nsprefix_ + ':' if (UseCapturedNS_ and self.finish_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfinish>%s</%sfinish>%s' % (
                namespaceprefix_, self.gds_format_boolean(self.finish, input_name='finish'), namespaceprefix_, eol_))
        if self.assigned is not None:
            namespaceprefix_ = self.assigned_nsprefix_ + ':' if (UseCapturedNS_ and self.assigned_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sassigned>%s</%sassigned>%s' % (
                namespaceprefix_, self.gds_format_boolean(self.assigned, input_name='assigned'), namespaceprefix_,
                eol_))
        if self.assign is not None:
            namespaceprefix_ = self.assign_nsprefix_ + ':' if (UseCapturedNS_ and self.assign_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sassign>%s</%sassign>%s' % (
                namespaceprefix_, self.gds_format_boolean(self.assign, input_name='assign'), namespaceprefix_, eol_))
        for behavior_ in self.behavior:
            namespaceprefix_ = self.behavior_nsprefix_ + ':' if (UseCapturedNS_ and self.behavior_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbehavior>%s</%sbehavior>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(behavior_), input_name='behavior')),
                namespaceprefix_, eol_))
        for action_ in self.action:
            namespaceprefix_ = self.action_nsprefix_ + ':' if (UseCapturedNS_ and self.action_nsprefix_) else ''
            action_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='action',
                           pretty_print=pretty_print)
        for actionRef_ in self.actionRef:
            namespaceprefix_ = self.actionRef_nsprefix_ + ':' if (UseCapturedNS_ and self.actionRef_nsprefix_) else ''
            actionRef_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='actionRef',
                              pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'perform':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'perform')
            ival_ = self.gds_validate_boolean(ival_, node, 'perform')
            self.perform = ival_
            self.perform_nsprefix_ = child_.prefix
        elif nodeName_ == 'delegate':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'delegate')
            ival_ = self.gds_validate_boolean(ival_, node, 'delegate')
            self.delegate = ival_
            self.delegate_nsprefix_ = child_.prefix
        elif nodeName_ == 'view':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'view')
            ival_ = self.gds_validate_boolean(ival_, node, 'view')
            self.view = ival_
            self.view_nsprefix_ = child_.prefix
        elif nodeName_ == 'cancel':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'cancel')
            ival_ = self.gds_validate_boolean(ival_, node, 'cancel')
            self.cancel = ival_
            self.cancel_nsprefix_ = child_.prefix
        elif nodeName_ == 'finish':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'finish')
            ival_ = self.gds_validate_boolean(ival_, node, 'finish')
            self.finish = ival_
            self.finish_nsprefix_ = child_.prefix
        elif nodeName_ == 'assigned':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'assigned')
            ival_ = self.gds_validate_boolean(ival_, node, 'assigned')
            self.assigned = ival_
            self.assigned_nsprefix_ = child_.prefix
        elif nodeName_ == 'assign':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'assign')
            ival_ = self.gds_validate_boolean(ival_, node, 'assign')
            self.assign = ival_
            self.assign_nsprefix_ = child_.prefix
        elif nodeName_ == 'behavior':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'behavior')
            value_ = self.gds_validate_string(value_, node, 'behavior')
            self.behavior.append(value_)
            self.behavior_nsprefix_ = child_.prefix
            # validate type behavior
            self.validate_behavior(self.behavior[-1])
        elif nodeName_ == 'action':
            obj_ = action.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.action.append(obj_)
            obj_.original_tagname_ = 'action'
        elif nodeName_ == 'actionRef':
            obj_ = actionRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.actionRef.append(obj_)
            obj_.original_tagname_ = 'actionRef'


# end class logic


class caseLogic(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'create': MemberSpec_('create', 'xs:boolean', 0, 1, {'minOccurs': '0', 'name': 'create', 'type': 'xs:boolean'},
                              None),
        'delete': MemberSpec_('delete', 'xs:boolean', 0, 1, {'minOccurs': '0', 'name': 'delete', 'type': 'xs:boolean'},
                              None),
        'view': MemberSpec_('view', 'xs:boolean', 0, 1, {'minOccurs': '0', 'name': 'view', 'type': 'xs:boolean'}, None),
        'action': MemberSpec_('action', 'action', 1, 1,
                              {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'action', 'type': 'action'}, None),
        'actionRef': MemberSpec_('actionRef', 'actionRef', 1, 1,
                                 {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'actionRef', 'type': 'actionRef'},
                                 None),
    }
    subclass = None
    superclass = None

    def __init__(self, create=None, delete=None, view=None, action=None, actionRef=None, gds_collector_=None,
                 **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.create = create
        self.create_nsprefix_ = None
        self.delete = delete
        self.delete_nsprefix_ = None
        self.view = view
        self.view_nsprefix_ = None
        if action is None:
            self.action = []
        else:
            self.action = action
        self.action_nsprefix_ = None
        if actionRef is None:
            self.actionRef = []
        else:
            self.actionRef = actionRef
        self.actionRef_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, caseLogic)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if caseLogic.subclass:
            return caseLogic.subclass(*args_, **kwargs_)
        else:
            return caseLogic(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_create(self):
        return self.create

    def set_create(self, create):
        self.create = set_boolean_value(create)

    def get_delete(self):
        return self.delete

    def set_delete(self, delete):
        self.delete = set_boolean_value(delete)

    def get_view(self):
        return self.view

    def set_view(self, view):
        self.view = set_boolean_value(view)

    def get_action(self):
        return self.action

    def set_action(self, action_):
        if all(isinstance(x, action) for x in action_):
            self.action = action_
        else:
            raise TypeError("Requires only action values inside an array")

    def add_action(self, value):
        if type(value) is action:
            self.action.append(value)
        else:
            raise TypeError("Requires action value")

    def insert_action_at(self, index, value):
        if 0 <= index <= len(self.action):
            if type(value) is action:
                self.action.insert(index, value)
            else:
                raise TypeError("Requires action value")
        else:
            raise IndexError("Invalid index value")

    def replace_action_at(self, index, value):
        if 0 <= index < len(self.action):
            if self.action[index]:
                if type(value) is action:
                    self.action[index] = value
                else:
                    raise TypeError("Requires action value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_actionRef(self):
        return self.actionRef

    def set_actionRef(self, actionRef_):
        if all(isinstance(x, actionRef) for x in actionRef_):
            self.actionRef = actionRef_
        else:
            raise TypeError("Requires only actionRef values inside an array")

    def add_actionRef(self, value):
        if type(value) is actionRef:
            self.actionRef.append(value)
        else:
            raise TypeError("Requires actionRef value")

    def insert_actionRef_at(self, index, value):
        if 0 <= index <= len(self.actionRef):
            if type(value) is actionRef:
                self.actionRef.insert(index, value)
            else:
                raise TypeError("Requires actionRef value")
        else:
            raise IndexError("Invalid index value")

    def replace_actionRef_at(self, index, value):
        if 0 <= index < len(self.actionRef):
            if self.actionRef[index]:
                if type(value) is actionRef:
                    self.actionRef[index] = value
                else:
                    raise TypeError("Requires actionRef value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def _hasContent(self):
        if (
                self.create is not None or
                self.delete is not None or
                self.view is not None or
                self.action or
                self.actionRef
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='caseLogic', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('caseLogic')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'caseLogic':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='caseLogic')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='caseLogic',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='caseLogic'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='caseLogic',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.create is not None:
            namespaceprefix_ = self.create_nsprefix_ + ':' if (UseCapturedNS_ and self.create_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%screate>%s</%screate>%s' % (
                namespaceprefix_, self.gds_format_boolean(self.create, input_name='create'), namespaceprefix_, eol_))
        if self.delete is not None:
            namespaceprefix_ = self.delete_nsprefix_ + ':' if (UseCapturedNS_ and self.delete_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdelete>%s</%sdelete>%s' % (
                namespaceprefix_, self.gds_format_boolean(self.delete, input_name='delete'), namespaceprefix_, eol_))
        if self.view is not None:
            namespaceprefix_ = self.view_nsprefix_ + ':' if (UseCapturedNS_ and self.view_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sview>%s</%sview>%s' % (
                namespaceprefix_, self.gds_format_boolean(self.view, input_name='view'), namespaceprefix_, eol_))
        for action_ in self.action:
            namespaceprefix_ = self.action_nsprefix_ + ':' if (UseCapturedNS_ and self.action_nsprefix_) else ''
            action_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='action',
                           pretty_print=pretty_print)
        for actionRef_ in self.actionRef:
            namespaceprefix_ = self.actionRef_nsprefix_ + ':' if (UseCapturedNS_ and self.actionRef_nsprefix_) else ''
            actionRef_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='actionRef',
                              pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'create':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'create')
            ival_ = self.gds_validate_boolean(ival_, node, 'create')
            self.create = ival_
            self.create_nsprefix_ = child_.prefix
        elif nodeName_ == 'delete':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'delete')
            ival_ = self.gds_validate_boolean(ival_, node, 'delete')
            self.delete = ival_
            self.delete_nsprefix_ = child_.prefix
        elif nodeName_ == 'view':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'view')
            ival_ = self.gds_validate_boolean(ival_, node, 'view')
            self.view = ival_
            self.view_nsprefix_ = child_.prefix
        elif nodeName_ == 'action':
            obj_ = action.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.action.append(obj_)
            obj_.original_tagname_ = 'action'
        elif nodeName_ == 'actionRef':
            obj_ = actionRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.actionRef.append(obj_)
            obj_.original_tagname_ = 'actionRef'


# end class caseLogic


class transactionRef(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'id': MemberSpec_('id', 'xs:string', 0, 0, {'name': 'id', 'type': 'xs:string'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, id=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = id
        self.id_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, transactionRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if transactionRef.subclass:
            return transactionRef.subclass(*args_, **kwargs_)
        else:
            return transactionRef(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_id(self):
        return self.id

    def set_id(self, id_):
        if type(id_) is str:
            self.id = id_
        else:
            raise TypeError("Requires str value")

    def _hasContent(self):
        if (
                self.id is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='transactionRef', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('transactionRef')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'transactionRef':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='transactionRef')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='transactionRef',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='transactionRef'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='transactionRef',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.id is not None:
            namespaceprefix_ = self.id_nsprefix_ + ':' if (UseCapturedNS_ and self.id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sid>%s</%sid>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.id), input_name='id')),
                namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'id')
            value_ = self.gds_validate_string(value_, node, 'id')
            self.id = value_
            self.id_nsprefix_ = child_.prefix


# end class transactionRef


class permissionRef(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'id': MemberSpec_('id', 'xs:string', 0, 0, {'name': 'id', 'type': 'xs:string'}, None),
        'logic': MemberSpec_('logic', 'logic', 0, 0, {'name': 'logic', 'type': 'logic'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, id=None, logic=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = id
        self.id_nsprefix_ = None
        self.logic = logic
        self.logic_nsprefix_ = None
        self.extensiontype_ = extensiontype_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, permissionRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if permissionRef.subclass:
            return permissionRef.subclass(*args_, **kwargs_)
        else:
            return permissionRef(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_id(self):
        return self.id

    def set_id(self, id_):
        if type(id_) is str:
            self.id = id_
        else:
            raise TypeError("Requires str value")

    def get_logic(self):
        return self.logic

    def set_logic(self, logic_):
        if type(logic_) is logic:
            self.logic = logic_
        else:
            raise TypeError("Requires logic value")

    def get_extensiontype_(self):
        return self.extensiontype_

    def set_extensiontype_(self, extensiontype_):
        self.extensiontype_ = extensiontype_

    def _hasContent(self):
        if (
                self.id is not None or
                self.logic is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='permissionRef', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('permissionRef')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'permissionRef':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='permissionRef')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='permissionRef',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='permissionRef'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='permissionRef',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.id is not None:
            namespaceprefix_ = self.id_nsprefix_ + ':' if (UseCapturedNS_ and self.id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sid>%s</%sid>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.id), input_name='id')),
                namespaceprefix_, eol_))
        if self.logic is not None:
            namespaceprefix_ = self.logic_nsprefix_ + ':' if (UseCapturedNS_ and self.logic_nsprefix_) else ''
            self.logic.export(outfile, level, namespaceprefix_, namespacedef_='', name_='logic',
                              pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'id')
            value_ = self.gds_validate_string(value_, node, 'id')
            self.id = value_
            self.id_nsprefix_ = child_.prefix
        elif nodeName_ == 'logic':
            obj_ = logic.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.logic = obj_
            obj_.original_tagname_ = 'logic'


# end class permissionRef


class casePermissionRef(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'id': MemberSpec_('id', 'xs:string', 0, 0, {'name': 'id', 'type': 'xs:string'}, None),
        'caseLogic': MemberSpec_('caseLogic', 'caseLogic', 0, 0, {'name': 'caseLogic', 'type': 'caseLogic'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, id=None, caseLogic=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = id
        self.id_nsprefix_ = None
        self.caseLogic = caseLogic
        self.caseLogic_nsprefix_ = None
        self.extensiontype_ = extensiontype_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, casePermissionRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if casePermissionRef.subclass:
            return casePermissionRef.subclass(*args_, **kwargs_)
        else:
            return casePermissionRef(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_id(self):
        return self.id

    def set_id(self, id_):
        if type(id_) is str:
            self.id = id_
        else:
            raise TypeError("Requires str value")

    def get_caseLogic(self):
        return self.caseLogic

    def set_caseLogic(self, caseLogic_):
        if type(caseLogic_) is caseLogic:
            self.caseLogic = caseLogic_
        else:
            raise TypeError("Requires caseLogic value")

    def get_extensiontype_(self):
        return self.extensiontype_

    def set_extensiontype_(self, extensiontype_):
        self.extensiontype_ = extensiontype_

    def _hasContent(self):
        if (
                self.id is not None or
                self.caseLogic is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='casePermissionRef',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('casePermissionRef')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'casePermissionRef':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='casePermissionRef')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='casePermissionRef',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='casePermissionRef'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='casePermissionRef',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.id is not None:
            namespaceprefix_ = self.id_nsprefix_ + ':' if (UseCapturedNS_ and self.id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sid>%s</%sid>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.id), input_name='id')),
                namespaceprefix_, eol_))
        if self.caseLogic is not None:
            namespaceprefix_ = self.caseLogic_nsprefix_ + ':' if (UseCapturedNS_ and self.caseLogic_nsprefix_) else ''
            self.caseLogic.export(outfile, level, namespaceprefix_, namespacedef_='', name_='caseLogic',
                                  pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'id')
            value_ = self.gds_validate_string(value_, node, 'id')
            self.id = value_
            self.id_nsprefix_ = child_.prefix
        elif nodeName_ == 'caseLogic':
            obj_ = caseLogic.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.caseLogic = obj_
            obj_.original_tagname_ = 'caseLogic'


# end class casePermissionRef


class dataRef(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'id': MemberSpec_('id', 'xs:string', 0, 0, {'name': 'id', 'type': 'xs:string'}, None),
        'logic': MemberSpec_('logic', 'logic', 0, 0, {'name': 'logic', 'type': 'logic'}, None),
        'layout': MemberSpec_('layout', 'layout', 0, 1, {'minOccurs': '0', 'name': 'layout', 'type': 'layout'}, None),
        'component': MemberSpec_('component', 'component', 0, 1,
                                 {'minOccurs': '0', 'name': 'component', 'type': 'component'}, None),
        'event': MemberSpec_('event', 'event', 1, 1,
                             {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'event', 'type': 'dataEvent'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, id=None, logic=None, layout=None, component=None, event=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = id
        self.id_nsprefix_ = None
        self.logic = logic
        self.logic_nsprefix_ = None
        self.layout = layout
        self.layout_nsprefix_ = None
        self.component = component
        self.component_nsprefix_ = None
        if event is None:
            self.event = []
        else:
            self.event = event
        self.event_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataRef.subclass:
            return dataRef.subclass(*args_, **kwargs_)
        else:
            return dataRef(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_id(self):
        return self.id

    def set_id(self, id_):
        if type(id_) is str:
            self.id = id_
        else:
            raise TypeError("Requires str value")

    def get_logic(self):
        return self.logic

    def set_logic(self, logic_):
        if type(logic_) is logic:
            self.logic = logic_
        else:
            raise TypeError("Requires logic value")

    def get_layout(self):
        return self.layout

    def set_layout(self, layout_):
        if type(layout_) is layout:
            self.layout = layout_
        else:
            raise TypeError("Requires layout value")

    def get_component(self):
        return self.component

    def set_component(self, component_):
        if type(component_) is component:
            self.component = component_
        else:
            raise TypeError("Requires component value")

    def get_event(self):
        return self.event

    # if you want your own specific event list , else it is an empty list
    def set_event(self, event_):
        if all(isinstance(x, dataEvent) for x in event_):
            self.event = event_
        else:
            raise TypeError("Requires only dataEvent values inside an array")

    def add_event(self, value):
        if type(value) is dataEvent:
            self.event.append(value)
        else:
            raise TypeError("Requires dataEvent value")

    def insert_event_at(self, index, value):
        if 0 <= index <= len(self.event):
            if type(value) is dataEvent:
                self.event.insert(index, value)
            else:
                raise TypeError("Requires dataEvent value")
        else:
            raise IndexError("Invalid index value")

    def replace_event_at(self, index, value):
        if 0 <= index < len(self.event):
            if self.event[index]:
                if type(value) is dataEvent:
                    self.event[index] = value
                else:
                    raise TypeError("Requires dataEvent value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def _hasContent(self):
        if (
                self.id is not None or
                self.logic is not None or
                self.layout is not None or
                self.component is not None or
                self.event
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='dataRef', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataRef')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataRef':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataRef')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataRef',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataRef'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='dataRef',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.id is not None:
            namespaceprefix_ = self.id_nsprefix_ + ':' if (UseCapturedNS_ and self.id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sid>%s</%sid>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.id), input_name='id')),
                namespaceprefix_, eol_))
        if self.logic is not None:
            namespaceprefix_ = self.logic_nsprefix_ + ':' if (UseCapturedNS_ and self.logic_nsprefix_) else ''
            self.logic.export(outfile, level, namespaceprefix_, namespacedef_='', name_='logic',
                              pretty_print=pretty_print)
        if self.layout is not None:
            namespaceprefix_ = self.layout_nsprefix_ + ':' if (UseCapturedNS_ and self.layout_nsprefix_) else ''
            self.layout.export(outfile, level, namespaceprefix_, namespacedef_='', name_='layout',
                               pretty_print=pretty_print)
        if self.component is not None:
            namespaceprefix_ = self.component_nsprefix_ + ':' if (UseCapturedNS_ and self.component_nsprefix_) else ''
            self.component.export(outfile, level, namespaceprefix_, namespacedef_='', name_='component',
                                  pretty_print=pretty_print)
        for event_ in self.event:
            namespaceprefix_ = self.event_nsprefix_ + ':' if (UseCapturedNS_ and self.event_nsprefix_) else ''
            event_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='event', pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'id')
            value_ = self.gds_validate_string(value_, node, 'id')
            self.id = value_
            self.id_nsprefix_ = child_.prefix
        elif nodeName_ == 'logic':
            obj_ = logic.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.logic = obj_
            obj_.original_tagname_ = 'logic'
        elif nodeName_ == 'layout':
            obj_ = layout.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.layout = obj_
            obj_.original_tagname_ = 'layout'
        elif nodeName_ == 'component':
            obj_ = component.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.component = obj_
            obj_.original_tagname_ = 'component'
        elif nodeName_ == 'event':
            obj_ = dataEvent.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.event.append(obj_)
            obj_.original_tagname_ = 'event'


# end class dataRef


class layout(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'x': MemberSpec_('x', ['nonNegativeInteger', 'xs:int'], 0, 1, {'minOccurs': '0', 'name': 'x', 'type': 'xs:int'},
                         None),
        'y': MemberSpec_('y', ['nonNegativeInteger', 'xs:int'], 0, 1, {'minOccurs': '0', 'name': 'y', 'type': 'xs:int'},
                         None),
        'rows': MemberSpec_('rows', ['nonNegativeInteger', 'xs:int'], 0, 1,
                            {'minOccurs': '0', 'name': 'rows', 'type': 'xs:int'}, None),
        'cols': MemberSpec_('cols', ['nonNegativeInteger', 'xs:int'], 0, 1,
                            {'minOccurs': '0', 'name': 'cols', 'type': 'xs:int'}, None),
        'offset': MemberSpec_('offset', ['nonNegativeInteger', 'xs:int'], 0, 1,
                              {'minOccurs': '0', 'name': 'offset', 'type': 'xs:int'}, None),
        'template': MemberSpec_('template', ['template', 'xs:string'], 0, 1,
                                {'minOccurs': '0', 'name': 'template', 'type': 'xs:string'}, None),
        'appearance': MemberSpec_('appearance', ['appearance', 'xs:string'], 0, 1,
                                  {'minOccurs': '0', 'name': 'appearance', 'type': 'xs:string'}, None),
        'alignment': MemberSpec_('alignment', ['fieldAlignment', 'xs:string'], 0, 1,
                                 {'minOccurs': '0', 'name': 'alignment', 'type': 'xs:string'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, x=None, y=None, rows=None, cols=None, offset=None, template=None, appearance=None,
                 alignment=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.x = x
        self.validate_nonNegativeInteger(self.x)
        self.x_nsprefix_ = None
        self.y = y
        self.validate_nonNegativeInteger(self.y)
        self.y_nsprefix_ = None
        self.rows = rows
        self.validate_nonNegativeInteger(self.rows)
        self.rows_nsprefix_ = None
        self.cols = cols
        self.validate_nonNegativeInteger(self.cols)
        self.cols_nsprefix_ = None
        self.offset = offset
        self.validate_nonNegativeInteger(self.offset)
        self.offset_nsprefix_ = None
        self.template = template
        self.validate_template(self.template)
        self.template_nsprefix_ = None
        self.appearance = appearance
        self.validate_appearance(self.appearance)
        self.appearance_nsprefix_ = None
        self.alignment = alignment
        self.validate_fieldAlignment(self.alignment)
        self.alignment_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, layout)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if layout.subclass:
            return layout.subclass(*args_, **kwargs_)
        else:
            return layout(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_x(self):
        return self.x

    def set_x(self, x):
        if type(x) is int:
            if x < 0:
                raise ValueError("The 'x' element has to be nonNegativeInteger")
            else:
                self.x = x
        else:
            raise TypeError("Requires int value")

    def get_y(self):
        return self.y

    def set_y(self, y):
        if type(y) is int:
            if y < 0:
                raise ValueError("The 'y' element has to be nonNegativeInteger")
            else:
                self.y = y
        else:
            raise TypeError("Requires int value")

    def get_rows(self):
        return self.rows

    def set_rows(self, rows):
        if type(rows) is int:
            if rows < 0:
                raise ValueError("The 'rows' element has to be nonNegativeInteger")
            else:
                self.rows = rows
        else:
            raise TypeError("Requires int value")

    def get_cols(self):
        return self.cols

    def set_cols(self, cols):
        if type(cols) is int:
            if cols < 0:
                raise ValueError("The 'cols' element has to be nonNegativeInteger")
            else:
                self.cols = cols
        else:
            raise TypeError("Requires int value")

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        if type(offset) is int:
            if offset < 0:
                raise ValueError("The 'offset' element has to be nonNegativeInteger")
            else:
                self.offset = offset
        else:
            raise TypeError("Requires int value")

    def get_template(self):
        return self.template

    def set_template(self, template_):
        if type(template_) is template:
            self.template = template_
        else:
            raise TypeError("Requires template value")

    def get_appearance(self):
        return self.appearance

    def set_appearance(self, appearance_):
        if type(appearance_) is appearance:
            self.appearance = appearance_
        else:
            raise TypeError("Requires appearance value")

    def get_alignment(self):
        return self.alignment

    def set_alignment(self, alignment):
        if type(alignment) is fieldAlignment:
            self.alignment = alignment
        else:
            raise TypeError("Requires fieldAlignment value")

    def validate_nonNegativeInteger(self, value):
        result = True
        # Validate type nonNegativeInteger, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on nonNegativeInteger' % {
                        "value": value, "lineno": lineno})
                result = False
        return result

    def validate_template(self, value):
        result = True
        # Validate type template, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['material', 'netgrif']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on template' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
        return result

    def validate_appearance(self, value):
        result = True
        # Validate type appearance, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['standard', 'outline', 'fill', 'legacy']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on appearance' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
        return result

    def validate_fieldAlignment(self, value):
        result = True
        # Validate type fieldAlignment, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['top', 'center', 'bottom']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on fieldAlignment' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
        return result

    def _hasContent(self):
        if (
                self.x is not None or
                self.y is not None or
                self.rows is not None or
                self.cols is not None or
                self.offset is not None or
                self.template is not None or
                self.appearance is not None or
                self.alignment is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='layout', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('layout')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'layout':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='layout')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='layout',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='layout'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='layout',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.x is not None:
            namespaceprefix_ = self.x_nsprefix_ + ':' if (UseCapturedNS_ and self.x_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sx>%s</%sx>%s' % (
                namespaceprefix_, self.gds_format_integer(self.x, input_name='x'), namespaceprefix_, eol_))
        if self.y is not None:
            namespaceprefix_ = self.y_nsprefix_ + ':' if (UseCapturedNS_ and self.y_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sy>%s</%sy>%s' % (
                namespaceprefix_, self.gds_format_integer(self.y, input_name='y'), namespaceprefix_, eol_))
        if self.rows is not None:
            namespaceprefix_ = self.rows_nsprefix_ + ':' if (UseCapturedNS_ and self.rows_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srows>%s</%srows>%s' % (
                namespaceprefix_, self.gds_format_integer(self.rows, input_name='rows'), namespaceprefix_, eol_))
        if self.cols is not None:
            namespaceprefix_ = self.cols_nsprefix_ + ':' if (UseCapturedNS_ and self.cols_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scols>%s</%scols>%s' % (
                namespaceprefix_, self.gds_format_integer(self.cols, input_name='cols'), namespaceprefix_, eol_))
        if self.offset is not None:
            namespaceprefix_ = self.offset_nsprefix_ + ':' if (UseCapturedNS_ and self.offset_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soffset>%s</%soffset>%s' % (
                namespaceprefix_, self.gds_format_integer(self.offset, input_name='offset'), namespaceprefix_, eol_))
        if self.template is not None:
            namespaceprefix_ = self.template_nsprefix_ + ':' if (UseCapturedNS_ and self.template_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stemplate>%s</%stemplate>%s' % (
                namespaceprefix_,
                self.gds_encode(self.gds_format_string(quote_xml(self.template), input_name='template')),
                namespaceprefix_, eol_))
        if self.appearance is not None:
            namespaceprefix_ = self.appearance_nsprefix_ + ':' if (UseCapturedNS_ and self.appearance_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sappearance>%s</%sappearance>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.appearance), input_name='appearance')), namespaceprefix_, eol_))
        if self.alignment is not None:
            namespaceprefix_ = self.alignment_nsprefix_ + ':' if (UseCapturedNS_ and self.alignment_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%salignment>%s</%salignment>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.alignment), input_name='alignment')), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'x' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'x')
            ival_ = self.gds_validate_integer(ival_, node, 'x')
            self.x = ival_
            self.x_nsprefix_ = child_.prefix
            # validate type nonNegativeInteger
            self.validate_nonNegativeInteger(self.x)
        elif nodeName_ == 'y' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'y')
            ival_ = self.gds_validate_integer(ival_, node, 'y')
            self.y = ival_
            self.y_nsprefix_ = child_.prefix
            # validate type nonNegativeInteger
            self.validate_nonNegativeInteger(self.y)
        elif nodeName_ == 'rows' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'rows')
            ival_ = self.gds_validate_integer(ival_, node, 'rows')
            self.rows = ival_
            self.rows_nsprefix_ = child_.prefix
            # validate type nonNegativeInteger
            self.validate_nonNegativeInteger(self.rows)
        elif nodeName_ == 'cols' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'cols')
            ival_ = self.gds_validate_integer(ival_, node, 'cols')
            self.cols = ival_
            self.cols_nsprefix_ = child_.prefix
            # validate type nonNegativeInteger
            self.validate_nonNegativeInteger(self.cols)
        elif nodeName_ == 'offset' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'offset')
            ival_ = self.gds_validate_integer(ival_, node, 'offset')
            self.offset = ival_
            self.offset_nsprefix_ = child_.prefix
            # validate type nonNegativeInteger
            self.validate_nonNegativeInteger(self.offset)
        elif nodeName_ == 'template':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'template')
            value_ = self.gds_validate_string(value_, node, 'template')
            self.template = value_
            self.template_nsprefix_ = child_.prefix
            # validate type template
            self.validate_template(self.template)
        elif nodeName_ == 'appearance':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'appearance')
            value_ = self.gds_validate_string(value_, node, 'appearance')
            self.appearance = value_
            self.appearance_nsprefix_ = child_.prefix
            # validate type appearance
            self.validate_appearance(self.appearance)
        elif nodeName_ == 'alignment':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'alignment')
            value_ = self.gds_validate_string(value_, node, 'alignment')
            self.alignment = value_
            self.alignment_nsprefix_ = child_.prefix
            # validate type fieldAlignment
            self.validate_fieldAlignment(self.alignment)


# end class layout


class assignedUser(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'cancel': MemberSpec_('cancel', 'xs:boolean', 0, 1, {'minOccurs': '0', 'name': 'cancel', 'type': 'xs:boolean'},
                              None),
        'reassign': MemberSpec_('reassign', 'xs:boolean', 0, 1,
                                {'minOccurs': '0', 'name': 'reassign', 'type': 'xs:boolean'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, cancel=None, reassign=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.cancel = cancel
        self.cancel_nsprefix_ = None
        self.reassign = reassign
        self.reassign_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, assignedUser)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if assignedUser.subclass:
            return assignedUser.subclass(*args_, **kwargs_)
        else:
            return assignedUser(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_cancel(self):
        return self.cancel

    def set_cancel(self, cancel):
        self.cancel = set_boolean_value(cancel)

    def get_reassign(self):
        return self.reassign

    def set_reassign(self, reassign):
        self.reassign = set_boolean_value(reassign)

    def _hasContent(self):
        if (
                self.cancel is not None or
                self.reassign is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='assignedUser', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('assignedUser')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'assignedUser':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='assignedUser')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='assignedUser',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='assignedUser'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='assignedUser',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.cancel is not None:
            namespaceprefix_ = self.cancel_nsprefix_ + ':' if (UseCapturedNS_ and self.cancel_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scancel>%s</%scancel>%s' % (
                namespaceprefix_, self.gds_format_boolean(self.cancel, input_name='cancel'), namespaceprefix_, eol_))
        if self.reassign is not None:
            namespaceprefix_ = self.reassign_nsprefix_ + ':' if (UseCapturedNS_ and self.reassign_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sreassign>%s</%sreassign>%s' % (
                namespaceprefix_, self.gds_format_boolean(self.reassign, input_name='reassign'), namespaceprefix_,
                eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'cancel':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'cancel')
            ival_ = self.gds_validate_boolean(ival_, node, 'cancel')
            self.cancel = ival_
            self.cancel_nsprefix_ = child_.prefix
        elif nodeName_ == 'reassign':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'reassign')
            ival_ = self.gds_validate_boolean(ival_, node, 'reassign')
            self.reassign = ival_
            self.reassign_nsprefix_ = child_.prefix


# end class assignedUser


class dataGroup(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'id': MemberSpec_('id', 'xs:string', 0, 0, {'name': 'id', 'type': 'xs:string'}, None),
        'cols': MemberSpec_('cols', ['nonNegativeInteger', 'xs:int'], 0, 1,
                            {'minOccurs': '0', 'name': 'cols', 'type': 'xs:int'}, None),
        'rows': MemberSpec_('rows', ['nonNegativeInteger', 'xs:int'], 0, 1,
                            {'minOccurs': '0', 'name': 'rows', 'type': 'xs:int'}, None),
        'layout': MemberSpec_('layout', ['layoutType', 'xs:string'], 0, 0, {'name': 'layout', 'type': 'xs:string'},
                              None),
        'title': MemberSpec_('title', 'i18nStringType', 0, 1,
                             {'minOccurs': '0', 'name': 'title', 'type': 'i18nStringType'}, None),
        'alignment': MemberSpec_('alignment', ['dataGroupAlignment', 'xs:string'], 0, 1,
                                 {'minOccurs': '0', 'name': 'alignment', 'type': 'xs:string'}, None),
        'stretch': MemberSpec_('stretch', 'xs:boolean', 0, 1,
                               {'minOccurs': '0', 'name': 'stretch', 'type': 'xs:boolean'}, None),
        'hideEmptyRows': MemberSpec_('hideEmptyRows', ['hideEmptyRows', 'xs:string'], 0, 1,
                                     {'minOccurs': '0', 'name': 'hideEmptyRows', 'type': 'xs:string'}, None),
        'compactDirection': MemberSpec_('compactDirection', ['compactDirection', 'xs:string'], 0, 1,
                                        {'minOccurs': '0', 'name': 'compactDirection', 'type': 'xs:string'}, None),
        'dataRef': MemberSpec_('dataRef', 'dataRef', 1, 1,
                               {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'dataRef', 'type': 'dataRef'},
                               None),
    }
    subclass = None
    superclass = None

    def __init__(self, id=None, cols=None, rows=None, layout=None, title=None, alignment=None, stretch=None,
                 hideEmptyRows=None, compactDirection=None, dataRef=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = id
        self.id_nsprefix_ = None
        self.cols = cols
        self.validate_nonNegativeInteger(self.cols)
        self.cols_nsprefix_ = None
        self.rows = rows
        self.validate_nonNegativeInteger(self.rows)
        self.rows_nsprefix_ = None
        self.layout = layout
        self.validate_layoutType(self.layout)
        self.layout_nsprefix_ = None
        self.title = title
        self.title_nsprefix_ = None
        self.alignment = alignment
        self.validate_dataGroupAlignment(self.alignment)
        self.alignment_nsprefix_ = None
        self.stretch = stretch
        self.stretch_nsprefix_ = None
        self.hideEmptyRows = hideEmptyRows
        self.validate_hideEmptyRows(self.hideEmptyRows)
        self.hideEmptyRows_nsprefix_ = None
        self.compactDirection = compactDirection
        self.validate_compactDirection(self.compactDirection)
        self.compactDirection_nsprefix_ = None
        if dataRef is None:
            self.dataRef = []
        else:
            self.dataRef = dataRef
        self.dataRef_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataGroup)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataGroup.subclass:
            return dataGroup.subclass(*args_, **kwargs_)
        else:
            return dataGroup(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_id(self):
        return self.id

    def set_id(self, id_):
        if type(id_) is str:
            self.id = id_
        else:
            raise TypeError("Requires str value")

    def get_cols(self):
        return self.cols

    def set_cols(self, cols):
        if type(cols) is int:
            if cols < 0:
                raise ValueError("The 'cols' element has to be nonNegativeInteger")
            else:
                self.cols = cols
        else:
            raise TypeError("Requires int value")

    def get_rows(self):
        return self.rows

    def set_rows(self, rows):
        if type(rows) is int:
            if rows < 0:
                raise ValueError("The 'rows' element has to be nonNegativeInteger")
            else:
                self.rows = rows
        else:
            raise TypeError("Requires int value")

    def get_layout(self):
        return self.layout

    def set_layout(self, layout_):
        if type(layout_) is layoutType:
            self.layout = layout_
        else:
            raise TypeError("Requires layoutType value")

    def get_title(self):
        return self.title

    def set_title(self, title):
        if type(title) is i18nStringType:
            self.title = title
        else:
            raise TypeError("Requires i18nStringType value")

    def get_alignment(self):
        return self.alignment

    def set_alignment(self, alignment):
        if type(alignment) is dataGroupAlignment:
            self.alignment = alignment
        else:
            raise TypeError("Requires dataGroupAlignment value")

    def get_stretch(self):
        return self.stretch

    def set_stretch(self, stretch):
        self.stretch = set_boolean_value(stretch)

    def get_hideEmptyRows(self):
        return self.hideEmptyRows

    def set_hideEmptyRows(self, hideEmptyRows_):
        if type(hideEmptyRows_) is hideEmptyRows:
            self.hideEmptyRows = hideEmptyRows_
        else:
            raise TypeError("Requires hideEmptyRows value")

    def get_compactDirection(self):
        return self.compactDirection

    def set_compactDirection(self, compactDirection_):
        if type(compactDirection_) is compactDirection:
            self.compactDirection = compactDirection_
        else:
            raise TypeError("Requires compactDirection value")

    def get_dataRef(self):
        return self.dataRef

    def set_dataRef(self, dataRef_):
        if all(isinstance(x, dataRef) for x in dataRef_):
            self.dataRef = dataRef_
        else:
            raise TypeError("Requires only dataRef values inside an array")

    def add_dataRef(self, value):
        if type(value) is dataRef:
            self.dataRef.append(value)
        else:
            raise TypeError("Requires dataRef value")

    def insert_dataRef_at(self, index, value):
        if 0 <= index <= len(self.dataRef):
            if type(value) is dataRef:
                self.dataRef.insert(index, value)
            else:
                raise TypeError("Requires dataRef value")
        else:
            raise IndexError("Invalid index value")

    def replace_dataRef_at(self, index, value):
        if 0 <= index < len(self.dataRef):
            if self.dataRef[index]:
                if type(value) is dataRef:
                    self.dataRef[index] = value
                else:
                    raise TypeError("Requires dataRef value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def validate_nonNegativeInteger(self, value):
        result = True
        # Validate type nonNegativeInteger, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on nonNegativeInteger' % {
                        "value": value, "lineno": lineno})
                result = False
        return result

    def validate_layoutType(self, value):
        result = True
        # Validate type layoutType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['flow', 'grid', 'legacy']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on layoutType' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
        return result

    def validate_dataGroupAlignment(self, value):
        result = True
        # Validate type dataGroupAlignment, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['start', 'center', 'end', 'left']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on dataGroupAlignment' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
        return result

    def validate_hideEmptyRows(self, value):
        result = True
        # Validate type hideEmptyRows, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['all', 'compacted', 'none']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on hideEmptyRows' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
        return result

    def validate_compactDirection(self, value):
        result = True
        # Validate type compactDirection, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['none', 'up']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on compactDirection' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
        return result

    def _hasContent(self):
        if (
                self.id is not None or
                self.cols is not None or
                self.rows is not None or
                self.layout is not None or
                self.title is not None or
                self.alignment is not None or
                self.stretch is not None or
                self.hideEmptyRows is not None or
                self.compactDirection is not None or
                self.dataRef
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='dataGroup', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataGroup')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataGroup':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataGroup')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataGroup',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataGroup'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='dataGroup',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.id is not None:
            namespaceprefix_ = self.id_nsprefix_ + ':' if (UseCapturedNS_ and self.id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sid>%s</%sid>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.id), input_name='id')),
                namespaceprefix_, eol_))
        if self.cols is not None:
            namespaceprefix_ = self.cols_nsprefix_ + ':' if (UseCapturedNS_ and self.cols_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scols>%s</%scols>%s' % (
                namespaceprefix_, self.gds_format_integer(self.cols, input_name='cols'), namespaceprefix_, eol_))
        if self.rows is not None:
            namespaceprefix_ = self.rows_nsprefix_ + ':' if (UseCapturedNS_ and self.rows_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srows>%s</%srows>%s' % (
                namespaceprefix_, self.gds_format_integer(self.rows, input_name='rows'), namespaceprefix_, eol_))
        if self.layout is not None:
            namespaceprefix_ = self.layout_nsprefix_ + ':' if (UseCapturedNS_ and self.layout_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slayout>%s</%slayout>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.layout), input_name='layout')),
                namespaceprefix_, eol_))
        if self.title is not None:
            namespaceprefix_ = self.title_nsprefix_ + ':' if (UseCapturedNS_ and self.title_nsprefix_) else ''
            self.title.export(outfile, level, namespaceprefix_, namespacedef_='', name_='title',
                              pretty_print=pretty_print)
        if self.alignment is not None:
            namespaceprefix_ = self.alignment_nsprefix_ + ':' if (UseCapturedNS_ and self.alignment_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%salignment>%s</%salignment>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.alignment), input_name='alignment')), namespaceprefix_, eol_))
        if self.stretch is not None:
            namespaceprefix_ = self.stretch_nsprefix_ + ':' if (UseCapturedNS_ and self.stretch_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstretch>%s</%sstretch>%s' % (
                namespaceprefix_, self.gds_format_boolean(self.stretch, input_name='stretch'), namespaceprefix_, eol_))
        if self.hideEmptyRows is not None:
            namespaceprefix_ = self.hideEmptyRows_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.hideEmptyRows_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%shideEmptyRows>%s</%shideEmptyRows>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.hideEmptyRows), input_name='hideEmptyRows')), namespaceprefix_,
                                                                       eol_))
        if self.compactDirection is not None:
            namespaceprefix_ = self.compactDirection_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.compactDirection_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scompactDirection>%s</%scompactDirection>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.compactDirection), input_name='compactDirection')),
                                                                             namespaceprefix_, eol_))
        for dataRef_ in self.dataRef:
            namespaceprefix_ = self.dataRef_nsprefix_ + ':' if (UseCapturedNS_ and self.dataRef_nsprefix_) else ''
            dataRef_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='dataRef',
                            pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'id')
            value_ = self.gds_validate_string(value_, node, 'id')
            self.id = value_
            self.id_nsprefix_ = child_.prefix
        elif nodeName_ == 'cols' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'cols')
            ival_ = self.gds_validate_integer(ival_, node, 'cols')
            self.cols = ival_
            self.cols_nsprefix_ = child_.prefix
            # validate type nonNegativeInteger
            self.validate_nonNegativeInteger(self.cols)
        elif nodeName_ == 'rows' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'rows')
            ival_ = self.gds_validate_integer(ival_, node, 'rows')
            self.rows = ival_
            self.rows_nsprefix_ = child_.prefix
            # validate type nonNegativeInteger
            self.validate_nonNegativeInteger(self.rows)
        elif nodeName_ == 'layout':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'layout')
            value_ = self.gds_validate_string(value_, node, 'layout')
            self.layout = value_
            self.layout_nsprefix_ = child_.prefix
            # validate type layoutType
            self.validate_layoutType(self.layout)
        elif nodeName_ == 'title':
            class_obj_ = self.get_class_obj_(child_, i18nStringType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.title = obj_
            obj_.original_tagname_ = 'title'
        elif nodeName_ == 'alignment':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'alignment')
            value_ = self.gds_validate_string(value_, node, 'alignment')
            self.alignment = value_
            self.alignment_nsprefix_ = child_.prefix
            # validate type dataGroupAlignment
            self.validate_dataGroupAlignment(self.alignment)
        elif nodeName_ == 'stretch':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'stretch')
            ival_ = self.gds_validate_boolean(ival_, node, 'stretch')
            self.stretch = ival_
            self.stretch_nsprefix_ = child_.prefix
        elif nodeName_ == 'hideEmptyRows':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'hideEmptyRows')
            value_ = self.gds_validate_string(value_, node, 'hideEmptyRows')
            self.hideEmptyRows = value_
            self.hideEmptyRows_nsprefix_ = child_.prefix
            # validate type hideEmptyRows
            self.validate_hideEmptyRows(self.hideEmptyRows)
        elif nodeName_ == 'compactDirection':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'compactDirection')
            value_ = self.gds_validate_string(value_, node, 'compactDirection')
            self.compactDirection = value_
            self.compactDirection_nsprefix_ = child_.prefix
            # validate type compactDirection
            self.validate_compactDirection(self.compactDirection)
        elif nodeName_ == 'dataRef':
            obj_ = dataRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dataRef.append(obj_)
            obj_.original_tagname_ = 'dataRef'


# end class dataGroup


class action(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'trigger': MemberSpec_('trigger', 'xs:string', 0, 1, {'use': 'optional', 'name': 'trigger'}),
        'id': MemberSpec_('id', 'xs:string', 0, 1, {'use': 'optional', 'name': 'id'}),
        'valueOf_': MemberSpec_('valueOf_', 'xs:string', 0),
    }
    subclass = None
    superclass = None

    def __init__(self, trigger_=None, id_=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.trigger = _cast(None, trigger_)
        self.trigger_nsprefix_ = None
        self.id = _cast(None, id_)
        self.id_nsprefix_ = None
        self.valueOf_ = valueOf_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, action)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if action.subclass:
            return action.subclass(*args_, **kwargs_)
        else:
            return action(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_trigger(self):
        return self.trigger

    def set_trigger(self, trigger_):
        if type(trigger_) is str:
            self.trigger = trigger_
        else:
            raise TypeError("Requires str value")

    def get_id(self):
        return self.id

    def set_id(self, id_):
        if type(id_) is str:
            self.id = id_
        else:
            raise TypeError("Requires str value")

    def get_valueOf_(self):
        return self.valueOf_

    def set_valueOf_(self, valueOf_):
        if type(valueOf_) is str:
            self.valueOf_ = valueOf_
        else:
            raise TypeError("Requires str value")

    def _hasContent(self):
        if (
                (1 if type(self.valueOf_) in [int, float] else self.valueOf_)
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='action', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('action')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'action':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='action')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='action',
                                 pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='action'):
        if self.trigger is not None and 'trigger' not in already_processed:
            already_processed.add('trigger')
            outfile.write(' trigger=%s' % (
                self.gds_encode(self.gds_format_string(quote_attrib(self.trigger), input_name='trigger')),))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')),))

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='action',
                        fromsubclass_=False, pretty_print=True):
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('trigger', node)
        if value is not None and 'trigger' not in already_processed:
            already_processed.add('trigger')
            self.trigger = value
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass


# end class action


class validations(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'validation': MemberSpec_('validation', 'validation', 1, 1,
                                  {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'validation',
                                   'type': 'validation'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, validation=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if validation is None:
            self.validation = []
        else:
            self.validation = validation
        self.validation_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, validations)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if validations.subclass:
            return validations.subclass(*args_, **kwargs_)
        else:
            return validations(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_validation(self):
        return self.validation

    def set_validation(self, validation_):
        if all(isinstance(x, validation) for x in validation_):
            self.validation = validation_
        else:
            raise TypeError("Requires only validation values inside an array")

    def add_validation(self, value):
        if type(value) is validation:
            self.validation.append(value)
        else:
            raise TypeError("Requires validation value")

    def insert_validation_at(self, index, value):
        if 0 <= index <= len(self.validation):
            if type(value) is validation:
                self.validation.insert(index, value)
            else:
                raise TypeError("Requires validation value")
        else:
            raise IndexError("Invalid index value")

    def replace_validation_at(self, index, value):
        if 0 <= index < len(self.validation):
            if self.validation[index]:
                if type(value) is validation:
                    self.validation[index] = value
                else:
                    raise TypeError("Requires validation value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def _hasContent(self):
        if (
                self.validation
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='validations', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('validations')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'validations':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='validations')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='validations',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='validations'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='validations',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for validation_ in self.validation:
            namespaceprefix_ = self.validation_nsprefix_ + ':' if (UseCapturedNS_ and self.validation_nsprefix_) else ''
            validation_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='validation',
                               pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'validation':
            obj_ = validation.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.validation.append(obj_)
            obj_.original_tagname_ = 'validation'


# end class validations


class validation(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'expression': MemberSpec_('expression', 'expression', 0, 0, {'name': 'expression', 'type': 'valid'}, None),
        'message': MemberSpec_('message', 'i18nStringType', 0, 0, {'name': 'message', 'type': 'i18nStringType'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, expression=None, message=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.expression = expression
        self.expression_nsprefix_ = None
        self.message = message
        self.message_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, validation)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if validation.subclass:
            return validation.subclass(*args_, **kwargs_)
        else:
            return validation(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_expression(self):
        return self.expression

    def set_expression(self, expression_):
        if type(expression_) is valid:
            self.expression = expression_
        else:
            raise TypeError("Requires valid value")

    def get_message(self):
        return self.message

    def set_message(self, message):
        if type(message) is i18nStringType:
            self.message = message
        else:
            raise TypeError("Requires i18nStringType value")

    def _hasContent(self):
        if (
                self.expression is not None or
                self.message is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='validation', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('validation')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'validation':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='validation')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='validation',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='validation'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='validation',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.expression is not None:
            namespaceprefix_ = self.expression_nsprefix_ + ':' if (UseCapturedNS_ and self.expression_nsprefix_) else ''
            self.expression.export(outfile, level, namespaceprefix_, namespacedef_='', name_='expression',
                                   pretty_print=pretty_print)
        if self.message is not None:
            namespaceprefix_ = self.message_nsprefix_ + ':' if (UseCapturedNS_ and self.message_nsprefix_) else ''
            self.message.export(outfile, level, namespaceprefix_, namespacedef_='', name_='message',
                                pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'expression':
            obj_ = valid.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.expression = obj_
            obj_.original_tagname_ = 'expression'
        elif nodeName_ == 'message':
            class_obj_ = self.get_class_obj_(child_, i18nStringType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.message = obj_
            obj_.original_tagname_ = 'message'


# end class validation


class trigger(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'type_': MemberSpec_('type_', 'triggerType', 0, 1, {'use': 'optional', 'name': 'type_'}),
        'exact': MemberSpec_('exact', 'xs:dateTime', 0, 1, {'name': 'exact', 'type': 'xs:dateTime'}, 13),
        'delay': MemberSpec_('delay', 'xs:duration', 0, 1, {'name': 'delay', 'type': 'xs:duration'}, 13),
    }
    subclass = None
    superclass = None

    def __init__(self, type_=None, exact=None, delay=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
        if isinstance(exact, str):
            initvalue_ = datetime_.datetime.strptime(exact, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = exact
        self.exact = initvalue_
        self.exact_nsprefix_ = None
        self.delay = delay
        self.delay_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, trigger)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if trigger.subclass:
            return trigger.subclass(*args_, **kwargs_)
        else:
            return trigger(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_exact(self):
        return self.exact

    def set_exact(self, exact):
        if self.delay is None:
            if type(exact) is datetime_.datetime:
                self.exact = exact
            else:
                raise TypeError("Requires datetime value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'delay' element.")

    def get_delay(self):
        return self.delay

    def set_delay(self, delay):
        if self.exact is None:
            if type(delay) is datetime_.timedelta:
                self.delay = delay
            else:
                raise TypeError("Requires timedelta value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains a 'exact' element.")

    def get_type(self):
        return self.type_

    def set_type_(self, type_):
        if type(type_) is triggerType:
            self.type_ = type_
        else:
            raise TypeError("Requires triggerType value")

    def validate_triggerType(self, value):
        # Validate type triggerType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['auto', 'user', 'time']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on triggerType' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False

    def _hasContent(self):
        if (
                self.exact is not None or
                self.delay is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='trigger', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('trigger')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'trigger':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='trigger')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='trigger',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='trigger'):
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(
                ' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')),))

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='trigger',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.exact is not None:
            namespaceprefix_ = self.exact_nsprefix_ + ':' if (UseCapturedNS_ and self.exact_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sexact>%s</%sexact>%s' % (
                namespaceprefix_, self.gds_format_datetime(self.exact, input_name='exact'), namespaceprefix_, eol_))
        if self.delay is not None:
            namespaceprefix_ = self.delay_nsprefix_ + ':' if (UseCapturedNS_ and self.delay_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdelay>%s</%sdelay>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.delay), input_name='delay')),
                namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.validate_triggerType(self.type_)  # validate type triggerType

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'exact':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.exact = dval_
            self.exact_nsprefix_ = child_.prefix
        elif nodeName_ == 'delay':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'delay')
            value_ = self.gds_validate_string(value_, node, 'delay')
            self.delay = value_
            self.delay_nsprefix_ = child_.prefix


# end class trigger


class documentRef(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'id': MemberSpec_('id', ['nonNegativeLong', 'xs:long'], 0, 0, {'name': 'id', 'type': 'xs:long'}, None),
        'fields': MemberSpec_('fields', ['nonNegativeLong', 'xs:long'], 1, 1,
                              {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'fields', 'type': 'xs:long'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, id=None, fields=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = id
        self.validate_nonNegativeLong(self.id)
        self.id_nsprefix_ = None
        if fields is None:
            self.fields = []
        else:
            self.fields = fields
        self.fields_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, documentRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if documentRef.subclass:
            return documentRef.subclass(*args_, **kwargs_)
        else:
            return documentRef(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_id(self):
        return self.id

    def set_id(self, id_):
        if type(id_) is int:
            if id_ < 0 or id_ > (2 ** 64 - 1):  # ** is ^
                raise ValueError("The 'id' element has to be nonNegativeLong")
            else:
                self.id = id_
        else:
            raise TypeError("Requires int value")

    def get_fields(self):
        return self.fields

    def set_fields(self, fields):
        if all(isinstance(x, int) for x in fields):
            if all(f < 0 or f > (2 ** 64 - 1) for f in fields):  # ** is ^
                raise ValueError("The 'fields' element has to be nonNegativeLong")
            else:
                self.fields = fields
        else:
            raise TypeError("Requires only int values inside an array")

    def add_fields(self, value):
        if type(value) is int:
            if value < 0 or value > (2 ** 64 - 1):  # ** is ^
                raise ValueError("The 'fields' element has to be nonNegativeLong")
            else:
                self.fields.append(value)
        else:
            raise TypeError("Requires int value")

    def insert_fields_at(self, index, value):
        if 0 <= index <= len(self.fields):
            if type(value) is int:
                if value < 0 or value > (2 ** 64 - 1):  # ** is ^
                    raise ValueError("The 'fields' element has to be nonNegativeLong")
                else:
                    self.fields.insert(index, value)
            else:
                raise TypeError("Requires int value")
        else:
            raise IndexError("Invalid index value")

    def replace_fields_at(self, index, value):
        if 0 <= index < len(self.fields):
            if self.fields[index]:
                if type(value) is int:
                    if value < 0 or value > (2 ** 64 - 1):  # ** is ^
                        raise ValueError("The 'fields' element has to be nonNegativeLong")
                    else:
                        self.fields[index] = value
                else:
                    raise TypeError("Requires int value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def validate_nonNegativeLong(self, value):
        result = True
        # Validate type nonNegativeLong, a restriction on xs:long.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on nonNegativeLong' % {
                        "value": value, "lineno": lineno})
                result = False
        return result

    def _hasContent(self):
        if (
                self.id is not None or
                self.fields
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='documentRef', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('documentRef')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'documentRef':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='documentRef')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='documentRef',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='documentRef'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='documentRef',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.id is not None:
            namespaceprefix_ = self.id_nsprefix_ + ':' if (UseCapturedNS_ and self.id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sid>%s</%sid>%s' % (
                namespaceprefix_, self.gds_format_integer(self.id, input_name='id'), namespaceprefix_, eol_))
        for fields_ in self.fields:
            namespaceprefix_ = self.fields_nsprefix_ + ':' if (UseCapturedNS_ and self.fields_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfields>%s</%sfields>%s' % (
                namespaceprefix_, self.gds_format_integer(fields_, input_name='fields'), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'id' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'id')
            ival_ = self.gds_validate_integer(ival_, node, 'id')
            self.id = ival_
            self.id_nsprefix_ = child_.prefix
            # validate type nonNegativeLong
            self.validate_nonNegativeLong(self.id)
        elif nodeName_ == 'fields' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'fields')
            ival_ = self.gds_validate_integer(ival_, node, 'fields')
            self.fields.append(ival_)
            self.fields_nsprefix_ = child_.prefix
            # validate type nonNegativeLong
            self.validate_nonNegativeLong(self.fields[-1])


# end class documentRef


class encryption(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'algorithm': MemberSpec_('algorithm', 'xs:string', 0, 1, {'use': 'optional', 'name': 'algorithm'}),
        'valueOf_': MemberSpec_('valueOf_', 'xs:boolean', 0),
    }
    subclass = None
    superclass = None

    def __init__(self, algorithm=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.algorithm = _cast(None, algorithm)
        self.algorithm_nsprefix_ = None
        self.valueOf_ = valueOf_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, encryption)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if encryption.subclass:
            return encryption.subclass(*args_, **kwargs_)
        else:
            return encryption(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_algorithm(self):
        return self.algorithm

    def set_algorithm(self, algorithm):
        if type(algorithm) is str:
            self.algorithm = algorithm
        else:
            raise TypeError("Requires str value")
        # self.algorithm = set_boolean_value(algorithm)

    def get_valueOf_(self):
        return self.valueOf_

    def set_valueOf_(self, valueOf_):
        self.valueOf_ = set_boolean_value(valueOf_)

    def _hasContent(self):
        if (
                (1 if type(self.valueOf_) in [int, float] else self.valueOf_)
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='encryption', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('encryption')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'encryption':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='encryption')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='encryption',
                                 pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='encryption'):
        if self.algorithm is not None and 'algorithm' not in already_processed:
            already_processed.add('algorithm')
            outfile.write(' algorithm=%s' % (
                self.gds_encode(self.gds_format_string(quote_attrib(self.algorithm), input_name='algorithm')),))

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='encryption',
                        fromsubclass_=False, pretty_print=True):
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('algorithm', node)
        if value is not None and 'algorithm' not in already_processed:
            already_processed.add('algorithm')
            self.algorithm = value

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass


# end class encryption


class i18nStringType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'name': MemberSpec_('name', 'xs:string', 0, 1, {'use': 'optional', 'name': 'name'}),
        'valueOf_': MemberSpec_('valueOf_', 'xs:string', 0),
    }
    subclass = None
    superclass = None

    def __init__(self, name=None, valueOf_=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.valueOf_ = valueOf_
        self.extensiontype_ = extensiontype_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, i18nStringType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if i18nStringType.subclass:
            return i18nStringType.subclass(*args_, **kwargs_)
        else:
            return i18nStringType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_name(self):
        return self.name

    def set_name(self, name):
        if type(name) is str:
            self.name = name
        else:
            raise TypeError("Requires str value")

    def get_valueOf_(self):
        return self.valueOf_

    def set_valueOf_(self, valueOf_):
        if type(valueOf_) is str:
            self.valueOf_ = valueOf_
        else:
            raise TypeError("Requires str value")

    def set_original_tagname_(self, original_tagname_):
        if type(original_tagname_) is str:
            self.original_tagname_ = original_tagname_
        else:
            raise TypeError("Requires str value")

    def get_extensiontype_(self):
        return self.extensiontype_

    def set_extensiontype_(self, extensiontype_):
        self.extensiontype_ = extensiontype_

    def _hasContent(self):
        if (
                (1 if type(self.valueOf_) in [int, float] else self.valueOf_)
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='i18nStringType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('i18nStringType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'i18nStringType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='i18nStringType')
        if self._hasContent():
            outfile.write(
                '>')  # different from e.g. transition because there I want to put the content in new lines, but here I want to put everything in the same line
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='i18nStringType',
                                 pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='i18nStringType'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(
                ' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')),))
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='i18nStringType',
                        fromsubclass_=False, pretty_print=True):
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass


# end class i18nStringType


class i18nStringTypeWithExpression(i18nStringType):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'dynamic': MemberSpec_('dynamic', 'xs:boolean', 0, 1, {'use': 'optional', 'name': 'dynamic'}),
        'valueOf_': MemberSpec_('valueOf_', 'i18nStringType', 0),
    }
    subclass = None
    superclass = i18nStringType

    def __init__(self, name=None, dynamic=False, valueOf_=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("i18nStringTypeWithExpression"), self).__init__(name, valueOf_, extensiontype_, **kwargs_)
        self.dynamic = _cast(bool, dynamic)
        self.dynamic_nsprefix_ = None
        self.valueOf_ = valueOf_
        self.extensiontype_ = extensiontype_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, i18nStringTypeWithExpression)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if i18nStringTypeWithExpression.subclass:
            return i18nStringTypeWithExpression.subclass(*args_, **kwargs_)
        else:
            return i18nStringTypeWithExpression(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_dynamic(self):
        return self.dynamic

    def set_dynamic(self, dynamic):
        self.dynamic = set_boolean_value(dynamic)

    def get_valueOf_(self):
        return self.valueOf_

    def set_valueOf_(self, valueOf_):
        if type(valueOf_) is str:
            self.valueOf_ = valueOf_
        else:
            raise TypeError("Requires str value")

    def get_extensiontype_(self):
        return self.extensiontype_

    def set_extensiontype_(self, extensiontype_):
        self.extensiontype_ = extensiontype_

    def _hasContent(self):
        if (
                (1 if type(self.valueOf_) in [int, float] else self.valueOf_) or
                super(i18nStringTypeWithExpression, self)._hasContent()
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='i18nStringTypeWithExpression',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('i18nStringTypeWithExpression')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'i18nStringTypeWithExpression':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_,
                               name_='i18nStringTypeWithExpression')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_,
                                 name_='i18nStringTypeWithExpression', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='',
                          name_='i18nStringTypeWithExpression'):
        super(i18nStringTypeWithExpression, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_,
                                                                    name_='i18nStringTypeWithExpression')
        if self.dynamic and 'dynamic' not in already_processed:
            already_processed.add('dynamic')
            outfile.write(' dynamic="%s"' % self.gds_format_boolean(self.dynamic, input_name='dynamic'))
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='',
                        name_='i18nStringTypeWithExpression', fromsubclass_=False, pretty_print=True):
        super(i18nStringTypeWithExpression, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_,
                                                                  name_, True, pretty_print=pretty_print)
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('dynamic', node)
        if value is not None and 'dynamic' not in already_processed:
            already_processed.add('dynamic')
            if value in ('true', '1'):
                self.dynamic = True
            elif value in ('false', '0'):
                self.dynamic = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
        super(i18nStringTypeWithExpression, self)._buildAttributes(node, attrs, already_processed)

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass


# end class i18nStringTypeWithExpression


class baseEvent(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'id': MemberSpec_('id', 'xs:string', 0, 0, {'name': 'id', 'type': 'xs:string'}, None),
        'actions': MemberSpec_('actions', 'actions', 1, 1,
                               {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'actions', 'type': 'actions'},
                               None),
        'message': MemberSpec_('message', 'i18nStringType', 0, 1,
                               {'minOccurs': '0', 'name': 'message', 'type': 'i18nStringType'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, id=None, actions=None, message=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = id
        self.id_nsprefix_ = None
        if actions is None:
            self.actions = []
        else:
            self.actions = actions
        self.actions_nsprefix_ = None
        self.message = message
        self.message_nsprefix_ = None
        self.extensiontype_ = extensiontype_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, baseEvent)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if baseEvent.subclass:
            return baseEvent.subclass(*args_, **kwargs_)
        else:
            return baseEvent(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_id(self):
        return self.id

    def set_id(self, id_):
        if type(id_) is str:
            self.id = id_
        else:
            raise TypeError("Requires str value")

    def get_actions(self):
        return self.actions

    def set_actions(self, actions_):
        if all(isinstance(x, actions) for x in actions_):
            self.actions = actions_
        else:
            raise TypeError("Requires only actions values inside an array")

    def add_actions(self, value):
        if type(value) is actions:
            self.actions.append(value)
        else:
            raise TypeError("Requires actions value")

    def insert_actions_at(self, index, value):
        if 0 <= index <= len(self.actions):
            if type(value) is action:
                self.actions.insert(index, value)
            else:
                raise TypeError("Requires actions value")
        else:
            raise IndexError("Invalid index value")

    def replace_actions_at(self, index, value):
        if 0 <= index < len(self.actions):
            if self.actions[index]:
                if type(value) is action:
                    self.actions[index] = value
                else:
                    raise TypeError("Requires actions value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_message(self):
        return self.message

    def set_message(self, message):
        if type(message) is i18nStringType:
            self.message = message
        else:
            raise TypeError("Requires i18nStringType value")

    def get_extensiontype_(self):
        return self.extensiontype_

    def set_extensiontype_(self, extensiontype_):
        self.extensiontype_ = extensiontype_

    def _hasContent(self):
        if (
                self.id is not None or
                self.actions or
                self.message is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='baseEvent', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('baseEvent')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'baseEvent':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='baseEvent')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='baseEvent',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='baseEvent'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='baseEvent',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.id is not None:
            namespaceprefix_ = self.id_nsprefix_ + ':' if (UseCapturedNS_ and self.id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sid>%s</%sid>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.id), input_name='id')),
                namespaceprefix_, eol_))
        for actions_ in self.actions:
            namespaceprefix_ = self.actions_nsprefix_ + ':' if (UseCapturedNS_ and self.actions_nsprefix_) else ''
            actions_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='actions',
                            pretty_print=pretty_print)
        if self.message is not None:
            namespaceprefix_ = self.message_nsprefix_ + ':' if (UseCapturedNS_ and self.message_nsprefix_) else ''
            self.message.export(outfile, level, namespaceprefix_, namespacedef_='', name_='message',
                                pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'id')
            value_ = self.gds_validate_string(value_, node, 'id')
            self.id = value_
            self.id_nsprefix_ = child_.prefix
        elif nodeName_ == 'actions':
            obj_ = actions.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.actions.append(obj_)
            obj_.original_tagname_ = 'actions'
        elif nodeName_ == 'message':
            class_obj_ = self.get_class_obj_(child_, i18nStringType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.message = obj_
            obj_.original_tagname_ = 'message'


# end class baseEvent


class dataEvent(baseEvent):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'type_': MemberSpec_('type_', 'dataEventType', 0, 0, {'use': 'required', 'name': 'type_'}),
    }
    subclass = None
    superclass = baseEvent

    def __init__(self, id=None, actions=None, message=None, type_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("dataEvent"), self).__init__(id, actions, message, **kwargs_)
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataEvent)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataEvent.subclass:
            return dataEvent.subclass(*args_, **kwargs_)
        else:
            return dataEvent(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_type(self):
        return self.type_

    def set_type_(self, type_):
        if type(type_) is dataEventType:
            self.type_ = type_
        else:
            raise TypeError("Requires dataEventType value")

    def validate_dataEventType(self, value):
        # Validate type dataEventType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['set', 'get']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on dataEventType' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False

    def _hasContent(self):
        if (
                super(dataEvent, self)._hasContent()
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='dataEvent', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataEvent')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataEvent':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataEvent')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataEvent',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataEvent'):
        super(dataEvent, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataEvent')
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(
                ' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')),))

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='dataEvent',
                        fromsubclass_=False, pretty_print=True):
        super(dataEvent, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True,
                                               pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.validate_dataEventType(self.type_)  # validate type dataEventType
        super(dataEvent, self)._buildAttributes(node, attrs, already_processed)

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(dataEvent, self)._buildChildren(child_, node, nodeName_, True)
        pass


# end class dataEvent


class caseEvent(baseEvent):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'type_': MemberSpec_('type_', 'caseEventType', 0, 0, {'use': 'required', 'name': 'type_'}),
    }
    subclass = None
    superclass = baseEvent

    def __init__(self, id=None, actions=None, message=None, type_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("caseEvent"), self).__init__(id, actions, message, **kwargs_)
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, caseEvent)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if caseEvent.subclass:
            return caseEvent.subclass(*args_, **kwargs_)
        else:
            return caseEvent(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_type(self):
        return self.type_

    def set_type_(self, type_):
        if type(type_) is caseEventType:
            self.type_ = type_
        else:
            raise TypeError("Requires caseEventType value")

    def validate_caseEventType(self, value):
        # Validate type caseEventType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['create', 'delete']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on caseEventType' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False

    def _hasContent(self):
        if (
                super(caseEvent, self)._hasContent()
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='caseEvent', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('caseEvent')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'caseEvent':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='caseEvent')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='caseEvent',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='caseEvent'):
        super(caseEvent, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='caseEvent')
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(
                ' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')),))

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='caseEvent',
                        fromsubclass_=False, pretty_print=True):
        super(caseEvent, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True,
                                               pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.validate_caseEventType(self.type_)  # validate type caseEventType
        super(caseEvent, self)._buildAttributes(node, attrs, already_processed)

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(caseEvent, self)._buildChildren(child_, node, nodeName_, True)
        pass


# end class caseEvent


class processEvent(baseEvent):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'type_': MemberSpec_('type_', 'processEventType', 0, 0, {'use': 'required', 'name': 'type_'}),
    }
    subclass = None
    superclass = baseEvent

    def __init__(self, id=None, actions=None, message=None, type_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("processEvent"), self).__init__(id, actions, message, **kwargs_)
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, processEvent)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if processEvent.subclass:
            return processEvent.subclass(*args_, **kwargs_)
        else:
            return processEvent(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_type(self):
        return self.type_

    def set_type_(self, type_):
        if type(type_) is processEventType:
            self.type_ = type_
        else:
            raise TypeError("Requires processEventType value")

    def validate_processEventType(self, value):
        # Validate type processEventType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['upload']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on processEventType' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False

    def _hasContent(self):
        if (
                super(processEvent, self)._hasContent()
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='processEvent', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('processEvent')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'processEvent':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='processEvent')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='processEvent',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='processEvent'):
        super(processEvent, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_,
                                                    name_='processEvent')
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(
                ' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')),))

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='processEvent',
                        fromsubclass_=False, pretty_print=True):
        super(processEvent, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True,
                                                  pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.validate_processEventType(self.type_)  # validate type processEventType
        super(processEvent, self)._buildAttributes(node, attrs, already_processed)

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(processEvent, self)._buildChildren(child_, node, nodeName_, True)
        pass


# end class processEvent


class actions(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'phase': MemberSpec_('phase', 'eventPhaseType', 0, 0, {'use': 'required', 'name': 'phase'}),
        'action': MemberSpec_('action', 'action', 1, 1,
                              {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'action', 'type': 'action'}, None),
        'actionRef': MemberSpec_('actionRef', 'actionRef', 1, 1,
                                 {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'actionRef', 'type': 'actionRef'},
                                 None),
    }
    subclass = None
    superclass = None

    def __init__(self, phase=None, action=None, actionRef=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.phase = _cast(None, phase)
        self.phase_nsprefix_ = None
        if action is None:
            self.action = []
        else:
            self.action = action
        self.action_nsprefix_ = None
        if actionRef is None:
            self.actionRef = []
        else:
            self.actionRef = actionRef
        self.actionRef_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, actions)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if actions.subclass:
            return actions.subclass(*args_, **kwargs_)
        else:
            return actions(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_action(self):
        return self.action

    def set_action(self, action_):
        if all(isinstance(x, action) for x in action_):
            self.action = action_
        else:
            raise TypeError("Requires only action values inside an array")

    def add_action(self, value):
        if type(value) is action:
            self.action.append(value)
        else:
            raise TypeError("Requires action value")

    def insert_action_at(self, index, value):
        if 0 <= index <= len(self.action):
            if type(value) is action:
                self.action.insert(index, value)
            else:
                raise TypeError("Requires action value")
        else:
            raise IndexError("Invalid index value")

    def replace_action_at(self, index, value):
        if 0 <= index < len(self.action):
            if self.action[index]:
                if type(value) is action:
                    self.action[index] = value
                else:
                    raise TypeError("Requires action value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_actionRef(self):
        return self.actionRef

    def set_actionRef(self, actionRef_):
        if all(isinstance(x, actionRef) for x in actionRef_):
            self.actionRef = actionRef_
        else:
            raise TypeError("Requires only actionRef values inside an array")

    def add_actionRef(self, value):
        if type(value) is actionRef:
            self.actionRef.append(value)
        else:
            raise TypeError("Requires actionRef value")

    def insert_actionRef_at(self, index, value):
        if 0 <= index <= len(self.actionRef):
            if type(value) is actionRef:
                self.actionRef.insert(index, value)
            else:
                raise TypeError("Requires actionRef value")
        else:
            raise IndexError("Invalid index value")

    def replace_actionRef_at(self, index, value):
        if 0 <= index < len(self.actionRef):
            if self.actionRef[index]:
                if type(value) is actionRef:
                    self.actionRef[index] = value
                else:
                    raise TypeError("Requires actionRef value")
            else:
                raise Exception("Invalid index value")
        else:
            raise IndexError("Index out of range")

    def get_phase(self):
        return self.phase

    def set_phase(self, phase):
        if type(phase) is eventPhaseType:
            self.phase = phase
        else:
            raise TypeError("Requires eventPhaseType value")

    def validate_eventPhaseType(self, value):
        # Validate type eventPhaseType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['pre', 'post']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on eventPhaseType' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False

    def _hasContent(self):
        if (
                self.action or
                self.actionRef
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='actions', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('actions')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'actions':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='actions')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='actions',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='actions'):
        if self.phase is not None and 'phase' not in already_processed:
            already_processed.add('phase')
            outfile.write(
                ' phase=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.phase), input_name='phase')),))

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='actions',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for action_ in self.action:
            namespaceprefix_ = self.action_nsprefix_ + ':' if (UseCapturedNS_ and self.action_nsprefix_) else ''
            action_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='action',
                           pretty_print=pretty_print)
        for actionRef_ in self.actionRef:
            namespaceprefix_ = self.actionRef_nsprefix_ + ':' if (UseCapturedNS_ and self.actionRef_nsprefix_) else ''
            actionRef_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='actionRef',
                              pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('phase', node)
        if value is not None and 'phase' not in already_processed:
            already_processed.add('phase')
            self.phase = value
            self.validate_eventPhaseType(self.phase)  # validate type eventPhaseType

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'action':
            obj_ = action.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.action.append(obj_)
            obj_.original_tagname_ = 'action'
        elif nodeName_ == 'actionRef':
            obj_ = actionRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.actionRef.append(obj_)
            obj_.original_tagname_ = 'actionRef'


# end class actions


class actionRef(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'id': MemberSpec_('id', 'xs:string', 0, 0, {'name': 'id', 'type': 'xs:string'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, id=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = id
        self.id_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, actionRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if actionRef.subclass:
            return actionRef.subclass(*args_, **kwargs_)
        else:
            return actionRef(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_id(self):
        return self.id

    def set_id(self, id_):
        if type(id_) is str:
            self.id = id_
        else:
            raise TypeError("Requires str value")

    def _hasContent(self):
        if (
                self.id is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='actionRef', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('actionRef')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'actionRef':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='actionRef')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='actionRef',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='actionRef'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='actionRef',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.id is not None:
            namespaceprefix_ = self.id_nsprefix_ + ':' if (UseCapturedNS_ and self.id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sid>%s</%sid>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.id), input_name='id')),
                namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'id')
            value_ = self.gds_validate_string(value_, node, 'id')
            self.id = value_
            self.id_nsprefix_ = child_.prefix


# end class actionRef


class fieldView(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'area': MemberSpec_('area', 'xs:string', 0, 0, {'name': 'area', 'type': 'xs:string'}, 14),
        'autocomplete': MemberSpec_('autocomplete', 'xs:string', 0, 0, {'name': 'autocomplete', 'type': 'xs:string'},
                                    14),
        'tree': MemberSpec_('tree', 'xs:string', 0, 0, {'name': 'tree', 'type': 'xs:string'}, 14),
        'table': MemberSpec_('table', 'xs:string', 0, 0, {'name': 'table', 'type': 'xs:string'}, 14),
        'image': MemberSpec_('image', 'booleanImageView', 0, 0, {'name': 'image', 'type': 'booleanImageView'}, 14),
        'editor': MemberSpec_('editor', 'xs:string', 0, 0, {'name': 'editor', 'type': 'xs:string'}, 14),
        'htmlEditor': MemberSpec_('htmlEditor', 'xs:string', 0, 0, {'name': 'htmlEditor', 'type': 'xs:string'}, 14),
        'buttonType': MemberSpec_('buttonType', ['buttonTypeType', 'xs:string'], 0, 0,
                                  {'name': 'buttonType', 'type': 'xs:string'}, 14),
        'list': MemberSpec_('list', ['listType', 'xs:int'], 0, 0, {'name': 'list', 'type': 'xs:int'}, 14),
    }
    subclass = None
    superclass = None

    def __init__(self, area=None, autocomplete=None, tree=None, table=None, image=None, editor=None, htmlEditor=None,
                 buttonType=None, list=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.area = area
        self.area_nsprefix_ = None
        self.autocomplete = autocomplete
        self.autocomplete_nsprefix_ = None
        self.tree = tree
        self.tree_nsprefix_ = None
        self.table = table
        self.table_nsprefix_ = None
        self.image = image
        self.image_nsprefix_ = None
        self.editor = editor
        self.editor_nsprefix_ = None
        self.htmlEditor = htmlEditor
        self.htmlEditor_nsprefix_ = None
        self.buttonType = buttonType
        self.validate_buttonTypeType(self.buttonType)
        self.buttonType_nsprefix_ = None
        self.list = list
        self.validate_listType(self.list)
        self.list_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, fieldView)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if fieldView.subclass:
            return fieldView.subclass(*args_, **kwargs_)
        else:
            return fieldView(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_area(self):
        return self.area

    def set_area(self, area):
        if self.autocomplete is None and self.tree is None and self.table is None and self.image is None \
                and self.editor is None and self.htmlEditor is None and self.buttonType is None and self.list is None:
            if type(area) is str:
                self.area = area
            else:
                raise TypeError("Requires str value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains other fieldView elements.")

    def get_autocomplete(self):
        return self.autocomplete

    def set_autocomplete(self, autocomplete):
        if self.area is None and self.tree is None and self.table is None and self.image is None \
                and self.editor is None and self.htmlEditor is None and self.buttonType is None and self.list is None:
            if type(autocomplete) is str:
                self.autocomplete = autocomplete
            else:
                raise TypeError("Requires str value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains other fieldView elements.")

    def get_tree(self):
        return self.tree

    def set_tree(self, tree):
        if self.area is None and self.autocomplete is None and self.table is None and self.image is None \
                and self.editor is None and self.htmlEditor is None and self.buttonType is None and self.list is None:
            if type(tree) is str:
                self.tree = tree
            else:
                raise TypeError("Requires str value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains other fieldView elements.")

    def get_table(self):
        return self.table

    def set_table(self, table):
        if self.area is None and self.tree is None and self.autocomplete is None and self.image is None \
                and self.editor is None and self.htmlEditor is None and self.buttonType is None and self.list is None:
            if type(table) is str:
                self.table = table
            else:
                raise TypeError("Requires str value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains other fieldView elements.")

    def get_image(self):
        return self.image

    def set_image(self, image):
        if self.area is None and self.tree is None and self.table is None and self.autocomplete is None \
                and self.editor is None and self.htmlEditor is None and self.buttonType is None and self.list is None:
            if type(image) is booleanImageView:
                self.image = image
            else:
                raise TypeError("Requires booleanImageView value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains other fieldView elements.")

    def get_editor(self):
        return self.editor

    def set_editor(self, editor_):
        if self.area is None and self.tree is None and self.table is None and self.image is None \
                and self.autocomplete is None and self.htmlEditor is None and self.buttonType is None \
                and self.list is None:
            self.editor = editor_
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains other fieldView elements.")

    def get_htmlEditor(self):
        return self.htmlEditor

    def set_htmlEditor(self, htmlEditor_):
        if self.area is None and self.tree is None and self.table is None and self.image is None \
                and self.autocomplete is None and self.editor is None and self.buttonType is None \
                and self.list is None:
            self.htmlEditor = htmlEditor_
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains other fieldView elements.")

    def get_buttonType(self):
        return self.buttonType

    def set_buttonType(self, buttonType_):
        if self.area is None and self.tree is None and self.table is None and self.image is None \
                and self.autocomplete is None and self.htmlEditor is None and self.editor is None \
                and self.list is None:
            if type(buttonType_) is buttonTypeType:
                self.buttonType = buttonType_
            else:
                raise TypeError("Requires eventPhaseType value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains other fieldView elements.")

    def get_list(self):
        return self.list

    def set_list(self, list_):
        if self.area is None and self.tree is None and self.table is None and self.image is None \
                and self.autocomplete is None and self.htmlEditor is None and self.buttonType is None \
                and self.editor is None:
            if type(list_) is str and len(list_) == 0:
                self.list = list_
            elif type(list_) is int:
                self.list = list_
            else:
                raise TypeError("Requires str value with length of 0 , or int value")
        else:
            raise ValueError("XML Schema choice element allows only one of the elements contained "
                                    "in the <choice> \n declaration to be present within the containing element. "
                                    "The document probably already contains other fieldView elements.")

    def validate_buttonTypeType(self, value):
        result = True
        # Validate type buttonTypeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['standard', 'raised', 'stroked', 'flat', 'icon', 'fab', 'minifab']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on buttonTypeType' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False
        return result

    def validate_listType(self, value):
        result = True
        # Validate type listType, a restriction on xs:int.
        pass
        return result

    def _hasContent(self):
        if (
                self.area is not None or
                self.autocomplete is not None or
                self.tree is not None or
                self.table is not None or
                self.image is not None or
                self.editor is not None or
                self.htmlEditor is not None or
                self.buttonType is not None or
                self.list is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='fieldView', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('fieldView')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'fieldView':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='fieldView')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='fieldView',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='fieldView'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='fieldView',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.area is not None:
            namespaceprefix_ = self.area_nsprefix_ + ':' if (UseCapturedNS_ and self.area_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sarea>%s</%sarea>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.area), input_name='area')),
                namespaceprefix_, eol_))
        if self.autocomplete is not None:
            namespaceprefix_ = self.autocomplete_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.autocomplete_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sautocomplete>%s</%sautocomplete>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.autocomplete), input_name='autocomplete')), namespaceprefix_,
                                                                     eol_))
        if self.tree is not None:
            namespaceprefix_ = self.tree_nsprefix_ + ':' if (UseCapturedNS_ and self.tree_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stree>%s</%stree>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.tree), input_name='tree')),
                namespaceprefix_, eol_))
        if self.table is not None:
            namespaceprefix_ = self.table_nsprefix_ + ':' if (UseCapturedNS_ and self.table_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stable>%s</%stable>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.table), input_name='table')),
                namespaceprefix_, eol_))
        if self.image is not None:
            namespaceprefix_ = self.image_nsprefix_ + ':' if (UseCapturedNS_ and self.image_nsprefix_) else ''
            self.image.export(outfile, level, namespaceprefix_, namespacedef_='', name_='image',
                              pretty_print=pretty_print)
        if self.editor is not None:
            namespaceprefix_ = self.editor_nsprefix_ + ':' if (UseCapturedNS_ and self.editor_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%seditor>%s</%seditor>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.editor), input_name='editor')),
                namespaceprefix_, eol_))
        if self.htmlEditor is not None:
            namespaceprefix_ = self.htmlEditor_nsprefix_ + ':' if (UseCapturedNS_ and self.htmlEditor_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%shtmlEditor>%s</%shtmlEditor>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.htmlEditor), input_name='htmlEditor')), namespaceprefix_, eol_))
        if self.buttonType is not None:
            namespaceprefix_ = self.buttonType_nsprefix_ + ':' if (UseCapturedNS_ and self.buttonType_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbuttonType>%s</%sbuttonType>%s' % (namespaceprefix_, self.gds_encode(
                self.gds_format_string(quote_xml(self.buttonType), input_name='buttonType')), namespaceprefix_, eol_))
        if self.list is not None:
            namespaceprefix_ = self.list_nsprefix_ + ':' if (UseCapturedNS_ and self.list_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slist>%s</%slist>%s' % (
                namespaceprefix_, self.gds_format_integer(self.list, input_name='list'), namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'area':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'area')
            value_ = self.gds_validate_string(value_, node, 'area')
            self.area = value_
            self.area_nsprefix_ = child_.prefix
        elif nodeName_ == 'autocomplete':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'autocomplete')
            value_ = self.gds_validate_string(value_, node, 'autocomplete')
            self.autocomplete = value_
            self.autocomplete_nsprefix_ = child_.prefix
        elif nodeName_ == 'tree':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'tree')
            value_ = self.gds_validate_string(value_, node, 'tree')
            self.tree = value_
            self.tree_nsprefix_ = child_.prefix
        elif nodeName_ == 'table':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'table')
            value_ = self.gds_validate_string(value_, node, 'table')
            self.table = value_
            self.table_nsprefix_ = child_.prefix
        elif nodeName_ == 'image':
            obj_ = booleanImageView.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.image = obj_
            obj_.original_tagname_ = 'image'
        elif nodeName_ == 'editor':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'editor')
            value_ = self.gds_validate_string(value_, node, 'editor')
            self.editor = value_
            self.editor_nsprefix_ = child_.prefix
        elif nodeName_ == 'htmlEditor':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'htmlEditor')
            value_ = self.gds_validate_string(value_, node, 'htmlEditor')
            self.htmlEditor = value_
            self.htmlEditor_nsprefix_ = child_.prefix
        elif nodeName_ == 'buttonType':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'buttonType')
            value_ = self.gds_validate_string(value_, node, 'buttonType')
            self.buttonType = value_
            self.buttonType_nsprefix_ = child_.prefix
            # validate type buttonTypeType
            self.validate_buttonTypeType(self.buttonType)
        elif nodeName_ == 'list' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'list')
            ival_ = self.gds_validate_integer(ival_, node, 'list')
            self.list = ival_
            self.list_nsprefix_ = child_.prefix
            # validate type listType
            self.validate_listType(self.list)


# end class fieldView


class editor(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {}
    subclass = None
    superclass = None

    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, editor)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if editor.subclass:
            return editor.subclass(*args_, **kwargs_)
        else:
            return editor(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='editor', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('editor')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'editor':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='editor')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='editor',
                                 pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='editor'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='editor',
                        fromsubclass_=False, pretty_print=True):
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass


# end class editor


class htmlEditor(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {}
    subclass = None
    superclass = None

    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, htmlEditor)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if htmlEditor.subclass:
            return htmlEditor.subclass(*args_, **kwargs_)
        else:
            return htmlEditor(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='htmlEditor', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('htmlEditor')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'htmlEditor':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='htmlEditor')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='htmlEditor',
                                 pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='htmlEditor'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='htmlEditor',
                        fromsubclass_=False, pretty_print=True):
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass


# end class htmlEditor


class booleanImageView(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'true': MemberSpec_('true', 'xs:string', 0, 0, {'name': 'true', 'type': 'xs:string'}, None),
        'false': MemberSpec_('false', 'xs:string', 0, 0, {'name': 'false', 'type': 'xs:string'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, true=None, false=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.true = true
        self.true_nsprefix_ = None
        self.false = false
        self.false_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, booleanImageView)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if booleanImageView.subclass:
            return booleanImageView.subclass(*args_, **kwargs_)
        else:
            return booleanImageView(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_true(self):
        return self.true

    def set_true(self, true):
        if type(true) is str:
            self.true = true
        else:
            raise TypeError("Requires str value")

    def get_false(self):
        return self.false

    def set_false(self, false):
        if type(false) is str:
            self.false = false
        else:
            raise TypeError("Requires str value")

    def _hasContent(self):
        if (
                self.true is not None or
                self.false is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='booleanImageView',
               pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('booleanImageView')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'booleanImageView':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='booleanImageView')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='booleanImageView',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='booleanImageView'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='booleanImageView',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.true is not None:
            namespaceprefix_ = self.true_nsprefix_ + ':' if (UseCapturedNS_ and self.true_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%strue>%s</%strue>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.true), input_name='true')),
                namespaceprefix_, eol_))
        if self.false is not None:
            namespaceprefix_ = self.false_nsprefix_ + ':' if (UseCapturedNS_ and self.false_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfalse>%s</%sfalse>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.false), input_name='false')),
                namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'true':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'true')
            value_ = self.gds_validate_string(value_, node, 'true')
            self.true = value_
            self.true_nsprefix_ = child_.prefix
        elif nodeName_ == 'false':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'false')
            value_ = self.gds_validate_string(value_, node, 'false')
            self.false = value_
            self.false_nsprefix_ = child_.prefix


# end class booleanImageView


class format(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'currency': MemberSpec_('currency', 'currency', 0, 0, {'name': 'currency', 'type': 'currency'}, 15),
    }
    subclass = None
    superclass = None

    def __init__(self, currency=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.currency = currency
        self.currency_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, format)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if format.subclass:
            return format.subclass(*args_, **kwargs_)
        else:
            return format(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_currency(self):
        return self.currency

    def set_currency(self, currency_):
        if type(currency_) is currency:
            self.currency = currency_
        else:
            raise TypeError("Requires currency value")

    def _hasContent(self):
        if (
                self.currency is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='format', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('format')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'format':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='format')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='format',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='format'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='format',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.currency is not None:
            namespaceprefix_ = self.currency_nsprefix_ + ':' if (UseCapturedNS_ and self.currency_nsprefix_) else ''
            self.currency.export(outfile, level, namespaceprefix_, namespacedef_='', name_='currency',
                                 pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'currency':
            obj_ = currency.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.currency = obj_
            obj_.original_tagname_ = 'currency'


# end class format


class currency(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', 'xs:string', 0, 0, {'default': 'EUR', 'name': 'code', 'type': 'xs:string'}, None),
        'fractionSize': MemberSpec_('fractionSize', 'xs:int', 0, 0, {'name': 'fractionSize', 'type': 'xs:int'}, None),
        'locale': MemberSpec_('locale', 'xs:string', 0, 0, {'name': 'locale', 'type': 'xs:string'}, None),
    }
    subclass = None
    superclass = None

    def __init__(self, code='EUR', fractionSize=None, locale=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = code
        self.code_nsprefix_ = None
        self.fractionSize = fractionSize
        self.fractionSize_nsprefix_ = None
        self.locale = locale
        self.locale_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, currency)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if currency.subclass:
            return currency.subclass(*args_, **kwargs_)
        else:
            return currency(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_code(self):
        return self.code

    def set_code(self, code):
        if type(code) is str:
            self.code = code
        else:
            raise TypeError("Requires str value")

    def get_fractionSize(self):
        return self.fractionSize

    def set_fractionSize(self, fractionSize):
        if type(fractionSize) is int:
            self.fractionSize = fractionSize
        else:
            raise TypeError("Requires int value")

    def get_locale(self):
        return self.locale

    def set_locale(self, locale):
        if type(locale) is str:
            self.locale = locale
        else:
            raise TypeError("Requires str value")

    def _hasContent(self):
        if (
                self.code != "EUR" or
                self.fractionSize is not None or
                self.locale is not None
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='currency', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('currency')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'currency':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='currency')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='currency',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='currency'):
        pass

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='currency',
                        fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            namespaceprefix_ = self.code_nsprefix_ + ':' if (UseCapturedNS_ and self.code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scode>%s</%scode>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.code), input_name='code')),
                namespaceprefix_, eol_))
        if self.code is None:
            namespaceprefix_ = self.code_nsprefix_ + ':' if (UseCapturedNS_ and self.code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scode>EUR</%scode/>%s' % (namespaceprefix_, namespaceprefix_, eol_))
        if self.fractionSize is not None:
            namespaceprefix_ = self.fractionSize_nsprefix_ + ':' if (
                    UseCapturedNS_ and self.fractionSize_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfractionSize>%s</%sfractionSize>%s' % (
                namespaceprefix_, self.gds_format_integer(self.fractionSize, input_name='fractionSize'),
                namespaceprefix_,
                eol_))
        if self.locale is not None:
            namespaceprefix_ = self.locale_nsprefix_ + ':' if (UseCapturedNS_ and self.locale_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slocale>%s</%slocale>%s' % (
                namespaceprefix_, self.gds_encode(self.gds_format_string(quote_xml(self.locale), input_name='locale')),
                namespaceprefix_, eol_))

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
        elif nodeName_ == 'fractionSize' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'fractionSize')
            ival_ = self.gds_validate_integer(ival_, node, 'fractionSize')
            self.fractionSize = ival_
            self.fractionSize_nsprefix_ = child_.prefix
        elif nodeName_ == 'locale':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'locale')
            value_ = self.gds_validate_string(value_, node, 'locale')
            self.locale = value_
            self.locale_nsprefix_ = child_.prefix


# end class currency


class event(baseEvent):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'type_': MemberSpec_('type_', 'eventType', 0, 0, {'use': 'required', 'name': 'type_'}),
        'title': MemberSpec_('title', 'i18nStringType', 0, 1,
                             {'minOccurs': '0', 'name': 'title', 'type': 'i18nStringType'}, None),
    }
    subclass = None
    superclass = baseEvent

    def __init__(self, id=None, actions=None, message=None, type_=None, title=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("event"), self).__init__(id, actions, message, **kwargs_)
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
        self.title = title
        self.title_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, event)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if event.subclass:
            return event.subclass(*args_, **kwargs_)
        else:
            return event(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_title(self):
        return self.title

    def set_title(self, title):
        if type(title) is i18nStringType:
            self.title = title
        else:
            raise TypeError("Requires i18nStringType value")

    def get_type(self):
        return self.type_

    def set_type_(self, type_):
        if type(type_) is eventType:
            self.type_ = type_
        else:
            raise TypeError("Requires eventType value")

    def validate_eventType(self, value):
        # Validate type eventType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value,
                                                                                                  "lineno": lineno, })
                return False
            value = value
            enumerations = ['assign', 'cancel', 'finish', 'delegate']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on eventType' % {
                        "value": encode_str_2_3(value), "lineno": lineno})
                result = False

    def _hasContent(self):
        if (
                self.title is not None or
                super(event, self)._hasContent()
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='event', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('event')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'event':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='event')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='event',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='event'):
        super(event, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='event')
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(
                ' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')),))

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='event', fromsubclass_=False,
                        pretty_print=True):
        super(event, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True,
                                           pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.title is not None:
            namespaceprefix_ = self.title_nsprefix_ + ':' if (UseCapturedNS_ and self.title_nsprefix_) else ''
            self.title.export(outfile, level, namespaceprefix_, namespacedef_='', name_='title',
                              pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.validate_eventType(self.type_)  # validate type eventType
        super(event, self)._buildAttributes(node, attrs, already_processed)

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'title':
            class_obj_ = self.get_class_obj_(child_, i18nStringType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.title = obj_
            obj_.original_tagname_ = 'title'
        super(event, self)._buildChildren(child_, node, nodeName_, True)


# end class event


class init(i18nStringTypeWithExpression):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'valueOf_': MemberSpec_('valueOf_', 'i18nStringTypeWithExpression', 0),
    }
    subclass = None
    superclass = i18nStringTypeWithExpression

    def __init__(self, name=None, dynamic=False, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("init"), self).__init__(name, dynamic, valueOf_, **kwargs_)
        self.valueOf_ = valueOf_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, init)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if init.subclass:
            return init.subclass(*args_, **kwargs_)
        else:
            return init(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_valueOf_(self):
        return self.valueOf_

    def set_valueOf_(self, valueOf_):
        if type(valueOf_) is str:
            self.valueOf_ = valueOf_
        else:
            raise TypeError("Requires str value")

    def _hasContent(self):
        if (
                (1 if type(self.valueOf_) in [int, float] else self.valueOf_) or
                super(init, self)._hasContent()
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='init', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('init')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'init':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='init')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='init',
                                 pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='init'):
        super(init, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='init')

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='init', fromsubclass_=False,
                        pretty_print=True):
        super(init, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True,
                                          pretty_print=pretty_print)
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        super(init, self)._buildAttributes(node, attrs, already_processed)

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass


# end class init


class caseUserRef(casePermissionRef):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {}
    subclass = None
    superclass = casePermissionRef

    def __init__(self, id=None, caseLogic=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("caseUserRef"), self).__init__(id, caseLogic, **kwargs_)

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, caseUserRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if caseUserRef.subclass:
            return caseUserRef.subclass(*args_, **kwargs_)
        else:
            return caseUserRef(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def _hasContent(self):
        if (
                super(caseUserRef, self)._hasContent()
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='caseUserRef', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('caseUserRef')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'caseUserRef':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='caseUserRef')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='caseUserRef',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='caseUserRef'):
        super(caseUserRef, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_,
                                                   name_='caseUserRef')

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='caseUserRef',
                        fromsubclass_=False, pretty_print=True):
        super(caseUserRef, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True,
                                                 pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        super(caseUserRef, self)._buildAttributes(node, attrs, already_processed)

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(caseUserRef, self)._buildChildren(child_, node, nodeName_, True)
        pass


# end class caseUserRef


class caseRoleRef(casePermissionRef):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {}
    subclass = None
    superclass = casePermissionRef

    def __init__(self, id=None, caseLogic=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("caseRoleRef"), self).__init__(id, caseLogic, **kwargs_)

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, caseRoleRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if caseRoleRef.subclass:
            return caseRoleRef.subclass(*args_, **kwargs_)
        else:
            return caseRoleRef(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def _hasContent(self):
        if (
                super(caseRoleRef, self)._hasContent()
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='caseRoleRef', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('caseRoleRef')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'caseRoleRef':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='caseRoleRef')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='caseRoleRef',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='caseRoleRef'):
        super(caseRoleRef, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_,
                                                   name_='caseRoleRef')

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='caseRoleRef',
                        fromsubclass_=False, pretty_print=True):
        super(caseRoleRef, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True,
                                                 pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        super(caseRoleRef, self)._buildAttributes(node, attrs, already_processed)

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(caseRoleRef, self)._buildChildren(child_, node, nodeName_, True)
        pass


# end class caseRoleRef


class userRef(permissionRef):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {}
    subclass = None
    superclass = permissionRef

    def __init__(self, id=None, logic=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("userRef"), self).__init__(id, logic, **kwargs_)

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, userRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if userRef.subclass:
            return userRef.subclass(*args_, **kwargs_)
        else:
            return userRef(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def _hasContent(self):
        if (
                super(userRef, self)._hasContent()
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='userRef', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('userRef')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'userRef':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='userRef')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='userRef',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='userRef'):
        super(userRef, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='userRef')

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='userRef',
                        fromsubclass_=False, pretty_print=True):
        super(userRef, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True,
                                             pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        super(userRef, self)._buildAttributes(node, attrs, already_processed)

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(userRef, self)._buildChildren(child_, node, nodeName_, True)
        pass


# end class userRef


class roleRef(permissionRef):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {}
    subclass = None
    superclass = permissionRef

    def __init__(self, id=None, logic=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("roleRef"), self).__init__(id, logic, **kwargs_)

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, roleRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if roleRef.subclass:
            return roleRef.subclass(*args_, **kwargs_)
        else:
            return roleRef(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def _hasContent(self):
        if (
                super(roleRef, self)._hasContent()
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='roleRef', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('roleRef')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'roleRef':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='roleRef')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='roleRef',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='roleRef'):
        super(roleRef, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='roleRef')

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='roleRef',
                        fromsubclass_=False, pretty_print=True):
        super(roleRef, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True,
                                             pretty_print=pretty_print)

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        super(roleRef, self)._buildAttributes(node, attrs, already_processed)

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(roleRef, self)._buildChildren(child_, node, nodeName_, True)
        pass


# end class roleRef


class option(i18nStringType):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'key': MemberSpec_('key', 'xs:string', 0, 0, {'use': 'required', 'name': 'key'}),
        'valueOf_': MemberSpec_('valueOf_', 'i18nStringType', 0),
    }
    subclass = None
    superclass = i18nStringType

    def __init__(self, name=None, key=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("option"), self).__init__(name, valueOf_, **kwargs_)
        self.key = _cast(None, key)
        self.key_nsprefix_ = None
        self.valueOf_ = valueOf_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, option)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if option.subclass:
            return option.subclass(*args_, **kwargs_)
        else:
            return option(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_key(self):
        return self.key

    def set_key(self, key, doc):
        if type(key) is str:
            if all(data_.options and key != option_.key for data_ in doc.data if data_.options is not None for option_
                   in data_.options.option):
                self.key = key
            else:
                raise ValueError("Requires unique key value")
        else:
            raise TypeError("Requires str value")

    def get_valueOf_(self):
        return self.valueOf_

    def set_valueOf_(self, valueOf_):
        if type(valueOf_) is str:
            self.valueOf_ = valueOf_
        else:
            raise TypeError("Requires str value")

    def _hasContent(self):
        if (
                (1 if type(self.valueOf_) in [int, float] else self.valueOf_) or
                super(option, self)._hasContent()
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='option', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('option')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'option':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='option')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='option',
                                 pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='option'):
        super(option, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='option')
        if self.key is not None and 'key' not in already_processed:
            already_processed.add('key')
            outfile.write(
                ' key=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.key), input_name='key')),))

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='option',
                        fromsubclass_=False, pretty_print=True):
        super(option, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True,
                                            pretty_print=pretty_print)
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('key', node)
        if value is not None and 'key' not in already_processed:
            already_processed.add('key')
            self.key = value
        super(option, self)._buildAttributes(node, attrs, already_processed)

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass


# end class option


class valid(expression):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'valueOf_': MemberSpec_('valueOf_', 'expression', 0),
    }
    subclass = None
    superclass = expression

    def __init__(self, dynamic=False, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("valid"), self).__init__(dynamic, valueOf_, **kwargs_)
        self.valueOf_ = valueOf_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, valid)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if valid.subclass:
            return valid.subclass(*args_, **kwargs_)
        else:
            return valid(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_valueOf_(self):
        return self.valueOf_

    def set_valueOf_(self, valueOf_):
        if type(valueOf_) is str:
            self.valueOf_ = valueOf_
        else:
            raise TypeError("Requires str value")

    def _hasContent(self):
        if (
                (1 if type(self.valueOf_) in [int, float] else self.valueOf_) or
                super(valid, self)._hasContent()
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='valid', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('valid')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'valid':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='valid')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='valid',
                                 pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='valid'):
        super(valid, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='valid')

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='valid', fromsubclass_=False,
                        pretty_print=True):
        super(valid, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True,
                                           pretty_print=pretty_print)
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        super(valid, self)._buildAttributes(node, attrs, already_processed)

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass


# end class valid


class document(documentType):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {}
    subclass = None
    superclass = documentType

    def __init__(self, id=None, version=None, initials=None, title=None, icon=None, defaultRole=None,
                 anonymousRole=None, transitionRole=None, caseName=None, roleRef=None, usersRef=None, userRef=None,
                 processEvents=None, caseEvents=None, transaction=None, role=None, function=None, data=None,
                 mapping=None, i18n=None, transition=None, place=None, arc=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("document"), self).__init__(id, version, initials, title, icon, defaultRole, anonymousRole,
                                                        transitionRole, caseName, roleRef, usersRef, userRef,
                                                        processEvents, caseEvents, transaction, role, function, data,
                                                        mapping, i18n, transition, place, arc, **kwargs_)

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, document)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if document.subclass:
            return document.subclass(*args_, **kwargs_)
        else:
            return document(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def _hasContent(self):
        if (
                super(document, self)._hasContent()
        ):
            return True
        else:
            return False

    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='document', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('document')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'document':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '',))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='document')
        if self._hasContent():
            outfile.write('>%s' % (eol_,))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='document',
                                 pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_,))

    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='document'):
        super(document, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='document')

    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='document',
                        fromsubclass_=False, pretty_print=True):
        super(document, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True,
                                              pretty_print=pretty_print)

    def build(self, node):  # , gds_collector_=None
        # self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_)  # , gds_collector_=gds_collector_
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        super(document, self)._buildAttributes(node, attrs, already_processed)

    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(document, self)._buildChildren(child_, node, nodeName_, True)
        pass


# end class document


GDSClassesMapping = {
}

USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    """
    Function takes the node of the root element
    :param node: node representing the root element of this tree.
    :return: a tag and a class that represents the node of the root element.
    """
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    prefix_tag = TagNamePrefix + tag
    root_class = GDSClassesMapping.get(prefix_tag)
    if root_class is None:
        root_class = globals().get(prefix_tag)
    return tag, root_class

def get_required_ns_prefix_defs(root_node):
    """
    Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    :param root_node:
    :return:
    """
    nsmap = {
        prefix: uri
        for node in root_node.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs

def validate_doc(element_tree):
    """
    The function first finds and sets the xml schema, then validates the xml document based on it, and
    if it is not valid, it prints an error and ends the program.
    :param element_tree: loaded xml document
    :return:
    """
    # get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # build a relative path to the XSD schema file from the script directory
    xsd_path = os.path.join(script_dir, '..', 'resources', 'petriflow.schema.xsd')
    # use the relative path to load the XSD schema file
    xml_schema_doc = etree_.parse(xsd_path)

    xml_schema = etree_.XMLSchema(xml_schema_doc)

    valid_status = xml_schema.validate(element_tree)

    if not valid_status:
        sys.stdout.write('*** Something went wrong ***\n')
        # it catches the error, prints it, and ends the program
        print(xml_schema.assertValid(element_tree))
        exit(1)


def import_xml(in_filename, silence=True):
    """
    Reads the xml document from the path and, if it exists and is valid, returns the object of the document element.
    :param in_filename: path to the xml document
    :param silence: boolean attribute, if it is False, it will write the structure of the document to the output
    terminal after successful loading
    :return:
    """
    doc = parse_xml_(in_filename)  # ElementTree
    validate_doc(doc)
    root_node = doc.getroot()
    root_tag, root_class = get_root_tag(root_node)
    set_namespace_defs(root_node, root_tag)
    if root_class is None:
        root_tag = 'document'
        root_class = document
    root_class_obj = root_class.factory()
    root_class_obj.build(root_node)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        root_node = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        root_class_obj.export(
            sys.stdout, 0, name_=root_tag,
            namespacedef_='',
            pretty_print=True)
    sys.stdout.write('*** XML document has been imported ***\n')
    return root_class_obj


def export_xml(out_filename, save_in_folder):
    """
    Using the export() function creates an ElementTree for the root element and writes the entire ElementTree
    to the specified location.
    :param out_filename: object to the element of the document that we want to export
    :param save_in_folder: path to the place where the document will be stored
    :return:
    """
    # print(type(out_filename))
    # print(out_filename.gds_elementtree_node_)
    # doc = etree_.ElementTree(out_filename.gds_elementtree_node_)

    # xml_string = etree_.tostring(out_filename)
    # xml_string = etree_.tostring(out_filename.gds_elementtree_node_)
    # doc = parse_xml_string_(xml_string, None)
    # validate_doc(etree_.ElementTree(out_filename.gds_elementtree_node_))
    new_file = open(save_in_folder, "w", encoding="utf-8")
    out_filename.export(new_file, 0)
    sys.stdout.write('*** XML document has been exported ***\n')
    return new_file


def import_string(in_string, silence=True):
    """
    Reads the xml document from the URL, returns a string which is then parsed and, if it exists and is valid,
    returns the object of the document element.
    :param in_string: path to the xml document
    :param silence: boolean attribute, if it is False, it will write the structure of the document to the output
    terminal after successful loading
    :return:
    """
    in_string = urlopen(in_string).read()  # z url navratova hodnota xmlka nie je xml ale str
    parser = None
    root_node = parse_xml_string_(in_string, parser)
    validate_doc(root_node.getroottree())
    root_tag, root_class = get_root_tag(root_node)
    set_namespace_defs(root_node, root_tag)
    if root_class is None:
        root_tag = 'document'
        root_class = document
    root_obj = root_class.factory()
    root_obj.build(root_node)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        root_node = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        root_obj.export(
            sys.stdout, 0, name_=root_tag,
            namespacedef_='')
    sys.stdout.write('*** XML document has been imported ***\n')
    return root_obj


def parse_etree(inFileName, silence=False, print_warnings=True,
               mapping=None, reverse_mapping=None, nsmap=None):
    parser = None
    doc = parse_xml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'transaction'
        rootClass = transaction
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if mapping is None:
        mapping = {}
    if reverse_mapping is None:
        reverse_mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping,
        reverse_mapping_=reverse_mapping, nsmap_=nsmap)
    reverse_node_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_node_mapping


def parse_literal(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parse_xml_(inFileName, parser)
    # gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'transaction'
        rootClass = transaction
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    # if not SaveElementTreeNode:
    #     doc = None
    #     rootNode = None
    doc = None
    if not silence:
        sys.stdout.write('#from xml_classes import *\n\n')
        sys.stdout.write('import xml_classes as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    # if print_warnings and len(gds_collector.get_messages()) > 0:
    #     separator = ('-' * 50) + '\n'
    #     sys.stderr.write(separator)
    #     sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
    #         len(gds_collector.get_messages()), ))
    #     gds_collector.write_messages(sys.stderr)
    #     sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        import_xml(args[0])
    else:
        usage()


if __name__ == '__main__':
    # import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {}

__all__ = [
    "action",
    "actionRef",
    "actions",
    "allowedNets",
    "appearance",
    "arc",
    "arc_type",
    "assignPolicy",
    "assignedUser",
    "baseEvent",
    "behavior",
    "booleanImageView",
    "breakpoint",
    "buttonTypeType",
    "caseEvent",
    "caseEvents",
    "caseEventType",
    "caseLogic",
    "casePermissionRef",
    "caseRoleRef",
    "caseUserRef",
    "compactDirection",
    "component",
    "currency",
    "data",
    "dataEvent",
    "dataEventType",
    "dataFocusPolicy",
    "dataGroup",
    "dataGroupAlignment",
    "dataRef",
    "data_type",
    "document",
    "documentRef",
    "documentType",
    "editor",
    "encryption",
    "event",
    "eventPhaseType",
    "eventType",
    "export_xml",
    "expression",
    "fieldAlignment",
    "fieldView",
    "finishPolicy",
    "format",
    "function",
    "hideEmptyRows",
    "htmlEditor",
    "i18n",
    "i18nStringType",
    "i18nStringTypeWithExpression",
    "icon",
    "iconType",
    "icons",
    "import_string",
    "import_xml",
    "init",
    "inits",
    "layout",
    "layoutType",
    "logic",
    "mapping",
    "option",
    "options",
    "permissionRef",
    "place",
    "processEvent",
    "processEventType",
    "processEvents",
    "properties",
    "property",
    "role",
    "roleRef",
    "scope",
    "template",
    "transaction",
    "transactionRef",
    "transition",
    "transitionLayout",
    "trigger",
    "triggerType",
    "userRef",
    "valid",
    "validation",
    "validations"
]
