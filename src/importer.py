
""" 
A little script to do import of .xml files for Modelangelo tool following the DSL standard.
Copyright (c) 2022 Marcus Grum
"""

__author__ = 'Marcus Grum, marcus.grum@uni-potsdam.de'
# SPDX-License-Identifier: AGPL-3.0-or-later or individual license
# SPDX-FileCopyrightText: 2022 Marcus Grum <marcus.grum@uni-potsdam.de>

import xml.etree.ElementTree as ET
import random
import string
from os import listdir
from os.path import isfile, join
from modelangeloInterface import *

if __name__ == '__main__':
    """
    This function imports dsl example files (.xml)
    and creates the corresponding Modelangelo file (.xml).
    """

    initialize_global_modelangelo_variables()
    exampleFolderPath = '../examples/'
    importFolderPath = 'import/'
    modelingFolderPath = 'modeling/'
    exportFolderPath = 'export/'

    # identify relevant example files in given exampleFolderPath  
    exampleFiles = [f for f in listdir(exampleFolderPath) if isfile(join(exampleFolderPath, f))]
    print(exampleFiles)

    # create and load example xml file of Modelangelo
    create_blancModelangeloFile(exampleFolderPath + modelingFolderPath + 'DslExample.xml')
    modelangeloXmlData = load_Data_from_xmlFile(exampleFolderPath + modelingFolderPath + 'DslExample.xml')
    #modelangeloXmlData = load_Data_from_xmlFile(exampleFolderPath + modelingFolderPath + 'DslExample_v02_manuallyCreated.xml') # created manually via Modelangelo    
    
    # test at Modelangelo: add any item to relevant models in order to check algorithms
    # modelangeloXmlData = modification_modelangelo_createAllNodeItemsTest(modelangeloXmlData)

    # create and load example xml-based dsl files
    chatBotXmlData_actions                      = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'actions.xml')
    chatBotXmlData_activities                   = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'activities.xml')
    chatBotXmlData_aliases                      = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'aliases.xml')
    chatBotXmlData_cases                        = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'cases.xml')
    chatBotXmlData_contacts                     = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'contacts.xml')
    chatBotXmlData_dialogs                      = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'dialogs.xml')
    chatBotXmlData_dialog_activity_integrations = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'dialog_activity_integrations.xml')
    chatBotXmlData_intents                      = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'intents.xml')
    chatBotXmlData_invoices                     = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'invoices.xml')
    chatBotXmlData_orders                       = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'orders.xml')
    chatBotXmlData_pricelists                   = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'pricelists.xml')
    chatBotXmlData_products                     = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'products.xml')
    chatBotXmlData_responses                    = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'responses.xml')
    chatBotXmlData_slots                        = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'slots.xml')
    chatBotXmlData_users                        = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'users.xml')

    # show all dsl data (four levels)
    #screen_jasonBasedXmlData(chatBotXmlData_actions)
    #screen_jasonBasedXmlData(chatBotXmlData_activities)
    #screen_jasonBasedXmlData(chatBotXmlData_aliases)
    #screen_jasonBasedXmlData(chatBotXmlData_cases)
    #screen_jasonBasedXmlData(chatBotXmlData_contacts)
    #screen_jasonBasedXmlData(chatBotXmlData_dialogs)
    #screen_jasonBasedXmlData(chatBotXmlData_dialog_activity_integrations)
    #screen_jasonBasedXmlData(chatBotXmlData_intents)
    #screen_jasonBasedXmlData(chatBotXmlData_invoices)
    #screen_jasonBasedXmlData(chatBotXmlData_orders)
    #screen_jasonBasedXmlData(chatBotXmlData_pricelists)
    #screen_jasonBasedXmlData(chatBotXmlData_products)
    #screen_jasonBasedXmlData(chatBotXmlData_responses)
    #screen_jasonBasedXmlData(chatBotXmlData_slots)
    #screen_jasonBasedXmlData(chatBotXmlData_users)

    # show all Modelangelo data
    #screen_xmlData(modelangeloXmlData)

    # merge current chatBotXmlData_x with blanc modelangelo.xml
    modelangeloXmlData = modification_modelangelo_importDslFiles(modelangeloXmlData, chatBotXmlData_dialogs, chatBotXmlData_dialog_activity_integrations, chatBotXmlData_aliases, chatBotXmlData_contacts, chatBotXmlData_users, chatBotXmlData_intents, chatBotXmlData_invoices, chatBotXmlData_orders, chatBotXmlData_pricelists, chatBotXmlData_products, chatBotXmlData_activities, chatBotXmlData_cases, chatBotXmlData_actions, chatBotXmlData_responses, chatBotXmlData_slots)
    
    # show modified Modelangelo data
    #screen_xmlData(modelangeloXmlData)

    # save modified Modelangelo data
    save_xmlData_to_file(modelangeloXmlData, exampleFolderPath + modelingFolderPath + 'DslExample.xml')