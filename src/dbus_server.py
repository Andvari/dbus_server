'''
Created on Oct 25, 2012

@author: nemo
'''

import os
import gtk
import dbus
import dbus.service
import gobject
from dbus.mainloop.glib import DBusGMainLoop

class MDB(dbus.service.Object):
    def __init__(self):
        DBusGMainLoop(set_as_default=True)
        dbus.service.Object.__init__(self, dbus.service.BusName('home.nemo.my_dbus', dbus.SessionBus()), '/home/nemo/my_dbus')
        
    @dbus.service.method(dbus_interface='home.nemo.my_dbus', in_signature='i')
    def print_num(self, a):
        print a
        
    @dbus.service.method(dbus_interface='home.nemo.my_dbus')
    def close_service(self):
        print "Service stopped."
        os._exit(True)
        

mdb = MDB()
print "Service started"
gobject.MainLoop().run()
