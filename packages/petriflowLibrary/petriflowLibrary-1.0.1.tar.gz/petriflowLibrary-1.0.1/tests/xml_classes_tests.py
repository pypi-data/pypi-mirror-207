import datetime
import unittest
import chardet
from lxml import etree
from lxml.etree import XMLSyntaxError
from petriflow import *


class TestDocumentXML(unittest.TestCase):

    def test_document_id_success(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        actual_id = doc.id
        expected_id = "hypouver"
        self.assertEqual(actual_id, expected_id)

    def test_correct_encoding(self):
        with open("../resources/hypouver.xml", 'rb') as f:
            actual_encoding = chardet.detect(f.read())['encoding']
            expected_encoding = "utf-8"
            self.assertEqual(actual_encoding, expected_encoding)

    def test_missing_required_attribute(self):
        with self.assertRaises(etree.DocumentInvalid):
            xml_classes.import_xml("../resources/missing_type_hypouver.xml")

    # testy na unikatne id, na meno, na kluce

    # def assertXmlNamespace(self, node, prefix, uri):
    #     """Asserts `node` declares namespace `uri` using `prefix`.
    #     One can use this method on element node.
    #     """
    #     self.assertIn(prefix, node.nsmap)
    #     self.assertEqual(node.nsmap.get(prefix), uri)

    # def test_validate_doc_according_to_xsd(self):
    #
    #     self.fail()

    # def test_assertXmlDocument(self, data = "../resources/hypouver.xml"):
    #     """Asserts `data` is an XML document and returns it.
    #     Assertion and XML parsing using lxml.
    #     """
    #     # no assertion yet
    #     try:
    #         doc = etree.fromstring(data)
    #     except XMLSyntaxError as e:
    #         raise self.fail('Input is not a valid XML document: %s' % e)
    #
    #     return doc

    def test_data_set_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = '555'
        doc.data[0].set_id('555', doc)
        self.assertEqual(doc.data[0].id, expectation)

    def test_data_set_not_unique_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = '555'
        doc.data[0].set_id('555', doc)
        with self.assertRaises(ValueError):
            doc.data[1].set_id('555', doc)

    def test_data_set_wrong_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.data[0].set_id(555, doc)

    def test_data_set_title(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = i18nStringType()
        expectation.set_valueOf_("Nadpis")
        expectation.set_original_tagname_('title')
        doc.data[0].set_title(expectation)
        self.assertEqual(doc.data[0].title, expectation)

    def test_data_set_wrong_title(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.data[0].set_title("Nadpis")

    def test_data_set_placeholder(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = i18nStringType()
        expectation.set_valueOf_("Symbol")
        expectation.set_original_tagname_('placeholder')
        doc.data[0].set_placeholder(expectation)
        self.assertEqual(doc.data[0].placeholder, expectation)

    def test_data_set_wrong_placeholder(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.data[0].set_placeholder("Symbol")

    def test_data_set_desc(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = i18nStringType()
        expectation.set_valueOf_("Popis")
        expectation.set_original_tagname_('placeholder')
        doc.data[0].set_desc(expectation)
        self.assertEqual(doc.data[0].desc, expectation)

    def test_data_set_wrong_desc(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.data[0].set_desc("Popis")

    def test_data_set_values_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        choice_child = options()
        doc.data[0].set_options(choice_child)
        with self.assertRaises(ValueError):
            my_values = []
            my_val = i18nStringTypeWithExpression()
            my_val.set_valueOf_("Hodnota")
            my_val.set_dynamic(True)
            my_val.set_name('meno')
            my_val.set_original_tagname_('values')
            my_values.append(my_val)
            doc.data[0].set_values(my_values)

    def test_data_set_values(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_val = i18nStringTypeWithExpression()
        my_val.set_valueOf_("Hodnota")
        my_val.set_dynamic(True)
        my_val.set_name('meno')
        my_val.set_original_tagname_('values')
        expectation.append(my_val)
        doc.data[0].set_values(expectation)
        self.assertEqual(doc.data[0].values, expectation)

    def test_data_add_values(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = i18nStringTypeWithExpression()
        expectation.set_valueOf_("Hodnota")
        expectation.set_dynamic(True)
        expectation.set_name("meno")
        expectation.set_original_tagname_('values')
        doc.data[0].add_values(expectation)
        self.assertEqual(doc.data[0].values[0], expectation)

    def test_data_add_wrong_values(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.data[0].add_values(i18nStringType())

    def test_data_insert_values_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        val = i18nStringTypeWithExpression()
        val.set_valueOf_("Hodnota")
        val.set_dynamic(True)
        val.set_name('meno')
        val.set_original_tagname_('values')
        with self.assertRaises(IndexError):
            doc.data[0].insert_values_at(1, val)

    def test_data_set_options_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        my_values = []
        my_val = i18nStringTypeWithExpression()
        my_val.set_valueOf_("Hodnota")
        my_val.set_dynamic(True)
        my_val.set_name('meno')
        my_val.set_original_tagname_('values')
        my_values.append(my_val)
        doc.data[0].set_values(my_values)
        with self.assertRaises(ValueError):
            choice_child = options()
            doc.data[0].set_options(choice_child)

    def test_data_set_options(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = options()
        doc.data[0].set_options(expectation)
        self.assertEqual(doc.data[0].options, expectation)

    def test_data_set_wrong_options(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.data[0].set_options("String")

    def test_data_set_valid_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        choice_child = validations()
        doc.data[0].set_validations(choice_child)
        with self.assertRaises(ValueError):
            my_valid = []
            my_val = valid()
            my_val.set_valueOf_("Validka")
            my_val.set_dynamic(True)
            my_valid.append(my_val)
            doc.data[0].set_valid(my_valid)

    def test_data_set_valid(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_val = valid()
        my_val.set_valueOf_("Validka")
        my_val.set_dynamic(True)
        expectation.append(my_val)
        doc.data[0].set_valid(expectation)
        self.assertEqual(doc.data[0].valid, expectation)

    def test_data_add_valid(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = valid()
        expectation.set_valueOf_("Validka")
        expectation.set_dynamic(True)
        doc.data[0].add_valid(expectation)
        self.assertEqual(doc.data[0].valid[0], expectation)

    def test_data_add_wrong_valid(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.data[0].add_valid(i18nStringType())

    def test_data_insert_valid_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        val = valid()
        val.set_valueOf_("Validka")
        val.set_dynamic(True)
        with self.assertRaises(IndexError):
            doc.data[0].insert_valid_at(1, val)

    def test_data_set_validations_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        my_valid = []
        my_val = valid()
        my_val.set_valueOf_("Validka")
        my_val.set_dynamic(True)
        my_valid.append(my_val)
        doc.data[0].set_valid(my_valid)
        with self.assertRaises(ValueError):
            choice_child = validations()
            doc.data[0].set_validations(choice_child)

    def test_data_set_validations(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = validations()
        doc.data[0].set_validations(expectation)
        self.assertEqual(doc.data[0].validations, expectation)

    def test_data_set_wrong_validations(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.data[0].set_validations(valid())

    def test_data_set_init_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_inits(inits())
        with self.assertRaises(ValueError):
            my_init = init()
            my_init.set_valueOf_("Initka")
            my_init.set_dynamic(True)
            my_init.set_name('meno')
            my_init.set_original_tagname_('init')
            doc.data[0].set_init(my_init)

    def test_data_set_init(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = init()
        expectation.set_valueOf_("Initka")
        expectation.set_dynamic(True)
        expectation.set_name('meno')
        expectation.set_original_tagname_('init')
        doc.data[0].set_init(expectation)
        self.assertEqual(doc.data[0].init, expectation)

    def test_data_set_wrong_init(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.data[0].set_init(inits())

    def test_data_set_inits_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        my_init = init()
        my_init.set_valueOf_("Initka")
        my_init.set_dynamic(True)
        my_init.set_name('meno')
        my_init.set_original_tagname_('init')
        doc.data[0].set_init(my_init)
        with self.assertRaises(ValueError):
            doc.data[0].set_inits(inits())

    def test_data_set_inits(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = inits()
        doc.data[0].set_inits(expectation)
        self.assertEqual(doc.data[0].inits, expectation)

    def test_data_set_wrong_inits(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.data[0].set_inits(init())

    def test_data_set_format(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = format()
        doc.data[0].set_format(expectation)
        self.assertEqual(doc.data[0].format, expectation)

    def test_data_set_wrong_format(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.data[0].set_format(i18nStringType())

    def test_data_set_view(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = fieldView()
        expectation.set_area('Area')
        doc.data[0].set_view(expectation)
        self.assertEqual(doc.data[0].view, expectation)

    def test_data_set_wrong_view(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.data[0].set_view(i18nStringType())

    def test_data_set_component(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = component()
        expectation.set_name('meno')
        doc.data[0].set_component(expectation)
        self.assertEqual(doc.data[0].component, expectation)

    def test_data_set_wrong_component(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.data[0].set_component(i18nStringType())

    def test_data_set_encryption(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = encryption()
        expectation.set_valueOf_(False)
        expectation.set_algorithm("algoritmus")
        doc.data[0].set_encryption(expectation)
        self.assertEqual(doc.data[0].encryption, expectation)

    def test_data_set_wrong_encryption(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.data[0].set_encryption(i18nStringType())

    def test_data_set_action_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        my_events = []
        my_e = dataEvent()
        my_e.set_type_(dataEventType.SET)
        my_e.set_id('101')
        my_events.append(my_e)
        doc.data[0].set_event(my_events)
        with self.assertRaises(ValueError):
            my_actions = []
            my_a = action()
            my_a.set_trigger("Triggerrr")
            my_a.set_id('001')
            my_a.set_valueOf_("Akcia")
            my_actions.append(my_a)
            doc.data[0].set_action(my_actions)

    def test_data_set_action(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_a = action()
        my_a.set_trigger("Triggerrr")
        my_a.set_id('001')
        my_a.set_valueOf_("Akcia")
        expectation.append(my_a)
        doc.data[0].set_action(expectation)
        self.assertEqual(doc.data[0].action, expectation)

    def test_data_add_action(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = action()
        expectation.set_trigger("Triggerrr")
        expectation.set_id('001')
        expectation.set_valueOf_("Akcia")
        doc.data[0].add_action(expectation)
        self.assertEqual(doc.data[0].action[0], expectation)

    def test_data_add_wrong_action(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.data[0].add_action(i18nStringType())

    def test_data_insert_action_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        act = action()
        act.set_trigger("Triggerrr")
        act.set_id('001')
        act.set_valueOf_("Akcia")
        with self.assertRaises(IndexError):
            doc.data[0].insert_action_at(1, act)

    def test_data_set_event_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        my_actions = []
        my_a = action()
        my_a.set_trigger("Triggerrr")
        my_a.set_id('001')
        my_a.set_valueOf_("Akcia")
        my_actions.append(my_a)
        doc.data[0].set_action(my_actions)
        with self.assertRaises(ValueError):
            my_events = []
            my_e = dataEvent()
            my_e.set_type_(dataEventType.SET)
            my_e.set_id('101')
            my_events.append(my_e)
            doc.data[0].set_event(my_events)

    def test_data_set_event(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_e = dataEvent()
        my_e.set_type_(dataEventType.SET)
        my_e.set_id('101')
        expectation.append(my_e)
        doc.data[0].set_event(expectation)
        self.assertEqual(doc.data[0].event, expectation)

    def test_data_add_event(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = dataEvent()
        expectation.set_type_(dataEventType.SET)
        expectation.set_id('101')
        doc.data[0].add_event(expectation)
        self.assertEqual(doc.data[0].event[0], expectation)

    def test_data_add_wrong_event(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.data[0].add_event(i18nStringType())

    def test_data_insert_event_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        eve = dataEvent()
        eve.set_type_(dataEventType.SET)
        eve.set_id('101')
        with self.assertRaises(IndexError):
            doc.data[0].insert_event_at(1, eve)

    def test_data_set_actionRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_ref = actionRef()
        my_ref.set_id('001')
        expectation.append(my_ref)
        doc.data[0].set_actionRef(expectation)
        self.assertEqual(doc.data[0].actionRef, expectation)

    def test_data_add_actionRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = actionRef()
        expectation.set_id('001')
        doc.data[0].add_actionRef(expectation)
        self.assertEqual(doc.data[0].actionRef[0], expectation)

    def test_data_add_wrong_actionRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.data[0].add_actionRef(i18nStringType())

    def test_data_insert_actionRef_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        ref = actionRef()
        ref.set_id('101')
        with self.assertRaises(IndexError):
            doc.data[0].insert_actionRef_at(1, ref)

    def test_data_set_documentRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = documentRef()
        expectation.set_id(555)
        fields = [17, 252, 86]
        expectation.set_fields(fields)
        doc.data[0].set_documentRef(expectation)
        self.assertEqual(doc.data[0].documentRef, expectation)

    def test_data_set_wrong_documentRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.data[0].set_documentRef(i18nStringType())

    def test_data_set_remote(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = ""
        doc.data[0].set_remote(expectation)
        self.assertEqual(doc.data[0].remote, expectation)

    def test_data_set_wrong_remote(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(ValueError):
            doc.data[0].set_remote("gap")

    def test_data_set_length(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = 15
        doc.data[0].set_length(expectation)
        self.assertEqual(doc.data[0].length, expectation)

    def test_data_set_wrong_length(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.data[0].set_length(i18nStringType())

    def test_data_set_allowedNets(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = allowedNets()
        nets = ["spicy", "boring", "interesting"]
        expectation.set_allowedNet(nets)
        doc.data[0].set_allowedNets(expectation)
        self.assertEqual(doc.data[0].allowedNets, expectation)

    def test_data_set_wrong_allowedNets(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.data[0].set_allowedNets(i18nStringType())

    def test_data_set_type(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = data_type.BUTTON
        doc.data[0].set_type_(expectation)
        self.assertEqual(doc.data[0].type_, expectation)

    def test_data_set_wrong_type(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.data[0].set_type_("not my type")

    def test_data_set_immediate(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = 'false'
        doc.data[0].set_immediate(False)
        self.assertEqual(doc.data[0].immediate, expectation)

    def test_data_set_wrong_immediate(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.data[0].set_immediate(i18nStringType())

#  end of data tag tests

    def test_function_set_scope(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_function(function())
        expectation = scope.PROCESS
        doc.function[0].set_scope(expectation)
        self.assertEqual(doc.function[0].scope, expectation)

    def test_function_set_wrong_scope(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_function(function())
        with self.assertRaises(TypeError):
            doc.function[0].set_scope("SCOPE")

    def test_function_set_name(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_function(function())
        expectation = "meno"
        doc.function[0].set_name(expectation)
        self.assertEqual(doc.function[0].name, expectation)

    def test_function_set_wrong_name(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_function(function())
        with self.assertRaises(TypeError):
            doc.function[0].set_scope(i18nStringType())

    def test_function_set_valueOf_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_function(function())
        expectation = "string value"
        doc.function[0].set_valueOf_(expectation)
        self.assertEqual(doc.function[0].valueOf_, expectation)

    def test_function_set_wrong_valueOf_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_function(function())
        with self.assertRaises(TypeError):
            doc.function[0].set_valueOf_(i18nStringType())

#  end of function tag tests

    def test_role_set_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = "FEI"
        doc.role[0].set_id(expectation, doc)
        self.assertEqual(doc.role[0].id, expectation)

    def test_role_set_not_unique_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = '555'
        doc.role[0].set_id(expectation, doc)
        with self.assertRaises(ValueError):
            doc.role[1].set_id(expectation, doc)

    def test_role_set_wrong_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.role[0].set_id(555, doc)

    def test_role_set_title_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_role(role())
        name = i18nStringType()
        name.set_name("meno")
        name.set_valueOf_("hodnota")
        name.set_original_tagname_('name')
        doc.role[3].set_name(name)
        with self.assertRaises(ValueError):
            title = i18nStringType()
            title.set_name("menucko")
            title.set_valueOf_("hodnota")
            title.set_original_tagname_('title')
            doc.role[3].set_title(title)

    def test_role_set_title(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = i18nStringType()
        expectation.set_valueOf_("Nadpis")
        expectation.set_name("meno")
        expectation.set_original_tagname_('title')
        doc.role[0].set_title(expectation)
        self.assertEqual(doc.role[0].title, expectation)

    def test_role_set_wrong_title(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.role[0].set_title("Nadpis")

    def test_role_set_name_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_role(role())
        title = i18nStringType()
        title.set_name("menucko")
        title.set_valueOf_("hodnota")
        title.set_original_tagname_('title')
        doc.role[3].set_title(title)
        with self.assertRaises(ValueError):
            name = i18nStringType()
            name.set_name("meno")
            name.set_valueOf_("hodnota")
            name.set_original_tagname_('name')
            doc.role[3].set_name(name)

    def test_role_set_name(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_role(role())
        expectation = i18nStringType()
        expectation.set_valueOf_("Nazov")
        expectation.set_name("meno")
        expectation.set_original_tagname_('name')
        doc.role[3].set_name(expectation)
        self.assertEqual(doc.role[3].name, expectation)

    def test_role_set_wrong_name(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_role(role())
        with self.assertRaises(TypeError):
            doc.role[3].set_name("Nazov")

    def test_role_set_event(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_e = event()
        my_e.set_id("EVE")
        my_e.set_type_(eventType.ASSIGN)
        tit = i18nStringType()
        tit.set_valueOf_("Nadpis")
        tit.set_name("meno")
        tit.set_original_tagname_('title')
        my_e.set_title(tit)
        expectation.append(my_e)
        doc.role[0].set_event(expectation)
        self.assertEqual(doc.role[0].event, expectation)

    def test_role_add_event(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = event()
        expectation.set_id("EVE")
        expectation.set_type_(eventType.ASSIGN)
        tit = i18nStringType()
        tit.set_valueOf_("Nadpis")
        tit.set_name("meno")
        tit.set_original_tagname_('title')
        expectation.set_title(tit)
        doc.role[0].add_event(expectation)
        self.assertEqual(doc.role[0].event[0], expectation)

    def test_role_add_wrong_event(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.role[0].add_event(i18nStringType())

    def test_role_insert_event_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        eve = event()
        eve.set_id("EVE")
        eve.set_type_(eventType.ASSIGN)
        tit = i18nStringType()
        tit.set_valueOf_("Nadpis")
        tit.set_name("meno")
        tit.set_original_tagname_('title')
        eve.set_title(tit)
        with self.assertRaises(IndexError):
            doc.role[0].insert_event_at(1, eve)

#  end of role tag tests

    def test_mapping_set_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_mapping(mapping())
        expectation = "FEI"
        doc.mapping[0].set_id(expectation, doc)
        self.assertEqual(doc.mapping[0].id, expectation)

    def test_mapping_set_not_unique_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_mapping(mapping())
        doc.add_mapping(mapping())
        expectation = '555'
        doc.mapping[0].set_id(expectation, doc)
        with self.assertRaises(ValueError):
            doc.mapping[1].set_id(expectation, doc)

    def test_mapping_set_wrong_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_mapping(mapping())
        with self.assertRaises(TypeError):
            doc.mapping[0].set_id(555, doc)

    def test_mapping_set_transitionRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_mapping(mapping())
        expectation = "referencia"
        doc.mapping[0].set_transitionRef(expectation)
        self.assertEqual(doc.mapping[0].transitionRef, expectation)

    def test_mapping_set_wrong_transitionRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_mapping(mapping())
        with self.assertRaises(TypeError):
            doc.mapping[0].set_transitionRef(i18nStringType())

    def test_mapping_set_roleRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_mapping(mapping())
        expectation = []
        my_ref = roleRef()
        my_ref.set_id("ID")
        expectation.append(my_ref)
        doc.mapping[0].set_roleRef(expectation)
        self.assertEqual(doc.mapping[0].roleRef, expectation)

    def test_mapping_add_roleRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_mapping(mapping())
        expectation = roleRef()
        expectation.set_id("ID")
        doc.mapping[0].add_roleRef(expectation)
        self.assertEqual(doc.mapping[0].roleRef[0], expectation)

    def test_mapping_add_wrong_roleRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_mapping(mapping())
        with self.assertRaises(TypeError):
            doc.mapping[0].add_roleRef(i18nStringType())

    def test_mapping_insert_roleRef_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_mapping(mapping())
        ref = roleRef()
        ref.set_id("ID")
        with self.assertRaises(IndexError):
            doc.mapping[0].insert_roleRef_at(1, ref)

    def test_mapping_set_dataRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_mapping(mapping())
        expectation = []
        my_ref = dataRef()
        my_ref.set_id("ID")
        expectation.append(my_ref)
        doc.mapping[0].set_dataRef(expectation)
        self.assertEqual(doc.mapping[0].dataRef, expectation)

    def test_mapping_add_dataRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_mapping(mapping())
        expectation = dataRef()
        expectation.set_id("ID")
        doc.mapping[0].add_dataRef(expectation)
        self.assertEqual(doc.mapping[0].dataRef[0], expectation)

    def test_mapping_add_wrong_dataRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_mapping(mapping())
        with self.assertRaises(TypeError):
            doc.mapping[0].add_dataRef(i18nStringType())

    def test_mapping_insert_dataRef_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_mapping(mapping())
        ref = dataRef()
        ref.set_id("ID")
        with self.assertRaises(IndexError):
            doc.mapping[0].insert_dataRef_at(1, ref)

    def test_mapping_set_dataGroup(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_mapping(mapping())
        expectation = []
        my_group = dataGroup()
        my_group.set_id("ID")
        my_group.set_cols(5)
        my_group.set_rows(12)
        my_group.set_layout(layoutType.GRID)
        my_group.set_alignment(dataGroupAlignment.CENTER)
        my_group.set_stretch(False)
        my_group.set_hideEmptyRows(hideEmptyRows.NONE)
        my_group.set_compactDirection(compactDirection.UP)
        expectation.append(my_group)
        doc.mapping[0].set_dataGroup(expectation)
        self.assertEqual(doc.mapping[0].dataGroup, expectation)

    def test_mapping_add_dataGroup(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_mapping(mapping())
        expectation = dataGroup()
        expectation.set_id("ID")
        expectation.set_cols(5)
        expectation.set_rows(12)
        expectation.set_layout(layoutType.GRID)
        expectation.set_alignment(dataGroupAlignment.CENTER)
        expectation.set_stretch(False)
        expectation.set_hideEmptyRows(hideEmptyRows.NONE)
        expectation.set_compactDirection(compactDirection.UP)
        doc.mapping[0].add_dataGroup(expectation)
        self.assertEqual(doc.mapping[0].dataGroup[0], expectation)

    def test_mapping_add_wrong_dataGroup(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_mapping(mapping())
        with self.assertRaises(TypeError):
            doc.mapping[0].add_dataGroup(i18nStringType())

    def test_mapping_insert_dataGroup_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_mapping(mapping())
        group = dataGroup()
        group.set_id("ID")
        group.set_cols(5)
        group.set_rows(12)
        group.set_layout(layoutType.GRID)
        group.set_alignment(dataGroupAlignment.CENTER)
        group.set_stretch(False)
        group.set_hideEmptyRows(hideEmptyRows.NONE)
        group.set_compactDirection(compactDirection.UP)
        with self.assertRaises(IndexError):
            doc.mapping[0].insert_dataGroup_at(1, group)

    def test_mapping_set_trigger(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_mapping(mapping())
        expectation = []
        my_ger = trigger()
        my_ger.set_type_(triggerType.USER)
        expectation.append(my_ger)
        doc.mapping[0].set_trigger(expectation)
        self.assertEqual(doc.mapping[0].trigger, expectation)

    def test_mapping_add_trigger(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_mapping(mapping())
        expectation = trigger()
        expectation.set_type_(triggerType.USER)
        doc.mapping[0].add_trigger(expectation)
        self.assertEqual(doc.mapping[0].trigger[0], expectation)

    def test_mapping_add_wrong_trigger(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_mapping(mapping())
        with self.assertRaises(TypeError):
            doc.mapping[0].add_trigger(i18nStringType())

    def test_mapping_insert_trigger_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_mapping(mapping())
        ger = trigger()
        ger.set_type_(triggerType.USER)
        with self.assertRaises(IndexError):
            doc.mapping[0].insert_trigger_at(1, ger)

#  end of mapping tag tests

    def test_transition_set_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = "FEI"
        doc.transition[0].set_id(expectation, doc)
        self.assertEqual(doc.transition[0].id, expectation)

    def test_transition_set_not_unique_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = '555'
        doc.transition[0].set_id(expectation, doc)
        with self.assertRaises(ValueError):
            doc.transition[1].set_id(expectation, doc)

    def test_transition_set_wrong_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].set_id(555, doc)

    def test_transition_set_x(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = 5
        doc.transition[0].set_x(expectation)
        self.assertEqual(doc.transition[0].x, expectation)

    def test_transition_set_negative_x(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(ValueError):
            doc.transition[0].set_x(-22)

    def test_transition_set_wrong_x(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].set_x("5")

    def test_transition_set_y(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = 12
        doc.transition[0].set_y(expectation)
        self.assertEqual(doc.transition[0].y, expectation)

    def test_transition_set_negative_y(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(ValueError):
            doc.transition[0].set_y(-33)

    def test_transition_set_wrong_y(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].set_y(i18nStringType())

    def test_transition_set_label(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = i18nStringType()
        expectation.set_name("meno")
        expectation.set_valueOf_("Štítok")
        expectation.set_original_tagname_('label')
        doc.transition[0].set_label(expectation)
        self.assertEqual(doc.transition[0].label, expectation)

    def test_transition_set_wrong_label(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].set_label("Štítok")

    def test_transition_set_layout(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = transitionLayout()
        expectation.set_cols(5)
        expectation.set_rows(12)
        expectation.set_offset(55)
        expectation.set_fieldAlignment(fieldAlignment.BOTTOM)
        expectation.set_hideEmptyRows(hideEmptyRows.COMPACTED)
        expectation.set_compactDirection(compactDirection.UP)
        expectation.set_type_(layoutType.LEGACY)
        doc.transition[0].set_layout(expectation)
        self.assertEqual(doc.transition[0].layout, expectation)

    def test_transition_set_wrong_layout(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].set_layout(layout())

    def test_transition_set_icon(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = "iconka"
        doc.transition[0].set_icon(expectation)
        self.assertEqual(doc.transition[0].icon, expectation)

    def test_transition_set_wrong_icon(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].set_icon(555)

    def test_transition_set_priority(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = 100
        doc.transition[0].set_priority(expectation)
        self.assertEqual(doc.transition[0].priority, expectation)

    def test_transition_set_negative_priority(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(ValueError):
            doc.transition[0].set_priority(-100)

    def test_transition_set_wrong_priority(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].set_priority("100")

    def test_transition_set_assignPolicy(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = assignPolicy.MANUAL
        doc.transition[0].set_assignPolicy(expectation)
        self.assertEqual(doc.transition[0].assignPolicy, expectation)

    def test_transition_set_wrong_assignPolicy(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].set_assignPolicy(i18nStringType())

    def test_transition_set_dataFocusPolicy(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = dataFocusPolicy.AUTO_EMPTY_REQUIRED
        doc.transition[0].set_dataFocusPolicy(expectation)
        self.assertEqual(doc.transition[0].dataFocusPolicy, expectation)

    def test_transition_set_wrong_dataFocusPolicy(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].set_dataFocusPolicy(i18nStringType())

    def test_transition_set_finishPolicy(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = finishPolicy.AUTO_NO_DATA
        doc.transition[0].set_finishPolicy(expectation)
        self.assertEqual(doc.transition[0].finishPolicy, expectation)

    def test_transition_set_wrong_finishPolicy(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].set_finishPolicy(i18nStringType())

    def test_transition_set_trigger(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_ger = trigger()
        my_ger.set_type_(triggerType.USER)
        expectation.append(my_ger)
        doc.transition[0].set_trigger(expectation)
        self.assertEqual(doc.transition[0].trigger, expectation)

    def test_transition_add_trigger(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = trigger()
        expectation.set_type_(triggerType.USER)
        doc.transition[0].add_trigger(expectation)
        self.assertEqual(doc.transition[0].trigger[0], expectation)

    def test_transition_add_wrong_trigger(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].add_trigger(i18nStringType())

    def test_transition_insert_trigger_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        ger = trigger()
        ger.set_type_(triggerType.USER)
        with self.assertRaises(IndexError):
            doc.transition[0].insert_trigger_at(1, ger)

    def test_transition_set_transactionRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = transactionRef()
        expectation.set_id("REF")
        doc.transition[0].set_transactionRef(expectation)
        self.assertEqual(doc.transition[0].transactionRef, expectation)

    def test_transition_set_wrong_transactionRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].set_transactionRef(i18nStringType())

    def test_transition_set_roleRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_ref = roleRef()
        my_ref.set_id("REF")
        expectation.append(my_ref)
        doc.transition[0].set_roleRef(expectation)
        self.assertEqual(doc.transition[0].roleRef, expectation)

    def test_transition_add_roleRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = roleRef()
        expectation.set_id("REF")
        doc.transition[0].add_roleRef(expectation)
        self.assertEqual(doc.transition[0].roleRef[0], expectation)

    def test_transition_add_wrong_roleRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].add_roleRef(i18nStringType())

    def test_transition_insert_roleRef_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        ref = roleRef()
        ref.set_id("REF")
        with self.assertRaises(IndexError):
            doc.transition[0].insert_roleRef_at(1, ref)

    def test_transition_set_usersRef_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        refs1 = []
        ref1 = userRef()
        ref1.set_id("REF1")
        refs1.append(ref1)
        doc.transition[0].set_userRef(refs1)
        with self.assertRaises(ValueError):
            refs2 = []
            ref2 = userRef()
            ref2.set_id("REF2")
            refs2.append(ref2)
            doc.transition[0].set_usersRef(refs2)

    def test_transition_set_usersRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_ref = userRef()
        my_ref.set_id("REF")
        expectation.append(my_ref)
        doc.transition[0].set_usersRef(expectation)
        self.assertEqual(doc.transition[0].usersRef, expectation)

    def test_transition_add_usersRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = userRef()
        expectation.set_id("REF")
        doc.transition[0].add_usersRef(expectation)
        self.assertEqual(doc.transition[0].usersRef[0], expectation)

    def test_transition_add_wrong_usersRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].add_usersRef(i18nStringType())

    def test_transition_insert_usersRef_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        ref = userRef()
        ref.set_id("REF")
        with self.assertRaises(IndexError):
            doc.transition[0].insert_usersRef_at(1, ref)

    def test_transition_set_userRef_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        refs2 = []
        ref2 = userRef()
        ref2.set_id("REF2")
        refs2.append(ref2)
        doc.transition[0].set_usersRef(refs2)
        with self.assertRaises(ValueError):
            refs1 = []
            ref1 = userRef()
            ref1.set_id("REF1")
            refs1.append(ref1)
            doc.transition[0].set_userRef(refs1)

    def test_transition_set_userRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_ref = userRef()
        my_ref.set_id("REF")
        expectation.append(my_ref)
        doc.transition[0].set_userRef(expectation)
        self.assertEqual(doc.transition[0].userRef, expectation)

    def test_transition_add_userRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = userRef()
        expectation.set_id("REF")
        doc.transition[0].add_userRef(expectation)
        self.assertEqual(doc.transition[0].userRef[0], expectation)

    def test_transition_add_wrong_userRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].add_userRef(i18nStringType())

    def test_transition_insert_userRef_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        ref = userRef()
        ref.set_id("REF")
        with self.assertRaises(IndexError):
            doc.transition[0].insert_userRef_at(1, ref)

    def test_transition_set_assignedUser(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = assignedUser()
        expectation.set_cancel(True)
        expectation.set_reassign(True)
        doc.transition[0].set_assignedUser(expectation)
        self.assertEqual(doc.transition[0].assignedUser, expectation)

    def test_transition_set_wrong_assignedUser(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].set_assignedUser(i18nStringType())

    def test_transition_set_dataRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_ref = dataRef()
        my_ref.set_id("REF")
        expectation.append(my_ref)
        doc.transition[0].set_dataRef(expectation)
        self.assertEqual(doc.transition[0].dataRef, expectation)

    def test_transition_add_dataRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = dataRef()
        expectation.set_id("REF")
        doc.transition[0].add_dataRef(expectation)
        self.assertEqual(doc.transition[0].dataRef[0], expectation)

    def test_transition_add_wrong_dataRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].add_dataRef(i18nStringType())

    def test_transition_insert_dataRef_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        ref = dataRef()
        ref.set_id("REF")
        with self.assertRaises(IndexError):
            doc.transition[0].insert_dataRef_at(1, ref)

    def test_transition_set_dataGroup(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_group = dataGroup()
        my_group.set_id("ID")
        my_group.set_cols(5)
        my_group.set_rows(12)
        my_group.set_layout(layoutType.GRID)
        my_group.set_alignment(dataGroupAlignment.CENTER)
        my_group.set_stretch(False)
        my_group.set_hideEmptyRows(hideEmptyRows.NONE)
        my_group.set_compactDirection(compactDirection.UP)
        expectation.append(my_group)
        doc.transition[1].set_dataGroup(expectation)
        self.assertEqual(doc.transition[1].dataGroup, expectation)

    def test_transition_add_dataGroup(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = dataGroup()
        expectation.set_id("ID")
        expectation.set_cols(5)
        expectation.set_rows(12)
        expectation.set_layout(layoutType.GRID)
        expectation.set_alignment(dataGroupAlignment.CENTER)
        expectation.set_stretch(False)
        expectation.set_hideEmptyRows(hideEmptyRows.NONE)
        expectation.set_compactDirection(compactDirection.UP)
        doc.transition[1].add_dataGroup(expectation)
        self.assertEqual(doc.transition[1].dataGroup[0], expectation)

    def test_transition_add_wrong_dataGroup(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[1].add_dataGroup(i18nStringType())

    def test_transition_insert_dataGroup_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        group = dataGroup()
        group.set_id("ID")
        group.set_cols(5)
        group.set_rows(12)
        group.set_layout(layoutType.GRID)
        group.set_alignment(dataGroupAlignment.CENTER)
        group.set_stretch(False)
        group.set_hideEmptyRows(hideEmptyRows.NONE)
        group.set_compactDirection(compactDirection.UP)
        with self.assertRaises(IndexError):
            doc.transition[1].insert_dataGroup_at(1, group)

    def test_transition_set_event(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_transition(transition())
        expectation = []
        my_e = event()
        my_e.set_id("EVE")
        my_e.set_type_(eventType.ASSIGN)
        tit = i18nStringType()
        tit.set_valueOf_("Nadpis")
        tit.set_name("meno")
        tit.set_original_tagname_('title')
        my_e.set_title(tit)
        expectation.append(my_e)
        doc.transition[4].set_event(expectation)
        self.assertEqual(doc.transition[4].event, expectation)

    def test_transition_add_event(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_transition(transition())
        expectation = event()
        expectation.set_id("EVE")
        expectation.set_type_(eventType.ASSIGN)
        tit = i18nStringType()
        tit.set_valueOf_("Nadpis")
        tit.set_name("meno")
        tit.set_original_tagname_('title')
        expectation.set_title(tit)
        doc.transition[4].add_event(expectation)
        self.assertEqual(doc.transition[4].event[0], expectation)

    def test_transition_add_wrong_event(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_transition(transition())
        with self.assertRaises(TypeError):
            doc.transition[4].add_event(i18nStringType())

    def test_transition_insert_event_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_transition(transition())
        eve = event()
        eve.set_id("EVE")
        eve.set_type_(eventType.ASSIGN)
        tit = i18nStringType()
        tit.set_valueOf_("Nadpis")
        tit.set_name("meno")
        tit.set_original_tagname_('title')
        eve.set_title(tit)
        with self.assertRaises(IndexError):
            doc.transition[4].insert_event_at(1, eve)

#  end of transition tag tests

    def test_transitionLayout_set_cols(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_transition(transition())
        expectation = 5
        layout_ = transitionLayout()
        layout_.set_cols(expectation)
        doc.transition[15].set_layout(layout_)
        self.assertEqual(doc.transition[15].layout.cols, expectation)

    def test_transitionLayout_set_negative_cols(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_transition(transition())
        layout_ = transitionLayout()
        doc.transition[15].set_layout(layout_)
        with self.assertRaises(ValueError):
            doc.transition[15].layout.set_cols(-22)

    def test_transitionLayout_set_wrong_cols(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_transition(transition())
        layout_ = transitionLayout()
        doc.transition[15].set_layout(layout_)
        with self.assertRaises(TypeError):
            doc.transition[15].layout.set_cols("stlpce")

    def test_transitionLayout_set_rows(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_transition(transition())
        expectation = 12
        layout_ = transitionLayout()
        layout_.set_rows(expectation)
        doc.transition[15].set_layout(layout_)
        self.assertEqual(doc.transition[15].layout.rows, expectation)

    def test_transitionLayout_set_negative_rows(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_transition(transition())
        layout_ = transitionLayout()
        doc.transition[15].set_layout(layout_)
        with self.assertRaises(ValueError):
            doc.transition[15].layout.set_rows(-100)

    def test_transitionLayout_set_wrong_rows(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_transition(transition())
        layout_ = transitionLayout()
        doc.transition[15].set_layout(layout_)
        with self.assertRaises(TypeError):
            doc.transition[15].layout.set_rows("riadky")

    def test_transitionLayout_set_offset(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_transition(transition())
        expectation = 55
        layout_ = transitionLayout()
        layout_.set_offset(expectation)
        doc.transition[15].set_layout(layout_)
        self.assertEqual(doc.transition[15].layout.offset, expectation)

    def test_transitionLayout_set_negative_offset(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_transition(transition())
        layout_ = transitionLayout()
        doc.transition[15].set_layout(layout_)
        with self.assertRaises(ValueError):
            doc.transition[15].layout.set_offset(-55)

    def test_transitionLayout_set_wrong_offset(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_transition(transition())
        layout_ = transitionLayout()
        doc.transition[15].set_layout(layout_)
        with self.assertRaises(TypeError):
            doc.transition[15].layout.set_offset(i18nStringType())

    def test_transitionLayout_set_fieldAlignment(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_transition(transition())
        expectation = fieldAlignment.TOP
        layout_ = transitionLayout()
        doc.transition[15].set_layout(layout_)
        doc.transition[15].layout.set_fieldAlignment(expectation)
        self.assertEqual(doc.transition[15].layout.fieldAlignment, expectation)

    def test_transitionLayout_set_wrong_fieldAlignment(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_transition(transition())
        layout_ = transitionLayout()
        doc.transition[15].set_layout(layout_)
        with self.assertRaises(TypeError):
            doc.transition[15].layout.set_fieldAlignment(i18nStringType())

    def test_transitionLayout_set_hideEmptyRows(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_transition(transition())
        expectation = hideEmptyRows.COMPACTED
        layout_ = transitionLayout()
        doc.transition[15].set_layout(layout_)
        doc.transition[15].layout.set_hideEmptyRows(expectation)
        self.assertEqual(doc.transition[15].layout.hideEmptyRows, expectation)

    def test_transitionLayout_set_wrong_hideEmptyRows(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_transition(transition())
        layout_ = transitionLayout()
        doc.transition[15].set_layout(layout_)
        with self.assertRaises(TypeError):
            doc.transition[15].layout.set_hideEmptyRows(i18nStringType())

    def test_transitionLayout_set_compactDirection(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_transition(transition())
        expectation = compactDirection.NONE
        layout_ = transitionLayout()
        doc.transition[15].set_layout(layout_)
        doc.transition[15].layout.set_compactDirection(expectation)
        self.assertEqual(doc.transition[15].layout.compactDirection, expectation)

    def test_transitionLayout_set_wrong_compactDirection(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_transition(transition())
        layout_ = transitionLayout()
        doc.transition[15].set_layout(layout_)
        with self.assertRaises(TypeError):
            doc.transition[15].layout.set_compactDirection(i18nStringType())

    def test_transitionLayout_set_type_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_transition(transition())
        expectation = layoutType.FLOW
        layout_ = transitionLayout()
        doc.transition[15].set_layout(layout_)
        doc.transition[15].layout.set_type_(expectation)
        self.assertEqual(doc.transition[15].layout.type_, expectation)

    def test_transitionLayout_set_wrong_type_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_transition(transition())
        layout_ = transitionLayout()
        doc.transition[15].set_layout(layout_)
        with self.assertRaises(TypeError):
            doc.transition[15].layout.set_type_(i18nStringType())

#  end of transitionLayout tag tests

    def test_place_set_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = '555'
        doc.place[0].set_id(expectation, doc)
        self.assertEqual(doc.place[0].id, expectation)

    def test_place_set_not_unique_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = '555'
        doc.place[0].set_id(expectation, doc)
        with self.assertRaises(ValueError):
            doc.place[1].set_id(expectation, doc)

    def test_place_set_wrong_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.place[0].set_id(555, doc)

    def test_place_set_x(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = 5
        doc.place[0].set_x(expectation)
        self.assertEqual(doc.place[0].x, expectation)

    def test_place_set_negative_x(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(ValueError):
            doc.place[0].set_x(-55)

    def test_place_set_wrong_x(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.place[0].set_x(i18nStringType())

    def test_place_set_y(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = 12
        doc.place[0].set_y(expectation)
        self.assertEqual(doc.place[0].y, expectation)

    def test_place_set_negative_y(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(ValueError):
            doc.place[0].set_y(-100)

    def test_place_set_wrong_y(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.place[0].set_y("coord")

    def test_place_set_label(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = i18nStringType()
        expectation.set_valueOf_("Štítok")
        expectation.set_original_tagname_('label')
        expectation.set_name("meno")
        doc.place[0].set_label(expectation)
        self.assertEqual(doc.place[0].label, expectation)

    def test_place_set_wrong_label(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.place[0].set_label("Štítok")

    def test_place_set_tokens(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = 1
        doc.place[0].set_tokens(expectation)
        self.assertEqual(doc.place[0].tokens, expectation)

    def test_place_set_negative_tokens(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(ValueError):
            doc.place[0].set_tokens(-1)

    def test_place_set_wrong_tokens(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.place[0].set_tokens("○")

    def test_place_set_isStatic_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_place(place())
        choice_child = True
        doc.place[15].set_static(choice_child)
        with self.assertRaises(ValueError):
            choice_child_2 = False
            doc.place[15].set_isStatic(choice_child_2)

    def test_place_set_isStatic(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_place(place())
        expectation = 'false'
        doc.place[15].set_isStatic(expectation)
        self.assertEqual(doc.place[15].isStatic, expectation)

    def test_place_set_wrong_isStatic(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_place(place())
        with self.assertRaises(TypeError):
            doc.place[15].set_isStatic("positive")

    def test_place_set_static_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_place(place())
        choice_child = False
        doc.place[15].set_isStatic(choice_child)
        with self.assertRaises(ValueError):
            choice_child_2 = True
            doc.place[15].set_static(choice_child_2)

    def test_place_set_static(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_place(place())
        expectation = 'true'
        doc.place[15].set_static(expectation)
        self.assertEqual(doc.place[15].static, expectation)

    def test_place_set_wrong_static(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_place(place())
        with self.assertRaises(TypeError):
            doc.place[15].set_static(i18nStringType())

#  end of place tag tests

    def test_arc_set_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = "FEI"
        doc.arc[0].set_id(expectation, doc)
        self.assertEqual(doc.arc[0].id, expectation)

    def test_arc_set_not_unique_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = '555'
        doc.arc[0].set_id(expectation, doc)
        with self.assertRaises(ValueError):
            doc.arc[1].set_id(expectation, doc)

    def test_arc_set_wrong_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.arc[0].set_id(555, doc)

    def test_arc_set_type_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = arc_type.INHIBITOR
        doc.arc[0].set_type_(expectation)
        self.assertEqual(doc.arc[0].type_, expectation)

    def test_arc_set_wrong_type_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.arc[0].set_type_(i18nStringType())

    def test_arc_set_sourceId(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = "S50"
        doc.arc[0].set_sourceId(expectation)
        self.assertEqual(doc.arc[0].sourceId, expectation)

    def test_arc_set_wrong_sourceId(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.arc[0].set_sourceId(50)

    def test_arc_set_destinationId(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = "p5"
        doc.arc[0].set_destinationId(expectation)
        self.assertEqual(doc.arc[0].destinationId, expectation)

    def test_arc_set_wrong_destinationId(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.arc[0].set_destinationId(i18nStringType())

    def test_place_set_multiplicity(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = 8
        doc.arc[0].set_multiplicity(expectation)
        self.assertEqual(doc.arc[0].multiplicity, expectation)

    def test_place_set_negative_multiplicity(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(ValueError):
            doc.arc[0].set_multiplicity(-8)

    def test_place_set_wrong_multiplicity(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.arc[0].set_multiplicity("8")

    def test_arc_set_reference(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = "referencia"
        doc.arc[0].set_reference(expectation)
        self.assertEqual(doc.arc[0].reference, expectation)

    def test_arc_set_wrong_reference(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.arc[0].set_reference(i18nStringType())

    def test_arc_set_breakpoint(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_point = breakpoint()
        my_point.set_x(5)
        my_point.set_y(12)
        expectation.append(my_point)
        doc.arc[0].set_breakpoint(expectation)
        self.assertEqual(doc.arc[0].breakpoint, expectation)

    def test_arc_add_breakpoint(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = breakpoint()
        expectation.set_x(5)
        expectation.set_y(12)
        doc.arc[0].add_breakpoint(expectation)
        self.assertEqual(doc.arc[0].breakpoint[0], expectation)

    def test_arc_add_wrong_breakpoint(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.arc[0].add_breakpoint(i18nStringType())

    def test_arc_insert_breakpoint_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        point = breakpoint()
        point.set_x(5)
        point.set_y(12)
        with self.assertRaises(IndexError):
            doc.arc[0].insert_breakpoint_at(1, point)

#  end of arc tag tests

    def test_i18n_set_i18nString(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_i18n(i18n())
        expectation = []
        my_string = i18nStringType()
        my_string.set_valueOf_("special")
        my_string.set_name("meno")
        my_string.set_original_tagname_('i18nString')
        expectation.append(my_string)
        doc.i18n[0].set_i18nString(expectation)
        self.assertEqual(doc.i18n[0].i18nString, expectation)

    def test_i18n_add_i18nString(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_i18n(i18n())
        expectation = i18nStringType()
        expectation.set_valueOf_("special")
        expectation.set_name("meno")
        expectation.set_original_tagname_('i18nString')
        doc.i18n[0].add_i18nString(expectation)
        self.assertEqual(doc.i18n[0].i18nString[0], expectation)

    def test_i18n_add_wrong_i18nString(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_i18n(i18n())
        with self.assertRaises(TypeError):
            doc.i18n[0].add_i18nString("reverzia")

    def test_i18n_insert_i18nString_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_i18n(i18n())
        string = i18nStringType()
        string.set_valueOf_("special")
        string.set_name("meno")
        string.set_original_tagname_('i18nString')
        with self.assertRaises(IndexError):
            doc.i18n[0].insert_i18nString_at(1, string)

    def test_i18n_set_locale(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_i18n(i18n())
        expectation = "local"
        doc.i18n[0].set_locale(expectation)
        self.assertEqual(doc.i18n[0].locale, expectation)

    def test_i18n_set_wrong_locale(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_i18n(i18n())
        with self.assertRaises(TypeError):
            doc.i18n[0].set_locale(i18nStringType())

#  end of i18n tag tests

    def test_processEvents_set_event(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_processEvents(processEvents())
        expectation = []
        my_eve = processEvent()
        my_eve.set_id("FEI")
        my_eve.set_type_(processEventType.UPLOAD)
        msg = i18nStringType()
        msg.set_valueOf_("sprava")
        msg.set_name("meno")
        msg.set_original_tagname_('message')
        my_eve.set_message(msg)
        expectation.append(my_eve)
        doc.processEvents.set_event(expectation)
        self.assertEqual(doc.processEvents.event, expectation)

    def test_processEvents_add_event(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_processEvents(processEvents())
        expectation = processEvent()
        expectation.set_id("FEI")
        expectation.set_type_(processEventType.UPLOAD)
        msg = i18nStringType()
        msg.set_valueOf_("sprava")
        msg.set_name("meno")
        msg.set_original_tagname_('message')
        expectation.set_message(msg)
        doc.processEvents.add_event(expectation)
        self.assertEqual(doc.processEvents.event[0], expectation)

    def test_processEvents_add_wrong_event(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_processEvents(processEvents())
        with self.assertRaises(TypeError):
            doc.processEvents.add_event(dataEvent())

    def test_processEvents_insert_event_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_processEvents(processEvents())
        eve = processEvent()
        eve.set_id("FEI")
        eve.set_type_(processEventType.UPLOAD)
        msg = i18nStringType()
        msg.set_valueOf_("sprava")
        msg.set_name("meno")
        msg.set_original_tagname_('message')
        eve.set_message(msg)
        with self.assertRaises(IndexError):
            doc.processEvents.insert_event_at(1, eve)

#  end of processEvents tag tests

    def test_caseEvents_set_event(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_caseEvents(caseEvents())
        expectation = []
        my_eve = caseEvent()
        my_eve.set_id("FEI")
        my_eve.set_type_(caseEventType.CREATE)
        msg = i18nStringType()
        msg.set_valueOf_("sprava")
        msg.set_name("meno")
        msg.set_original_tagname_('message')
        my_eve.set_message(msg)
        expectation.append(my_eve)
        doc.caseEvents.set_event(expectation)
        self.assertEqual(doc.caseEvents.event, expectation)

    def test_caseEvents_add_event(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_caseEvents(caseEvents())
        expectation = caseEvent()
        expectation.set_id("FEI")
        expectation.set_type_(caseEventType.DELETE)
        msg = i18nStringType()
        msg.set_valueOf_("sprava")
        msg.set_name("meno")
        msg.set_original_tagname_('message')
        expectation.set_message(msg)
        doc.caseEvents.add_event(expectation)
        self.assertEqual(doc.caseEvents.event[0], expectation)

    def test_caseEvents_add_wrong_event(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_caseEvents(caseEvents())
        with self.assertRaises(TypeError):
            doc.caseEvents.add_event(dataEvent())

    def test_caseEvents_insert_event_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_caseEvents(caseEvents())
        eve = caseEvent()
        eve.set_id("FEI")
        eve.set_type_(caseEventType.CREATE)
        msg = i18nStringType()
        msg.set_valueOf_("sprava")
        msg.set_name("meno")
        msg.set_original_tagname_('message')
        eve.set_message(msg)
        with self.assertRaises(IndexError):
            doc.caseEvents.insert_event_at(1, eve)

#  end of caseEvents tag tests

    def test_documentType_set_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = "FEI"
        doc.set_id(expectation)
        self.assertEqual(doc.id, expectation)

    def test_documentType_set_wrong_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.set_id(555)

    def test_documentType_set_version(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = "verzia"
        doc.set_version(expectation)
        self.assertEqual(doc.version, expectation)

    def test_documentType_set_wrong_version(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.set_version(000)

    def test_documentType_set_initials(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = "POV"
        doc.set_initials(expectation)
        self.assertEqual(doc.initials, expectation)

    def test_documentType_set_wrong_initials(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(Exception):
            doc.set_initials(111)

    def test_documentType_set_wrong_length_initials(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(Exception):
            doc.set_initials("INIT")

    def test_documentType_set_title(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = i18nStringType()
        expectation.set_valueOf_("Nadpis")
        expectation.set_name("meno")
        expectation.set_original_tagname_('title')
        doc.set_title(expectation)
        self.assertEqual(doc.title, expectation)

    def test_documentType_set_wrong_title(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.set_title("Nadpis")

    def test_documentType_set_icon(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = "icona"
        doc.set_icon(expectation)
        self.assertEqual(doc.icon, expectation)

    def test_documentType_set_wrong_icon(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.set_icon(icon())

    def test_documentType_set_defaultRole(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = 'true'
        doc.set_defaultRole(expectation)
        self.assertEqual(doc.defaultRole, expectation)

    def test_documentType_set_wrong_defaultRole(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.set_defaultRole("pravda")

    def test_documentType_set_anonymousRole(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = 'false'
        doc.set_anonymousRole(expectation)
        self.assertEqual(doc.anonymousRole, expectation)

    def test_documentType_set_wrong_anonymousRole(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.set_anonymousRole("loz")

    def test_documentType_set_transitionRole(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = 'true'
        doc.set_transitionRole(expectation)
        self.assertEqual(doc.transitionRole, expectation)

    def test_documentType_set_wrong_transitionRole(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.set_transitionRole("pravda")

    def test_documentType_set_caseName(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = i18nStringTypeWithExpression()
        expectation.set_valueOf_("pripad")
        expectation.set_name("meno")
        expectation.set_original_tagname_('caseName')
        expectation.set_dynamic(False)
        doc.set_caseName(expectation)
        self.assertEqual(doc.caseName, expectation)

    def test_documentType_set_wrong_caseName(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.set_caseName("pripad")

    def test_documentType_set_roleRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_ref = caseRoleRef()
        my_ref.set_id("ID")
        expectation.append(my_ref)
        doc.set_roleRef(expectation)
        self.assertEqual(doc.roleRef, expectation)

    def test_documentType_add_roleRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = caseRoleRef()
        expectation.set_id("ID")
        doc.add_roleRef(expectation)
        self.assertEqual(doc.roleRef[0], expectation)

    def test_documentType_add_wrong_roleRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.add_roleRef(i18nStringType())

    def test_documentType_insert_roleRef_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        ref = caseRoleRef()
        ref.set_id("ID")
        with self.assertRaises(IndexError):
            doc.insert_roleRef_at(1, ref)

    def test_documentType_set_usersRef_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        choice_child = []
        ref = caseUserRef()
        ref.set_id("USER")
        choice_child.append(ref)
        doc.set_userRef(choice_child)
        with self.assertRaises(ValueError):
            choice_child_2 = []
            ref_2 = caseUserRef()
            ref_2.set_id("USERS")
            choice_child_2.append(ref_2)
            doc.set_usersRef(choice_child_2)

    def test_documentType_set_usersRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_ref = caseUserRef()
        my_ref.set_id("ID")
        expectation.append(my_ref)
        doc.set_usersRef(expectation)
        self.assertEqual(doc.usersRef, expectation)

    def test_documentType_add_usersRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = caseUserRef()
        expectation.set_id("ID")
        doc.add_usersRef(expectation)
        self.assertEqual(doc.usersRef[0], expectation)

    def test_documentType_add_wrong_usersRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.add_usersRef(i18nStringType())

    def test_documentType_insert_usersRef_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        ref = caseUserRef()
        ref.set_id("ID")
        with self.assertRaises(IndexError):
            doc.insert_usersRef_at(1, ref)

    def test_documentType_set_userRef_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        choice_child = []
        ref = caseUserRef()
        ref.set_id("USERS")
        choice_child.append(ref)
        doc.set_usersRef(choice_child)
        with self.assertRaises(ValueError):
            choice_child_2 = []
            ref_2 = caseUserRef()
            ref_2.set_id("USER")
            choice_child_2.append(ref_2)
            doc.set_userRef(choice_child_2)

    def test_documentType_set_userRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_ref = caseUserRef()
        my_ref.set_id("ID")
        expectation.append(my_ref)
        doc.set_userRef(expectation)
        self.assertEqual(doc.userRef, expectation)

    def test_documentType_add_userRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = caseUserRef()
        expectation.set_id("ID")
        doc.add_userRef(expectation)
        self.assertEqual(doc.userRef[0], expectation)

    def test_documentType_add_wrong_userRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.add_userRef(i18nStringType())

    def test_documentType_insert_userRef_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        ref = caseUserRef()
        ref.set_id("ID")
        with self.assertRaises(IndexError):
            doc.insert_userRef_at(1, ref)

    def test_documentType_set_processEvents(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = processEvents()
        doc.set_processEvents(expectation)
        self.assertEqual(doc.processEvents, expectation)

    def test_documentType_set_wrong_processEvents(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.set_processEvents("proces")

    def test_documentType_set_caseEvents(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = caseEvents()
        doc.set_caseEvents(expectation)
        self.assertEqual(doc.caseEvents, expectation)

    def test_documentType_set_wrong_caseEvents(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.set_caseEvents("pripad")

    def test_documentType_set_transaction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        tra = transaction()
        tra.set_id("TT")
        tit = i18nStringType()
        tit.set_valueOf_("Nazov")
        tit.set_name("meno")
        tit.set_original_tagname_('title')
        tra.set_title(tit)
        expectation.append(tra)
        doc.set_transaction(expectation)
        self.assertEqual(doc.transaction, expectation)

    def test_documentType_add_transaction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = transaction()
        expectation.set_id("TT")
        tit = i18nStringType()
        tit.set_valueOf_("Nazov")
        tit.set_name("meno")
        tit.set_original_tagname_('title')
        expectation.set_title(tit)
        doc.add_transaction(expectation)
        self.assertEqual(doc.transaction[0], expectation)

    def test_documentType_add_wrong_transaction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.add_transaction(i18nStringType())

    def test_documentType_insert_transaction_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        tra = transaction()
        tra.set_id("TT")
        tit = i18nStringType()
        tit.set_valueOf_("Nazov")
        tit.set_name("meno")
        tit.set_original_tagname_('title')
        tra.set_title(tit)
        with self.assertRaises(IndexError):
            doc.insert_transaction_at(1, tra)

    def test_documentType_set_role(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_role = role()
        my_role.set_id("ID", doc)
        n = i18nStringType()
        n.set_valueOf_("tit")
        n.set_name("meno")
        n.set_original_tagname_('name')
        my_role.set_name(n)
        expectation.append(my_role)
        doc.set_role(expectation)
        self.assertEqual(doc.role, expectation)

    def test_documentType_add_role(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = role()
        expectation.set_id("ID", doc)
        n = i18nStringType()
        n.set_valueOf_("tit")
        n.set_name("meno")
        n.set_original_tagname_('name')
        expectation.set_name(n)
        doc.add_role(expectation)
        self.assertEqual(doc.role[3], expectation)

    def test_documentType_add_wrong_role(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.add_role(i18nStringType())

    def test_documentType_insert_role_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        role_ = role()
        role_.set_id("ID", doc)
        n = i18nStringType()
        n.set_valueOf_("tit")
        n.set_name("meno")
        n.set_original_tagname_('name')
        role_.set_name(n)
        with self.assertRaises(IndexError):
            doc.insert_role_at(4, role_)

    def test_documentType_set_function(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_fun = function()
        my_fun.set_name("meno")
        my_fun.set_valueOf_("hodnota")
        my_fun.set_scope(scope.PROCESS)
        expectation.append(my_fun)
        doc.set_function(expectation)
        self.assertEqual(doc.function, expectation)

    def test_documentType_add_function(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = function()
        expectation.set_name("meno")
        expectation.set_valueOf_("hodnota")
        expectation.set_scope(scope.PROCESS)
        doc.add_function(expectation)
        self.assertEqual(doc.function[0], expectation)

    def test_documentType_add_wrong_function(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.add_function(i18nStringType())

    def test_documentType_insert_function_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        fun = function()
        fun.set_name("meno")
        fun.set_valueOf_("hodnota")
        fun.set_scope(scope.PROCESS)
        with self.assertRaises(IndexError):
            doc.insert_function_at(1, fun)

    def test_documentType_set_data(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_data = data()
        my_data.set_id("777", doc)
        my_data.set_type_(data_type.BUTTON)
        expectation.append(my_data)
        doc.set_data(expectation)
        self.assertEqual(doc.data, expectation)

    def test_documentType_add_data(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = data()
        expectation.set_id("777", doc)
        expectation.set_type_(data_type.BUTTON)
        doc.add_data(expectation)
        self.assertEqual(doc.data[8], expectation)

    def test_documentType_add_wrong_data(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.add_data(i18nStringType())

    def test_documentType_insert_data_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        dat = data()
        dat.set_id("777", doc)
        dat.set_type_(data_type.BUTTON)
        with self.assertRaises(IndexError):
            doc.insert_data_at(9, dat)

    def test_documentType_set_mapping(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_map = mapping()
        my_map.set_id("ID", doc)
        my_map.set_transitionRef("refer")
        expectation.append(my_map)
        doc.set_mapping(expectation)
        self.assertEqual(doc.mapping, expectation)

    def test_documentType_add_mapping(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = mapping()
        expectation.set_id("ID", doc)
        expectation.set_transitionRef("refer")
        doc.add_mapping(expectation)
        self.assertEqual(doc.mapping[0], expectation)

    def test_documentType_add_wrong_mapping(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.add_mapping(i18nStringType())

    def test_documentType_insert_mapping_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        map_ = mapping()
        map_.set_id("ID", doc)
        map_.set_transitionRef("refer")
        with self.assertRaises(IndexError):
            doc.insert_mapping_at(1, map_)

    def test_documentType_set_i18n(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_str = i18n()
        my_str.set_locale("local")
        expectation.append(my_str)
        doc.set_i18n(expectation)
        self.assertEqual(doc.i18n, expectation)

    def test_documentType_add_i18n(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = i18n()
        expectation.set_locale("local")
        doc.add_i18n(expectation)
        self.assertEqual(doc.i18n[0], expectation)

    def test_documentType_add_wrong_i18n(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.add_i18n(i18nStringType())

    def test_documentType_insert_i18n_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        str_ = i18n()
        str_.set_locale("local")
        with self.assertRaises(IndexError):
            doc.insert_i18n_at(1, str_)

    def test_documentType_set_transition(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_tra = transition()
        my_tra.set_id("ID", doc)
        my_tra.set_x(5)
        my_tra.set_y(12)
        expectation.append(my_tra)
        doc.set_transition(expectation)
        self.assertEqual(doc.transition, expectation)

    def test_documentType_add_transition(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = transition()
        expectation.set_id("ID", doc)
        expectation.set_x(5)
        expectation.set_y(12)
        doc.add_transition(expectation)
        self.assertEqual(doc.transition[15], expectation)

    def test_documentType_add_wrong_transition(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.add_transition(i18nStringType())

    def test_documentType_insert_transition_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        tra = transition()
        tra.set_id("ID", doc)
        tra.set_x(5)
        tra.set_y(12)
        with self.assertRaises(IndexError):
            doc.insert_transition_at(16, tra)

    def test_documentType_set_place(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_p = place()
        my_p.set_id("ID", doc)
        my_p.set_x(20)
        my_p.set_y(100)
        my_p.set_tokens(6)
        my_p.set_static(True)
        expectation.append(my_p)
        doc.set_place(expectation)
        self.assertEqual(doc.place, expectation)

    def test_documentType_add_place(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = place()
        expectation.set_id("ID", doc)
        expectation.set_x(20)
        expectation.set_y(100)
        expectation.set_tokens(6)
        expectation.set_static(True)
        doc.add_place(expectation)
        self.assertEqual(doc.place[15], expectation)

    def test_documentType_add_wrong_place(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.add_place(i18nStringType())

    def test_documentType_insert_place_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        place_ = place()
        place_.set_id("ID", doc)
        place_.set_x(20)
        place_.set_y(100)
        place_.set_tokens(6)
        place_.set_static(True)
        with self.assertRaises(IndexError):
            doc.insert_place_at(16, place_)

    def test_documentType_set_arc(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_arc = arc()
        my_arc.set_id("ID", doc)
        my_arc.set_type_(arc_type.VARIABLE)
        my_arc.set_sourceId("t1_0")
        my_arc.set_destinationId("t15_0")
        my_arc.set_multiplicity(5)
        expectation.append(my_arc)
        doc.set_arc(expectation)
        self.assertEqual(doc.arc, expectation)

    def test_documentType_add_arc(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = arc()
        expectation.set_id("ID", doc)
        expectation.set_type_(arc_type.VARIABLE)
        expectation.set_sourceId("t1_0")
        expectation.set_destinationId("t15_0")
        expectation.set_multiplicity(5)
        doc.add_arc(expectation)
        self.assertEqual(doc.arc[33], expectation)

    def test_documentType_add_wrong_arc(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.add_arc(i18nStringType())

    def test_documentType_insert_arc_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        arc_ = arc()
        arc_.set_id("ID", doc)
        arc_.set_type_(arc_type.VARIABLE)
        arc_.set_sourceId("t1_0")
        arc_.set_destinationId("t15_0")
        arc_.set_multiplicity(5)
        with self.assertRaises(IndexError):
            doc.insert_arc_at(34, arc_)

#  end of documentType tag tests

    def test_breakpoint_set_x(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.arc[0].add_breakpoint(breakpoint())
        expectation = 5
        doc.arc[0].breakpoint[0].set_x(expectation)
        self.assertEqual(doc.arc[0].breakpoint[0].x, expectation)

    def test_breakpoint_set_negative_x(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.arc[0].add_breakpoint(breakpoint())
        with self.assertRaises(ValueError):
            doc.arc[0].breakpoint[0].set_x(-100)

    def test_breakpoint_set_wrong_x(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.arc[0].add_breakpoint(breakpoint())
        with self.assertRaises(TypeError):
            doc.arc[0].breakpoint[0].set_x("5")

    def test_breakpoint_set_y(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.arc[0].add_breakpoint(breakpoint())
        expectation = 12
        doc.arc[0].breakpoint[0].set_y(expectation)
        self.assertEqual(doc.arc[0].breakpoint[0].y, expectation)

    def test_breakpoint_set_negative_y(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.arc[0].add_breakpoint(breakpoint())
        with self.assertRaises(ValueError):
            doc.arc[0].breakpoint[0].set_y(-55)

    def test_breakpoint_set_wrong_y(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.arc[0].add_breakpoint(breakpoint())
        with self.assertRaises(TypeError):
            doc.arc[0].breakpoint[0].set_y(i18nStringType())

#  end of breakpoint tag tests

    def test_options_set_option_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_data(data())
        doc.data[8].set_options(options())
        choice_child = init()
        choice_child.set_name("meno")
        choice_child.set_dynamic(True)
        choice_child.set_valueOf_("hodnota")
        choice_child.set_original_tagname_('init')
        doc.data[8].options.set_init(choice_child)
        with self.assertRaises(ValueError):
            choice_child_2 = []
            opt = option()
            opt.set_valueOf_("moznost")
            opt.set_name('meno')
            opt.set_original_tagname_('option')
            opt.set_key("K1", doc)
            choice_child_2.append(opt)
            doc.data[8].options.set_option(choice_child_2)

    def test_documentType_set_option(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_data(data())
        doc.data[8].set_options(options())
        expectation = []
        my_opt = option()
        my_opt.set_key("K1", doc)
        my_opt.set_valueOf_("hodnota")
        expectation.append(my_opt)
        doc.data[8].options.set_option(expectation)
        self.assertEqual(doc.data[8].options.option, expectation)

    def test_documentType_add_option(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_data(data())
        doc.data[8].set_options(options())
        expectation = option()
        expectation.set_key("K1", doc)
        expectation.set_valueOf_("hodnota")
        doc.data[8].options.add_option(expectation)
        self.assertEqual(doc.data[8].options.option[0], expectation)

    def test_documentType_add_wrong_option(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_data(data())
        doc.data[8].set_options(options())
        with self.assertRaises(TypeError):
            doc.data[8].options.add_option(i18nStringType())

    def test_documentType_insert_option_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_data(data())
        doc.data[8].set_options(options())
        opt = option()
        opt.set_key("K1", doc)
        opt.set_valueOf_("hodnota")
        with self.assertRaises(IndexError):
            doc.data[8].options.insert_option_at(8, opt)

    def test_options_set_init_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_data(data())
        doc.data[8].set_options(options())
        choice_child_2 = []
        opt = option()
        opt.set_valueOf_("moznost")
        opt.set_name('meno')
        opt.set_original_tagname_('option')
        opt.set_key("K1", doc)
        choice_child_2.append(opt)
        doc.data[8].options.set_option(choice_child_2)
        with self.assertRaises(ValueError):
            choice_child = init()
            choice_child.set_name("meno")
            choice_child.set_dynamic(True)
            choice_child.set_valueOf_("hodnota")
            choice_child.set_original_tagname_('init')
            doc.data[8].options.set_init(choice_child)

    def test_options_set_init(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_data(data())
        doc.data[8].set_options(options())
        expectation = init()
        expectation.set_valueOf_("initka")
        expectation.set_name("meno")
        expectation.set_dynamic(False)
        expectation.set_original_tagname_('init')
        doc.data[8].options.set_init(expectation)
        self.assertEqual(doc.data[8].options.init, expectation)

    def test_options_set_wrong_init(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_data(data())
        doc.data[8].set_options(options())
        with self.assertRaises(TypeError):
            doc.data[8].options.set_init(i18nStringType())

#  end of options tag tests

    def test_inits_set_option(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_inits(inits())
        expectation = []
        my_init = init()
        my_init.set_valueOf_("val")
        expectation.append(my_init)
        doc.data[0].inits.set_init(expectation)
        self.assertEqual(doc.data[0].inits.init, expectation)

    def test_inits_add_option(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_inits(inits())
        expectation = init()
        expectation.set_valueOf_("val")
        doc.data[0].inits.add_init(expectation)
        self.assertEqual(doc.data[0].inits.init[0], expectation)

    def test_inits_add_wrong_option(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_inits(inits())
        with self.assertRaises(TypeError):
            doc.data[0].inits.add_init(i18nStringType())

    def test_inits_insert_option_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_inits(inits())
        init_ = init()
        init_.set_valueOf_("val")
        with self.assertRaises(IndexError):
            doc.data[0].inits.insert_init_at(1, init_)

#  end of inits tag tests

    def test_expression_set_dynamic(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_validations(validations())
        doc.data[0].validations.add_validation(validation())
        doc.data[0].validations.validation[0].set_expression(valid())
        expectation = 'false'
        doc.data[0].validations.validation[0].expression.set_dynamic(expectation)
        self.assertEqual(doc.data[0].validations.validation[0].expression.dynamic, expectation)

    def test_expression_set_wrong_dynamic(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_validations(validations())
        doc.data[0].validations.add_validation(validation())
        doc.data[0].validations.validation[0].set_expression(valid())
        with self.assertRaises(TypeError):
            doc.data[0].validations.validation[0].expression.set_dynamic(i18nStringType())

    def test_expression_set_valueOf_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_validations(validations())
        doc.data[0].validations.add_validation(validation())
        doc.data[0].validations.validation[0].set_expression(valid())
        expectation = "hodnota"
        doc.data[0].validations.validation[0].expression.set_valueOf_(expectation)
        self.assertEqual(doc.data[0].validations.validation[0].expression.valueOf_, expectation)

    def test_expression_set_wrong_valueOf_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_validations(validations())
        doc.data[0].validations.add_validation(validation())
        doc.data[0].validations.validation[0].set_expression(valid())
        with self.assertRaises(TypeError):
            doc.data[0].validations.validation[0].expression.set_valueOf_(100)

#  end of expression tag tests

    def test_component_set_name(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        expectation = "meno"
        doc.data[0].component.set_name(expectation)
        self.assertEqual(doc.data[0].component.name, expectation)

    def test_component_set_wrong_name(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        with self.assertRaises(TypeError):
            doc.data[0].component.set_name(i18nStringType())

    def test_component_set_property_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        choice_child_1 = properties()
        doc.data[0].component.set_properties(choice_child_1)
        with self.assertRaises(ValueError):
            choice_child_2 = []
            prop = property()
            prop.set_valueOf_("hodnota")
            prop.set_key("K2")
            choice_child_2.append(prop)
            doc.data[0].component.set_property(choice_child_2)

    def test_component_set_property(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        expectation = []
        my_prop = property()
        my_prop.set_valueOf_("val")
        my_prop.set_key("K2")
        expectation.append(my_prop)
        doc.data[0].component.set_property(expectation)
        self.assertEqual(doc.data[0].component.property, expectation)

    def test_component_add_property(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        expectation = property()
        expectation.set_valueOf_("val")
        expectation.set_key("K2")
        doc.data[0].component.add_property(expectation)
        self.assertEqual(doc.data[0].component.property[0], expectation)

    def test_component_add_wrong_property(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        with self.assertRaises(TypeError):
            doc.data[0].component.add_property(i18nStringType())

    def test_component_insert_property_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        prop_ = property()
        prop_.set_valueOf_("val")
        prop_.set_key("K2")
        with self.assertRaises(IndexError):
            doc.data[0].component.insert_property_at(1, prop_)

    def test_component_set_properties_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        choice_child_1 = []
        prop = property()
        prop.set_valueOf_("hodnota")
        prop.set_key("K2")
        choice_child_1.append(prop)
        doc.data[0].component.set_property(choice_child_1)
        with self.assertRaises(ValueError):
            choice_child_2 = properties()
            doc.data[0].component.set_properties(choice_child_2)

    def test_component_set_properties(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        expectation = properties()
        doc.data[0].component.set_properties(expectation)
        self.assertEqual(doc.data[0].component.properties, expectation)

    def test_component_set_wrong_properties(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        with self.assertRaises(TypeError):
            doc.data[0].component.set_properties(i18nStringType())

#  end of component tag tests

    def test_property_set_key(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        doc.data[0].component.add_property(property())
        expectation = "kluc"
        doc.data[0].component.property[0].set_key(expectation)
        self.assertEqual(doc.data[0].component.property[0].key, expectation)

    def test_property_set_wrong_key(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        doc.data[0].component.add_property(property())
        with self.assertRaises(TypeError):
            doc.data[0].component.property[0].set_key(i18nStringType())

    def test_property_set_valueOf_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        doc.data[0].component.add_property(property())
        expectation = "hodnota"
        doc.data[0].component.property[0].set_valueOf_(expectation)
        self.assertEqual(doc.data[0].component.property[0].valueOf_, expectation)

    def test_property_set_wrong_valueOf_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        doc.data[0].component.add_property(property())
        with self.assertRaises(TypeError):
            doc.data[0].component.property[0].set_valueOf_(i18nStringType())

#  end of property tag tests

    def test_properties_set_property(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        doc.data[0].component.set_properties(properties())
        expectation = []
        my_prop = property()
        my_prop.set_valueOf_("val")
        my_prop.set_key("K2")
        expectation.append(my_prop)
        doc.data[0].component.properties.set_property(expectation)
        self.assertEqual(doc.data[0].component.properties.property, expectation)

    def test_properties_add_property(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        doc.data[0].component.set_properties(properties())
        expectation = property()
        expectation.set_valueOf_("val")
        expectation.set_key("K2")
        doc.data[0].component.properties.add_property(expectation)
        self.assertEqual(doc.data[0].component.properties.property[0], expectation)

    def test_properties_add_wrong_property(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        doc.data[0].component.set_properties(properties())
        with self.assertRaises(TypeError):
            doc.data[0].component.properties.add_property(i18nStringType())

    def test_properties_insert_property_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        doc.data[0].component.set_properties(properties())
        prop_ = property()
        prop_.set_valueOf_("val")
        prop_.set_key("K2")
        with self.assertRaises(IndexError):
            doc.data[0].component.properties.insert_property_at(1, prop_)

    def test_properties_set_option_icons(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        doc.data[0].component.set_properties(properties())
        expectation = icons()
        doc.data[0].component.properties.set_option_icons(expectation)
        self.assertEqual(doc.data[0].component.properties.option_icons, expectation)

    def test_properties_set_wrong_option_icons(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        doc.data[0].component.set_properties(properties())
        with self.assertRaises(TypeError):
            doc.data[0].component.properties.set_option_icons(icon())

#  end of properties tag tests

    def test_icons_set_icon(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        doc.data[0].component.set_properties(properties())
        doc.data[0].component.properties.set_option_icons(icons())
        expectation = []
        my_icon = icon()
        my_icon.set_key("K3")
        my_icon.set_valueOf_("hodnota")
        my_icon.set_type_(iconType.SVG)
        expectation.append(my_icon)
        doc.data[0].component.properties.option_icons.set_icon(expectation)
        self.assertEqual(doc.data[0].component.properties.option_icons.icon, expectation)

    def test_icons_add_icon(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        doc.data[0].component.set_properties(properties())
        doc.data[0].component.properties.set_option_icons(icons())
        expectation = icon()
        expectation.set_key("K3")
        expectation.set_valueOf_("hodnota")
        expectation.set_type_(iconType.SVG)
        doc.data[0].component.properties.option_icons.add_icon(expectation)
        self.assertEqual(doc.data[0].component.properties.option_icons.icon[0], expectation)

    def test_icons_add_wrong_icon(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        doc.data[0].component.set_properties(properties())
        doc.data[0].component.properties.set_option_icons(icons())
        with self.assertRaises(TypeError):
            doc.data[0].component.properties.option_icons.add_icon(i18nStringType())

    def test_icons_insert_icon_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        doc.data[0].component.set_properties(properties())
        doc.data[0].component.properties.set_option_icons(icons())
        icon_ = icon()
        icon_.set_key("K3")
        icon_.set_valueOf_("hodnota")
        icon_.set_type_(iconType.SVG)
        with self.assertRaises(IndexError):
            doc.data[0].component.properties.option_icons.insert_icon_at(1, icon_)

#  end of icons tag tests

    def test_icon_set_key(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        doc.data[0].component.set_properties(properties())
        doc.data[0].component.properties.set_option_icons(icons())
        doc.data[0].component.properties.option_icons.add_icon(icon())
        expectation = "K4"
        doc.data[0].component.properties.option_icons.icon[0].set_key(expectation)
        self.assertEqual(doc.data[0].component.properties.option_icons.icon[0].key, expectation)

    def test_icon_set_wrong_key(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        doc.data[0].component.set_properties(properties())
        doc.data[0].component.properties.set_option_icons(icons())
        doc.data[0].component.properties.option_icons.add_icon(icon())
        with self.assertRaises(TypeError):
            doc.data[0].component.properties.option_icons.icon[0].set_key(i18nStringType())

    def test_icon_set_type_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        doc.data[0].component.set_properties(properties())
        doc.data[0].component.properties.set_option_icons(icons())
        doc.data[0].component.properties.option_icons.add_icon(icon())
        expectation = iconType.MATERIAL
        doc.data[0].component.properties.option_icons.icon[0].set_type_(expectation)
        self.assertEqual(doc.data[0].component.properties.option_icons.icon[0].type_, expectation)

    def test_icon_set_wrong_type_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        doc.data[0].component.set_properties(properties())
        doc.data[0].component.properties.set_option_icons(icons())
        doc.data[0].component.properties.option_icons.add_icon(icon())
        with self.assertRaises(TypeError):
            doc.data[0].component.properties.option_icons.icon[0].set_type_("type")

    def test_icon_set_valueOf_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        doc.data[0].component.set_properties(properties())
        doc.data[0].component.properties.set_option_icons(icons())
        doc.data[0].component.properties.option_icons.add_icon(icon())
        expectation = "hodnota"
        doc.data[0].component.properties.option_icons.icon[0].set_valueOf_(expectation)
        self.assertEqual(doc.data[0].component.properties.option_icons.icon[0].valueOf_, expectation)

    def test_icon_set_wrong_valueOf_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_component(component())
        doc.data[0].component.set_properties(properties())
        doc.data[0].component.properties.set_option_icons(icons())
        doc.data[0].component.properties.option_icons.add_icon(icon())
        with self.assertRaises(TypeError):
            doc.data[0].component.properties.option_icons.icon[0].set_valueOf_(i18nStringType())

#  end of icon tag tests

    def test_allowedNets_set_allowedNet(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_allowedNets(allowedNets())
        expectation = []
        my_net = "siet"
        expectation.append(my_net)
        doc.data[0].allowedNets.set_allowedNet(expectation)
        self.assertEqual(doc.data[0].allowedNets.allowedNet, expectation)

    def test_allowedNets_add_allowedNet(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_allowedNets(allowedNets())
        expectation = "siet"
        doc.data[0].allowedNets.add_allowedNet(expectation)
        self.assertEqual(doc.data[0].allowedNets.allowedNet[0], expectation)

    def test_allowedNets_add_wrong_allowedNet(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_allowedNets(allowedNets())
        with self.assertRaises(TypeError):
            doc.data[0].allowedNets.add_allowedNet(i18nStringType())

    def test_allowedNets_insert_allowedNet_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_allowedNets(allowedNets())
        net = "siet"
        with self.assertRaises(IndexError):
            doc.data[0].allowedNets.insert_allowedNet_at(1, net)

#  end of allowedNets tag tests

    def test_logic_set_perform(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        expectation = 'false'
        doc.transition[0].roleRef[0].logic.set_perform(expectation)
        self.assertEqual(doc.transition[0].roleRef[0].logic.perform, expectation)

    def test_logic_set_wrong_perform(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        with self.assertRaises(TypeError):
            doc.transition[0].roleRef[0].logic.set_perform("performation")

    def test_logic_set_delegate(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        expectation = 'true'
        doc.transition[0].roleRef[0].logic.set_delegate(expectation)
        self.assertEqual(doc.transition[0].roleRef[0].logic.delegate, expectation)

    def test_logic_set_wrong_delegate(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        with self.assertRaises(TypeError):
            doc.transition[0].roleRef[0].logic.set_delegate("delegation")

    def test_logic_set_view(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        expectation = 'false'
        doc.transition[0].roleRef[0].logic.set_view(expectation)
        self.assertEqual(doc.transition[0].roleRef[0].logic.view, expectation)

    def test_logic_set_wrong_view(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        with self.assertRaises(TypeError):
            doc.transition[0].roleRef[0].logic.set_view("viewer")

    def test_logic_set_cancel(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        expectation = 'true'
        doc.transition[0].roleRef[0].logic.set_cancel(expectation)
        self.assertEqual(doc.transition[0].roleRef[0].logic.cancel, expectation)

    def test_logic_set_wrong_cancel(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        with self.assertRaises(TypeError):
            doc.transition[0].roleRef[0].logic.set_cancel("cancelation")

    def test_logic_set_finish(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        expectation = 'false'
        doc.transition[0].roleRef[0].logic.set_finish(expectation)
        self.assertEqual(doc.transition[0].roleRef[0].logic.finish, expectation)

    def test_logic_set_wrong_finish(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        with self.assertRaises(TypeError):
            doc.transition[0].roleRef[0].logic.set_finish("finishion")

    def test_logic_set_assigned_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        choice_child_1 = True
        doc.transition[0].roleRef[0].logic.set_assign(choice_child_1)
        with self.assertRaises(ValueError):
            choice_child_2 = False
            doc.transition[0].roleRef[0].logic.set_assigned(choice_child_2)

    def test_logic_set_assigned(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        expectation = 'false'
        doc.transition[0].roleRef[0].logic.set_assigned(expectation)
        self.assertEqual(doc.transition[0].roleRef[0].logic.assigned, expectation)

    def test_logic_set_wrong_assigned(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        with self.assertRaises(TypeError):
            doc.transition[0].roleRef[0].logic.set_assigned("zapisany")

    def test_logic_set_assign_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        choice_child_1 = False
        doc.transition[0].roleRef[0].logic.set_assigned(choice_child_1)
        with self.assertRaises(ValueError):
            choice_child_2 = True
            doc.transition[0].roleRef[0].logic.set_assign(choice_child_2)

    def test_logic_set_assign(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        expectation = 'true'
        doc.transition[0].roleRef[0].logic.set_assign(expectation)
        self.assertEqual(doc.transition[0].roleRef[0].logic.assign, expectation)

    def test_logic_set_wrong_assign(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        with self.assertRaises(TypeError):
            doc.transition[0].roleRef[0].logic.set_assign("zapis")

    def test_logic_set_behavior(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        expectation = []
        my_beha = behavior.FORBIDDEN
        expectation.append(my_beha)
        doc.transition[0].roleRef[0].logic.set_behavior(expectation)
        self.assertEqual(doc.transition[0].roleRef[0].logic.behavior, expectation)

    def test_logic_add_behavior(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        expectation = behavior.EDITABLE
        doc.transition[0].roleRef[0].logic.add_behavior(expectation)
        self.assertEqual(doc.transition[0].roleRef[0].logic.behavior[0], expectation)

    def test_logic_add_wrong_behavior(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        with self.assertRaises(TypeError):
            doc.transition[0].roleRef[0].logic.add_behavior("WILD")

    def test_logic_insert_behavior_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        beha = behavior.HIDDEN
        with self.assertRaises(IndexError):
            doc.transition[0].roleRef[0].logic.insert_behavior_at(1, beha)

    def test_logic_set_action(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        expectation = []
        my_act = action()
        my_act.set_id("ID")
        my_act.set_valueOf_("hodnota")
        my_act.set_trigger("triggered")
        expectation.append(my_act)
        doc.transition[0].roleRef[0].logic.set_action(expectation)
        self.assertEqual(doc.transition[0].roleRef[0].logic.action, expectation)

    def test_logic_add_action(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        expectation = action()
        expectation.set_id("ID")
        expectation.set_valueOf_("hodnota")
        expectation.set_trigger("triggered")
        doc.transition[0].roleRef[0].logic.add_action(expectation)
        self.assertEqual(doc.transition[0].roleRef[0].logic.action[0], expectation)

    def test_logic_add_wrong_action(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        with self.assertRaises(TypeError):
            doc.transition[0].roleRef[0].logic.add_action(i18nStringType())

    def test_logic_insert_action_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        act = action()
        act.set_id("ID")
        act.set_valueOf_("hodnota")
        act.set_trigger("triggered")
        with self.assertRaises(IndexError):
            doc.transition[0].roleRef[0].logic.insert_action_at(1, act)

    def test_logic_set_actionRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        expectation = []
        my_ref = actionRef()
        my_ref.set_id("REF")
        expectation.append(my_ref)
        doc.transition[0].roleRef[0].logic.set_actionRef(expectation)
        self.assertEqual(doc.transition[0].roleRef[0].logic.actionRef, expectation)

    def test_logic_add_actionRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        expectation = actionRef()
        expectation.set_id("REF")
        doc.transition[0].roleRef[0].logic.add_actionRef(expectation)
        self.assertEqual(doc.transition[0].roleRef[0].logic.actionRef[0], expectation)

    def test_logic_add_wrong_actionRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        with self.assertRaises(TypeError):
            doc.transition[0].roleRef[0].logic.add_actionRef(i18nStringType())

    def test_logic_insert_actionRef_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        doc.transition[0].roleRef[0].set_logic(logic())
        ref = actionRef()
        ref.set_id("REF")
        with self.assertRaises(IndexError):
            doc.transition[0].roleRef[0].logic.insert_actionRef_at(1, ref)

#  end of logic tag tests

    def test_caseLogic_set_create(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_roleRef(caseRoleRef())
        doc.roleRef[0].set_caseLogic(caseLogic())
        expectation = 'false'
        doc.roleRef[0].caseLogic.set_create(expectation)
        self.assertEqual(doc.roleRef[0].caseLogic.create, expectation)

    def test_caseLogic_set_wrong_create(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_roleRef(caseRoleRef())
        doc.roleRef[0].set_caseLogic(caseLogic())
        with self.assertRaises(TypeError):
            doc.roleRef[0].caseLogic.set_create(i18nStringType())

    def test_caseLogic_set_delete(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_roleRef(caseRoleRef())
        doc.roleRef[0].set_caseLogic(caseLogic())
        expectation = 'false'
        doc.roleRef[0].caseLogic.set_delete(expectation)
        self.assertEqual(doc.roleRef[0].caseLogic.delete, expectation)

    def test_caseLogic_set_wrong_delete(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_roleRef(caseRoleRef())
        doc.roleRef[0].set_caseLogic(caseLogic())
        with self.assertRaises(TypeError):
            doc.roleRef[0].caseLogic.set_delete("delete")

    def test_caseLogic_set_view(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_roleRef(caseRoleRef())
        doc.roleRef[0].set_caseLogic(caseLogic())
        expectation = 'false'
        doc.roleRef[0].caseLogic.set_view(expectation)
        self.assertEqual(doc.roleRef[0].caseLogic.view, expectation)

    def test_caseLogic_set_wrong_view(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_roleRef(caseRoleRef())
        doc.roleRef[0].set_caseLogic(caseLogic())
        with self.assertRaises(TypeError):
            doc.roleRef[0].caseLogic.set_view(i18nStringType())

    def test_caseLogic_set_action(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_roleRef(caseRoleRef())
        doc.roleRef[0].set_caseLogic(caseLogic())
        expectation = []
        my_act = action()
        my_act.set_id("ACT")
        expectation.append(my_act)
        doc.roleRef[0].caseLogic.set_action(expectation)
        self.assertEqual(doc.roleRef[0].caseLogic.action, expectation)

    def test_caseLogic_add_action(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_roleRef(caseRoleRef())
        doc.roleRef[0].set_caseLogic(caseLogic())
        expectation = action()
        expectation.set_id("ACT")
        doc.roleRef[0].caseLogic.add_action(expectation)
        self.assertEqual(doc.roleRef[0].caseLogic.action[0], expectation)

    def test_caseLogic_add_wrong_action(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_roleRef(caseRoleRef())
        doc.roleRef[0].set_caseLogic(caseLogic())
        with self.assertRaises(TypeError):
            doc.roleRef[0].caseLogic.add_action(i18nStringType())

    def test_caseLogic_insert_action_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_roleRef(caseRoleRef())
        doc.roleRef[0].set_caseLogic(caseLogic())
        act = action()
        act.set_id("ACT")
        with self.assertRaises(IndexError):
            doc.roleRef[0].caseLogic.insert_action_at(1, act)

    def test_caseLogic_set_actionRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_roleRef(caseRoleRef())
        doc.roleRef[0].set_caseLogic(caseLogic())
        expectation = []
        my_ref = actionRef()
        my_ref.set_id("REF")
        expectation.append(my_ref)
        doc.roleRef[0].caseLogic.set_actionRef(expectation)
        self.assertEqual(doc.roleRef[0].caseLogic.actionRef, expectation)

    def test_caseLogic_add_actionRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_roleRef(caseRoleRef())
        doc.roleRef[0].set_caseLogic(caseLogic())
        expectation = actionRef()
        expectation.set_id("REF")
        doc.roleRef[0].caseLogic.add_actionRef(expectation)
        self.assertEqual(doc.roleRef[0].caseLogic.actionRef[0], expectation)

    def test_caseLogic_add_wrong_actionRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_roleRef(caseRoleRef())
        doc.roleRef[0].set_caseLogic(caseLogic())
        with self.assertRaises(TypeError):
            doc.roleRef[0].caseLogic.add_actionRef("referencia")

    def test_caseLogic_insert_actionRef_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_roleRef(caseRoleRef())
        doc.roleRef[0].set_caseLogic(caseLogic())
        ref = actionRef()
        ref.set_id("REF")
        with self.assertRaises(IndexError):
            doc.roleRef[0].caseLogic.insert_actionRef_at(1, ref)

#  end of caseLogic tag tests

    def test_transactionRef_set_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].set_transactionRef(transactionRef())
        expectation = '555'
        doc.transition[0].transactionRef.set_id(expectation)
        self.assertEqual(doc.transition[0].transactionRef.id, expectation)

    def test_transactionRef_set_wrong_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].set_transactionRef(transactionRef())
        with self.assertRaises(TypeError):
            doc.transition[0].transactionRef.set_id(555)

#  end of transactionRef tag tests

    def test_permissionRef_set_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        expectation = '555'
        doc.transition[0].roleRef[0].set_id(expectation)
        self.assertEqual(doc.transition[0].roleRef[0].id, expectation)

    def test_permissionRef_set_wrong_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        with self.assertRaises(TypeError):
            doc.transition[0].roleRef[0].set_id(i18nStringType())

    def test_permissionRef_set_logic(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        expectation = logic()
        expectation.set_cancel(False)
        expectation.set_finish(False)
        expectation.set_view(True)
        expectation.set_perform(True)
        expectation.set_delegate(True)
        expectation.set_assigned(True)
        expectation.add_behavior(behavior.REQUIRED)
        doc.transition[0].roleRef[0].set_logic(expectation)
        self.assertEqual(doc.transition[0].roleRef[0].logic, expectation)

    def test_permissionRef_set_wrong_logic(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_roleRef(roleRef())
        with self.assertRaises(TypeError):
            doc.transition[0].roleRef[0].set_logic("logic")

#  end of permissionRef tag tests

    def test_casePermissionRef_set_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_roleRef(caseRoleRef())
        expectation = 'ID'
        doc.roleRef[0].set_id(expectation)
        self.assertEqual(doc.roleRef[0].id, expectation)

    def test_casePermissionRef_set_wrong_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_roleRef(caseRoleRef())
        with self.assertRaises(TypeError):
            doc.roleRef[0].set_id(777)

    def test_casePermissionRef_set_logic(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_roleRef(caseRoleRef())
        expectation = caseLogic()
        expectation.set_create(True)
        expectation.set_delete(False)
        expectation.set_view(False)
        doc.roleRef[0].set_caseLogic(expectation)
        self.assertEqual(doc.roleRef[0].caseLogic, expectation)

    def test_casePermissionRef_set_wrong_logic(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.add_roleRef(caseRoleRef())
        with self.assertRaises(TypeError):
            doc.roleRef[0].set_caseLogic(i18nStringType())

#  end of casePermissionRef tag tests

    def test_dataRef_set_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        expectation = 'ID'
        doc.transition[0].dataRef[0].set_id(expectation)
        self.assertEqual(doc.transition[0].dataRef[0].id, expectation)

    def test_dataRef_set_wrong_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        with self.assertRaises(TypeError):
            doc.transition[0].dataRef[0].set_id(100)

    def test_dataRef_set_logic(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        expectation = logic()
        expectation.set_cancel(False)
        expectation.set_finish(False)
        expectation.set_view(True)
        expectation.set_perform(True)
        expectation.set_delegate(True)
        expectation.set_assigned(True)
        expectation.add_behavior(behavior.FORBIDDEN)
        doc.transition[0].dataRef[0].set_logic(expectation)
        self.assertEqual(doc.transition[0].dataRef[0].logic, expectation)

    def test_dataRef_set_wrong_logic(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        with self.assertRaises(TypeError):
            doc.transition[0].dataRef[0].set_logic(i18nStringType())

    def test_dataRef_set_layout(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        expectation = layout()
        expectation.set_x(1)
        expectation.set_y(10)
        expectation.set_cols(5)
        expectation.set_rows(12)
        expectation.set_offset(55)
        doc.transition[0].dataRef[0].set_layout(expectation)
        self.assertEqual(doc.transition[0].dataRef[0].layout, expectation)

    def test_dataRef_set_wrong_layout(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        with self.assertRaises(TypeError):
            doc.transition[0].dataRef[0].set_layout(transitionLayout())

    def test_dataRef_set_component(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        expectation = component()
        expectation.set_name("meno")
        doc.transition[0].dataRef[0].set_component(expectation)
        self.assertEqual(doc.transition[0].dataRef[0].component, expectation)

    def test_dataRef_set_wrong_component(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        with self.assertRaises(TypeError):
            doc.transition[0].dataRef[0].set_component("component")

    def test_dataRef_set_event(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        expectation = []
        my_eve = dataEvent()
        my_eve.set_id("1406")
        my_eve.set_type_(dataEventType.SET)
        msg = i18nStringType()
        msg.set_name("meno")
        msg.set_valueOf_("sprava")
        msg.set_original_tagname_('message')
        my_eve.set_message(msg)
        expectation.append(my_eve)
        doc.transition[0].dataRef[0].set_event(expectation)
        self.assertEqual(doc.transition[0].dataRef[0].event, expectation)

    def test_dataRef_add_event(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        expectation = dataEvent()
        expectation.set_id("1406")
        expectation.set_type_(dataEventType.SET)
        msg = i18nStringType()
        msg.set_name("meno")
        msg.set_valueOf_("sprava")
        msg.set_original_tagname_('message')
        expectation.set_message(msg)
        doc.transition[0].dataRef[0].add_event(expectation)
        self.assertEqual(doc.transition[0].dataRef[0].event[0], expectation)

    def test_dataRef_add_wrong_event(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        with self.assertRaises(TypeError):
            doc.transition[0].dataRef[0].add_event("event")

    def test_dataRef_insert_event_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        eve = dataEvent()
        eve.set_id("1406")
        eve.set_type_(dataEventType.SET)
        msg = i18nStringType()
        msg.set_name("meno")
        msg.set_valueOf_("sprava")
        msg.set_original_tagname_('message')
        eve.set_message(msg)
        with self.assertRaises(IndexError):
            doc.transition[0].dataRef[0].insert_event_at(1, eve)

#  end of dataRef tag tests

    def test_layout_set_x(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        doc.transition[0].dataRef[0].set_layout(layout())
        expectation = 5
        doc.transition[0].dataRef[0].layout.set_x(expectation)
        self.assertEqual(doc.transition[0].dataRef[0].layout.x, expectation)

    def test_layout_set_negative_x(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        doc.transition[0].dataRef[0].set_layout(layout())
        with self.assertRaises(ValueError):
            doc.transition[0].dataRef[0].layout.set_x(-10)

    def test_layout_set_wrong_x(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        doc.transition[0].dataRef[0].set_layout(layout())
        with self.assertRaises(TypeError):
            doc.transition[0].dataRef[0].layout.set_x("x")

    def test_layout_set_y(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        doc.transition[0].dataRef[0].set_layout(layout())
        expectation = 5
        doc.transition[0].dataRef[0].layout.set_y(expectation)
        self.assertEqual(doc.transition[0].dataRef[0].layout.y, expectation)

    def test_layout_set_negative_y(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        doc.transition[0].dataRef[0].set_layout(layout())
        with self.assertRaises(ValueError):
            doc.transition[0].dataRef[0].layout.set_y(-20)

    def test_layout_set_wrong_y(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        doc.transition[0].dataRef[0].set_layout(layout())
        with self.assertRaises(TypeError):
            doc.transition[0].dataRef[0].layout.set_y(i18nStringType())

    def test_layout_set_rows(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        doc.transition[0].dataRef[0].set_layout(layout())
        expectation = 5
        doc.transition[0].dataRef[0].layout.set_rows(expectation)
        self.assertEqual(doc.transition[0].dataRef[0].layout.rows, expectation)

    def test_layout_set_negative_rows(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        doc.transition[0].dataRef[0].set_layout(layout())
        with self.assertRaises(ValueError):
            doc.transition[0].dataRef[0].layout.set_rows(-30)

    def test_layout_set_wrong_rows(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        doc.transition[0].dataRef[0].set_layout(layout())
        with self.assertRaises(TypeError):
            doc.transition[0].dataRef[0].layout.set_rows("rows")

    def test_layout_set_cols(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        doc.transition[0].dataRef[0].set_layout(layout())
        expectation = 5
        doc.transition[0].dataRef[0].layout.set_cols(expectation)
        self.assertEqual(doc.transition[0].dataRef[0].layout.cols, expectation)

    def test_layout_set_negative_cols(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        doc.transition[0].dataRef[0].set_layout(layout())
        with self.assertRaises(ValueError):
            doc.transition[0].dataRef[0].layout.set_cols(-40)

    def test_layout_set_wrong_cols(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        doc.transition[0].dataRef[0].set_layout(layout())
        with self.assertRaises(TypeError):
            doc.transition[0].dataRef[0].layout.set_cols(i18nStringType())

    def test_layout_set_offset(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        doc.transition[0].dataRef[0].set_layout(layout())
        expectation = 5
        doc.transition[0].dataRef[0].layout.set_offset(expectation)
        self.assertEqual(doc.transition[0].dataRef[0].layout.offset, expectation)

    def test_layout_set_negative_offset(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        doc.transition[0].dataRef[0].set_layout(layout())
        with self.assertRaises(ValueError):
            doc.transition[0].dataRef[0].layout.set_offset(-50)

    def test_layout_set_wrong_offset(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        doc.transition[0].dataRef[0].set_layout(layout())
        with self.assertRaises(TypeError):
            doc.transition[0].dataRef[0].layout.set_offset("offset")

    def test_layout_set_template(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        doc.transition[0].dataRef[0].set_layout(layout())
        expectation = template.NETGRIF
        doc.transition[0].dataRef[0].layout.set_template(expectation)
        self.assertEqual(doc.transition[0].dataRef[0].layout.template, expectation)

    def test_layout_set_wrong_template(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        doc.transition[0].dataRef[0].set_layout(layout())
        with self.assertRaises(TypeError):
            doc.transition[0].dataRef[0].layout.set_template("CHATGPT")

    def test_layout_set_appearance(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        doc.transition[0].dataRef[0].set_layout(layout())
        expectation = appearance.FILL
        doc.transition[0].dataRef[0].layout.set_appearance(expectation)
        self.assertEqual(doc.transition[0].dataRef[0].layout.appearance, expectation)

    def test_layout_set_wrong_appearance(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        doc.transition[0].dataRef[0].set_layout(layout())
        with self.assertRaises(TypeError):
            doc.transition[0].dataRef[0].layout.set_appearance(i18nStringType())

    def test_layout_set_alignment(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        doc.transition[0].dataRef[0].set_layout(layout())
        expectation = fieldAlignment.TOP
        doc.transition[0].dataRef[0].layout.set_alignment(expectation)
        self.assertEqual(doc.transition[0].dataRef[0].layout.alignment, expectation)

    def test_layout_set_wrong_alignment(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_dataRef(dataRef())
        doc.transition[0].dataRef[0].set_layout(layout())
        with self.assertRaises(TypeError):
            doc.transition[0].dataRef[0].layout.set_alignment("TOP")

#  end of layout tag tests

    def test_assignedUser_set_cancel(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].set_assignedUser(assignedUser())
        expectation = 'true'
        doc.transition[0].assignedUser.set_cancel(expectation)
        self.assertEqual(doc.transition[0].assignedUser.cancel, expectation)

    def test_assignedUser_set_wrong_cancel(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].set_assignedUser(assignedUser())
        with self.assertRaises(TypeError):
            doc.transition[0].assignedUser.set_cancel("cancel")

    def test_assignedUser_set_reassign(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].set_assignedUser(assignedUser())
        expectation = 'false'
        doc.transition[0].assignedUser.set_reassign(expectation)
        self.assertEqual(doc.transition[0].assignedUser.reassign, expectation)

    def test_assignedUser_set_wrong_reassign(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].set_assignedUser(assignedUser())
        with self.assertRaises(TypeError):
            doc.transition[0].assignedUser.set_reassign(i18nStringType())

#  end of assignedUser tag tests

    def test_dataGroup_set_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = '555'
        doc.transition[0].dataGroup[0].set_id(expectation)
        self.assertEqual(doc.transition[0].dataGroup[0].id, expectation)

    def test_dataGroup_set_wrong_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].dataGroup[0].set_id(555)

    def test_dataGroup_set_cols(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = 5
        doc.transition[0].dataGroup[0].set_cols(expectation)
        self.assertEqual(doc.transition[0].dataGroup[0].cols, expectation)

    def test_dataGroup_set_negative_cols(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(ValueError):
            doc.transition[0].dataGroup[0].set_cols(-5)

    def test_dataGroup_set_wrong_cols(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].dataGroup[0].set_cols("5")

    def test_dataGroup_set_rows(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = 12
        doc.transition[0].dataGroup[0].set_rows(expectation)
        self.assertEqual(doc.transition[0].dataGroup[0].rows, expectation)

    def test_dataGroup_set_negative_rows(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(ValueError):
            doc.transition[0].dataGroup[0].set_rows(-12)

    def test_dataGroup_set_wrong_rows(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].dataGroup[0].set_rows("12")

    def test_dataGroup_set_layout(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = layoutType.FLOW
        doc.transition[0].dataGroup[0].set_layout(expectation)
        self.assertEqual(doc.transition[0].dataGroup[0].layout, expectation)

    def test_dataGroup_set_wrong_layout(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].dataGroup[0].set_layout(i18nStringType())

    def test_dataGroup_set_title(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = i18nStringType()
        expectation.set_name("meno")
        expectation.set_valueOf_("nazov")
        expectation.set_original_tagname_('title')
        doc.transition[0].dataGroup[0].set_title(expectation)
        self.assertEqual(doc.transition[0].dataGroup[0].title, expectation)

    def test_dataGroup_set_wrong_title(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].dataGroup[0].set_title("nazov")

    def test_dataGroup_set_alignment(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = dataGroupAlignment.END
        doc.transition[0].dataGroup[0].set_alignment(expectation)
        self.assertEqual(doc.transition[0].dataGroup[0].alignment, expectation)

    def test_dataGroup_set_wrong_alignment(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].dataGroup[0].set_alignment(i18nStringType())

    def test_dataGroup_set_stretch(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = 'true'
        doc.transition[0].dataGroup[0].set_stretch(expectation)
        self.assertEqual(doc.transition[0].dataGroup[0].stretch, expectation)

    def test_dataGroup_set_wrong_stretch(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].dataGroup[0].set_stretch("pravda")

    def test_dataGroup_set_hideEmptyRows(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = hideEmptyRows.ALL
        doc.transition[0].dataGroup[0].set_hideEmptyRows(expectation)
        self.assertEqual(doc.transition[0].dataGroup[0].hideEmptyRows, expectation)

    def test_dataGroup_set_wrong_hideEmptyRows(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].dataGroup[0].set_hideEmptyRows("hidden")

    def test_dataGroup_set_compactDirection(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = compactDirection.NONE
        doc.transition[0].dataGroup[0].set_compactDirection(expectation)
        self.assertEqual(doc.transition[0].dataGroup[0].compactDirection, expectation)

    def test_dataGroup_set_wrong_compactDirection(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].dataGroup[0].set_compactDirection(True)

    def test_dataGroup_set_dataRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = []
        my_ref = dataRef()
        my_ref.set_id("1406")
        my_ref.set_id("ID")
        expectation.append(my_ref)
        doc.transition[0].dataGroup[0].set_dataRef(expectation)
        self.assertEqual(doc.transition[0].dataGroup[0].dataRef, expectation)

    def test_dataGroup_add_dataRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = dataRef()
        expectation.set_id("1406")
        expectation.set_id("ID")
        doc.transition[0].dataGroup[0].add_dataRef(expectation)
        self.assertEqual(doc.transition[0].dataGroup[0].dataRef[1], expectation)

    def test_dataGroup_add_wrong_dataRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].dataGroup[0].add_dataRef(i18nStringType())

    def test_dataGroup_insert_dataRef_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        ref = dataRef()
        ref.set_id("1406")
        ref.set_id("ID")
        with self.assertRaises(IndexError):
            doc.transition[0].dataGroup[0].insert_dataRef_at(2, ref)

#  end of dataGroup tag tests

    def test_action_set_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].add_action(action())
        expectation = 'ACT1'
        doc.data[0].action[0].set_id(expectation)
        self.assertEqual(doc.data[0].action[0].id, expectation)

    def test_action_set_wrong_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].add_action(action())
        with self.assertRaises(TypeError):
            doc.data[0].action[0].set_id(i18nStringType())

    def test_action_set_trigger(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].add_action(action())
        expectation = 'triggered'
        doc.data[0].action[0].set_trigger(expectation)
        self.assertEqual(doc.data[0].action[0].trigger, expectation)

    def test_action_set_wrong_trigger(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].add_action(action())
        with self.assertRaises(TypeError):
            doc.data[0].action[0].set_trigger(555)

    def test_action_set_valueOf_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].add_action(action())
        expectation = 'hodnota'
        doc.data[0].action[0].set_valueOf_(expectation)
        self.assertEqual(doc.data[0].action[0].valueOf_, expectation)

    def test_action_set_wrong_valueOf_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].add_action(action())
        with self.assertRaises(TypeError):
            doc.data[0].action[0].set_valueOf_(True)

#  end of action tag tests

    def test_validations_set_validation(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_validations(validations())
        expectation = []
        my_val = validation()
        msg = i18nStringType()
        msg.set_valueOf_("sprava")
        msg.set_name("meno")
        msg.set_original_tagname_('message')
        my_val.set_message(msg)
        exp = valid()
        exp.set_valueOf_("vyraz")
        exp.set_dynamic(False)
        my_val.set_expression(exp)
        expectation.append(my_val)
        doc.data[0].validations.set_validation(expectation)
        self.assertEqual(doc.data[0].validations.validation, expectation)

    def test_validations_add_validation(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_validations(validations())
        expectation = validation()
        msg = i18nStringType()
        msg.set_valueOf_("sprava")
        msg.set_name("meno")
        msg.set_original_tagname_('message')
        expectation.set_message(msg)
        exp = valid()
        exp.set_valueOf_("vyraz")
        exp.set_dynamic(False)
        expectation.set_expression(exp)
        doc.data[0].validations.add_validation(expectation)
        self.assertEqual(doc.data[0].validations.validation[0], expectation)

    def test_validations_add_wrong_validation(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_validations(validations())
        with self.assertRaises(TypeError):
            doc.data[0].validations.add_validation(i18nStringType())

    def test_validations_insert_validation_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_validations(validations())
        val = validation()
        msg = i18nStringType()
        msg.set_valueOf_("sprava")
        msg.set_name("meno")
        msg.set_original_tagname_('message')
        val.set_message(msg)
        exp = valid()
        exp.set_valueOf_("vyraz")
        exp.set_dynamic(False)
        val.set_expression(exp)
        with self.assertRaises(IndexError):
            doc.data[0].validations.insert_validation_at(1, val)

#  end of validations tag tests

    def test_validation_set_expression(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_validations(validations())
        doc.data[0].validations.add_validation(validation())
        expectation = valid()
        expectation.set_dynamic(False)
        expectation.set_valueOf_("vyraz")
        doc.data[0].validations.validation[0].set_expression(expectation)
        self.assertEqual(doc.data[0].validations.validation[0].expression, expectation)

    def test_validation_set_wrong_expression(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_validations(validations())
        doc.data[0].validations.add_validation(validation())
        with self.assertRaises(TypeError):
            doc.data[0].validations.validation[0].set_expression(i18nStringType())

    def test_validation_set_message(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_validations(validations())
        doc.data[0].validations.add_validation(validation())
        expectation = i18nStringType()
        expectation.set_valueOf_("message")
        expectation.set_name("meno")
        expectation.set_original_tagname_('message')
        doc.data[0].validations.validation[0].set_message(expectation)
        self.assertEqual(doc.data[0].validations.validation[0].message, expectation)

    def test_validation_set_wrong_message(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_validations(validations())
        doc.data[0].validations.add_validation(validation())
        with self.assertRaises(TypeError):
            doc.data[0].validations.validation[0].set_message("sprava")

#  end of validation tag tests

    def test_trigger_set_exact_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_trigger(trigger())
        choice_child_1 = datetime.timedelta(days=1, hours=15, minutes=40)
        doc.transition[0].trigger[0].set_delay(choice_child_1)
        with self.assertRaises(ValueError):
            choice_child_2 = datetime.datetime.now()
            doc.transition[0].trigger[0].set_exact(choice_child_2)

    def test_trigger_set_exact(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_trigger(trigger())
        expectation = datetime.datetime.now()
        doc.transition[0].trigger[0].set_exact(expectation)
        self.assertEqual(doc.transition[0].trigger[0].exact, expectation)

    def test_trigger_set_wrong_exact(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_trigger(trigger())
        with self.assertRaises(TypeError):
            doc.transition[0].trigger[0].set_exact("16.02.2024")

    def test_trigger_set_delay_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_trigger(trigger())
        choice_child_1 = datetime.datetime.now()
        doc.transition[0].trigger[0].set_exact(choice_child_1)
        with self.assertRaises(ValueError):
            choice_child_2 = datetime.timedelta(days=1, hours=15, minutes=40)
            doc.transition[0].trigger[0].set_delay(choice_child_2)

    def test_trigger_set_delay(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_trigger(trigger())
        expectation = datetime.timedelta(days=1, hours=15, minutes=40)
        doc.transition[0].trigger[0].set_delay(expectation)
        self.assertEqual(doc.transition[0].trigger[0].delay, expectation)

    def test_trigger_set_wrong_delay(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_trigger(trigger())
        with self.assertRaises(TypeError):
            doc.transition[0].trigger[0].set_delay(datetime.datetime.now())

    def test_trigger_set_type_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_trigger(trigger())
        expectation = triggerType.TIME
        doc.transition[0].trigger[0].set_type_(expectation)
        self.assertEqual(doc.transition[0].trigger[0].type_, expectation)

    def test_trigger_set_wrong_type_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.transition[0].add_trigger(trigger())
        with self.assertRaises(TypeError):
            doc.transition[0].trigger[0].set_type_("triggered")

#  end of trigger tag tests

    def test_documentRef_set_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_documentRef(documentRef())
        expectation = 1
        doc.data[0].documentRef.set_id(expectation)
        self.assertEqual(doc.data[0].documentRef.id, expectation)

    def test_documentRef_set_negative_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_documentRef(documentRef())
        with self.assertRaises(ValueError):
            doc.data[0].documentRef.set_id(-1)

    def test_documentRef_set_nonLong_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_documentRef(documentRef())
        non_long = 2 ** 64
        with self.assertRaises(ValueError):
            doc.data[0].documentRef.set_id(non_long)

    def test_documentRef_set_wrong_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_documentRef(documentRef())
        with self.assertRaises(TypeError):
            doc.data[0].documentRef.set_id("number")

    def test_documentRef_set_fields(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_documentRef(documentRef())
        expectation = []
        my_field = 1406
        expectation.append(my_field)
        doc.data[0].documentRef.set_fields(expectation)
        self.assertEqual(doc.data[0].documentRef.fields, expectation)

    def test_documentRef_add_fields(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_documentRef(documentRef())
        expectation = 1406
        doc.data[0].documentRef.add_fields(expectation)
        self.assertEqual(doc.data[0].documentRef.fields[0], expectation)

    def test_documentRef_add_wrong_fields(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_documentRef(documentRef())
        with self.assertRaises(TypeError):
            doc.data[0].documentRef.add_fields(i18nStringType())

    def test_documentRef_insert_fields_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_documentRef(documentRef())
        field_ = 1406
        with self.assertRaises(IndexError):
            doc.data[0].documentRef.insert_fields_at(1, field_)

#  end of documentRef tag tests

    def test_encryption_set_algorithm(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_encryption(encryption())
        expectation = "algoritmus"
        doc.data[0].encryption.set_algorithm(expectation)
        self.assertEqual(doc.data[0].encryption.algorithm, expectation)

    def test_encryption_set_wrong_algorithm(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_encryption(encryption())
        with self.assertRaises(TypeError):
            doc.data[0].encryption.set_algorithm(True)

    def test_encryption_set_valueOf_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_encryption(encryption())
        expectation = 'true'
        doc.data[0].encryption.set_valueOf_(expectation)
        self.assertEqual(doc.data[0].encryption.valueOf_, expectation)

    def test_encryption_set_wrong_valueOf_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_encryption(encryption())
        with self.assertRaises(TypeError):
            doc.data[0].encryption.set_valueOf_("hodnota")

#  end of encryption tag tests

    def test_i18nStringType_set_name(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_title(i18nStringType())
        expectation = "meno"
        doc.title.set_name(expectation)
        self.assertEqual(doc.title.name, expectation)

    def test_i18nStringType_set_wrong_name(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_title(i18nStringType())
        with self.assertRaises(TypeError):
            doc.title.set_name(123)

    def test_i18nStringType_set_valueOf_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_title(i18nStringType())
        expectation = 'true'
        doc.title.set_valueOf_(expectation)
        self.assertEqual(doc.title.valueOf_, expectation)

    def test_i18nStringType_set_wrong_valueOf_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_title(i18nStringType())
        with self.assertRaises(TypeError):
            doc.title.set_valueOf_(False)

    def test_i18nStringType_set_original_tagname_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_title(i18nStringType())
        expectation = 'title'
        doc.title.set_original_tagname_(expectation)
        self.assertEqual(doc.title.original_tagname_, expectation)

    def test_i18nStringType_set_wrong_original_tagname_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_title(i18nStringType())
        with self.assertRaises(TypeError):
            doc.title.set_original_tagname_(i18nStringType())

#  end of i18nStringType tag tests

    def test_i18nStringTypeWithExpression_set_dynamic(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_caseName(i18nStringTypeWithExpression())
        expectation = 'true'
        doc.caseName.set_dynamic(expectation)
        self.assertEqual(doc.caseName.dynamic, expectation)

    def test_i18nStringTypeWithExpression_set_wrong_dynamic(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_caseName(i18nStringTypeWithExpression())
        with self.assertRaises(TypeError):
            doc.caseName.set_dynamic(123)

    def test_i18nStringTypeWithExpression_set_valueOf_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_caseName(i18nStringTypeWithExpression())
        expectation = "hodnota"
        doc.caseName.set_valueOf_(expectation)
        self.assertEqual(doc.caseName.valueOf_, expectation)

    def test_i18nStringTypeWithExpression_set_wrong_valueOf_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_caseName(i18nStringTypeWithExpression())
        with self.assertRaises(TypeError):
            doc.caseName.set_valueOf_(i18nStringType())

    def test_i18nStringTypeWithExpression_set_name(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_caseName(i18nStringTypeWithExpression())
        expectation = "meno"
        doc.caseName.set_name(expectation)
        self.assertEqual(doc.caseName.name, expectation)

    def test_i18nStringTypeWithExpression_set_wrong_name(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_caseName(i18nStringTypeWithExpression())
        with self.assertRaises(TypeError):
            doc.caseName.set_name(False)

#  end of i18nStringTypeWithExpression tag tests

    def test_baseEvent_set_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.role[0].add_event(event())
        expectation = 'ACT1'
        doc.role[0].event[0].set_id(expectation)
        self.assertEqual(doc.role[0].event[0].id, expectation)

    def test_baseEvent_set_wrong_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.role[0].add_event(event())
        with self.assertRaises(TypeError):
            doc.role[0].event[0].set_id(1)

    def test_baseEvent_set_actions(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.role[0].add_event(event())
        expectation = []
        my_act = actions()
        my_act.set_phase(eventPhaseType.POST)
        expectation.append(my_act)
        doc.role[0].event[0].set_actions(expectation)
        self.assertEqual(doc.role[0].event[0].actions, expectation)

    def test_baseEvent_add_actions(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.role[0].add_event(event())
        expectation = actions()
        expectation.set_phase(eventPhaseType.POST)
        doc.role[0].event[0].add_actions(expectation)
        self.assertEqual(doc.role[0].event[0].actions[0], expectation)

    def test_baseEvent_add_wrong_actions(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.role[0].add_event(event())
        with self.assertRaises(TypeError):
            doc.role[0].event[0].add_actions(i18nStringType())

    def test_baseEvent_insert_actions_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.role[0].add_event(event())
        act = actions()
        act.set_phase(eventPhaseType.POST)
        with self.assertRaises(IndexError):
            doc.role[0].event[0].insert_actions_at(1, act)

    def test_baseEvent_set_message(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.role[0].add_event(event())
        expectation = i18nStringType()
        expectation.set_name("meno")
        expectation.set_valueOf_("sprava")
        expectation.set_original_tagname_('message')
        doc.role[0].event[0].set_message(expectation)
        self.assertEqual(doc.role[0].event[0].message, expectation)

    def test_baseEvent_set_wrong_message(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.role[0].add_event(event())
        with self.assertRaises(TypeError):
            doc.role[0].event[0].set_message("wrong msg type")

#  end of baseEvent tag tests

    def test_dataEvent_set_type_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].add_event(dataEvent())
        expectation = dataEventType.GET
        doc.data[0].event[0].set_type_(expectation)
        self.assertEqual(doc.data[0].event[0].type_, expectation)

    def test_dataEvent_set_wrong_type_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].add_event(dataEvent())
        with self.assertRaises(TypeError):
            doc.data[0].event[0].set_type_("data type")

#  end of dataEvent tag tests

    def test_caseEvent_set_type_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_caseEvents(caseEvents())
        doc.caseEvents.add_event(caseEvent())
        expectation = caseEventType.DELETE
        doc.caseEvents.event[0].set_type_(expectation)
        self.assertEqual(doc.caseEvents.event[0].type_, expectation)

    def test_caseEvent_set_wrong_type_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_caseEvents(caseEvents())
        doc.caseEvents.add_event(caseEvent())
        with self.assertRaises(TypeError):
            doc.caseEvents.event[0].set_type_(i18nStringType())

#  end of caseEvent tag tests

    def test_processEvent_set_type_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_processEvents(processEvents())
        doc.processEvents.add_event(processEvent())
        expectation = processEventType.UPLOAD
        doc.processEvents.event[0].set_type_(expectation)
        self.assertEqual(doc.processEvents.event[0].type_, expectation)

    def test_processEvent_set_wrong_type_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.set_processEvents(processEvents())
        doc.processEvents.add_event(processEvent())
        with self.assertRaises(TypeError):
            doc.processEvents.event[0].set_type_(i18nStringType())

#  end of processEvent tag tests

    def test_actions_set_action(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.role[0].add_event(event())
        doc.role[0].event[0].add_actions(actions())
        expectation = []
        my_act = action()
        my_act.set_id("ID")
        my_act.set_trigger("triggered")
        my_act.set_valueOf_("hodnota")
        expectation.append(my_act)
        doc.role[0].event[0].actions[0].set_action(expectation)
        self.assertEqual(doc.role[0].event[0].actions[0].action, expectation)

    def test_actions_add_action(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.role[0].add_event(event())
        doc.role[0].event[0].add_actions(actions())
        expectation = action()
        expectation.set_id("ID")
        expectation.set_trigger("triggered")
        expectation.set_valueOf_("hodnota")
        doc.role[0].event[0].actions[0].add_action(expectation)
        self.assertEqual(doc.role[0].event[0].actions[0].action[0], expectation)

    def test_actions_add_wrong_action(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.role[0].add_event(event())
        doc.role[0].event[0].add_actions(actions())
        with self.assertRaises(TypeError):
            doc.role[0].event[0].actions[0].add_action(i18nStringType())

    def test_actions_insert_action_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.role[0].add_event(event())
        doc.role[0].event[0].add_actions(actions())
        act = action()
        act.set_id("ID")
        act.set_trigger("triggered")
        act.set_valueOf_("hodnota")
        with self.assertRaises(IndexError):
            doc.role[0].event[0].actions[0].insert_action_at(1, act)

    def test_actions_set_actionRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.role[0].add_event(event())
        doc.role[0].event[0].add_actions(actions())
        expectation = []
        my_ref = actionRef()
        my_ref.set_id("REF")
        expectation.append(my_ref)
        doc.role[0].event[0].actions[0].set_actionRef(expectation)
        self.assertEqual(doc.role[0].event[0].actions[0].actionRef, expectation)

    def test_actions_add_actionRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.role[0].add_event(event())
        doc.role[0].event[0].add_actions(actions())
        expectation = actionRef()
        expectation.set_id("REF")
        doc.role[0].event[0].actions[0].add_actionRef(expectation)
        self.assertEqual(doc.role[0].event[0].actions[0].actionRef[0], expectation)

    def test_actions_add_wrong_actionRef(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.role[0].add_event(event())
        doc.role[0].event[0].add_actions(actions())
        with self.assertRaises(TypeError):
            doc.role[0].event[0].actions[0].add_actionRef("referencia")

    def test_actions_insert_actionRef_at_wrong_index(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.role[0].add_event(event())
        doc.role[0].event[0].add_actions(actions())
        ref = actionRef()
        ref.set_id("REF")
        with self.assertRaises(IndexError):
            doc.role[0].event[0].actions[0].insert_actionRef_at(1, ref)

    def test_actions_set_phase(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.role[0].add_event(event())
        doc.role[0].event[0].add_actions(actions())
        expectation = eventPhaseType.PRE
        doc.role[0].event[0].actions[0].set_phase(expectation)
        self.assertEqual(doc.role[0].event[0].actions[0].phase, expectation)

    def test_actions_set_wrong_phase(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.role[0].add_event(event())
        doc.role[0].event[0].add_actions(actions())
        with self.assertRaises(TypeError):
            doc.role[0].event[0].actions[0].set_phase("start")

#  end of actions tag tests

    def test_actionRef_set_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.role[0].add_event(event())
        doc.role[0].event[0].add_actions(actions())
        doc.role[0].event[0].actions[0].add_actionRef(actionRef())
        expectation = 'REF1'
        doc.role[0].event[0].actions[0].actionRef[0].set_id(expectation)
        self.assertEqual(doc.role[0].event[0].actions[0].actionRef[0].id, expectation)

    def test_actionRef_set_wrong_id(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.role[0].add_event(event())
        doc.role[0].event[0].add_actions(actions())
        doc.role[0].event[0].actions[0].add_actionRef(actionRef())
        with self.assertRaises(TypeError):
            doc.role[0].event[0].actions[0].actionRef[0].set_id(123)

#  end of actionRef tag tests

    def test_fieldView_set_area_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        choice_child_1 = "strom"
        doc.data[0].view.set_tree(choice_child_1)
        with self.assertRaises(ValueError):
            choice_child_2 = "area"
            doc.data[0].view.set_area(choice_child_2)

    def test_fieldView_set_area(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        expectation = "area"
        doc.data[0].view.set_area(expectation)
        self.assertEqual(doc.data[0].view.area, expectation)

    def test_fieldView_set_wrong_area(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        with self.assertRaises(TypeError):
            doc.data[0].view.set_area(i18nStringType())

    def test_fieldView_set_autocomplete_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        choice_child_1 = "stol"
        doc.data[0].view.set_table(choice_child_1)
        with self.assertRaises(ValueError):
            choice_child_2 = "auto complete"
            doc.data[0].view.set_autocomplete(choice_child_2)

    def test_fieldView_set_autocomplete(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        expectation = "auto complete"
        doc.data[0].view.set_autocomplete(expectation)
        self.assertEqual(doc.data[0].view.autocomplete, expectation)

    def test_fieldView_set_wrong_autocomplete(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        with self.assertRaises(TypeError):
            doc.data[0].view.set_autocomplete(False)

    def test_fieldView_set_tree_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        choice_child_1 = booleanImageView()
        choice_child_1.set_true("true")
        doc.data[0].view.set_image(choice_child_1)
        with self.assertRaises(ValueError):
            choice_child_2 = "strom"
            doc.data[0].view.set_tree(choice_child_2)

    def test_fieldView_set_tree(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        expectation = "strom"
        doc.data[0].view.set_tree(expectation)
        self.assertEqual(doc.data[0].view.tree, expectation)

    def test_fieldView_set_wrong_tree(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        with self.assertRaises(TypeError):
            doc.data[0].view.set_tree(222)

    def test_fieldView_set_table_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        choice_child_1 = "area"
        doc.data[0].view.set_area(choice_child_1)
        with self.assertRaises(ValueError):
            choice_child_2 = "stol"
            doc.data[0].view.set_table(choice_child_2)

    def test_fieldView_set_table(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        expectation = "stol"
        doc.data[0].view.set_table(expectation)
        self.assertEqual(doc.data[0].view.table, expectation)

    def test_fieldView_set_wrong_table(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        with self.assertRaises(TypeError):
            doc.data[0].view.set_table(i18nStringType())

    def test_fieldView_set_image_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        choice_child_1 = "automatic"
        doc.data[0].view.set_autocomplete(choice_child_1)
        with self.assertRaises(ValueError):
            choice_child_2 = booleanImageView()
            choice_child_2.set_false("false")
            doc.data[0].view.set_image(choice_child_2)

    def test_fieldView_set_image(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        expectation = booleanImageView()
        expectation.set_true("true")
        doc.data[0].view.set_image(expectation)
        self.assertEqual(doc.data[0].view.image, expectation)

    def test_fieldView_set_wrong_image(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        with self.assertRaises(TypeError):
            doc.data[0].view.set_image(True)

    def test_fieldView_set_editor_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        choice_child_1 = "stol"
        doc.data[0].view.set_table(choice_child_1)
        with self.assertRaises(ValueError):
            choice_child_2 = "anyType"
            doc.data[0].view.set_editor(choice_child_2)

    def test_fieldView_set_editor(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        expectation = "anyType"
        doc.data[0].view.set_editor(expectation)
        self.assertEqual(doc.data[0].view.editor, expectation)

    def test_fieldView_set_htmlEditor_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        choice_child_1 = "editor"
        doc.data[0].view.set_editor(choice_child_1)
        with self.assertRaises(ValueError):
            choice_child_2 = "anyType html"
            doc.data[0].view.set_htmlEditor(choice_child_2)

    def test_fieldView_set_htmlEditor(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        expectation = "anyType html"
        doc.data[0].view.set_htmlEditor(expectation)
        self.assertEqual(doc.data[0].view.htmlEditor, expectation)

    def test_fieldView_set_buttonType_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        choice_child_1 = booleanImageView()
        choice_child_1.set_true("true")
        doc.data[0].view.set_image(choice_child_1)
        with self.assertRaises(ValueError):
            choice_child_2 = buttonTypeType.RAISED
            doc.data[0].view.set_buttonType(choice_child_2)

    def test_fieldView_set_buttonType(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        expectation = buttonTypeType.STROKED
        doc.data[0].view.set_buttonType(expectation)
        self.assertEqual(doc.data[0].view.buttonType, expectation)

    def test_fieldView_set_wrong_buttonType(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        with self.assertRaises(TypeError):
            doc.data[0].view.set_buttonType('ROUND')

    def test_fieldView_set_list_choice_restriction(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        choice_child_1 = buttonTypeType.FAB
        doc.data[0].view.set_buttonType(choice_child_1)
        with self.assertRaises(ValueError):
            choice_child_2 = 555
            doc.data[0].view.set_list(choice_child_2)

    def test_fieldView_set_string_list(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        expectation = ""
        doc.data[0].view.set_list(expectation)
        self.assertEqual(doc.data[0].view.list, expectation)

    def test_fieldView_set_integer_list(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        expectation = 1406
        doc.data[0].view.set_list(expectation)
        self.assertEqual(doc.data[0].view.list, expectation)

    def test_fieldView_set_wrong_list(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        with self.assertRaises(TypeError):
            doc.data[0].view.set_list("nonEmpty string")

#  end of fieldView tag tests

    def test_booleanImageView_set_true(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        doc.data[0].view.set_image(booleanImageView())
        expectation = "true"
        doc.data[0].view.image.set_true(expectation)
        self.assertEqual(doc.data[0].view.image.true, expectation)

    def test_booleanImageView_set_wrong_true(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        doc.data[0].view.set_image(booleanImageView())
        with self.assertRaises(TypeError):
            doc.data[0].view.image.set_true(True)

    def test_booleanImageView_set_false(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        doc.data[0].view.set_image(booleanImageView())
        expectation = "false"
        doc.data[0].view.image.set_false(expectation)
        self.assertEqual(doc.data[0].view.image.false, expectation)

    def test_booleanImageView_set_wrong_false(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_view(fieldView())
        doc.data[0].view.set_image(booleanImageView())
        with self.assertRaises(TypeError):
            doc.data[0].view.image.set_false(False)

#  end of booleanImageView tag tests

    def test_format_set_currency(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_format(format())
        expectation = currency()
        expectation.set_code("kod")
        expectation.set_locale("locale")
        expectation.set_fractionSize(123)
        doc.data[0].format.set_currency(expectation)
        self.assertEqual(doc.data[0].format.currency, expectation)

    def test_format_set_wrong_currency(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_format(format())
        with self.assertRaises(TypeError):
            doc.data[0].format.set_currency("$")

#  end of format tag tests

    def test_currency_set_code(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_format(format())
        doc.data[0].format.set_currency(currency())
        expectation = "kod"
        doc.data[0].format.currency.set_code(expectation)
        self.assertEqual(doc.data[0].format.currency.code, expectation)

    def test_currency_set_wrong_code(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_format(format())
        doc.data[0].format.set_currency(currency())
        with self.assertRaises(TypeError):
            doc.data[0].format.currency.set_code(1111)

    def test_currency_set_fractionSize(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_format(format())
        doc.data[0].format.set_currency(currency())
        expectation = 1406
        doc.data[0].format.currency.set_fractionSize(expectation)
        self.assertEqual(doc.data[0].format.currency.fractionSize, expectation)

    def test_currency_set_wrong_fractionSize(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_format(format())
        doc.data[0].format.set_currency(currency())
        with self.assertRaises(TypeError):
            doc.data[0].format.currency.set_fractionSize(i18nStringType())

    def test_currency_set_locale(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_format(format())
        doc.data[0].format.set_currency(currency())
        expectation = "locale"
        doc.data[0].format.currency.set_locale(expectation)
        self.assertEqual(doc.data[0].format.currency.locale, expectation)

    def test_currency_set_wrong_locale(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_format(format())
        doc.data[0].format.set_currency(currency())
        with self.assertRaises(TypeError):
            doc.data[0].format.currency.set_locale(False)

#  end of currency tag tests

    def test_event_set_type_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = eventType.ASSIGN
        doc.transition[0].event[0].set_type_(expectation)
        self.assertEqual(doc.transition[0].event[0].type_, expectation)

    def test_event_set_wrong_type_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].event[0].set_type_("type")

    def test_event_set_title(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        expectation = i18nStringType()
        expectation.set_valueOf_("nadpis")
        expectation.set_name("meno")
        expectation.set_original_tagname_('title')
        doc.transition[0].event[0].set_title(expectation)
        self.assertEqual(doc.transition[0].event[0].title, expectation)

    def test_event_set_wrong_title(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        with self.assertRaises(TypeError):
            doc.transition[0].event[0].set_title("nadpis")

#  end of event tag tests

    def test_init_set_valueOf_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_init(init())
        expectation = "hodnota"
        doc.data[0].init.set_valueOf_(expectation)
        self.assertEqual(doc.data[0].init.valueOf_, expectation)

    def test_init_set_wrong_valueOf_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_init(init())
        with self.assertRaises(TypeError):
            doc.data[0].init.set_valueOf_(123)

#  end of init tag tests

    def test_option_set_key(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_options(options())
        doc.data[0].options.add_option(option())
        expectation = "K_123"
        doc.data[0].options.option[0].set_key(expectation, doc)
        self.assertEqual(doc.data[0].options.option[0].key, expectation)

    def test_option_set_wrong_key(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_options(options())
        doc.data[0].options.add_option(option())
        with self.assertRaises(TypeError):
            doc.data[0].options.option[0].set_key(123, doc)

    def test_option_set_not_unique_key(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_options(options())
        doc.data[0].options.add_option(option())
        doc.data[0].options.add_option(option())
        expectation = "K_123"
        doc.data[0].options.option[0].set_key(expectation, doc)
        with self.assertRaises(ValueError):
            doc.data[0].options.option[1].set_key(expectation, doc)

    def test_option_set_valueOf_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_options(options())
        doc.data[0].options.add_option(option())
        expectation = "hodnota"
        doc.data[0].options.option[0].set_valueOf_(expectation)
        self.assertEqual(doc.data[0].options.option[0].valueOf_, expectation)

    def test_option_set_wrong_valueOf_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].set_options(options())
        doc.data[0].options.add_option(option())
        with self.assertRaises(TypeError):
            doc.data[0].options.option[0].set_valueOf_(i18nStringType())

#  end of option tag tests

    def test_valid_set_valueOf_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].add_valid(valid())
        expectation = "hodnota"
        doc.data[0].valid[0].set_valueOf_(expectation)
        self.assertEqual(doc.data[0].valid[0].valueOf_, expectation)

    def test_valid_set_wrong_valueOf_(self):
        doc = xml_classes.import_xml("../resources/hypouver.xml")
        doc.data[0].add_valid(valid())
        with self.assertRaises(TypeError):
            doc.data[0].valid[0].set_valueOf_(123)

#  end of valid tag tests

if __name__ == '__main__':
    unittest.main()
