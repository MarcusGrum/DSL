
""" 
A little script to do export of .xml files of Modelangelo modeling tool following the DSL standard. 
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
    This function exports the by Modelangelo modified data to dsl files
    """
    
    initialize_global_modelangelo_variables()
    exampleFolderPath = '../examples/'
    importFolderPath = 'import/'
    modelingFolderPath = 'modeling/'
    exportFolderPath = 'export/'

    # identify relevant example files in given exampleFolderPath  
    exampleFiles = [f for f in listdir(exampleFolderPath) if isfile(join(exampleFolderPath, f))]
    print(exampleFiles)
    
    # load modified xml file of Modelangelo
    modelangeloXmlData = load_Data_from_xmlFile(exampleFolderPath + modelingFolderPath + 'DslExample.xml')
    #modelangeloXmlData = load_Data_from_xmlFile(exampleFolderPath + 'DslExample_v03_manuallyCreated.xml') # created manually via Modelangelo    
    
    # show all Modelangelo data
    #screen_xmlData(modelangeloXmlData)
    
    # load example xml-based dsl files (just to debug on base of comparison - to be deleted)
    #chatBotXmlData_actions_                      = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'actions.xml')
    #chatBotXmlData_activities_                   = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'activities.xml')
    #chatBotXmlData_aliases_                      = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'aliases.xml')
    #chatBotXmlData_cases_                        = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'cases.xml')
    #chatBotXmlData_contacts_                     = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'contacts.xml')
    #chatBotXmlData_dialogs_                      = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'dialogs.xml')
    #chatBotXmlData_dialog_activity_integrations_ = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + importFolderPath + 'dialog_activity_integrations.xml')
    #chatBotXmlData_intents_                      = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'intents.xml')
    #chatBotXmlData_invoices_                     = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'invoices.xml')
    #chatBotXmlData_orders_                       = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'orders.xml')
    #chatBotXmlData_pricelists_                   = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'pricelists.xml')
    #chatBotXmlData_products_                     = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'products.xml')
    #chatBotXmlData_responses_                    = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'responses.xml')
    #chatBotXmlData_slots_                        = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'slots.xml')
    #chatBotXmlData_users_                        = load_Data_from_xmlFile(exampleFolderPath + importFolderPath + 'users.xml')
     
    # show all dsl data (four levels) (just to debug on base of comparison - to be deleted)
    #screen_jasonBasedXmlData(chatBotXmlData_actions_)
    #screen_jasonBasedXmlData(chatBotXmlData_activities_)
    #screen_jasonBasedXmlData(chatBotXmlData_aliases_)
    #screen_jasonBasedXmlData(chatBotXmlData_cases_)
    #screen_jasonBasedXmlData(chatBotXmlData_contacts_)
    #screen_jasonBasedXmlData(chatBotXmlData_dialogs_)
    #screen_jasonBasedXmlData(cdialog_activity_integrations_)
    #screen_jasonBasedXmlData(chatBotXmlData_intents_)
    #screen_jasonBasedXmlData(chatBotXmlData_invoices_)
    #screen_jasonBasedXmlData(chatBotXmlData_orders_)
    #screen_jasonBasedXmlData(chatBotXmlData_pricelists_)
    #screen_jasonBasedXmlData(chatBotXmlData_products_)
    #screen_jasonBasedXmlData(chatBotXmlData_responses_)
    #screen_jasonBasedXmlData(chatBotXmlData_slots_)
    #screen_jasonBasedXmlData(chatBotXmlData_users_)
    
    # export current data from modelangelo.xml to chatBotXmlData_x
    chatBotXmlData_dialogs, chatBotXmlData_dialog_activity_integrations, chatBotXmlData_aliases, chatBotXmlData_contacts, chatBotXmlData_users, chatBotXmlData_intents, chatBotXmlData_invoices, chatBotXmlData_orders, chatBotXmlData_pricelists, chatBotXmlData_products, chatBotXmlData_activities, chatBotXmlData_cases, chatBotXmlData_actions, chatBotXmlData_responses, chatBotXmlData_slots = modification_modelangelo_exportDslFiles(modelangeloXmlData)
    
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
    
    # save modified dsl data
    save_xmlData_to_file_pretty(chatBotXmlData_actions,                      exampleFolderPath + exportFolderPath + 'actions.xml')
    save_xmlData_to_file_pretty(chatBotXmlData_activities,                   exampleFolderPath + exportFolderPath + 'activities.xml')
    save_xmlData_to_file_pretty(chatBotXmlData_aliases,                      exampleFolderPath + exportFolderPath + 'aliases.xml')
    save_xmlData_to_file_pretty(chatBotXmlData_cases,                        exampleFolderPath + exportFolderPath + 'cases.xml')
    save_xmlData_to_file_pretty(chatBotXmlData_contacts,                     exampleFolderPath + exportFolderPath + 'contacts.xml')
    save_xmlData_to_file_pretty(chatBotXmlData_dialogs,                      exampleFolderPath + exportFolderPath + 'dialogs.xml')
    save_xmlData_to_file_pretty(chatBotXmlData_dialog_activity_integrations, exampleFolderPath + exportFolderPath + 'dialog_activity_integrations.xml')
    save_xmlData_to_file_pretty(chatBotXmlData_intents,                      exampleFolderPath + exportFolderPath + 'intents.xml')
    save_xmlData_to_file_pretty(chatBotXmlData_invoices,                     exampleFolderPath + exportFolderPath + 'invoices.xml')
    save_xmlData_to_file_pretty(chatBotXmlData_orders,                       exampleFolderPath + exportFolderPath + 'orders.xml')
    save_xmlData_to_file_pretty(chatBotXmlData_pricelists,                   exampleFolderPath + exportFolderPath + 'pricelists.xml')
    save_xmlData_to_file_pretty(chatBotXmlData_products,                     exampleFolderPath + exportFolderPath + 'products.xml')
    save_xmlData_to_file_pretty(chatBotXmlData_responses,                    exampleFolderPath + exportFolderPath + 'responses.xml')
    save_xmlData_to_file_pretty(chatBotXmlData_slots,                        exampleFolderPath + exportFolderPath + 'slots.xml')
    save_xmlData_to_file_pretty(chatBotXmlData_users,                        exampleFolderPath + exportFolderPath + 'users.xml')