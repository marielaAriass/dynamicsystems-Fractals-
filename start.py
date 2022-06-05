#!/usr/bin/env python
# coding: utf-8

# In[6]:


# MoleWhat menu page
# Copyright (C) 2022  Karime Ochoa Jacinto
#                     Luis Aaron Nieto Cruz
#                     Miriam Guadalupe Valdez Maldonado
#                     Mariela Yael Arias Rojo
#                     Anton Pashkov
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from guizero import *
from guizero import App, PushButton

from menu import menu



def start(app):
    a = menu(app)
    Box(app, align="top", width=500, height=70)

    # Level container box
    level_box = Box(app, align="top", width=900, height=510, layout="grid")
    level_box.bg = 'white'

    for y in [0,0]:
        for x in [0,2,3,4,5,6]:            
            button = Box(level_box, grid=[x, y], width=155, height=155)

            button = Drawing(level_box, grid=[3,2], width=250, height=250)

            button.tk.config(cursor = "hand1")
            button.triangle(60, 10, 60, 150, 200, 80, color ="#8AC926")

            
            home = Box(level_box, grid=[3,3], height=35, width=300)

            text = Text(home, text='Molewhat?', color="black", bg="white",size=35,width=100,height=100)

            button.when_clicked = a
         
            
app = App(title = 'MoleWhat?', height=650, width=900)
app.bg = "#1982C4"
start(app)
app.tk.resizable(False, False)

app.display()


# In[ ]:




