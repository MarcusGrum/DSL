
""" 
A little script to provide basic functions for import and export of Modelangelo tool following the DSL standard. 
Copyright (c) 2022 Marcus Grum
""" 

__author__ = 'Marcus Grum, marcus.grum@uni-potsdam.de'
# SPDX-License-Identifier: AGPL-3.0-or-later or individual license
# SPDX-FileCopyrightText: 2022 Marcus Grum <marcus.grum@uni-potsdam.de>

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import random
import string
from os import listdir
from os.path import isfile, join
from xml.dom import minidom

def initialize_global_modelangelo_variables():
    """This function initializes relevant variables globally."""
        
    global maxIdOfNodeItems
    maxIdOfNodeItems = 0
    
    global maxIdOfEdgeItems
    maxIdOfEdgeItems = 0
    
    global maxIdOfLabelItems
    maxIdOfLabelItems = 0
    
    global maxIdOfMutantObjects
    maxIdOfMutantObjects = 0
    
    global maxIdOfMutantConnections
    maxIdOfMutantConnections = 0
    
    global maxIdOfAttributes
    maxIdOfAttributes = 0      

    global maxIdOfMetaAttributes          
    maxIdOfMetaAttributes = 0

    global maxIdOfMetaAttributesToGraphics
    maxIdOfMetaAttributesToGraphics = 0
    
    global processView_x, processView_y
    processView_x = 0
    processView_y = 0
    
    global activityView_x, activityView_y
    activityView_x = 0
    activityView_y = 0
    
    global knowledgeOverview_x, knowledgeOverview_y
    knowledgeOverview_x = 0
    knowledgeOverview_y = 0

def create_blancModelangeloFile(path):
    """
    This functions creates a Modelangelo xml compliant file having one model for each kind of view.
    """
    
    f = open(path, 'w')
    f.writelines('<dataset>\n')
    #f.writelines('  <attribute />\n')
    f.writelines('  <attribute_visibility />\n')
    #f.writelines('  <edge_item />\n')
    #f.writelines('  <label_item />\n')
    #f.writelines('  <meta_attribute />\n')
    f.writelines('  <meta_attributes_to_graphic />\n')
    f.writelines('  <model area="" attentiongroup="" author="Modelangelo DSL Import Module" contentlanguage="" date="2021-01-25 11:52:47.0" description="Process view generated on the basis of DSL file" id="1" localname="[NULL]" location="" mail="" name="Example-ProcessView" project="1" publicmodel="not relevant" state="draft" url="none" validfor="" validuntil="2023-03-01" version="v01" view="DSL.process_view" />\n')
    f.writelines('  <model area="" attentiongroup="" author="Modelangelo DSL Import Module" contentlanguage="" date="2021-01-25 11:52:47.0" description="Activity view generated on the basis of DSL file" id="2" localname="[NULL]" location="" mail="" name="Example-ActivityView" project="1" publicmodel="not relevant" state="draft" url="none" validfor="" validuntil="2023-03-01" version="v01" view="DSL.activity_view" />\n')
    f.writelines('  <model area="" attentiongroup="" author="Modelangelo DSL Import Module" contentlanguage="" date="2021-01-25 11:52:47.0" description="Knowledge overview generated on the basis of DSL file" id="3" localname="[NULL]" location="" mail="" name="Example-KnowledgeOverview" project="1" publicmodel="not relevant" state="draft" url="none" validfor="" validuntil="2023-03-01" version="v01" view="DSL.knowledge_overview" />\n')
    #f.writelines('  <mutant_connection />\n')
    #f.writelines('  <mutant_object />\n')
    #f.writelines('  <node_item />\n')
    f.writelines('  <project area="" attentiongroup="" author="Modelangelo DSL Import Module" contentlanguage="" date="2021-01-25 11:52:47.0" description="This is a project to show DSL importer module." id="1" localname="" location="" mail="" meta_model="dsl" name="DSL-Importer-Example" publicproject="not relevant" state="draft" url="none" validfor="" validuntil="2023-03-01" version="v01" />\n')
    f.writelines('  <property name="project.last-used-model" value="2" />\n')
    f.writelines('  <view />\n')
    f.writelines('  <graphics_to_view />\n')
    f.writelines('</dataset>\n')
    f.close()

def create_edgeItem(xmlData, model, connectionCreated_type, source_item_id, target_item_id, source_mutant_id, target_mutant_id, labelCreated_Text, X, Y):
    """This function creates one edgeItem element."""
    
    # work with global maximal IDs
    global maxIdOfNodeItems
    global maxIdOfEdgeItems
    global maxIdOfLabelItems
    global maxIdOfMutantObjects
    global maxIdOfMutantConnections
    global maxIdOfAttributes
    global maxIdOfMetaAttributes
    global maxIdOfMetaAttributesToGraphics
        
    mutantConnectionCreated_MC_ID = ''.join([random.choice(string.ascii_lowercase + string.digits) for n in range(12)])
    
    # reservation for new edge_item
    maxIdOfEdgeItems = maxIdOfEdgeItems + 1 
    maxIdOfLabelItems = maxIdOfLabelItems + 1
    maxIdOfMutantConnections = maxIdOfMutantConnections + 1
    
    # add edge item
    newEdgeItem = ET.Element("edge_item")
    newEdgeItem.set('id', str(maxIdOfEdgeItems))
    newEdgeItem.set('model', str(model))
    newEdgeItem.set('mutant_connection', str(maxIdOfMutantConnections))
    newEdgeItem.set('shape', 'dsl.edges.' + connectionCreated_type)
    newEdgeItem.set('source', str(source_item_id))
    newEdgeItem.set('target', str(target_item_id))
    newEdgeItem.set('source_edge', '[NULL]')
    newEdgeItem.set('target_edge', '[NULL]')
    newEdgeItem.set('type', '0')
    newEdgeItem.set('shape_data', '')
    newEdgeItem.set('size', '2.0')
    newEdgeItem.set('fill_color', '-16777216') 
    newEdgeItem.set('stroke_color', '-16777216')
    newEdgeItem.set('stroke_width', '2.0')
    newEdgeItem.set('labeled', 'true')
    newEdgeItem.set('visible', 'true')
    newEdgeItem.set('data_group', 'graph.edges')
    xmlData.append(newEdgeItem)
    
    # add mutant connection
    newMutantConnection =  ET.Element("mutant_connection")
    newMutantConnection.set('id', str(maxIdOfMutantConnections))
    newMutantConnection.set('mc_id', str(mutantConnectionCreated_MC_ID))
    newMutantConnection.set('default_shape', 'dsl.edges.' + connectionCreated_type)
    newMutantConnection.set('source', str(source_mutant_id))
    newMutantConnection.set('target', str(target_mutant_id))
    newMutantConnection.set('source_connection', '[NULL]')
    newMutantConnection.set('target_connection', '[NULL]')
    xmlData.append(newMutantConnection)
    
    # add label item
    newLabelItem =  ET.Element("label_item")
    newLabelItem.set('id', str(maxIdOfLabelItems))
    newLabelItem.set('node', '[NULL]')
    newLabelItem.set('edge', str(maxIdOfEdgeItems))
    newLabelItem.set('text', labelCreated_Text)
    newLabelItem.set('x', str(100.0))
    newLabelItem.set('y', str(100.0))
    newLabelItem.set('font', '')
    newLabelItem.set('font_color', '-16777216')
    newLabelItem.set('font_size', '12')
    newLabelItem.set('visible', 'true')
    newLabelItem.set('h_align', '0')
    newLabelItem.set('v_align', '0')
    xmlData.append(newLabelItem)
    
    #return xmlData

def create_nodeItem(xmlData, model, nodeCreated_type, labelCreated_Text, X, Y, parent_id):
    """This function creates one nodeItem element."""
    
    # work with global maximal IDs
    global maxIdOfNodeItems
    global maxIdOfEdgeItems
    global maxIdOfLabelItems
    global maxIdOfMutantObjects
    global maxIdOfMutantConnections
    global maxIdOfAttributes
    global maxIdOfMetaAttributes
    global maxIdOfMetaAttributesToGraphics
        
    mutantObjectCreated_MO_ID = ''.join([random.choice(string.ascii_lowercase + string.digits) for n in range(12)])
    
    # reservation for new node_item
    maxIdOfNodeItems = maxIdOfNodeItems + 1 
    maxIdOfLabelItems = maxIdOfLabelItems + 1
    maxIdOfMutantObjects = maxIdOfMutantObjects + 1
       
    # add node_item
    newNodeItem = ET.Element("node_item")
    newNodeItem.set('id', str(maxIdOfNodeItems))
    newNodeItem.set('model', str(model))
    newNodeItem.set('mutant_object', str(maxIdOfMutantObjects))
    newNodeItem.set('shape', 'dsl.nodes.' + nodeCreated_type)
    if(parent_id != 0):
        newNodeItem.set('parent', str(parent_id))
    else:
        newNodeItem.set('parent', '[NULL]')
    newNodeItem.set('x', str(X))
    newNodeItem.set('y', str(Y))
    newNodeItem.set('z', '268435956')
    if (nodeCreated_type == 'task'):
        newNodeItem.set('width', '80.0')
        newNodeItem.set('height', '33.0')
        newNodeItem.set('fill_color', '-2162740')
    elif (nodeCreated_type == 'process_border'):
        newNodeItem.set('width', '120.0')
        newNodeItem.set('height', '33.0')
        #newNodeItem.set('width', '1060.0')
        #newNodeItem.set('height', '180.0')
        newNodeItem.set('fill_color', '-1')
    elif (nodeCreated_type == 'role'):
        newNodeItem.set('width', '80.0')
        newNodeItem.set('height', '33.0')
        newNodeItem.set('fill_color', '-48')
    elif (nodeCreated_type == 'information_system'):
        newNodeItem.set('width', '80.0')
        newNodeItem.set('height', '33.0')
        newNodeItem.set('fill_color', '-48')
    elif (nodeCreated_type == 'and'):
        newNodeItem.set('width', '33.0')
        newNodeItem.set('height', '33.0')
        newNodeItem.set('fill_color', '-1')
    elif (nodeCreated_type == 'or'):
        newNodeItem.set('width', '33.0')
        newNodeItem.set('height', '33.0')
        newNodeItem.set('fill_color', '-1')
    elif (nodeCreated_type == 'xor'):
        newNodeItem.set('width', '33.0')
        newNodeItem.set('height', '33.0')
        newNodeItem.set('fill_color', '-1')
    elif (nodeCreated_type == 'activity_border'):
        newNodeItem.set('width', '120.0')
        newNodeItem.set('height', '33.0')
        newNodeItem.set('fill_color', '-1')
    elif (nodeCreated_type == 'conversion'):
        newNodeItem.set('width', '80.0')
        newNodeItem.set('height', '33.0')
        newNodeItem.set('fill_color', '-4398647')
    elif (nodeCreated_type == 'information_object'):
        newNodeItem.set('width', '100.0')
        newNodeItem.set('height', '33.0')
        newNodeItem.set('fill_color', '-1394761')
    elif (nodeCreated_type == 'knowledge_object'):
        newNodeItem.set('width', '100.0')
        newNodeItem.set('height', '33.0')
        newNodeItem.set('fill_color', '-2704169')
    elif (nodeCreated_type == 'mixed_knowledge_object'):
        newNodeItem.set('width', '100.0')
        newNodeItem.set('height', '33.0')
        newNodeItem.set('fill_color', '-2704169')
    elif (nodeCreated_type == 'person'):
        newNodeItem.set('width', '63.0')
        newNodeItem.set('height', '45.0') # 33.0
        newNodeItem.set('fill_color', '-1')
    elif (nodeCreated_type == 'knowledge_border'):
        newNodeItem.set('width', '120.0')
        newNodeItem.set('height', '33.0')
        newNodeItem.set('fill_color', '-1')
    else:
        newNodeItem.set('width', '90.0')
        newNodeItem.set('fill_color', '-1')
        newNodeItem.set('height', '33.0')
    newNodeItem.set('size', '1.0')        
    newNodeItem.set('stroke_color', '-16711423')
    newNodeItem.set('stroke_width', '1.0')
    newNodeItem.set('labeled', 'true')
    newNodeItem.set('visible', 'true')
    newNodeItem.set('data_group', 'graph.nodes')
    xmlData.append(newNodeItem)
    
    # add mutant_object
    newMutantObject =  ET.Element("mutant_object")
    newMutantObject.set('id', str(maxIdOfMutantObjects))
    newMutantObject.set('mo_id', str(mutantObjectCreated_MO_ID))
    newMutantObject.set('default_shape', 'dsl.nodes.' + nodeCreated_type)
    xmlData.append(newMutantObject)
    
    # add label_item
    newLabelItem =  ET.Element("label_item")
    newLabelItem.set('id', str(maxIdOfLabelItems))
    newLabelItem.set('node', str(maxIdOfNodeItems))
    newLabelItem.set('edge', '[NULL]')
    newLabelItem.set('text', labelCreated_Text)
    newLabelItem.set('x', str(X))
    newLabelItem.set('y', str(Y))
    newLabelItem.set('font', 'MyriadPro-Regular')
    newLabelItem.set('font_color', '-16777216')
    newLabelItem.set('font_size', '12')
    newLabelItem.set('visible', 'true')
    newLabelItem.set('h_align', '2')
    if ((nodeCreated_type == 'process_border') or (nodeCreated_type == 'activity_border') or (nodeCreated_type == 'knowledge_border')):
        newLabelItem.set('v_align', '4')
    else:
        newLabelItem.set('v_align', '2')
    xmlData.append(newLabelItem)
    
    #return xmlData

def create_attributeItem(xmlData, name, value, data_type, mutant_id):
    """This function creates one attributeItem element."""

    printing = False

    # work with global maximal IDs
    global maxIdOfNodeItems
    global maxIdOfEdgeItems
    global maxIdOfLabelItems
    global maxIdOfMutantObjects
    global maxIdOfMutantConnections
    global maxIdOfAttributes
    global maxIdOfMetaAttributes
    global maxIdOfMetaAttributesToGraphics

    metaAttributeCreated_AT_ID = ''.join([random.choice(string.ascii_lowercase + string.digits) for n in range(12)])
    
    # reservation for new edge_item
    maxIdOfAttributes = maxIdOfAttributes + 1

    # check if meta_attribute already exists
    metaAttributeExists = False
    for child_1 in xmlData: # root level
        if printing: print('', child_1.tag, child_1.attrib, child_1.text)
        if('meta_attribute' == child_1.tag):
            if(child_1.attrib['name'] == name):
                metaAttributeExists = True
                currentIdOfMetaAttributes = child_1.attrib['id']
    if(metaAttributeExists == False):
        maxIdOfMetaAttributes = maxIdOfMetaAttributes + 1
        currentIdOfMetaAttributes = maxIdOfMetaAttributes

        # add meta attribute
        newMetaAttribute = ET.Element("meta_attribute")
        newMetaAttribute.set('id', str(maxIdOfMetaAttributes))
        newMetaAttribute.set('at_id', str(metaAttributeCreated_AT_ID))
        newMetaAttribute.set('name', str(name))
        newMetaAttribute.set('data_type', str(data_type))
        xmlData.append(newMetaAttribute)

    # add attribute
    newAttribute = ET.Element("attribute")
    newAttribute.set('id', str(maxIdOfAttributes))
    newAttribute.set('meta_attribute', str(currentIdOfMetaAttributes))
    newAttribute.set('mutant_object', str(mutant_id))
    newAttribute.set('mutant_connection', str('[NULL]'))
    newAttribute.set('meta_attributes_to_graphic', str('[NULL]'))
    newAttribute.set('value', str(value))
    xmlData.append(newAttribute)

def load_Data_from_xmlFile(path):
    """
    This function loads a xml compliant file and returns the xml content by the element called 'xmlData'.
    """ 
    tree = ET.parse(path)
    xmlData = tree.getroot()
    
    # care about small caps
    for child in xmlData:
        element = child.attrib
        if element.keys():
            temp=[]
            for name, value in element.items():
                temp.append([name, value])
            for i in range(len(temp)):
                element[temp[i][0].lower()] = element.pop(temp[i][0])
                
    return xmlData

def screen_xmlData(xmlData):
    """
    This functions screens the ElementTreeData content by console output of the element called 'xmlData'.
    """ 
    for child in xmlData:
        print(child.tag, child.attrib)
        
def screen_jasonBasedXmlData(xmlData):
    """
    This functions screens the ElementTreeData content by console output of the element called 'xmlData'.
    """ 
    for child_1 in xmlData: # root level
        print('', child_1.tag, child_1.attrib, child_1.text)
        for child_2 in child_1: # dialog level
            print('  ', child_2.tag, child_2.attrib, child_2.text)
            for child_3 in child_2: # item level
                print('     ', child_3.tag, child_3.attrib, child_3.text)
                for child_4 in child_3: # dialog_name/step level
                    print('         ', child_4.tag, child_4.attrib, child_4.text)
                    for child_5 in child_4: # item level
                        print('             ', child_5.tag, child_5.attrib, child_5.text)
                        for child_6 in child_5: # utterance level
                            print('                 ', child_6.tag, child_6.attrib, child_6.text)
                            for child_7 in child_6: # user_response/bot_response level
                                print('                     ', child_7.tag, child_7.attrib, child_7.text)  
                                for child_8 in child_7: # response/intent level
                                    print('                         ', child_8.tag, child_8.attrib, child_8.text)
                                    for child_9 in child_8: # slot(name/value) level
                                        print('                             ', child_9.tag, child_9.attrib, child_9.text) 

def save_xmlData_to_file(xmlData, path):
    """
    This functions saves the xml content of the element called 'xmlData' to the 'path'.
    """ 
    # create a new XML file with the results for Anaconda3
    tree = ET.ElementTree(xmlData)
    tree.write(path)
    
def save_xmlData_to_file_pretty(xmlData, path):
    """
    This functions saves the xml content of the element called 'xmlData' to the 'path'.
    """ 
    # create a new XML file with the results for Anaconda3
    prettified_xmlStr = prettify(xmlData)
    output_file = open(path, "w")
    output_file.write(prettified_xmlStr)
    output_file.close()

def modification_modelangelo_createAllNodeItemsTest(modelangeloXmlData):
    """
    This function creates all kinds of nodeItems and adds it to xml data called 'modelangeloXmlData' and returns it.
    """ 
    global processView_x, processView_y, activityView_x, activityView_y, knowledgeOverview_x, knowledgeOverview_y
    
    # - test process view items
    create_nodeItem(modelangeloXmlData, 1, 'process_border', 'Process Border', processView_x, processView_y)
    processView_y = processView_y + 40
    create_nodeItem(modelangeloXmlData, 1, 'task', 'Task-Label', processView_x, processView_y, 0)
    create_nodeItem(modelangeloXmlData, 1, 'task', 'Task-Label', processView_x + 120, processView_y, 0)
    create_edgeItem(modelangeloXmlData, 1, 'control_flow', 2, 3, 2, 3, '', processView_x+100, processView_y)
    processView_y = processView_y + 40
    create_nodeItem(modelangeloXmlData, 1, 'information_system', 'Information System', processView_x, processView_y, 0)
    processView_y = processView_y + 40
    create_nodeItem(modelangeloXmlData, 1, 'and', '', processView_x, processView_y, 0)
    processView_y = processView_y + 40
    create_nodeItem(modelangeloXmlData, 1, 'or', '', processView_x, processView_y, 0)
    processView_y = processView_y + 40
    create_nodeItem(modelangeloXmlData, 1, 'xor', '', processView_x, processView_y, 0)
    processView_y = processView_y + 40
    create_nodeItem(modelangeloXmlData, 1, 'role', 'Role', processView_x, processView_y, 0)
    processView_y = processView_y + 40
    
    # - test activity view items
    create_nodeItem(modelangeloXmlData, 2, 'activity_border', 'Activity Border', activityView_x, activityView_y, 0)
    activityView_y = activityView_y + 40
    create_nodeItem(modelangeloXmlData, 2, 'conversion', 'Activity', activityView_x, activityView_y, 0)
    activityView_y = activityView_y + 40
    create_nodeItem(modelangeloXmlData, 2, 'information_system', 'Information System', activityView_x, activityView_y, 0)
    activityView_y = activityView_y + 40
    create_nodeItem(modelangeloXmlData, 2, 'person', 'Person', activityView_x, activityView_y, 0)
    activityView_y = activityView_y + 40
    create_nodeItem(modelangeloXmlData, 2, 'information_object', 'Explicit Knowledge', activityView_x, activityView_y, 0)
    activityView_y = activityView_y + 40
    create_nodeItem(modelangeloXmlData, 2, 'knowledge_object', 'Tacit Knowledge', activityView_x, activityView_y, 0)
    activityView_y = activityView_y + 40
    create_nodeItem(modelangeloXmlData, 2, 'mixed_knowledge_object', 'Mixed Knowledge', activityView_x, activityView_y, 0)
    activityView_y = activityView_y + 40
    
    # - test knowledge overview items
    create_nodeItem(modelangeloXmlData, 3, 'knowledge_border', 'Knowledge Border', knowledgeOverview_x, knowledgeOverview_y, 0)
    knowledgeOverview_y = knowledgeOverview_y + 40
    create_nodeItem(modelangeloXmlData, 3, 'information_system', 'Information System', knowledgeOverview_x, knowledgeOverview_y, 0)
    knowledgeOverview_y = knowledgeOverview_y + 40
    create_nodeItem(modelangeloXmlData, 3, 'person', 'Person', knowledgeOverview_x, knowledgeOverview_y, 0)
    knowledgeOverview_y = knowledgeOverview_y + 40
    create_nodeItem(modelangeloXmlData, 3, 'information_object', 'Explicit Knowledge', knowledgeOverview_x, knowledgeOverview_y, 0)
    knowledgeOverview_y = knowledgeOverview_y + 40
    create_nodeItem(modelangeloXmlData, 3, 'knowledge_object', 'Tacit Knowledge', knowledgeOverview_x, knowledgeOverview_y, 0)
    knowledgeOverview_y = knowledgeOverview_y + 40
    create_nodeItem(modelangeloXmlData, 3, 'mixed_knowledge_object', 'Mixed Knowledge', knowledgeOverview_x, knowledgeOverview_y, 0)
    knowledgeOverview_y = knowledgeOverview_y + 40
    
    return modelangeloXmlData

def modification_modelangelo_importDslFiles(modelangeloXmlData, chatBotXmlData_dialogs, chatBotXmlData_dialog_activity_integrations, chatBotXmlData_aliases, chatBotXmlData_contacts, chatBotXmlData_users, chatBotXmlData_intents, chatBotXmlData_invoices, chatBotXmlData_orders, chatBotXmlData_pricelists, chatBotXmlData_products, chatBotXmlData_activities, chatBotXmlData_cases, chatBotXmlData_actions, chatBotXmlData_responses, chatBotXmlData_slots):
    """
    This function creates all kinds of nodeItems and adds it to xml data called 'modelangeloXmlData' and returns it.
    """

    printing = False

    global processView_x, processView_y, activityView_x, activityView_y, knowledgeOverview_x, knowledgeOverview_y
    
    # work with global maximal IDs
    global maxIdOfNodeItems
    global maxIdOfEdgeItems
    global maxIdOfLabelItems
    global maxIdOfMutantObjects
    global maxIdOfMutantConnections
    global maxIdOfAttributes
    global maxIdOfMetaAttributes
    global maxIdOfMetaAttributesToGraphics
    
    # import dialogs.dsl xml file
    print('importing dialogs...')
    parent_id = 0
    for child_1 in chatBotXmlData_dialogs: # root level
        if printing: print('', child_1.tag, child_1.attrib, child_1.text)
        for child_2 in child_1: # dialog level
            if printing: print('  ', child_2.tag, child_2.attrib, child_2.text)
            for child_3 in child_2: # item level
                if printing: print('     ', child_3.tag, child_3.attrib, child_3.text)
                # indicate individual dialog by process_border node
                if(child_3.tag=='dialog_name'):
                    processView_x = 0
                    processView_y = processView_y + 200
                    create_nodeItem(modelangeloXmlData, 1, 'process_border', child_3.text, processView_x-40, processView_y, 0)
                    processView_y = processView_y + 40
                    parent_id = maxIdOfNodeItems
                    task_no = 0
                for child_4 in child_3: # dialog_name/step level
                    if printing: print('         ', child_4.tag, child_4.attrib, child_4.text)
                    for child_5 in child_4: # item level
                        if printing: print('             ', child_5.tag, child_5.attrib, child_5.text)
                        # reset x so that each dialog starts at 0
                        processView_x = 0
                        for child_6 in child_5: # utterance level
                            if printing: print('                 ', child_6.tag, child_6.attrib, child_6.text)
                            for child_7 in child_6: # user_response/bot_response level
                                if printing: print('                     ', child_7.tag, child_7.attrib, child_7.text)
                                for child_8 in child_7: # response/intent level
                                    if printing: print('                         ', child_8.tag, child_8.attrib, child_8.text)
                                    if(child_8.tag=='intent'):
                                        create_nodeItem(modelangeloXmlData, 1, 'task', child_8.text, processView_x, processView_y, parent_id)
                                        processView_x = processView_x + 80
                                        task_no = task_no + 1
                                        if (task_no > 1):
                                            create_edgeItem(modelangeloXmlData, 1, 'control_flow', maxIdOfNodeItems-2, maxIdOfNodeItems, maxIdOfMutantObjects-2, maxIdOfMutantObjects, '', processView_x+60, processView_y)
                                    if(child_8.tag=='response'):
                                        create_nodeItem(modelangeloXmlData, 1, 'task', child_8.text, processView_x, processView_y, parent_id)
                                        processView_x = processView_x + 80
                                        task_no = task_no + 1
                                        if (task_no > 1):
                                            create_edgeItem(modelangeloXmlData, 1, 'control_flow', maxIdOfNodeItems-2, maxIdOfNodeItems, maxIdOfMutantObjects-2, maxIdOfMutantObjects, '', processView_x+60, processView_y)
                                    if(child_8.tag=='slot'):
                                        name = ''
                                        value = ''
                                        for child_9 in child_8: # slot(name/value) level
                                            if printing: print('                             ', child_9.tag, child_9.attrib, child_9.text)
                                            if(child_9.tag=='name'):
                                                name = child_9.text
                                            if(child_9.tag=='value'):
                                                value = child_9.text
                                                create_attributeItem(modelangeloXmlData, name, value, 'Text', maxIdOfMutantObjects)
     
                                # position role of user_response/bot_response 
                                if(child_7.tag=='user_response'):
                                    create_nodeItem(modelangeloXmlData, 1, 'role', 'User', processView_x-80, processView_y+70, parent_id)
                                    create_edgeItem(modelangeloXmlData, 1, 'membership', maxIdOfNodeItems, maxIdOfNodeItems-1, maxIdOfMutantObjects, maxIdOfMutantObjects-1, '', processView_x, processView_y+70)
                                if(child_7.tag=='bot_response'):
                                    create_nodeItem(modelangeloXmlData, 1, 'information_system', 'Chatbot', processView_x-80, processView_y+70, parent_id)
                                    create_edgeItem(modelangeloXmlData, 1, 'membership', maxIdOfNodeItems, maxIdOfNodeItems-1, maxIdOfMutantObjects, maxIdOfMutantObjects-1, '', processView_x, processView_y+70)
                            # increase x so that each dialog step shifts from left to right
                            processView_x = processView_x + 100
    # import aliases.dsl xml file
    print('importing aliases...')
    for child_1 in chatBotXmlData_aliases: # root level
        if printing: print('', child_1.tag, child_1.attrib, child_1.text)
        # indicate individual alias sections by knowledge_border node
        if(child_1.tag=='aliases'):
            create_nodeItem(modelangeloXmlData, 3, 'knowledge_border', child_1.tag, knowledgeOverview_x-40, knowledgeOverview_y, 0)
            knowledgeOverview_y = knowledgeOverview_y + 40
            border_id = maxIdOfNodeItems
        for child_2 in child_1: # aliases level
            if printing: print('  ', child_2.tag, child_2.attrib, child_2.text)
            for child_3 in child_2: # item level
                if printing: print('     ', child_3.tag, child_3.attrib, child_3.text)
                if(child_3.tag!=''):
                    create_nodeItem(modelangeloXmlData, 3, 'information_system', 'CRM', knowledgeOverview_x+160, knowledgeOverview_y, border_id)
                    create_nodeItem(modelangeloXmlData, 3, 'information_object', child_3.tag, knowledgeOverview_x, knowledgeOverview_y, border_id)
                    create_edgeItem(modelangeloXmlData, 3, 'membership', maxIdOfNodeItems, maxIdOfNodeItems-1, maxIdOfMutantObjects, maxIdOfMutantObjects-1, '', knowledgeOverview_x+80, knowledgeOverview_y)
                    knowledgeOverview_y = knowledgeOverview_y + 80
                    parent_id = maxIdOfNodeItems
                    child_no = 0
                for child_4 in child_3: # member level
                    if printing: print('         ', child_4.tag, child_4.attrib, child_4.text)
                    if(child_4.tag!=''):
                        create_nodeItem(modelangeloXmlData, 3, 'information_object', child_4.text, knowledgeOverview_x, knowledgeOverview_y, border_id)
                        knowledgeOverview_x = knowledgeOverview_x + 120
                        create_edgeItem(modelangeloXmlData, 3, 'aggregation', maxIdOfNodeItems, maxIdOfNodeItems-1-child_no, maxIdOfMutantObjects, maxIdOfMutantObjects-1-child_no, '', knowledgeOverview_x+40, knowledgeOverview_y+40)
                        child_no = child_no + 1
    # import contacts.dsl xml file
    knowledgeOverview_x  = 0
    knowledgeOverview_y = knowledgeOverview_y + 80        
    print('importing contacts...')
    for child_1 in chatBotXmlData_contacts: # contacts level
        if printing: print('', child_1.tag, child_1.attrib, child_1.text)
        # indicate individual contact sections by knowledge_border node
        if(child_1.tag=='contacts'):
            create_nodeItem(modelangeloXmlData, 3, 'knowledge_border', child_1.tag, knowledgeOverview_x-40, knowledgeOverview_y, 0)
            knowledgeOverview_y = knowledgeOverview_y + 40
            border_id = maxIdOfNodeItems
        for child_2 in child_1: # item level
            if printing: print('  ', child_2.tag, child_2.attrib, child_2.text)
            for child_3 in child_2: # fullName/gender/jobTitle/city/country/postalCode level
                if printing: print('     ', child_3.tag, child_3.attrib, child_3.text)
                if(child_3.tag=='fullName'):
                    create_nodeItem(modelangeloXmlData, 3, 'information_system', 'CRM', knowledgeOverview_x+160, knowledgeOverview_y, border_id)
                    create_nodeItem(modelangeloXmlData, 3, 'information_object', child_3.text, knowledgeOverview_x, knowledgeOverview_y, border_id)
                    create_edgeItem(modelangeloXmlData, 3, 'membership', maxIdOfNodeItems, maxIdOfNodeItems-1, maxIdOfMutantObjects, maxIdOfMutantObjects-1, '', knowledgeOverview_x+80, knowledgeOverview_y)
                    knowledgeOverview_y = knowledgeOverview_y + 60
                    parent_id = maxIdOfNodeItems
                    child_no = 0
                    for child_3b in child_2: # fullName/gender/jobTitle/city/country/postalCode level
                        if printing: print('         ', child_3b.tag, child_3b.attrib, child_3b.text)
                        if(child_3b.tag!=''):
                            #create_nodeItem(modelangeloXmlData, 3, 'information_object', child_3b.text, knowledgeOverview_x, knowledgeOverview_y, border_id)
                            #knowledgeOverview_x = knowledgeOverview_x + 120
                            #create_edgeItem(modelangeloXmlData, 3, 'aggregation', maxIdOfNodeItems, maxIdOfNodeItems-1-child_no, maxIdOfMutantObjects, maxIdOfMutantObjects-1-child_no, '', knowledgeOverview_x+40, knowledgeOverview_y+40)
                            #child_no = child_no + 1
                            create_attributeItem(modelangeloXmlData, child_3b.tag, child_3b.text, 'Text', maxIdOfMutantObjects)

    # import users.dsl xml file
    knowledgeOverview_x  = 0
    knowledgeOverview_y = knowledgeOverview_y + 20
    print('importing users...')
    for child_1 in chatBotXmlData_users: # users level
        if printing: print('', child_1.tag, child_1.attrib, child_1.text)
        # indicate individual users sections by knowledge_border node
        if(child_1.tag=='users'):
            create_nodeItem(modelangeloXmlData, 3, 'knowledge_border', child_1.tag, knowledgeOverview_x-40, knowledgeOverview_y, 0)
            knowledgeOverview_y = knowledgeOverview_y + 40
            border_id = maxIdOfNodeItems
        for child_2 in child_1: # item level
            if printing: print('  ', child_2.tag, child_2.attrib, child_2.text)
            for child_3 in child_2: # identifier/name/businessUnit/title/phone level
                if printing: print('     ', child_3.tag, child_3.attrib, child_3.text)
                if(child_3.tag=='name'):
                    create_nodeItem(modelangeloXmlData, 3, 'information_system', 'HRM', knowledgeOverview_x+160, knowledgeOverview_y, border_id)
                    create_nodeItem(modelangeloXmlData, 3, 'information_object', child_3.text, knowledgeOverview_x, knowledgeOverview_y, border_id)
                    create_edgeItem(modelangeloXmlData, 3, 'membership', maxIdOfNodeItems, maxIdOfNodeItems-1, maxIdOfMutantObjects, maxIdOfMutantObjects-1, '', knowledgeOverview_x+80, knowledgeOverview_y)
                    knowledgeOverview_y = knowledgeOverview_y + 60
                    parent_id = maxIdOfNodeItems
                    child_no = 0
                    for child_3b in child_2: # identifier/name/businessUnit/title/phone level
                        if printing: print('         ', child_3b.tag, child_3b.attrib, child_3b.text)
                        if(child_3b.tag!=''):
                            #create_nodeItem(modelangeloXmlData, 3, 'information_object', child_3b.text, knowledgeOverview_x, knowledgeOverview_y, border_id)
                            #knowledgeOverview_x = knowledgeOverview_x + 120
                            #create_edgeItem(modelangeloXmlData, 3, 'aggregation', maxIdOfNodeItems, maxIdOfNodeItems-1-child_no, maxIdOfMutantObjects, maxIdOfMutantObjects-1-child_no, '', knowledgeOverview_x+40, knowledgeOverview_y+40)
                            #child_no = child_no + 1
                            create_attributeItem(modelangeloXmlData, child_3b.tag, child_3b.text, 'Text', maxIdOfMutantObjects)

    # import intents.dsl xml file
    knowledgeOverview_x  = 0
    knowledgeOverview_y = knowledgeOverview_y + 20
    print('importing intents...')
    for child_1 in chatBotXmlData_intents: # intents level
        if printing: print('', child_1.tag, child_1.attrib, child_1.text)
        # indicate individual users sections by knowledge_border node
        if(child_1.tag=='intents'):
            create_nodeItem(modelangeloXmlData, 3, 'knowledge_border', child_1.tag, knowledgeOverview_x-40, knowledgeOverview_y, 0)
            knowledgeOverview_y = knowledgeOverview_y + 40
            border_id = maxIdOfNodeItems
        for child_2 in child_1: # item level
            if printing: print('  ', child_2.tag, child_2.attrib, child_2.text)
            knowledgeOverview_x = 0
            
            for child_3 in child_2: # greet/goodbye level
                if printing: print('     ', child_3.tag, child_3.attrib, child_3.text)
                if(child_3.tag!=''):
                    create_nodeItem(modelangeloXmlData, 3, 'information_system', 'Chatbot', knowledgeOverview_x+160, knowledgeOverview_y, border_id)
                    create_nodeItem(modelangeloXmlData, 3, 'information_object', child_3.tag, knowledgeOverview_x, knowledgeOverview_y, border_id)
                    create_edgeItem(modelangeloXmlData, 3, 'membership', maxIdOfNodeItems, maxIdOfNodeItems-1, maxIdOfMutantObjects, maxIdOfMutantObjects-1, '', knowledgeOverview_x+80, knowledgeOverview_y)
                    knowledgeOverview_y = knowledgeOverview_y + 60
                    parent_id = maxIdOfNodeItems
                    child_no = 0
                for child_4 in child_3: # hey/hello/... level
                    if printing: print('         ', child_4.tag, child_4.attrib, child_4.text)
                    if('\n' in child_4.text) != True:
                        create_nodeItem(modelangeloXmlData, 3, 'information_object', child_4.text, knowledgeOverview_x, knowledgeOverview_y, border_id)
                        knowledgeOverview_x = knowledgeOverview_x + 120
                        create_edgeItem(modelangeloXmlData, 3, 'aggregation', maxIdOfNodeItems, maxIdOfNodeItems-1-child_no, maxIdOfMutantObjects, maxIdOfMutantObjects-1-child_no, '', knowledgeOverview_x+40, knowledgeOverview_y+40)
                        child_no = child_no + 1
                    else:
                        for child_5 in child_4: # slots level
                            if printing: print('             ', child_5.tag, child_5.attrib, child_5.text)
                            for child_6 in child_5: # item level
                                if printing: print('                 ', child_6.tag, child_6.attrib, child_6.text)
                                name = ''
                                value = ''  
                                for child_7 in child_6: # text/slot level
                                    if printing: print('                     ', child_7.tag, child_7.attrib, child_7.text)
                                    if(child_7.tag=='text'):
                                        text = child_7.text
                                    if(child_7.tag=='slot'):
                                        slot = child_7.text
                                        create_nodeItem(modelangeloXmlData, 3, 'information_object', text + ' $' + slot, knowledgeOverview_x, knowledgeOverview_y, border_id)
                                        knowledgeOverview_x = knowledgeOverview_x + 120
                                        create_edgeItem(modelangeloXmlData, 3, 'aggregation', maxIdOfNodeItems, maxIdOfNodeItems-1-child_no, maxIdOfMutantObjects, maxIdOfMutantObjects-1-child_no, '', knowledgeOverview_x+40, knowledgeOverview_y+40)
                                        child_no = child_no + 1
                                        create_attributeItem(modelangeloXmlData, 'text', text, 'Text', maxIdOfMutantObjects)
                                        create_attributeItem(modelangeloXmlData, 'slot', slot, 'Text', maxIdOfMutantObjects)
            knowledgeOverview_y = knowledgeOverview_y + 60
            
    # import responses.dsl xml file
    knowledgeOverview_x  = 0
    knowledgeOverview_y = knowledgeOverview_y + 20
    print('importing responses...')
    for child_1 in chatBotXmlData_responses: # intents level
        if printing: print('', child_1.tag, child_1.attrib, child_1.text)
        # indicate individual users sections by knowledge_border node
        if(child_1.tag=='responses'):
            create_nodeItem(modelangeloXmlData, 3, 'knowledge_border', child_1.tag, knowledgeOverview_x-40, knowledgeOverview_y, 0)
            knowledgeOverview_y = knowledgeOverview_y + 40
            border_id = maxIdOfNodeItems
        for child_2 in child_1: # item level
            if printing: print('  ', child_2.tag, child_2.attrib, child_2.text)
            knowledgeOverview_x = 0
            
            for child_3 in child_2: # greet/goodbye level
                if printing: print('     ', child_3.tag, child_3.attrib, child_3.text)
                if(child_3.tag!=''):
                    create_nodeItem(modelangeloXmlData, 3, 'information_system', 'Chatbot', knowledgeOverview_x+160, knowledgeOverview_y, border_id)
                    create_nodeItem(modelangeloXmlData, 3, 'information_object', child_3.tag, knowledgeOverview_x, knowledgeOverview_y, border_id)
                    create_edgeItem(modelangeloXmlData, 3, 'membership', maxIdOfNodeItems, maxIdOfNodeItems-1, maxIdOfMutantObjects, maxIdOfMutantObjects-1, '', knowledgeOverview_x+80, knowledgeOverview_y)
                    knowledgeOverview_y = knowledgeOverview_y + 60
                    parent_id = maxIdOfNodeItems
                    child_no = 0
                for child_4 in child_3: # hey/hello/... level
                    if printing: print('         ', child_4.tag, child_4.attrib, child_4.text)
                    if('\n' in child_4.text) != True:
                        create_nodeItem(modelangeloXmlData, 3, 'information_object', child_4.text, knowledgeOverview_x, knowledgeOverview_y, border_id)
                        knowledgeOverview_x = knowledgeOverview_x + 120
                        create_edgeItem(modelangeloXmlData, 3, 'aggregation', maxIdOfNodeItems, maxIdOfNodeItems-1-child_no, maxIdOfMutantObjects, maxIdOfMutantObjects-1-child_no, '', knowledgeOverview_x+40, knowledgeOverview_y+40)
                        child_no = child_no + 1
                    else:
                        for child_5 in child_4: # slots level
                            if printing: print('             ', child_5.tag, child_5.attrib, child_5.text)
                            for child_6 in child_5: # item level
                                if printing: print('                 ', child_6.tag, child_6.attrib, child_6.text)
                                name = ''
                                value = ''  
                                for child_7 in child_6: # text/slot level
                                    if printing: print('                     ', child_7.tag, child_7.attrib, child_7.text)
                                    if(child_7.tag=='text'):
                                        text = child_7.text
                                    if(child_7.tag=='slot'):
                                        slot = child_7.text
                                        create_nodeItem(modelangeloXmlData, 3, 'information_object', text + ' $' + slot, knowledgeOverview_x, knowledgeOverview_y, border_id)
                                        knowledgeOverview_x = knowledgeOverview_x + 120
                                        create_edgeItem(modelangeloXmlData, 3, 'aggregation', maxIdOfNodeItems, maxIdOfNodeItems-1-child_no, maxIdOfMutantObjects, maxIdOfMutantObjects-1-child_no, '', knowledgeOverview_x+40, knowledgeOverview_y+40)
                                        child_no = child_no + 1
                                        create_attributeItem(modelangeloXmlData, 'text', text, 'Text', maxIdOfMutantObjects)
                                        create_attributeItem(modelangeloXmlData, 'slot', slot, 'Text', maxIdOfMutantObjects)
            knowledgeOverview_y = knowledgeOverview_y + 60

    # import invoices.dsl xml file
    knowledgeOverview_x  = 0
    knowledgeOverview_y = knowledgeOverview_y + 20
    print('importing invoices...')
    for child_1 in chatBotXmlData_invoices: # invoices level
        if printing: print('', child_1.tag, child_1.attrib, child_1.text)
        # indicate individual users sections by knowledge_border node
        if(child_1.tag=='invoices'):
            create_nodeItem(modelangeloXmlData, 3, 'knowledge_border', child_1.tag, knowledgeOverview_x-40, knowledgeOverview_y, 0)
            knowledgeOverview_y = knowledgeOverview_y + 40
            border_id = maxIdOfNodeItems
        for child_2 in child_1: # item level
            if printing: print('  ', child_2.tag, child_2.attrib, child_2.text)
            for child_3 in child_2: # invoiceId/customer/listPrice/billToCity/billToCountry/billToZipcode/totalAmount level
                if printing: print('     ', child_3.tag, child_3.attrib, child_3.text)
                if(child_3.tag=='invoiceId'):
                    create_nodeItem(modelangeloXmlData, 3, 'information_system', 'Billing System', knowledgeOverview_x+160, knowledgeOverview_y, border_id)
                    create_nodeItem(modelangeloXmlData, 3, 'information_object', child_3.text, knowledgeOverview_x, knowledgeOverview_y, border_id)
                    create_edgeItem(modelangeloXmlData, 3, 'membership', maxIdOfNodeItems, maxIdOfNodeItems-1, maxIdOfMutantObjects, maxIdOfMutantObjects-1, '', knowledgeOverview_x+80, knowledgeOverview_y)
                    knowledgeOverview_y = knowledgeOverview_y + 60
                    parent_id = maxIdOfNodeItems
                    child_no = 0
                    for child_3b in child_2: # invoiceId/customer/listPrice/billToCity/billToCountry/billToZipcode/totalAmount level
                        if printing: print('         ', child_3b.tag, child_3b.attrib, child_3b.text)
                        if(child_3b.tag!=''):
                            #create_nodeItem(modelangeloXmlData, 3, 'information_object', child_3b.text, knowledgeOverview_x, knowledgeOverview_y, border_id)
                            #knowledgeOverview_x = knowledgeOverview_x + 120
                            #create_edgeItem(modelangeloXmlData, 3, 'aggregation', maxIdOfNodeItems, maxIdOfNodeItems-1-child_no, maxIdOfMutantObjects, maxIdOfMutantObjects-1-child_no, '', knowledgeOverview_x+40, knowledgeOverview_y+40)
                            #child_no = child_no + 1
                            create_attributeItem(modelangeloXmlData, child_3b.tag, child_3b.text, 'Text', maxIdOfMutantObjects)

    # import orders.dsl xml file
    knowledgeOverview_x  = 0
    knowledgeOverview_y = knowledgeOverview_y + 20
    print('importing orders...')
    for child_1 in chatBotXmlData_orders: # orders level
        if printing: print('', child_1.tag, child_1.attrib, child_1.text)
        # indicate individual users sections by knowledge_border node
        if(child_1.tag=='orders'):
            create_nodeItem(modelangeloXmlData, 3, 'knowledge_border', child_1.tag, knowledgeOverview_x-40, knowledgeOverview_y, 0)
            knowledgeOverview_y = knowledgeOverview_y + 40
            border_id = maxIdOfNodeItems
        for child_2 in child_1: # item level
            if printing: print('  ', child_2.tag, child_2.attrib, child_2.text)
            for child_3 in child_2: # attribute level
                if printing: print('     ', child_3.tag, child_3.attrib, child_3.text)
                if(child_3.tag=='orderId'):
                    create_nodeItem(modelangeloXmlData, 3, 'information_system', 'Order System', knowledgeOverview_x+160, knowledgeOverview_y, border_id)
                    create_nodeItem(modelangeloXmlData, 3, 'information_object', child_3.text, knowledgeOverview_x, knowledgeOverview_y, border_id)
                    create_edgeItem(modelangeloXmlData, 3, 'membership', maxIdOfNodeItems, maxIdOfNodeItems-1, maxIdOfMutantObjects, maxIdOfMutantObjects-1, '', knowledgeOverview_x+80, knowledgeOverview_y)
                    knowledgeOverview_y = knowledgeOverview_y + 60
                    parent_id = maxIdOfNodeItems
                    child_no = 0
                    for child_3b in child_2: # attribute level
                        if printing: print('         ', child_3b.tag, child_3b.attrib, child_3b.text)
                        if(child_3b.tag!=''):
                            #create_nodeItem(modelangeloXmlData, 3, 'information_object', child_3b.text, knowledgeOverview_x, knowledgeOverview_y, border_id)
                            #knowledgeOverview_x = knowledgeOverview_x + 120
                            #create_edgeItem(modelangeloXmlData, 3, 'aggregation', maxIdOfNodeItems, maxIdOfNodeItems-1-child_no, maxIdOfMutantObjects, maxIdOfMutantObjects-1-child_no, '', knowledgeOverview_x+40, knowledgeOverview_y+40)
                            #child_no = child_no + 1
                            create_attributeItem(modelangeloXmlData, child_3b.tag, child_3b.text, 'Text', maxIdOfMutantObjects)

    # import pricelists.dsl xml file
    knowledgeOverview_x  = 0
    knowledgeOverview_y = knowledgeOverview_y + 20
    print('importing pricelists...')
    for child_1 in chatBotXmlData_pricelists: # pricelists level
        if printing: print('', child_1.tag, child_1.attrib, child_1.text)
        # indicate individual users sections by knowledge_border node
        if(child_1.tag=='pricelists'):
            create_nodeItem(modelangeloXmlData, 3, 'knowledge_border', child_1.tag, knowledgeOverview_x-40, knowledgeOverview_y, 0)
            knowledgeOverview_y = knowledgeOverview_y + 40
            border_id = maxIdOfNodeItems
        for child_2 in child_1: # item level
            if printing: print('  ', child_2.tag, child_2.attrib, child_2.text)
            for child_3 in child_2: # attribute level
                if printing: print('     ', child_3.tag, child_3.attrib, child_3.text)
                if(child_3.tag=='name'):
                    create_nodeItem(modelangeloXmlData, 3, 'information_system', 'Pricelist System', knowledgeOverview_x+160, knowledgeOverview_y, border_id)
                    create_nodeItem(modelangeloXmlData, 3, 'information_object', child_3.text, knowledgeOverview_x, knowledgeOverview_y, border_id)
                    create_edgeItem(modelangeloXmlData, 3, 'membership', maxIdOfNodeItems, maxIdOfNodeItems-1, maxIdOfMutantObjects, maxIdOfMutantObjects-1, '', knowledgeOverview_x+80, knowledgeOverview_y)
                    knowledgeOverview_y = knowledgeOverview_y + 60
                    parent_id = maxIdOfNodeItems
                    child_no = 0
                    for child_3b in child_2: # attribute level
                        if printing: print('         ', child_3b.tag, child_3b.attrib, child_3b.text)
                        if(child_3b.tag!=''):
                            #create_nodeItem(modelangeloXmlData, 3, 'information_object', child_3b.text, knowledgeOverview_x, knowledgeOverview_y, border_id)
                            #knowledgeOverview_x = knowledgeOverview_x + 120
                            #create_edgeItem(modelangeloXmlData, 3, 'aggregation', maxIdOfNodeItems, maxIdOfNodeItems-1-child_no, maxIdOfMutantObjects, maxIdOfMutantObjects-1-child_no, '', knowledgeOverview_x+40, knowledgeOverview_y+40)
                            #child_no = child_no + 1
                            create_attributeItem(modelangeloXmlData, child_3b.tag, child_3b.text, 'Text', maxIdOfMutantObjects)

    # import products.dsl xml file
    knowledgeOverview_x  = 0
    knowledgeOverview_y = knowledgeOverview_y + 20
    print('importing products...')
    for child_1 in chatBotXmlData_products: # pricelists level
        if printing: print('', child_1.tag, child_1.attrib, child_1.text)
        # indicate individual users sections by knowledge_border node
        if(child_1.tag=='products'):
            create_nodeItem(modelangeloXmlData, 3, 'knowledge_border', child_1.tag, knowledgeOverview_x-40, knowledgeOverview_y, 0)
            knowledgeOverview_y = knowledgeOverview_y + 40
            border_id = maxIdOfNodeItems
        for child_2 in child_1: # item level
            if printing: print('  ', child_2.tag, child_2.attrib, child_2.text)
            knowledgeOverview_x = 0
            for child_3 in child_2: # attribute level
                if printing: print('     ', child_3.tag, child_3.attrib, child_3.text)
                if(child_3.tag=='name'):
                    create_nodeItem(modelangeloXmlData, 3, 'information_system', 'PIM', knowledgeOverview_x+160, knowledgeOverview_y, border_id)
                    create_nodeItem(modelangeloXmlData, 3, 'information_object', child_3.text, knowledgeOverview_x, knowledgeOverview_y, border_id)
                    create_edgeItem(modelangeloXmlData, 3, 'membership', maxIdOfNodeItems, maxIdOfNodeItems-1, maxIdOfMutantObjects, maxIdOfMutantObjects-1, '', knowledgeOverview_x+80, knowledgeOverview_y)
                    knowledgeOverview_y = knowledgeOverview_y + 60
                    parent_id = maxIdOfNodeItems
                    child1_no = 0
                    for child_3b in child_2: # attribute level
                        if printing: print('         ', child_3b.tag, child_3b.attrib, child_3b.text)
                        if(child_3b.tag!='category') and (child_3b.tag!='attributes'):
                            #create_nodeItem(modelangeloXmlData, 3, 'information_object', child_3b.text, knowledgeOverview_x, knowledgeOverview_y, border_id)
                            #knowledgeOverview_x = knowledgeOverview_x + 120
                            #create_edgeItem(modelangeloXmlData, 3, 'aggregation', maxIdOfNodeItems, maxIdOfNodeItems-1-child1_no, maxIdOfMutantObjects, maxIdOfMutantObjects-1-child1_no, '', knowledgeOverview_x+40, knowledgeOverview_y+40)
                            #child_no = child_no + 1
                            create_attributeItem(modelangeloXmlData, child_3b.tag, child_3b.text, 'Text', maxIdOfMutantObjects)
                        else:
                            create_nodeItem(modelangeloXmlData, 3, 'information_object', child_3b.tag, knowledgeOverview_x, knowledgeOverview_y, border_id)
                            knowledgeOverview_x = knowledgeOverview_x + 120
                            create_edgeItem(modelangeloXmlData, 3, 'aggregation', maxIdOfNodeItems, maxIdOfNodeItems-1-child1_no, maxIdOfMutantObjects, maxIdOfMutantObjects-1-child1_no, '', knowledgeOverview_x+40, knowledgeOverview_y+40)
                            child1_no = child1_no + 1
                            child2_no = 0
                            for child_4 in child_3b: # category/attributes level
                                if printing: print('             ', child_4.tag, child_4.attrib, child_4.text)
                                #create_nodeItem(modelangeloXmlData, 3, 'information_object', child_4.text, knowledgeOverview_x, knowledgeOverview_y, border_id)
                                #knowledgeOverview_x = knowledgeOverview_x + 120
                                #create_edgeItem(modelangeloXmlData, 3, 'aggregation', maxIdOfNodeItems, maxIdOfNodeItems-1-child2_no, maxIdOfMutantObjects, maxIdOfMutantObjects-1-child2_no, '', knowledgeOverview_x+40, knowledgeOverview_y+40)
                                create_attributeItem(modelangeloXmlData, child_4.tag, child_4.text, 'Text', maxIdOfMutantObjects)
                                child2_no = child2_no + 1
            knowledgeOverview_y = knowledgeOverview_y + 60   

    # import activities.dsl xml file
    knowledgeOverview_x  = 0
    knowledgeOverview_y = knowledgeOverview_y + 20
    print('importing activities...')
    for child_1 in chatBotXmlData_activities: # activities level
        if printing: print('', child_1.tag, child_1.attrib, child_1.text)
        # indicate individual users sections by knowledge_border node
        if(child_1.tag=='activities'):
            create_nodeItem(modelangeloXmlData, 3, 'knowledge_border', child_1.tag, knowledgeOverview_x-40, knowledgeOverview_y, 0)
            knowledgeOverview_y = knowledgeOverview_y + 40
            border_id = maxIdOfNodeItems
        for child_2 in child_1: # item level
            if printing: print('  ', child_2.tag, child_2.attrib, child_2.text)
            for child_3 in child_2: # attribute level
                if printing: print('     ', child_3.tag, child_3.attrib, child_3.text)
                if(child_3.tag=='type'): # subject / type
                    create_nodeItem(modelangeloXmlData, 3, 'information_system', 'Status System', knowledgeOverview_x+160, knowledgeOverview_y, border_id)
                    create_nodeItem(modelangeloXmlData, 3, 'information_object', child_3.text, knowledgeOverview_x, knowledgeOverview_y, border_id)
                    create_edgeItem(modelangeloXmlData, 3, 'membership', maxIdOfNodeItems, maxIdOfNodeItems-1, maxIdOfMutantObjects, maxIdOfMutantObjects-1, '', knowledgeOverview_x+80, knowledgeOverview_y)
                    knowledgeOverview_y = knowledgeOverview_y + 60
                    parent_id = maxIdOfNodeItems
                    child_no = 0
                    for child_3b in child_2: # attribute level
                        if printing: print('         ', child_3b.tag, child_3b.attrib, child_3b.text)
                        if(child_3b.tag!=''):
                            #create_nodeItem(modelangeloXmlData, 3, 'information_object', child_3b.text, knowledgeOverview_x, knowledgeOverview_y, border_id)
                            #knowledgeOverview_x = knowledgeOverview_x + 120
                            #create_edgeItem(modelangeloXmlData, 3, 'aggregation', maxIdOfNodeItems, maxIdOfNodeItems-1-child_no, maxIdOfMutantObjects, maxIdOfMutantObjects-1-child_no, '', knowledgeOverview_x+40, knowledgeOverview_y+40)
                            #child_no = child_no + 1
                            create_attributeItem(modelangeloXmlData, child_3b.tag, child_3b.text, 'Text', maxIdOfMutantObjects)

    # import cases.dsl xml file
    knowledgeOverview_x  = 0
    knowledgeOverview_y = knowledgeOverview_y + 20
    print('importing cases...')
    for child_1 in chatBotXmlData_cases: # activities level
        if printing: print('', child_1.tag, child_1.attrib, child_1.text)
        # indicate individual users sections by knowledge_border node
        if(child_1.tag=='cases'):
            create_nodeItem(modelangeloXmlData, 3, 'knowledge_border', child_1.tag, knowledgeOverview_x-40, knowledgeOverview_y, 0)
            knowledgeOverview_y = knowledgeOverview_y + 40
            border_id = maxIdOfNodeItems
        for child_2 in child_1: # item level
            if printing: print('  ', child_2.tag, child_2.attrib, child_2.text)
            for child_3 in child_2: # attribute level
                if printing: print('     ', child_3.tag, child_3.attrib, child_3.text)
                if(child_3.tag=='title'): # title or caseId
                    create_nodeItem(modelangeloXmlData, 3, 'information_system', 'Ticket System', knowledgeOverview_x+160, knowledgeOverview_y, border_id)
                    create_nodeItem(modelangeloXmlData, 3, 'information_object', child_3.text, knowledgeOverview_x, knowledgeOverview_y, border_id)
                    create_edgeItem(modelangeloXmlData, 3, 'membership', maxIdOfNodeItems, maxIdOfNodeItems-1, maxIdOfMutantObjects, maxIdOfMutantObjects-1, '', knowledgeOverview_x+80, knowledgeOverview_y)
                    knowledgeOverview_y = knowledgeOverview_y + 60
                    parent_id = maxIdOfNodeItems
                    child_no = 0
                    for child_3b in child_2: # attribute level
                        if printing: print('         ', child_3b.tag, child_3b.attrib, child_3b.text)
                        if(child_3b.tag!=''):
                            #create_nodeItem(modelangeloXmlData, 3, 'information_object', child_3b.text, knowledgeOverview_x, knowledgeOverview_y, border_id)
                            #knowledgeOverview_x = knowledgeOverview_x + 120
                            #create_edgeItem(modelangeloXmlData, 3, 'aggregation', maxIdOfNodeItems, maxIdOfNodeItems-1-child_no, maxIdOfMutantObjects, maxIdOfMutantObjects-1-child_no, '', knowledgeOverview_x+40, knowledgeOverview_y+40)
                            #child_no = child_no + 1
                            create_attributeItem(modelangeloXmlData, child_3b.tag, child_3b.text, 'Text', maxIdOfMutantObjects)

    # import slots.dsl xml file
    knowledgeOverview_x  = 0
    knowledgeOverview_y = knowledgeOverview_y + 20        
    print('importing slots...')
    for child_1 in chatBotXmlData_slots: # slots level
        if printing: print('', child_1.tag, child_1.attrib, child_1.text)
        # indicate individual alias sections by knowledge_border node
        if(child_1.tag=='slots'):
            create_nodeItem(modelangeloXmlData, 3, 'knowledge_border', child_1.tag, knowledgeOverview_x-40, knowledgeOverview_y, 0)
            knowledgeOverview_y = knowledgeOverview_y + 40
            border_id = maxIdOfNodeItems
            create_nodeItem(modelangeloXmlData, 3, 'information_system', 'Chatbot', knowledgeOverview_x+160, knowledgeOverview_y, border_id)
            create_nodeItem(modelangeloXmlData, 3, 'information_object', 'Working Memory', knowledgeOverview_x, knowledgeOverview_y, border_id)
            create_edgeItem(modelangeloXmlData, 3, 'membership', maxIdOfNodeItems, maxIdOfNodeItems-1, maxIdOfMutantObjects, maxIdOfMutantObjects-1, '', knowledgeOverview_x+80, knowledgeOverview_y)
            knowledgeOverview_y = knowledgeOverview_y + 80
            parent_id = maxIdOfNodeItems
            child_no = 0
        for child_2 in child_1: # item level
            if printing: print('  ', child_2.tag, child_2.attrib, child_2.text)
            for child_3 in child_2: # product_request/first_name/size/... level
                if printing: print('     ', child_3.tag, child_3.attrib, child_3.text)
                if(child_3.tag!=''):
                    create_nodeItem(modelangeloXmlData, 3, 'information_object', child_3.tag, knowledgeOverview_x, knowledgeOverview_y, border_id)
                    knowledgeOverview_x = knowledgeOverview_x + 120
                    create_edgeItem(modelangeloXmlData, 3, 'aggregation', maxIdOfNodeItems, maxIdOfNodeItems-1-child_no, maxIdOfMutantObjects, maxIdOfMutantObjects-1-child_no, '', knowledgeOverview_x+40, knowledgeOverview_y+40)
                    child_no = child_no + 1
                    if(child_3.text!=''):
                        #create_nodeItem(modelangeloXmlData, 3, 'information_object', child_3b.text, knowledgeOverview_x, knowledgeOverview_y, border_id)
                        #knowledgeOverview_x = knowledgeOverview_x + 120
                        #create_edgeItem(modelangeloXmlData, 3, 'aggregation', maxIdOfNodeItems, maxIdOfNodeItems-1-child_no, maxIdOfMutantObjects, maxIdOfMutantObjects-1-child_no, '', knowledgeOverview_x+40, knowledgeOverview_y+40)
                        #child_no = child_no + 1
                        create_attributeItem(modelangeloXmlData, 'slot', child_3.text, 'Text', maxIdOfMutantObjects)

    # import actions from
    # actions.dsl xml file  = activities
    # and responses.dsl xml file   = transfers = activity task association
    activityView_x  = 0
    activityView_y = activityView_y + 20
    print('importing actions and responses...')
    for child_1 in chatBotXmlData_dialog_activity_integrations: # integrations level
        if printing: print('', child_1.tag, child_1.attrib, child_1.text)
        for child_2 in child_1: # item level
            if printing: print('  ', child_2.tag, child_2.attrib, child_2.text)
            activityView_x = 0
            for child_3 in child_2: # greet/utter_greet/... level
                if printing: print('     ', child_3.tag, child_3.attrib, child_3.text)
                # indicate individual task activity associations by activity_border node
                create_nodeItem(modelangeloXmlData, 2, 'activity_border', child_3.tag, activityView_x-40, activityView_y, 0)         
                activityView_y = activityView_y + 40
                border_id = maxIdOfNodeItems
                for child_4 in child_3: # item. level
                    if printing: print('         ', child_4.tag, child_4.attrib, child_4.text)
                    current_activityName = child_4.text
                    for child_a in chatBotXmlData_actions: # actions level
                        if printing: print('         ->', child_a.tag, child_a.attrib, child_a.text)
                        for child_b in child_a: # item level
                            if printing: print('         ->    ', child_b.tag, child_b.attrib, child_b.text)
                            if(current_activityName in child_b.text):
                                print('', current_activityName, child_b.text)
                                InputObject_y = 0
                                OutputObject_y = 0
                                InputObjects_No = 0
                                OutputObjects_No = 0
                                maxObject_y = 0
                                activityView_x = activityView_x + 240
                                create_nodeItem(modelangeloXmlData, 2, 'conversion', current_activityName, activityView_x, activityView_y, border_id)
                                for child_c in child_b: # input/output level
                                    if printing: print('         ->        ', child_c.tag, child_c.attrib, child_c.text)
                                    
                                    # check for tacit or explicit knowledge
                                    objectType = 'knowledge_object'
                                    objectName = 'Customer'
                                    slot_value = ''
                                    informationObjectTypeBoolean = False
                                    # identify relevant label of knowledge or information object
                                    for childM_1 in modelangeloXmlData:
                                        if printing: print('         ->        -->', childM_1.tag, childM_1.attrib, childM_1.text)
                                        if('label_item' == childM_1.tag):
                                            if(childM_1.attrib['text'] == child_c.text):
                                                currentNode = childM_1.attrib['node'] 
                                                # identify corresponding knowledge or information object
                                                for childM_2 in modelangeloXmlData:
                                                    if printing: print('         ->        -->    ', childM_2.tag, childM_2.attrib, childM_2.text)
                                                    if('node_item' == childM_2.tag) and (childM_2.attrib['id'] == currentNode):
                                                        if(('knowledge_object' in childM_2.attrib['shape']) == False):
                                                            informationObjectTypeBoolean = True    
                                        elif('meta_attribute' == childM_1.tag):
                                            if((child_c.text in childM_1.attrib['name']) == True):
                                                informationObjectTypeBoolean = True
                                    if(informationObjectTypeBoolean):        
                                        objectType = 'information_object'
                                        objectName = 'xy System'
                                        if(child_c.text in ET.tostring(chatBotXmlData_products).decode()):
                                            objectName = 'PIM'
                                        elif(child_c.text in ET.tostring(chatBotXmlData_intents).decode()):
                                            objectName = 'Chatbot'
                                        #elif(child_c.text in ET.tostring(chatBotXmlData_actions).decode()):
                                        #    objectName = 'Chatbot'   
                                        elif(child_c.text in ET.tostring(chatBotXmlData_activities).decode()):
                                            objectName = 'Chatbot'
                                        elif(child_c.text in ET.tostring(chatBotXmlData_aliases).decode()):
                                            objectName = 'CRM'
                                        elif(child_c.text in ET.tostring(chatBotXmlData_cases).decode()):
                                            objectName = 'Chatbot'
                                        elif(child_c.text in ET.tostring(chatBotXmlData_contacts).decode()):
                                            objectName = 'CRM'
                                        elif(child_c.text in ET.tostring(chatBotXmlData_users).decode()):
                                            objectName = 'HRM'
                                        elif(child_c.text in ET.tostring(chatBotXmlData_invoices).decode()):
                                            objectName = 'Billing System'
                                        elif(child_c.text in ET.tostring(chatBotXmlData_orders).decode()):
                                            objectName = 'Order System'
                                        elif(child_c.text in ET.tostring(chatBotXmlData_pricelists).decode()):
                                            objectName = 'Pricelist System'
                                        #elif(child_c.text in ET.tostring(chatBotXmlData_dialog_activity_integrations).decode()):
                                        #    objectName = 'Chatbot'
                                        #elif(child_c.text in ET.tostring(chatBotXmlData_dialog_activity_responses).decode()):
                                        #    objectName = 'Chatbot'
                                        elif(child_c.text in ET.tostring(chatBotXmlData_slots).decode()):
                                            objectName = 'Chatbot'

                                    # identify slot value for information objects
                                    for child_s1 in chatBotXmlData_slots: # slots level
                                        if printing: print('', child_s1.tag, child_s1.attrib, child_s1.text)
                                        for child_s2 in child_s1: # item level
                                            if printing: print('  ', child_s2.tag, child_s2.attrib, child_s2.text)
                                            for child_s3 in child_s2: # product_request/first_name/size/... level
                                                if printing: print('     ', child_s3.tag, child_s3.attrib, child_s3.text)
                                                if(child_s3.tag==child_c.text):
                                                    slot_value = child_s3.text

                                    # position input objects    
                                    if('input'==child_c.tag):
                                        if(informationObjectTypeBoolean):
                                            create_nodeItem(modelangeloXmlData, 2, 'information_system', objectName, activityView_x-240, activityView_y+InputObject_y, border_id)
                                        else:
                                            create_nodeItem(modelangeloXmlData, 2, 'person', objectName, activityView_x-240, activityView_y+InputObject_y, border_id)
                                        create_nodeItem(modelangeloXmlData, 2, objectType, child_c.text, activityView_x-130, activityView_y+InputObject_y, border_id)
                                        create_edgeItem(modelangeloXmlData, 2, 'undefined_conversion', maxIdOfNodeItems, maxIdOfNodeItems-InputObjects_No*2-2, maxIdOfMutantObjects, maxIdOfMutantObjects-InputObjects_No*2-2, '', activityView_x+80, activityView_y+40)
                                        create_edgeItem(modelangeloXmlData, 2, 'membership', maxIdOfNodeItems, maxIdOfNodeItems-1, maxIdOfMutantObjects, maxIdOfMutantObjects-1, '', activityView_x+80, activityView_y+40)
                                        if(informationObjectTypeBoolean):
                                            create_attributeItem(modelangeloXmlData, 'slot', slot_value, 'Text', maxIdOfMutantObjects)
                                        InputObjects_No = InputObjects_No + 1
                                        InputObject_y = InputObject_y + 40
                                    
                                    # position output objects
                                    if('output'==child_c.tag):
                                        if(informationObjectTypeBoolean):
                                            create_nodeItem(modelangeloXmlData, 2, 'information_system', objectName, activityView_x+240, activityView_y+OutputObject_y, border_id)
                                        else:
                                            create_nodeItem(modelangeloXmlData, 2, 'person', objectName, activityView_x+240, activityView_y+OutputObject_y, border_id)
                                        create_nodeItem(modelangeloXmlData, 2, objectType, child_c.text, activityView_x+110, activityView_y+OutputObject_y, border_id)
                                        create_edgeItem(modelangeloXmlData, 2, 'undefined_conversion', maxIdOfNodeItems-InputObjects_No*2-OutputObjects_No*2-2, maxIdOfNodeItems, maxIdOfMutantObjects-InputObjects_No*2-OutputObjects_No*2-2, maxIdOfMutantObjects, '', activityView_x+80, activityView_y+40)
                                        create_edgeItem(modelangeloXmlData, 2, 'membership', maxIdOfNodeItems, maxIdOfNodeItems-1, maxIdOfMutantObjects, maxIdOfMutantObjects-1, '', activityView_x+80, activityView_y+40)
                                        if(informationObjectTypeBoolean):
                                            create_attributeItem(modelangeloXmlData, 'slot', slot_value, 'Text', maxIdOfMutantObjects)
                                        OutputObjects_No = OutputObjects_No + 1
                                        OutputObject_y = OutputObject_y + 40
                                maxObject_y = max([InputObject_y, OutputObject_y])
                activityView_y = activityView_y + maxObject_y + 40

    # import missing actions from 
    # actions.dsl xml file  = activities
    # and responses.dsl xml file   = transfers = activity task association
    activityView_x  = 0
    activityView_y = activityView_y + 20
    print('importing missing activities from actions and responses...')
    for child_1 in chatBotXmlData_actions: # action level
        if printing: print('', child_1.tag, child_1.attrib, child_1.text)
        activityView_x = 0
        # indicate individual task activity associations by activity_border node
        create_nodeItem(modelangeloXmlData, 2, 'activity_border', 'Activities having no task, yet', activityView_x-40, activityView_y, 0)         
        activityView_y = activityView_y + 40
        border_id = maxIdOfNodeItems
        for child_2 in child_1: # item level with activities
            if printing: print('  ', child_2.tag, child_2.attrib, child_2.text)
            activityHasTask = False
            current_activityName = child_2.text
            for child_a in chatBotXmlData_dialog_activity_integrations: # integrations level
                if printing: print('         ->', child_a.tag, child_a.attrib, child_a.text)
                for child_b in child_a: # item level
                    if printing: print('         ->    ', child_b.tag, child_b.attrib, child_b.text)
                    for child_c in child_b: # greet/utter_greet/... level
                        if printing: print('         ->    ', child_c.tag, child_c.attrib, child_c.text)
                        for child_d in child_c: # item level
                            if printing: print('         ->    ', child_d.tag, child_d.attrib, child_d.text)
                            if(child_d.text in current_activityName):
                                activityHasTask = True
            if(activityHasTask==False):
                create_nodeItem(modelangeloXmlData, 2, 'conversion', current_activityName, activityView_x, activityView_y+InputObject_y, border_id)
                activityView_x = activityView_x + 120
        activityView_y = activityView_y + maxObject_y + 40       

    return modelangeloXmlData

def modification_modelangelo_exportDslFiles(modelangeloXmlData):
    """
    This function creates all kinds of dsl data from modelangeloXmlData data. These are called 'chatBotXmlData_x' and are returned.
    """ 

    printing = False

    # users.xml
    print('exporting users...')
    chatBotXmlData_users = Element('root')
    first_hierarchy = SubElement(chatBotXmlData_users, 'users')
    for child_1 in modelangeloXmlData:
        if((child_1.tag == 'label_item') and (child_1.attrib['text'] == 'users')):
            label_nodeId = child_1.attrib['node']
            for child_2 in modelangeloXmlData:
                if((child_2.tag == 'node_item') and (child_2.attrib['parent'] == str(label_nodeId)) and ('information_object' in child_2.attrib['shape'])):
                    second_hierarchy = SubElement(first_hierarchy, 'item')    
                    nodeItem_Id = child_2.attrib['id']
                    nodeItem_MutantObject = child_2.attrib['mutant_object']
                    print('nodeItem_Id=', nodeItem_Id)
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'identifier'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'name'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'businessUnit'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'title'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'phone'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
    
    # users.xml
    print('exporting contacts...')
    chatBotXmlData_contacts = Element('root')
    first_hierarchy = SubElement(chatBotXmlData_contacts, 'contacts')
    for child_1 in modelangeloXmlData:
        if((child_1.tag == 'label_item') and (child_1.attrib['text'] == 'contacts')):
            label_nodeId = child_1.attrib['node']
            for child_2 in modelangeloXmlData:
                if((child_2.tag == 'node_item') and (child_2.attrib['parent'] == str(label_nodeId)) and ('information_object' in child_2.attrib['shape'])):
                    second_hierarchy = SubElement(first_hierarchy, 'item')    
                    nodeItem_Id = child_2.attrib['id']
                    nodeItem_MutantObject = child_2.attrib['mutant_object']
                    print('nodeItem_Id=', nodeItem_Id)
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'fullName'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'gender'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'jobTitle'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'city'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'country'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'postalCode'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'currentOffer'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
    
    # invoices.xml
    print('exporting invoices...')
    chatBotXmlData_invoices = Element('root')
    first_hierarchy = SubElement(chatBotXmlData_invoices, 'invoices')
    for child_1 in modelangeloXmlData:
        if((child_1.tag == 'label_item') and (child_1.attrib['text'] == 'invoices')):
            label_nodeId = child_1.attrib['node']
            for child_2 in modelangeloXmlData:
                if((child_2.tag == 'node_item') and (child_2.attrib['parent'] == str(label_nodeId)) and ('information_object' in child_2.attrib['shape'])):
                    second_hierarchy = SubElement(first_hierarchy, 'item')    
                    nodeItem_Id = child_2.attrib['id']
                    nodeItem_MutantObject = child_2.attrib['mutant_object']
                    print('nodeItem_Id=', nodeItem_Id)
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'invoiceId'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'customer'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'listPrice'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'billToCity'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'billToCountry'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'billToZipcode'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'totalAmount'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
    
    # orders.xml
    print('exporting orders...')
    chatBotXmlData_orders = Element('root')
    first_hierarchy = SubElement(chatBotXmlData_orders, 'orders')
    for child_1 in modelangeloXmlData:
        if((child_1.tag == 'label_item') and (child_1.attrib['text'] == 'orders')):
            label_nodeId = child_1.attrib['node']
            for child_2 in modelangeloXmlData:
                if((child_2.tag == 'node_item') and (child_2.attrib['parent'] == str(label_nodeId)) and ('information_object' in child_2.attrib['shape'])):
                    second_hierarchy = SubElement(first_hierarchy, 'item')    
                    nodeItem_Id = child_2.attrib['id']
                    nodeItem_MutantObject = child_2.attrib['mutant_object']
                    print('nodeItem_Id=', nodeItem_Id)
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'orderId'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'customer'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'orderDate'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'deliveryDate'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'orderStatus'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'billToCity'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'billToCountry'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'billToZipcode'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'orderDiscount'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'shipmentMethod'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'totalAmount'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']                
    
    # pricelists.xml
    print('exporting pricelists...')
    chatBotXmlData_pricelists = Element('root')
    first_hierarchy = SubElement(chatBotXmlData_pricelists, 'pricelists')
    for child_1 in modelangeloXmlData:
        if((child_1.tag == 'label_item') and (child_1.attrib['text'] == 'pricelists')):
            label_nodeId = child_1.attrib['node']
            for child_2 in modelangeloXmlData:
                if((child_2.tag == 'node_item') and (child_2.attrib['parent'] == str(label_nodeId)) and ('information_object' in child_2.attrib['shape'])):
                    second_hierarchy = SubElement(first_hierarchy, 'item')    
                    nodeItem_Id = child_2.attrib['id']
                    nodeItem_MutantObject = child_2.attrib['mutant_object']
                    print('nodeItem_Id=', nodeItem_Id)
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'name'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'startDate'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'endDate'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'description'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                                    
    # activities.xml
    print('exporting activities...')
    chatBotXmlData_activities = Element('root')
    first_hierarchy = SubElement(chatBotXmlData_activities, 'activities')
    for child_1 in modelangeloXmlData:
        if((child_1.tag == 'label_item') and (child_1.attrib['text'] == 'activities')):
            label_nodeId = child_1.attrib['node']
            for child_2 in modelangeloXmlData:
                if((child_2.tag == 'node_item') and (child_2.attrib['parent'] == str(label_nodeId)) and ('information_object' in child_2.attrib['shape'])):
                    second_hierarchy = SubElement(first_hierarchy, 'item')    
                    nodeItem_Id = child_2.attrib['id']
                    nodeItem_MutantObject = child_2.attrib['mutant_object']
                    print('nodeItem_Id=', nodeItem_Id)
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'subject'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'type'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'status'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'priority'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'dateCreated'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                                    
    # cases.xml
    print('exporting cases...')
    chatBotXmlData_cases = Element('root')
    first_hierarchy = SubElement(chatBotXmlData_cases, 'cases')
    for child_1 in modelangeloXmlData:
        if((child_1.tag == 'label_item') and (child_1.attrib['text'] == 'cases')):
            label_nodeId = child_1.attrib['node']
            for child_2 in modelangeloXmlData:
                if((child_2.tag == 'node_item') and (child_2.attrib['parent'] == str(label_nodeId)) and ('information_object' in child_2.attrib['shape'])):
                    second_hierarchy = SubElement(first_hierarchy, 'item')    
                    nodeItem_Id = child_2.attrib['id']
                    nodeItem_MutantObject = child_2.attrib['mutant_object']
                    print('nodeItem_Id=', nodeItem_Id)
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'title'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'caseId'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'priority'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'status'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
                    # identify value of parameter called attributeName
                    for child_3 in modelangeloXmlData:
                        attributeName = 'satisfaction'
                        if((child_3.tag == 'meta_attribute') and (child_3.attrib['name'] == attributeName)):
                            metaAttribute_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                    third_hierarchy = SubElement(second_hierarchy, attributeName)
                                    third_hierarchy.text = child_4.attrib['value']
    
    # slots.xml
    print('exporting slots...')
    chatBotXmlData_slots = Element('root')
    first_hierarchy = SubElement(chatBotXmlData_slots, 'slots')
    for child_1 in modelangeloXmlData:
        if((child_1.tag == 'label_item') and (child_1.attrib['text'] == 'slots')):
            label_nodeId = child_1.attrib['node']
            for child_2 in modelangeloXmlData:
                if((child_2.tag == 'node_item') and (child_2.attrib['parent'] == str(label_nodeId)) and ('information_object' in child_2.attrib['shape'])):  
                    nodeItem_Id = child_2.attrib['id']
                    nodeItem_MutantObject = child_2.attrib['mutant_object']
                    print('nodeItem_Id=', nodeItem_Id)
                    for child_3 in modelangeloXmlData:
                        if((child_3.tag == 'label_item') and (child_3.attrib['node'] == str(nodeItem_Id)) and (child_3.attrib['text'] != 'Working Memory')):                     
                            second_hierarchy = SubElement(first_hierarchy, 'item')
                            # identify value of parameter called attributeName
                            for child_4 in modelangeloXmlData:
                                attributeName = 'slot'
                                if((child_4.tag == 'meta_attribute') and (child_4.attrib['name'] == attributeName)):
                                    metaAttribute_Id = child_4.attrib['id']
                                    for child_4 in modelangeloXmlData:
                                        if((child_4.tag == 'attribute') and (child_4.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_4.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                            third_hierarchy = SubElement(second_hierarchy, child_3.attrib['text'])
                                            third_hierarchy.text = child_4.attrib['value']
                                            
    # products.xml
    print('exporting products...')
    chatBotXmlData_products = Element('root')
    first_hierarchy = SubElement(chatBotXmlData_products, 'products')
    for child_1 in modelangeloXmlData:
        if((child_1.tag == 'label_item') and (child_1.attrib['text'] == 'products')):
            label_nodeId = child_1.attrib['node']
            for child_2 in modelangeloXmlData:
                if((child_2.tag == 'node_item') and (child_2.attrib['parent'] == str(label_nodeId)) and ('information_object' in child_2.attrib['shape'])):  
                    nodeItem_Id = child_2.attrib['id']
                    nodeItem_MutantObject = child_2.attrib['mutant_object']
                    print('nodeItem_Id=', nodeItem_Id)
                    for child_3 in modelangeloXmlData:
                        if((child_3.tag == 'label_item') and (child_3.attrib['node'] == str(nodeItem_Id))):                     
                            if((child_3.attrib['text'] != 'category') and (child_3.attrib['text'] != 'attributes')):
                                second_hierarchy = SubElement(first_hierarchy, 'item')
                                # identify value of parameter called attributeName
                                for child_4 in modelangeloXmlData:
                                    attributeName = 'identifier'
                                    if((child_4.tag == 'meta_attribute') and (child_4.attrib['name'] == attributeName)):
                                        metaAttribute_Id = child_4.attrib['id']
                                        for child_5 in modelangeloXmlData:
                                            if((child_5.tag == 'attribute') and (child_5.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_5.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                                third_hierarchy = SubElement(second_hierarchy, attributeName)
                                                third_hierarchy.text = child_5.attrib['value']
                                # identify value of parameter called attributeName
                                for child_4 in modelangeloXmlData:
                                    attributeName = 'name'
                                    if((child_4.tag == 'meta_attribute') and (child_4.attrib['name'] == attributeName)):
                                        metaAttribute_Id = child_4.attrib['id']
                                        for child_5 in modelangeloXmlData:
                                            if((child_5.tag == 'attribute') and (child_5.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_5.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                                third_hierarchy = SubElement(second_hierarchy, attributeName)
                                                third_hierarchy.text = child_5.attrib['value']
                                # identify value of parameter called attributeName
                                for child_4 in modelangeloXmlData:
                                    attributeName = 'family'
                                    if((child_4.tag == 'meta_attribute') and (child_4.attrib['name'] == attributeName)):
                                        metaAttribute_Id = child_4.attrib['id']
                                        for child_5 in modelangeloXmlData:
                                            if((child_5.tag == 'attribute') and (child_5.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_5.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                                third_hierarchy = SubElement(second_hierarchy, attributeName)
                                                third_hierarchy.text = child_5.attrib['value']
                            
                            else:
                                third_hierarchy = SubElement(second_hierarchy, child_3.attrib['text'])
                                
                                
                                # identify value of parameter called attributeName
                                for child_4 in modelangeloXmlData:
                                    attributeName = 'weight'
                                    if(child_4.tag == 'meta_attribute'):
                                        metaAttribute_Id = child_4.attrib['id']
                                        for child_5 in modelangeloXmlData:
                                            if((child_5.tag == 'attribute') and (child_5.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_5.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                                fourth_hierarchy = SubElement(third_hierarchy, child_4.attrib['name'])
                                                fourth_hierarchy.text = child_5.attrib['value']
    
    # aliases.xml
    print('exporting aliases...')
    chatBotXmlData_aliases = Element('root')
    first_hierarchy = SubElement(chatBotXmlData_aliases, 'aliases')
    for child_1 in modelangeloXmlData:
        if((child_1.tag == 'label_item') and (child_1.attrib['text'] == 'aliases')):
            label_nodeId = child_1.attrib['node']
            for child_2 in modelangeloXmlData:
                if((child_2.tag == 'node_item') and (child_2.attrib['parent'] == str(label_nodeId)) and ('information_object' in child_2.attrib['shape'])):  
                    nodeItem_Id = child_2.attrib['id'] # all information objects of intents
                    if printing: print('nodeItem_Id=', nodeItem_Id)
                    nodeItem_isParent = False
                    for child_3 in modelangeloXmlData:
                        if((child_3.tag == 'edge_item') and (child_3.attrib['target'] == str(nodeItem_Id))):
                            nodeItem_isParent = True
                            nodeItem_parentId = child_2.attrib['id']
                    if(nodeItem_isParent):
                        if printing: print('nodeItem_parentId=', nodeItem_parentId)
                        second_hierarchy = SubElement(first_hierarchy, 'item')
                        for child_3 in modelangeloXmlData:
                            if((child_3.tag == 'label_item') and (child_3.attrib['node'] == str(nodeItem_Id))):                     
                                third_hierarchy = SubElement(second_hierarchy, child_3.attrib['text'])
                        for child_3 in modelangeloXmlData:
                            if((child_3.tag == 'edge_item') and (child_3.attrib['target'] == str(nodeItem_parentId))):
                                nodeItem_childId = child_3.attrib['source']
                                if printing: print('  nodeItem_childId=', nodeItem_childId)
                                for child_4 in modelangeloXmlData:
                                    if((child_4.tag == 'label_item') and (child_4.attrib['node'] == str(nodeItem_childId))):
                                        fourth_hierarchy = SubElement(third_hierarchy, 'item')
                                        fourth_hierarchy.text = child_4.attrib['text']
    
    # intents.xml
    print('exporting intents...')                        
    chatBotXmlData_intents = Element('root')
    first_hierarchy = SubElement(chatBotXmlData_intents, 'intents')
    for child_1 in modelangeloXmlData:
        if((child_1.tag == 'label_item') and (child_1.attrib['text'] == 'intents')):
            label_nodeId = child_1.attrib['node']
            for child_2 in modelangeloXmlData:
                if((child_2.tag == 'node_item') and (child_2.attrib['parent'] == str(label_nodeId)) and ('information_object' in child_2.attrib['shape'])):  
                    nodeItem_Id = child_2.attrib['id'] # all information objects of intents
                    print('nodeItem_Id=', nodeItem_Id)
                    nodeItem_isParent = False
                    for child_3 in modelangeloXmlData:
                        if((child_3.tag == 'edge_item') and (child_3.attrib['target'] == str(nodeItem_Id))):
                            nodeItem_isParent = True
                            nodeItem_parentId = child_2.attrib['id']
                    if(nodeItem_isParent):
                        if printing: print('nodeItem_parentId=', nodeItem_parentId)
                        second_hierarchy = SubElement(first_hierarchy, 'item')
                        for child_3 in modelangeloXmlData:
                            if((child_3.tag == 'label_item') and (child_3.attrib['node'] == str(nodeItem_Id))):                     
                                third_hierarchy = SubElement(second_hierarchy, child_3.attrib['text'])
                        for child_3 in modelangeloXmlData:
                            if((child_3.tag == 'edge_item') and (child_3.attrib['target'] == str(nodeItem_parentId))):
                                nodeItem_childId = child_3.attrib['source']
                                if printing: print('  nodeItem_childId=', nodeItem_childId)
                                for child_4 in modelangeloXmlData:
                                    if((child_4.tag == 'label_item') and (child_4.attrib['node'] == str(nodeItem_childId))):                     
                                        # identify relevant mutant id for attribute identification
                                        for child_5 in modelangeloXmlData:
                                            if((child_5.tag == 'node_item') and (child_5.attrib['id'] == str(nodeItem_childId))):  
                                                nodeItem_MutantObject = child_5.attrib['mutant_object']
                                        nodeItem_hasAttributes = False
                                        # identify value of parameter called attributeName
                                        for child_6 in modelangeloXmlData:
                                            attributeName = 'text'
                                            if((child_6.tag == 'meta_attribute') and (child_6.attrib['name'] == attributeName)):
                                                metaAttribute_Id = child_6.attrib['id']
                                                for child_7 in modelangeloXmlData:
                                                    if((child_7.tag == 'attribute') and (child_7.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_7.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                                        nodeItem_hasAttributes = True
                                                        fourth_hierarchy = SubElement(third_hierarchy, 'item')
                                                        fifth_hierarchy = SubElement(fourth_hierarchy, 'slots')
                                                        sixth_hierarchy = SubElement(fifth_hierarchy, 'item')
                                                        
                                                        seventh_hierarchy = SubElement(sixth_hierarchy, attributeName)
                                                        seventh_hierarchy.text = child_7.attrib['value']
                                                        if printing: print(child_7.attrib['value'])
                                        # identify value of parameter called attributeName 
                                        # a) handle this search in equal footing of previous search, because attributes may be independent. (x)
                                        # b) alternatively, nest this search at the if statement of previous search, so that this is realized only together with the previous attribute.
                                        for child_6 in modelangeloXmlData:
                                            attributeName = 'slot'
                                            if((child_6.tag == 'meta_attribute') and (child_6.attrib['name'] == attributeName)):
                                                metaAttribute_Id = child_6.attrib['id']
                                                for child_7 in modelangeloXmlData:
                                                    if((child_7.tag == 'attribute') and (child_7.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_7.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                                        seventh_hierarchy = SubElement(sixth_hierarchy, attributeName)
                                                        seventh_hierarchy.text = child_7.attrib['value']
                                                        if printing: print(child_7.attrib['value'])
                                        if(nodeItem_hasAttributes==False):
                                            fourth_hierarchy = SubElement(third_hierarchy, 'item')
                                            fourth_hierarchy.text = child_4.attrib['text']
    
    # responses.xml
    print('exporting responses...')                        
    chatBotXmlData_responses = Element('root')
    first_hierarchy = SubElement(chatBotXmlData_responses, 'responses')
    for child_1 in modelangeloXmlData:
        if((child_1.tag == 'label_item') and (child_1.attrib['text'] == 'responses')):
            label_nodeId = child_1.attrib['node']
            for child_2 in modelangeloXmlData:
                if((child_2.tag == 'node_item') and (child_2.attrib['parent'] == str(label_nodeId)) and ('information_object' in child_2.attrib['shape'])):  
                    nodeItem_Id = child_2.attrib['id'] # all information objects of intents
                    print('nodeItem_Id=', nodeItem_Id)
                    nodeItem_isParent = False
                    for child_3 in modelangeloXmlData:
                        if((child_3.tag == 'edge_item') and (child_3.attrib['target'] == str(nodeItem_Id))):
                            nodeItem_isParent = True
                            nodeItem_parentId = child_2.attrib['id']
                    if(nodeItem_isParent):
                        if printing: print('nodeItem_parentId=', nodeItem_parentId)
                        second_hierarchy = SubElement(first_hierarchy, 'item')
                        for child_3 in modelangeloXmlData:
                            if((child_3.tag == 'label_item') and (child_3.attrib['node'] == str(nodeItem_Id))):                     
                                third_hierarchy = SubElement(second_hierarchy, child_3.attrib['text'])
                        for child_3 in modelangeloXmlData:
                            if((child_3.tag == 'edge_item') and (child_3.attrib['target'] == str(nodeItem_parentId))):
                                nodeItem_childId = child_3.attrib['source']
                                if printing: print('  nodeItem_childId=', nodeItem_childId)
                                for child_4 in modelangeloXmlData:
                                    if((child_4.tag == 'label_item') and (child_4.attrib['node'] == str(nodeItem_childId))):                     
                                        # identify relevant mutant id for attribute identification
                                        for child_5 in modelangeloXmlData:
                                            if((child_5.tag == 'node_item') and (child_5.attrib['id'] == str(nodeItem_childId))):  
                                                nodeItem_MutantObject = child_5.attrib['mutant_object']
                                        nodeItem_hasAttributes = False
                                        # identify value of parameter called attributeName
                                        for child_6 in modelangeloXmlData:
                                            attributeName = 'text'
                                            if((child_6.tag == 'meta_attribute') and (child_6.attrib['name'] == attributeName)):
                                                metaAttribute_Id = child_6.attrib['id']
                                                for child_7 in modelangeloXmlData:
                                                    if((child_7.tag == 'attribute') and (child_7.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_7.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                                        nodeItem_hasAttributes = True
                                                        fourth_hierarchy = SubElement(third_hierarchy, 'item')
                                                        fifth_hierarchy = SubElement(fourth_hierarchy, 'slots')
                                                        sixth_hierarchy = SubElement(fifth_hierarchy, 'item')
                                                        
                                                        seventh_hierarchy = SubElement(sixth_hierarchy, attributeName)
                                                        seventh_hierarchy.text = child_7.attrib['value']
                                                        if printing: print(child_7.attrib['value'])
                                        # identify value of parameter called attributeName 
                                        # a) handle this search in equal footing of previous search, because attributes may be independent. (x)
                                        # b) alternatively, nest this search at the if statement of previous search, so that this is realized only together with the previous attribute.
                                        for child_6 in modelangeloXmlData:
                                            attributeName = 'slot'
                                            if((child_6.tag == 'meta_attribute') and (child_6.attrib['name'] == attributeName)):
                                                metaAttribute_Id = child_6.attrib['id']
                                                for child_7 in modelangeloXmlData:
                                                    if((child_7.tag == 'attribute') and (child_7.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_7.attrib['mutant_object'] == str(nodeItem_MutantObject))):
                                                        seventh_hierarchy = SubElement(sixth_hierarchy, attributeName)
                                                        seventh_hierarchy.text = child_7.attrib['value']
                                                        if printing: print(child_7.attrib['value'])
                                        if(nodeItem_hasAttributes==False):
                                            fourth_hierarchy = SubElement(third_hierarchy, 'item')
                                            fourth_hierarchy.text = child_4.attrib['text']
                       
    # actions.xml
    print('exporting actions...')
    #Current differences resulted by export:
    #1) the order of items listed at actions2.xml is different.
    #2) There is a new line for the item text (e.g. "receive_greeting", "transmit_greeting", etc).                  
    chatBotXmlData_actions = Element('root')
    first_hierarchy = SubElement(chatBotXmlData_actions, 'actions')
    for child_1 in modelangeloXmlData:
        if((child_1.tag == 'node_item') and ('conversion' in child_1.attrib['shape'])):  
            nodeItem_Id = child_1.attrib['id'] # all conversion objects of actions
            print('nodeItem_Id=', nodeItem_Id)                           
            for child_2 in modelangeloXmlData:
                if((child_2.tag == 'label_item') and (child_2.attrib['node'] == str(nodeItem_Id))):
                    second_hierarchy = SubElement(first_hierarchy, 'item')
                    second_hierarchy.text = child_2.attrib['text']
                    # identify input elements
                    for child_3 in modelangeloXmlData:
                        if((child_3.tag == 'edge_item') and (child_3.attrib['target'] == str(nodeItem_Id))):
                            input_nodeItem_Id = child_3.attrib['source']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'label_item') and (child_4.attrib['node'] == str(input_nodeItem_Id))):
                                    third_hierarchy = SubElement(second_hierarchy, 'input')
                                    third_hierarchy.text = child_4.attrib['text']
                    # identify output elements
                    for child_3 in modelangeloXmlData:
                        if((child_3.tag == 'edge_item') and (child_3.attrib['source'] == str(nodeItem_Id))):
                            output_nodeItem_Id = child_3.attrib['target']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'label_item') and (child_4.attrib['node'] == str(output_nodeItem_Id))):
                                    third_hierarchy = SubElement(second_hierarchy, 'output')
                                    third_hierarchy.text = child_4.attrib['text']
             
    # dialog_activity_integrations.xml
    print('exporting dialog_activity_integrations...')
    chatBotXmlData_dialog_activity_integrations = Element('root')
    first_hierarchy = SubElement(chatBotXmlData_dialog_activity_integrations, 'integrations')
    for child_1 in modelangeloXmlData:
        if((child_1.tag == 'node_item') and ('activity_border' in child_1.attrib['shape'])):
            nodeItem_Id = child_1.attrib['id']
            print('nodeItem_Id=', nodeItem_Id)
            for child_2 in modelangeloXmlData:
                if((child_2.tag == 'label_item') and (child_2.attrib['node'] == str(nodeItem_Id)) and (child_2.attrib['text'] != 'Activities having no task, yet')):
                    second_hierarchy = SubElement(first_hierarchy, 'item')
                    third_hierarchy = SubElement(second_hierarchy, child_2.attrib['text'])
                    if printing: print('child_2.attrib[text]=', child_2.attrib['text'])
                    for child_3 in modelangeloXmlData:
                        if((child_3.tag == 'node_item') and (child_3.attrib['parent'] == str(nodeItem_Id)) and ('conversion' in child_3.attrib['shape'])):
                            conversionItem_Id = child_3.attrib['id']
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'label_item') and (child_4.attrib['node'] == str(conversionItem_Id))):
                                    fourth_hierarchy = SubElement(third_hierarchy, 'item')
                                    fourth_hierarchy.text = child_4.attrib['text']
       
    # dialogs.xml
    print('exporting dialogs...')       
    chatBotXmlData_dialogs = Element('root')
    first_hierarchy = SubElement(chatBotXmlData_dialogs, 'dialogs')
    for child_1 in modelangeloXmlData:
        if((child_1.tag == 'node_item') and ('process_border' in child_1.attrib['shape'])):
            processBorderItem_Id = child_1.attrib['id']
            print('nodeItem_Id=', processBorderItem_Id)
            for child_2 in modelangeloXmlData:
                if((child_2.tag == 'label_item') and (child_2.attrib['node'] == str(processBorderItem_Id))):
                    processBorderItem_Text = child_2.attrib['text']
                    second_hierarchy = SubElement(first_hierarchy, 'item')
                    third_hierarchy = SubElement(second_hierarchy, 'dialog_name')
                    third_hierarchy.text = processBorderItem_Text # e.g. "ask_for_product"
                    third_hierarchy = SubElement(second_hierarchy, 'steps')
                    fourth_hierarchy = SubElement(third_hierarchy, 'item')
                    fifth_hierarchy = SubElement(fourth_hierarchy, 'utterances')
                    if printing: print('processBorderItem_Title=', processBorderItem_Text)
                    for child_3 in modelangeloXmlData:
                        if((child_3.tag == 'node_item') and (child_3.attrib['parent'] == str(processBorderItem_Id)) and ('task' in child_3.attrib['shape'])):
                            taskItem_Id = child_3.attrib['id']
                            taskItem_MutantObject = child_3.attrib['mutant_object']
                            sixth_hierarchy = SubElement(fifth_hierarchy, 'item')
                            for child_4 in modelangeloXmlData:
                                if((child_4.tag == 'label_item') and (child_4.attrib['node'] == str(taskItem_Id))):
                                    taskItem_Text = child_4.attrib['text'] # e.g. "greet"  
                                    for child_5 in modelangeloXmlData:
                                        if((child_5.tag == 'edge_item') and (child_5.attrib['target'] == str(taskItem_Id))):
                                            roleOrSystem_Id = child_5.attrib['source']
                                            for child_6 in modelangeloXmlData:
                                                if((child_6.tag == 'label_item') and (child_6.attrib['node'] == str(roleOrSystem_Id))):
                                                    roleOrSystem_Text = child_6.attrib['text'] # e.g. "User" or "Chatbot"  
                                                    if(roleOrSystem_Text=='User'):
                                                        seventh_hierarchy = SubElement(sixth_hierarchy, 'user_response')
                                                        eigth_hierarchy = SubElement(seventh_hierarchy, 'intent')
                                                        eigth_hierarchy.text = taskItem_Text
                                                        # identify value of parameter called attributeName
                                                        if printing: print('taskItem_MutantObject=', taskItem_MutantObject)
                                                        for child_7 in modelangeloXmlData:
                                                            if((child_7.tag == 'meta_attribute')):
                                                                metaAttribute_Id = child_7.attrib['id']
                                                                metaAttribute_Name = child_7.attrib['name']
                                                                if printing: print('  metaAttribute_Id=', metaAttribute_Id)
                                                                for child_8 in modelangeloXmlData:
                                                                    if((child_8.tag == 'attribute') and (child_8.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_8.attrib['mutant_object'] == str(taskItem_MutantObject))):
                                                                        eigth_hierarchy = SubElement(seventh_hierarchy, 'slot')
                                                                        ninth_hierarchy = SubElement(eigth_hierarchy, 'name')
                                                                        ninth_hierarchy.text = metaAttribute_Name
                                                                        ninth_hierarchy = SubElement(eigth_hierarchy, 'value')
                                                                        ninth_hierarchy.text = child_8.attrib['value']
                                                                        if printing: print('    child_8.attrib[value]', metaAttribute_Name, child_8.attrib['value'])
                                                    elif(roleOrSystem_Text=='Chatbot'):
                                                        seventh_hierarchy = SubElement(sixth_hierarchy, 'bot_response')
                                                        eigth_hierarchy = SubElement(seventh_hierarchy, 'response')
                                                        eigth_hierarchy.text = taskItem_Text
                                                        # identify value of parameter called attributeName
                                                        if printing: print('taskItem_MutantObject=', taskItem_MutantObject)
                                                        for child_7 in modelangeloXmlData:
                                                            if((child_7.tag == 'meta_attribute')):
                                                                metaAttribute_Id = child_7.attrib['id']
                                                                metaAttribute_Name = child_7.attrib['name']
                                                                if printing: print('  metaAttribute_Id=', metaAttribute_Id)
                                                                for child_8 in modelangeloXmlData:
                                                                    if((child_8.tag == 'attribute') and (child_8.attrib['meta_attribute'] == str(metaAttribute_Id)) and (child_8.attrib['mutant_object'] == str(taskItem_MutantObject))):
                                                                        eigth_hierarchy = SubElement(seventh_hierarchy, 'slot')
                                                                        ninth_hierarchy = SubElement(eigth_hierarchy, 'name')
                                                                        ninth_hierarchy.text = metaAttribute_Name
                                                                        ninth_hierarchy = SubElement(eigth_hierarchy, 'value')
                                                                        ninth_hierarchy.text = child_8.attrib['value']
                                                                        if printing: print('    child_8.attrib[value]', metaAttribute_Name, child_8.attrib['value'])
                                                    else:
                                                        pass
    
    return chatBotXmlData_dialogs, chatBotXmlData_dialog_activity_integrations, chatBotXmlData_aliases, chatBotXmlData_contacts, chatBotXmlData_users, chatBotXmlData_intents, chatBotXmlData_invoices, chatBotXmlData_orders, chatBotXmlData_pricelists, chatBotXmlData_products, chatBotXmlData_activities, chatBotXmlData_cases, chatBotXmlData_actions, chatBotXmlData_responses, chatBotXmlData_slots

def prettify(xmlStr):
    """ This function returns a pretty-printed XML string for the Element."""
    
    INDENT = "    "
    rough_string = ET.tostring(xmlStr, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    prettified_xmlStr = reparsed.toprettyxml(indent=INDENT)    
    
    return prettified_xmlStr 

if __name__ == '__main__':
    """
    This function is not required so far.
    """
    
