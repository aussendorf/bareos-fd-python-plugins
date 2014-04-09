#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Bareos python class for VMware related backup and restore 
# (c) Bareos GmbH & Co. KG
# AGPL v.3
# Author: Maik Aussendorf

from BareosFdPluginHypervisor import *

class BareosFdPluginVMware (BareosFdPluginHypervisor):
    '''
    VMware related backup and restore stuff 
    '''       
    def parse_plugin_definition(self,context, plugindef):
        '''
        Parses the plugin argmuents and reads files from file given by argument 'vmname'
        '''
        BareosFdPluginHypervisor.parse_plugin_definition(self, context, plugindef);
        return bRCs['bRC_OK'];

    def get_vm_details (self,context):
        '''
        Returns vm details as a dictionary(?)
        '''
        pass;

# vim: ts=4 tabstop=4 expandtab shiftwidth=4 softtabstop=4
