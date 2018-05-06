#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import os
import dbus


class LogoutWindow:

    def cancel(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def logout(self, widget):
        os.system("openbox --exit")

    def suspend(self, widget):
        os.system("suspend")

    def reboot(self, widget):
        os.system("reboot")

    def shutdown(self, widget):
        os.system("poweroff")

    def __init__(self):

        # Create a new window.
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Exit? Choose an option:")
        self.window.set_resizable(False)
        self.window.set_position(1)
        self.window.connect("delete_event", self.cancel)
        self.window.set_border_width(8)

        # Create a box to pack widgets into.
        self.box = gtk.HBox(False, 0)
        self.window.add(self.box)

        # Create logout button.
        self.logout_button = gtk.Button("Log out")
        self.logout_button.connect("clicked", self.logout)
        self.box.pack_start(self.logout_button, True, True, 0)
        self.logout_button.show()

        # Create suspend button.
        self.suspend_button = gtk.Button("Suspend")
        self.suspend_button.connect("clicked", self.suspend)
        self.box.pack_start(self.suspend_button, True, True, 0)
        self.suspend_button.show()

        # Create reboot button.
        self.reboot_button = gtk.Button("Reboot")
        self.reboot_button.connect("clicked", self.reboot)
        self.box.pack_start(self.reboot_button, True, True, 0)
        self.reboot_button.show()

        # Create shutdown button.
        self.shutdown_button = gtk.Button("Shutdown")
        self.shutdown_button.connect("clicked", self.shutdown)
        self.box.pack_start(self.shutdown_button, True, True, 0)
        self.shutdown_button.show()

        for button in (self.logout_button, self.suspend_button, self.reboot_button, self.shutdown_button):
            button.set_border_width(8)

        self.box.show()
        self.window.show()

def on_left_click(event):
  # optimization: if the window is already open, do nothing
  LogoutWindow()  
  gtk.main()

if __name__ == "__main__":
    icon = gtk.StatusIcon()
    icon.set_from_file(os.path.realpath(os.path.dirname(__file__)) + "/icon.png")
    icon.connect('activate', on_left_click)
    gtk.main()