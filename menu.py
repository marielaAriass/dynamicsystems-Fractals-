#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
"""MoleWhat menu page
Provides a guizero function that creates a level menu, allowing the user to
select levels to play and view already completed levels. Level type is selected
randomly.
"""

from guizero import App, Box, Text, Drawing
from random import choice

# TODO: Uncomment the following imports when the functions are done
# from start import start
# from mc_question import mc_question
# from writing_question import writing_question

# Temporary testing functions; they will be removed when the other pages will
# be done...


def test1_func(event_data):
    # Test function: replace with mc_question
    print("You chose", event_data.widget.value, "Circular squares")


def test2_func(event_data):
    # Test function: replace with writing_question
    print("You chose", event_data.widget.value, "Impossible possibilities")


def test3_func():
    # Test function: replace with start function
    print("You want to go home?")


def dim(event_data):
    event_data.widget.bg = "#D5D5D5"


def undim(event_data):
    event_data.widget.bg = "white"


def menu(app):
    """Clears the window and shows the level menu."""

    # Clear window
    while len(app.children) != 0:
        app.children[0].destroy()

    # Set background color to blue (#1982C4)
    app.bg = "#1982C4"

    # Add an empty top box to set the top boundary for the level squares
    Box(app, align="top", width="fill", height=140)

    # Level container box
    level_box = Box(app, align="top", width=755, height=380, layout="grid")
    colors = [
        "#8AC926",
        "#8AC926",
        "#FFCA3A",
        "#FFCA3A",
        "#FF595E",
        "#FF595E",
        "#6A4C93",
        "#6A4C93",
    ]

    # Buttons
    i = 0
    for y in [0, 2]:
        for x in [0, 2, 4, 6]:
            button = Box(level_box, grid=[x, y], width=155, height=155)
            button.set_border(10, colors[i])
            button.tk.config(bg="white")
            text = Text(
                button,
                text=i + 1,
                color="black",
                bg="white",
                size=40,
                width=155,
                height=155,
            )

            # Change cursor to a "hand" on mouse hover
            text.tk.config(cursor="hand1")

            # Random choice between "multiple choice" and "writing"
            func = choice([test1_func, test2_func])
            text.when_clicked = func

            # Dim on mouse hover
            text.when_mouse_enters = dim
            text.when_mouse_leaves = undim
            i += 1

    # Space between buttons
    for x in [1, 3, 5]:
        for y in [0, 2]:
            Box(level_box, grid=[x, y], width=45, height=155)
    Box(level_box, grid=[0, 1, 7, 1], height=65, width=755)

    # "Home" button container box
    home_box = Box(app, align="bottom", height=130, width=800)

    # Draw the home button
    home = Drawing(home_box, align="right", width=100, height=100)
    home.oval(5, 5, 95, 95, color="#FF595E")
    home.triangle(50, 20, 24, 45, 76, 45, color="#8AC926")
    home.rectangle(35, 45, 65, 70, color="#FFCA3A")
    home.tk.config(cursor="hand1")
    home.when_clicked = test3_func


if __name__ == "__main__":
    """Testing."""

    app = App(title="MoleWhat", width=900, height=650)
    app.tk.resizable(False, False)
    menu(app)
    app.display()

