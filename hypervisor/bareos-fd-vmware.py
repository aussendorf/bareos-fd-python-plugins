#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Bareos-fd-vmware is a python Bareos FD Plugin intended to backup and restore VMware images and configuration

import sys
sys.path.append('/usr/lib64/bareos/plugins/');

# Provided by the Bareos FD Python plugin interface
from bareosfd import *
from bareos_fd_consts import *

# This module contains the wrapper functions called by the Bareos-FD, the functions call the corresponding
# methods from your plugin class
from BareosFdWrapper import *

# This module contains the used plugin class
from BareosFdPluginVMware import *


def load_bareos_plugin(context, plugindef):
    '''
    This function is called by the Bareos-FD to load the plugin
    We use it to intantiate the plugin class
    '''
    BareosFdWrapper.bareos_fd_plugin_object = BareosFdPluginVMware(context, plugindef);

    return bRCs['bRC_OK'];

# the rest is done in the Plugin module
