#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Bareos python plugins baseclass for hypervisor related backup and restore 
# (c) Bareos GmbH & Co. KG
# AGPL v.3
# Author: Maik Aussendorf

import sys
sys.path.append('/usr/lib64/bareos/plugins/');

import BareosFdWrapper
from  BareosFdPluginBaseclass import *


class BareosFdPluginHypervisor (BareosFdPluginBaseclass):
    '''
    Baseclass for hypervisor related backup and restore 
    Will need deried classes with hypervisor specific implementation
    '''       

    def parse_plugin_definition(self,context, plugindef):
        '''
        Parses the plugin argmuents and reads files from file given by argument 'vmname'
        '''
        BareosFdPluginBaseclass.parse_plugin_definition(self, context, plugindef);
        if (not 'vmname' in self.options):
            DebugMessage(context, 100, "Option \'vmname\' not defined.\n");
            return bRCs['bRC_Error'];
        DebugMessage(context, 100, "Using " + self.options['vmname'] + "\n");
        return bRCs['bRC_OK'];

    def get_vm_details (self,context):
        '''
        Returns vm details as a dictionary(?)
        '''
        pass;

# vim: ts=4 tabstop=4 expandtab shiftwidth=4 softtabstop=4
