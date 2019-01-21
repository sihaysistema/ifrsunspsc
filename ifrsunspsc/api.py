# -*- coding: utf-8 -*-
# Copyright (c) 2019, SHS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import json
import requests
import os

# Permite trabajar con acentos, ñ, simbolos, etc
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

@frappe.whitelist(allow_guest=True)
def addlvl1(center):
    try:
        # First, establish which is this company running the method, or default to global company
        #this_company = frappe.defaults.get_user_default("Company") || frappe.defaults.get_global_default("company")
        this_company = frappe.db.get_value("Global Defaults", None, "default_company")
        #frappe.msgprint(_(this_company))
        root_cost_center = frappe.db.get_values('Cost Center',
                                                filters={'lft': 1, 'is_group': 1, 'company': this_company},
                                                fieldname=['name'], as_dict=1)
          
        frappe.msgprint(_(root_cost_center[0]['name']))
        
        #for r in root_cost_center:
        #    frappe.msgprint(_(r.name))
        unspsc = frappe.new_doc("Cost Center")
        unspsc.cost_center_name = 'UNSPSC'
        unspsc.parent_cost_center = root_cost_center[0]['name']
        unspsc.company = this_company
        unspsc.is_group = 1
        #unspsc.lft = 3
        #unspsc.rgt = 4
        unspsc.old_parent = root_cost_center[0]['name']
        unspsc.save(ignore_permissions=True)
   
    except:
        frappe.msgprint(_('FAIL'))
    return 'hello'