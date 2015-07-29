# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 09:33:43 2015

@author: shubo
"""

#!/usr/bin/env python
#
# Copyright 2009-2012 Canonical Ltd.
#
# Authors: Neil Jagdish Patel <neil.patel@canonical.com>
#          Jono Bacon <jono@ubuntu.com>
#          David Planella <david.planella@ubuntu.com>
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of either or both of the following licenses:
#
# 1) the GNU Lesser General Public License version 3, as published by the 
# Free Software Foundation; and/or
# 2) the GNU Lesser General Public License version 2.1, as published by 
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranties of 
# MERCHANTABILITY, SATISFACTORY QUALITY or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the applicable version of the GNU Lesser General Public 
# License for more details.
#
# You should have received a copy of both the GNU Lesser General Public 
# License version 3 and version 2.1 along with this program.  If not, see 
# <http://www.gnu.org/licenses/>
#

from gi.repository import Gtk
from gi.repository import AppIndicator3 as appindicator


#def menuitem_response(w, buf):
#  print buf

if __name__ == "__main__":
#appindicator.Indicator.new(client_name,icon_set,category)
  ind = appindicator.Indicator.new (
                        "wakatime-desktop-client",
                        "indicator-messages",
                        appindicator.IndicatorCategory.APPLICATION_STATUS)
  ind.set_status (appindicator.IndicatorStatus.ACTIVE)
  ind.set_attention_icon ("indicator-messages-new")
  ind.set_icon('wakatime-white')

  # create a menu
  menu = Gtk.Menu()

  # create some 
  menu_item_login = Gtk.MenuItem("Login")
  menu_item_logout =Gtk.MenuItem("Logout")
  menu_item_log = Gtk.MenuItem("View detailed logs")
  menu.append(menu_item_login)
  menu.append(menu_item_log)
  menu.append(menu_item_logout)  

  # this is where you would connect your menu item up with a function:
  
  # menu_items.connect("activate", menuitem_response, buf)
  # menu_items.connect("activate", menuitem_response, buf)
  # menu_items.connect("activate", menuitem_response, buf) 
    

  # show the items
  menu_item_login.show()
  menu_item_log.show()
  menu_item_logout.show()

  ind.set_menu(menu)

  Gtk.main()
