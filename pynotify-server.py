#!/usr/bin/python

#Server program listens to port 8250, Send a text
# message to this port and it will display in the desktop

from socket import *
import pynotify
import gtk
import sys
import logging
import gobject

def log(msg):
    LOG_FILENAME = '/tmp/pynotify.log'
    logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
    logging.debug(msg)



class PyNotifyServer: 
    # activate callback 
    def activate( self, widget, data=None): 
        dialog = gtk.MessageDialog( 
        parent         = None, 
        flags          = gtk.DIALOG_DESTROY_WITH_PARENT, 
        type           = gtk.MESSAGE_INFO, 
        buttons        = gtk.BUTTONS_OK, 
        message_format = "Listening to port 8250 for messages") 
        dialog.set_title('Pynotify-Server') 
        dialog.connect('response', self.show_hide) 
        dialog.show() 
   # Show_Hide callback 
    def  show_hide(self, widget,response_id, data= None): 
        if response_id == gtk.RESPONSE_YES: 
                widget.hide() 
        else: 
                widget.hide() 
    # destroyer callback 
    def  destroyer(self, widget,response_id, data= None): 
        if response_id == gtk.RESPONSE_OK:
            self.UDPSock.close()
            gtk.main_quit()
                
        else: 
            widget.hide() 
    # popup callback 
    def popup(self, button, widget, data=None): 
        dialog = gtk.MessageDialog( 
        parent         = None, 
        flags          = gtk.DIALOG_DESTROY_WITH_PARENT, 
        type           = gtk.MESSAGE_INFO, 
        buttons        = gtk.BUTTONS_OK_CANCEL, 
        message_format = "Do you want to close this application?") 
        dialog.set_title('Quit?') 
        dialog.connect('response', self.destroyer) 
        dialog.show()
        
    def notify(self,UDPSock,condition):
        data,addr = UDPSock.recvfrom(self.buf)
	if not data:
            return False
        else:
            m = pynotify.Notification(data,"Broadcasted from: "+addr[0])
            #m.set_timeout(10)
            m.show()
            return True
            
    def __init__(self): 
        # create a new Status Icon 
        self.staticon = gtk.StatusIcon() 
        self.staticon.set_from_stock(gtk.STOCK_ABOUT) 
        #self.staticon.set_blinking(True) 
        self.staticon.connect("activate", self.activate) 
        self.staticon.connect("popup_menu", self.popup) 
        self.staticon.set_visible(True)
        # Set the socket parameters
        self.host = ""
        self.port = 8250
        self.buf = 1024
        self.addr = (self.host,self.port)
        
        # Create socket and bind to address
        self.UDPSock = socket(AF_INET,SOCK_DGRAM)
        self.UDPSock.bind(self.addr)
        pynotify.init("Pynotify Echo")
        gobject.io_add_watch(self.UDPSock, gobject.IO_IN, self.notify)
        # invoking the main() 
        gtk.main()
if __name__ == "__main__": 
    pynotify_server = PyNotifyServer() 
    

