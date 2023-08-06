#!/usr/bin/env python

#
# Generated Fri Dec 16 21:03:57 2022 by generateDS.py version 2.41.1.
# Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)]
#
# Command line options:
#   ('-o', 'xml_classes.py')
#   ('-s', 'xml_subclasses.py')
#   ('--super', 'import_xml_file')
#
# Command line arguments:
#   xsd_scheme/petriflow.schema.xsd
#
# Command line:
#   D:/PyCharm Projects/petriflowLibrary/venv/Scripts/generateDS.py -o "xml_classes.py" -s "xml_subclasses.py" --super="import_xml_file" resources/petriflow.schema.xsd
#
# Current working directory (os.getcwd()):
#   petriflowLibrary
#

import os
import sys
from urllib.request import urlopen

from lxml import etree as etree_

import petriflow.xml_classes as supermod


def parse_xml_(infile, parser=None, **kwargs):
    """

    :param infile:
    :param parser:
    :param kwargs:
    :return:
    """
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc


def parse_xml_string_(in_string, parser=None, **kwargs):
    """

    :param in_string:
    :param parser:
    :param kwargs:
    :return:
    """
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(in_string, parser=parser, **kwargs)
    return element


def set_namespace_defs(location):
    """
    Adding the required namespace prefix definitions to the global variable GenerateDSNamespaceDefs_
    :param location: schemaLocation & noNamespaceSchemaLocation provides hints to the XML processor as to how to
    associate an XSD with an XML document. We use noNamespaceSchemaLocation, because there is no namespace
    :return:
    """
    dict_ = {"document": 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation=' +
                         location}
    supermod.GenerateDSNamespaceDefs_.clear()
    supermod.GenerateDSNamespaceDefs_.update(dict_)


#
# Globals
#

ExternalEncoding = ''
SaveElementTreeNode = True
NamespaceDefsLocation = "https://petriflow.com/petriflow.schema.xsd"


#
# Data representation classes
#


class transactionSub(supermod.transaction):
    def __init__(self, id=None, title=None, **kwargs_):
        super(transactionSub, self).__init__(id, title, **kwargs_)


supermod.transaction.subclass = transactionSub


# end class transactionSub

class dataSub(supermod.data):
    def __init__(self, type_=None, immediate=None, id=None, title=None, placeholder=None, desc=None, values=None,
                 options=None, valid=None, validations=None, init=None, inits=None, format=None, view=None,
                 component=None, encryption=None, action=None, event=None, actionRef=None, documentRef=None,
                 remote=None, length=None, allowedNets=None, **kwargs_):
        super(dataSub, self).__init__(type_, immediate, id, title, placeholder, desc, values, options, valid,
                                      validations, init, inits, format, view, component, encryption, action, event,
                                      actionRef, documentRef, remote, length, allowedNets, **kwargs_)


supermod.data.subclass = dataSub


# end class dataSub


class functionSub(supermod.function):
    def __init__(self, scope=None, name=None, valueOf_=None, **kwargs_):
        super(functionSub, self).__init__(scope, name, valueOf_, **kwargs_)


supermod.function.subclass = functionSub


# end class functionSub


class roleSub(supermod.role):
    def __init__(self, id=None, title=None, name=None, event=None, **kwargs_):
        super(roleSub, self).__init__(id, title, name, event, **kwargs_)


supermod.role.subclass = roleSub


# end class roleSub


class mappingSub(supermod.mapping):
    def __init__(self, id=None, transitionRef=None, roleRef=None, dataRef=None, dataGroup=None, trigger=None,
                 **kwargs_):
        super(mappingSub, self).__init__(id, transitionRef, roleRef, dataRef, dataGroup, trigger, **kwargs_)


supermod.mapping.subclass = mappingSub


# end class mappingSub


class transitionSub(supermod.transition):
    def __init__(self, id=None, x=None, y=None, label=None, layout=None, icon=None, priority=None, assignPolicy=None,
                 dataFocusPolicy=None, finishPolicy=None, trigger=None, transactionRef=None, roleRef=None,
                 usersRef=None, userRef=None, assignedUser=None, dataRef=None, dataGroup=None, event=None, **kwargs_):
        super(transitionSub, self).__init__(id, x, y, label, layout, icon, priority, assignPolicy, dataFocusPolicy,
                                            finishPolicy, trigger, transactionRef, roleRef, usersRef, userRef,
                                            assignedUser, dataRef, dataGroup, event, **kwargs_)


supermod.transition.subclass = transitionSub


# end class transitionSub


class transitionLayoutSub(supermod.transitionLayout):
    def __init__(self, type_=None, cols=None, rows=None, offset=None, fieldAlignment=None, hideEmptyRows=None,
                 compactDirection=None, **kwargs_):
        super(transitionLayoutSub, self).__init__(type_, cols, rows, offset, fieldAlignment, hideEmptyRows,
                                                  compactDirection, **kwargs_)


supermod.transitionLayout.subclass = transitionLayoutSub


# end class transitionLayoutSub


class placeSub(supermod.place):
    def __init__(self, id=None, x=None, y=None, label=None, tokens=None, isStatic=None, static=None, **kwargs_):
        super(placeSub, self).__init__(id, x, y, label, tokens, isStatic, static, **kwargs_)


supermod.place.subclass = placeSub


# end class placeSub


class arcSub(supermod.arc):
    def __init__(self, id=None, type_='regular', sourceId=None, destinationId=None, multiplicity=None, reference=None,
                 breakpoint=None, **kwargs_):
        super(arcSub, self).__init__(id, type_, sourceId, destinationId, multiplicity, reference, breakpoint, **kwargs_)


supermod.arc.subclass = arcSub


# end class arcSub


class i18nSub(supermod.i18n):
    def __init__(self, locale=None, i18nString=None, **kwargs_):
        super(i18nSub, self).__init__(locale, i18nString, **kwargs_)


supermod.i18n.subclass = i18nSub


# end class i18nSub


class processEventsSub(supermod.processEvents):
    def __init__(self, event=None, **kwargs_):
        super(processEventsSub, self).__init__(event, **kwargs_)


supermod.processEvents.subclass = processEventsSub


# end class processEventsSub


class caseEventsSub(supermod.caseEvents):
    def __init__(self, event=None, **kwargs_):
        super(caseEventsSub, self).__init__(event, **kwargs_)


supermod.caseEvents.subclass = caseEventsSub


# end class caseEventsSub


class documentTypeSub(supermod.documentType):
    def __init__(self, id=None, version=None, initials=None, title=None, icon=None, defaultRole=True,
                 anonymousRole=True, transitionRole=True, caseName=None, roleRef=None, usersRef=None, userRef=None,
                 processEvents=None, caseEvents=None, transaction=None, role=None, function=None, data=None,
                 mapping=None, i18n=None, transition=None, place=None, arc=None, extensiontype_=None, **kwargs_):
        super(documentTypeSub, self).__init__(id, version, initials, title, icon, defaultRole, anonymousRole,
                                              transitionRole, caseName, roleRef, usersRef, userRef, processEvents,
                                              caseEvents, transaction, role, function, data, mapping, i18n, transition,
                                              place, arc, extensiontype_, **kwargs_)


supermod.documentType.subclass = documentTypeSub


# end class documentTypeSub


class breakpointSub(supermod.breakpoint):
    def __init__(self, x=None, y=None, **kwargs_):
        super(breakpointSub, self).__init__(x, y, **kwargs_)


supermod.breakpoint.subclass = breakpointSub


# end class breakpointSub


class optionsSub(supermod.options):
    def __init__(self, option=None, init=None, **kwargs_):
        super(optionsSub, self).__init__(option, init, **kwargs_)


supermod.options.subclass = optionsSub


# end class optionsSub


class initsSub(supermod.inits):
    def __init__(self, init=None, **kwargs_):
        super(initsSub, self).__init__(init, **kwargs_)


supermod.inits.subclass = initsSub


# end class initsSub


class expressionSub(supermod.expression):
    def __init__(self, dynamic=False, valueOf_=None, extensiontype_=None, **kwargs_):
        super(expressionSub, self).__init__(dynamic, valueOf_, extensiontype_, **kwargs_)


supermod.expression.subclass = expressionSub


# end class expressionSub


class componentSub(supermod.component):
    def __init__(self, name=None, property=None, properties=None, **kwargs_):
        super(componentSub, self).__init__(name, property, properties, **kwargs_)


supermod.component.subclass = componentSub


# end class componentSub


class propertySub(supermod.property):
    def __init__(self, key=None, valueOf_=None, **kwargs_):
        super(propertySub, self).__init__(key, valueOf_, **kwargs_)


supermod.property.subclass = propertySub


# end class propertySub


class propertiesSub(supermod.properties):
    def __init__(self, property=None, option_icons=None, **kwargs_):
        super(propertiesSub, self).__init__(property, option_icons, **kwargs_)


supermod.properties.subclass = propertiesSub


# end class propertiesSub


class iconsSub(supermod.icons):
    def __init__(self, icon=None, **kwargs_):
        super(iconsSub, self).__init__(icon, **kwargs_)


supermod.icons.subclass = iconsSub


# end class iconsSub


class iconSub(supermod.icon):
    def __init__(self, key=None, type_=None, valueOf_=None, **kwargs_):
        super(iconSub, self).__init__(key, type_, valueOf_, **kwargs_)


supermod.icon.subclass = iconSub


# end class iconSub


class allowedNetsSub(supermod.allowedNets):
    def __init__(self, allowedNet=None, **kwargs_):
        super(allowedNetsSub, self).__init__(allowedNet, **kwargs_)


supermod.allowedNets.subclass = allowedNetsSub


# end class allowedNetsSub


class logicSub(supermod.logic):
    def __init__(self, perform=None, delegate=None, view=None, cancel=None, finish=None, assigned=None, assign=None,
                 behavior=None, action=None, actionRef=None, **kwargs_):
        super(logicSub, self).__init__(perform, delegate, view, cancel, finish, assigned, assign, behavior, action,
                                       actionRef, **kwargs_)


supermod.logic.subclass = logicSub


# end class logicSub


class caseLogicSub(supermod.caseLogic):
    def __init__(self, create=None, delete=None, view=None, action=None, actionRef=None, **kwargs_):
        super(caseLogicSub, self).__init__(create, delete, view, action, actionRef, **kwargs_)


supermod.caseLogic.subclass = caseLogicSub


# end class caseLogicSub


class transactionRefSub(supermod.transactionRef):
    def __init__(self, id=None, **kwargs_):
        super(transactionRefSub, self).__init__(id, **kwargs_)


supermod.transactionRef.subclass = transactionRefSub


# end class transactionRefSub


class permissionRefSub(supermod.permissionRef):
    def __init__(self, id=None, logic=None, extensiontype_=None, **kwargs_):
        super(permissionRefSub, self).__init__(id, logic, extensiontype_, **kwargs_)


supermod.permissionRef.subclass = permissionRefSub


# end class permissionRefSub


class casePermissionRefSub(supermod.casePermissionRef):
    def __init__(self, id=None, caseLogic=None, extensiontype_=None, **kwargs_):
        super(casePermissionRefSub, self).__init__(id, caseLogic, extensiontype_, **kwargs_)


supermod.casePermissionRef.subclass = casePermissionRefSub


# end class casePermissionRefSub


class dataRefSub(supermod.dataRef):
    def __init__(self, id=None, logic=None, layout=None, component=None, event=None, **kwargs_):
        super(dataRefSub, self).__init__(id, logic, layout, component, event, **kwargs_)


supermod.dataRef.subclass = dataRefSub


# end class dataRefSub


class layoutSub(supermod.layout):
    def __init__(self, x=None, y=None, rows=None, cols=None, offset=None, template=None, appearance=None,
                 alignment=None, **kwargs_):
        super(layoutSub, self).__init__(x, y, rows, cols, offset, template, appearance, alignment, **kwargs_)


supermod.layout.subclass = layoutSub


# end class layoutSub


class assignedUserSub(supermod.assignedUser):
    def __init__(self, cancel=None, reassign=None, **kwargs_):
        super(assignedUserSub, self).__init__(cancel, reassign, **kwargs_)


supermod.assignedUser.subclass = assignedUserSub


# end class assignedUserSub


class dataGroupSub(supermod.dataGroup):
    def __init__(self, id=None, cols=None, rows=None, layout=None, title=None, alignment=None, stretch=None,
                 hideEmptyRows=None, compactDirection=None, dataRef=None, **kwargs_):
        super(dataGroupSub, self).__init__(id, cols, rows, layout, title, alignment, stretch, hideEmptyRows,
                                           compactDirection, dataRef, **kwargs_)


supermod.dataGroup.subclass = dataGroupSub


# end class dataGroupSub


class actionSub(supermod.action):
    def __init__(self, trigger=None, id=None, valueOf_=None, **kwargs_):
        super(actionSub, self).__init__(trigger, id, valueOf_, **kwargs_)


supermod.action.subclass = actionSub


# end class actionSub


class validationsSub(supermod.validations):
    def __init__(self, validation=None, **kwargs_):
        super(validationsSub, self).__init__(validation, **kwargs_)


supermod.validations.subclass = validationsSub


# end class validationsSub


class validationSub(supermod.validation):
    def __init__(self, expression=None, message=None, **kwargs_):
        super(validationSub, self).__init__(expression, message, **kwargs_)


supermod.validation.subclass = validationSub


# end class validationSub


class triggerSub(supermod.trigger):
    def __init__(self, type_=None, exact=None, delay=None, **kwargs_):
        super(triggerSub, self).__init__(type_, exact, delay, **kwargs_)


supermod.trigger.subclass = triggerSub


# end class triggerSub


class documentRefSub(supermod.documentRef):
    def __init__(self, id=None, fields=None, **kwargs_):
        super(documentRefSub, self).__init__(id, fields, **kwargs_)


supermod.documentRef.subclass = documentRefSub


# end class documentRefSub


class encryptionSub(supermod.encryption):
    def __init__(self, algorithm=None, valueOf_=None, **kwargs_):
        super(encryptionSub, self).__init__(algorithm, valueOf_, **kwargs_)


supermod.encryption.subclass = encryptionSub


# end class encryptionSub


class i18nStringTypeSub(supermod.i18nStringType):
    def __init__(self, name=None, valueOf_=None, extensiontype_=None, **kwargs_):
        super(i18nStringTypeSub, self).__init__(name, valueOf_, extensiontype_, **kwargs_)


supermod.i18nStringType.subclass = i18nStringTypeSub


# end class i18nStringTypeSub


class i18nStringTypeWithExpressionSub(supermod.i18nStringTypeWithExpression):
    def __init__(self, name=None, dynamic=False, valueOf_=None, extensiontype_=None, **kwargs_):
        super(i18nStringTypeWithExpressionSub, self).__init__(name, dynamic, valueOf_, extensiontype_, **kwargs_)


supermod.i18nStringTypeWithExpression.subclass = i18nStringTypeWithExpressionSub


# end class i18nStringTypeWithExpressionSub


class baseEventSub(supermod.baseEvent):
    def __init__(self, id=None, actions=None, message=None, extensiontype_=None, **kwargs_):
        super(baseEventSub, self).__init__(id, actions, message, extensiontype_, **kwargs_)


supermod.baseEvent.subclass = baseEventSub


# end class baseEventSub


class dataEventSub(supermod.dataEvent):
    def __init__(self, id=None, actions=None, message=None, type_=None, **kwargs_):
        super(dataEventSub, self).__init__(id, actions, message, type_, **kwargs_)


supermod.dataEvent.subclass = dataEventSub


# end class dataEventSub


class caseEventSub(supermod.caseEvent):
    def __init__(self, id=None, actions=None, message=None, type_=None, **kwargs_):
        super(caseEventSub, self).__init__(id, actions, message, type_, **kwargs_)


supermod.caseEvent.subclass = caseEventSub


# end class caseEventSub


class processEventSub(supermod.processEvent):
    def __init__(self, id=None, actions=None, message=None, type_=None, **kwargs_):
        super(processEventSub, self).__init__(id, actions, message, type_, **kwargs_)


supermod.processEvent.subclass = processEventSub


# end class processEventSub


class actionsSub(supermod.actions):
    def __init__(self, phase=None, action=None, actionRef=None, **kwargs_):
        super(actionsSub, self).__init__(phase, action, actionRef, **kwargs_)


supermod.actions.subclass = actionsSub


# end class actionsSub


class actionRefSub(supermod.actionRef):
    def __init__(self, id=None, **kwargs_):
        super(actionRefSub, self).__init__(id, **kwargs_)


supermod.actionRef.subclass = actionRefSub


# end class actionRefSub


class fieldViewSub(supermod.fieldView):
    def __init__(self, area=None, autocomplete=None, tree=None, table=None, image=None, editor=None, htmlEditor=None,
                 buttonType=None, list=None, **kwargs_):
        super(fieldViewSub, self).__init__(area, autocomplete, tree, table, image, editor, htmlEditor, buttonType, list,
                                           **kwargs_)


supermod.fieldView.subclass = fieldViewSub


# end class fieldViewSub


class booleanImageViewSub(supermod.booleanImageView):
    def __init__(self, true=None, false=None, **kwargs_):
        super(booleanImageViewSub, self).__init__(true, false, **kwargs_)


supermod.booleanImageView.subclass = booleanImageViewSub


# end class booleanImageViewSub


class formatSub(supermod.format):
    def __init__(self, currency=None, **kwargs_):
        super(formatSub, self).__init__(currency, **kwargs_)


supermod.format.subclass = formatSub


# end class formatSub


class currencySub(supermod.currency):
    def __init__(self, code='EUR', fractionSize=None, locale=None, **kwargs_):
        super(currencySub, self).__init__(code, fractionSize, locale, **kwargs_)


supermod.currency.subclass = currencySub


# end class currencySub


class eventSub(supermod.event):
    def __init__(self, id=None, actions=None, message=None, type_=None, title=None, **kwargs_):
        super(eventSub, self).__init__(id, actions, message, type_, title, **kwargs_)


supermod.event.subclass = eventSub


# end class eventSub


class initSub(supermod.init):
    def __init__(self, name=None, dynamic=False, valueOf_=None, **kwargs_):
        super(initSub, self).__init__(name, dynamic, valueOf_, **kwargs_)


supermod.init.subclass = initSub


# end class initSub


class caseUserRefSub(supermod.caseUserRef):
    def __init__(self, id=None, caseLogic=None, **kwargs_):
        super(caseUserRefSub, self).__init__(id, caseLogic, **kwargs_)


supermod.caseUserRef.subclass = caseUserRefSub


# end class caseUserRefSub


class caseRoleRefSub(supermod.caseRoleRef):
    def __init__(self, id=None, caseLogic=None, **kwargs_):
        super(caseRoleRefSub, self).__init__(id, caseLogic, **kwargs_)


supermod.caseRoleRef.subclass = caseRoleRefSub


# end class caseRoleRefSub


class userRefSub(supermod.userRef):
    def __init__(self, id=None, logic=None, **kwargs_):
        super(userRefSub, self).__init__(id, logic, **kwargs_)


supermod.userRef.subclass = userRefSub


# end class userRefSub


class roleRefSub(supermod.roleRef):
    def __init__(self, id=None, logic=None, **kwargs_):
        super(roleRefSub, self).__init__(id, logic, **kwargs_)


supermod.roleRef.subclass = roleRefSub


# end class roleRefSub


class optionSub(supermod.option):
    def __init__(self, name=None, key=None, valueOf_=None, **kwargs_):
        super(optionSub, self).__init__(name, key, valueOf_, **kwargs_)


supermod.option.subclass = optionSub


# end class optionSub


class validSub(supermod.valid):
    def __init__(self, dynamic=False, valueOf_=None, **kwargs_):
        super(validSub, self).__init__(dynamic, valueOf_, **kwargs_)


supermod.valid.subclass = validSub


# end class validSub


class documentSub(supermod.document):
    def __init__(self, id=None, version=None, initials=None, title=None, icon=None, defaultRole=True,
                 anonymousRole=True, transitionRole=True, caseName=None, roleRef=None, usersRef=None, userRef=None,
                 processEvents=None, caseEvents=None, transaction=None, role=None, function=None, data=None,
                 mapping=None, i18n=None, transition=None, place=None, arc=None, **kwargs_):
        super(documentSub, self).__init__(id, version, initials, title, icon, defaultRole, anonymousRole,
                                          transitionRole, caseName, roleRef, usersRef, userRef, processEvents,
                                          caseEvents, transaction, role, function, data, mapping, i18n, transition,
                                          place, arc, **kwargs_)


supermod.document.subclass = documentSub


# end class documentSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def validate_doc(doc):
    """
    The function first finds and sets the xml schema, then validates the xml document based on it, and
    if it is not valid, it prints an error and ends the program
    :param doc: loaded xml document
    :return:
    """
    # get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # build a relative path to the XSD schema file from the script directory
    xsd_path = os.path.join(script_dir, '..', 'resources', 'petriflow.schema.xsd')
    # use the relative path to load the XSD schema file
    xml_schema_doc = etree_.parse(xsd_path)

    xml_schema = etree_.XMLSchema(xml_schema_doc)

    if not xml_schema.validate(doc):
        sys.stdout.write('*** Something went wrong ***\n')
        # it catches the error, prints it, and ends the program
        print(xml_schema.assertValid(doc))


def import_xml(in_filename, silence=True, namespace_defs_location=NamespaceDefsLocation):
    """
    Reads the xml document from the path and, if it exists and is valid, returns the object of the document element.
    :param in_filename: path to the xml document
    :param silence: boolean attribute, if it is False, it will write the structure of the document to the output
    terminal after successful loading
    :param namespace_defs_location: schemaLocation & noNamespaceSchemaLocation provides hints to the XML processor
    as to how to associate an XSD with an XML document. We use noNamespaceSchemaLocation, because there is no namespace
    :return:
    """
    set_namespace_defs(namespace_defs_location)
    parser = None
    doc = parse_xml_(in_filename, parser)
    validate_doc(doc)
    root_node = doc.getroot()
    root_tag, root_class = get_root_tag(root_node)
    if root_class is None:
        root_tag = 'document'
        root_class = supermod.document
    root_obj = root_class.factory()
    root_obj.build(root_node)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        root_node = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        root_obj.export(
            sys.stdout, 0, name_=root_tag,
            namespacedef_='',
            pretty_print=True)
    sys.stdout.write('*** XML document has been imported ***\n')
    return root_obj


def export_xml(out_filename, save_in_folder):
    """
    Using the export() function creates an ElementTree for the root element and writes the entire ElementTree
    to the specified location.
    :param out_filename: object to the element of the document that we want to export
    :param save_in_folder: path to the place where the document will be stored
    :return:
    """
    new_file = open(save_in_folder, "w", encoding="utf-8")
    out_filename.export(new_file, 0)
    return new_file


def import_string(in_string, silence=True, namespace_defs_location=NamespaceDefsLocation):
    """
    Reads the xml document from the path and, if it exists and is valid, returns the object of the document element.
    :param in_string: path to the xml document
    :param silence: boolean attribute, if it is False, it will write the structure of the document to the output
    terminal after successful loading
    :param namespace_defs_location: schemaLocation & noNamespaceSchemaLocation provides hints to the XML processor
    as to how to associate an XSD with an XML document. We use noNamespaceSchemaLocation, because there is no namespace
    :return:
    """
    in_string = urlopen(in_string).read()  # z url navratova hodnota xmlka nie je xml ale str
    set_namespace_defs(namespace_defs_location)
    parser = None
    root_node = parse_xml_string_(in_string, parser)
    validate_doc(root_node.getroottree())
    root_tag, root_class = get_root_tag(root_node)
    if root_class is None:
        root_tag = 'document'
        root_class = supermod.document
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


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parse_xml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'transaction'
        rootClass = supermod.transaction
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parse_xml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'transaction'
        rootClass = supermod.transaction
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from import_xml_file import *\n\n')
        sys.stdout.write('import import_xml_file as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj

USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    import_xml(infilename)


if __name__ == '__main__':
    # import pdb; pdb.set_trace()
    main()
