from __future__ import annotations

from aqt import gui_hooks, mw
from aqt.qt import *
from aqt.utils import tooltip
from aqt.utils import showInfo
from aqt.utils import showWarning

from pynput.keyboard import Controller




# Define the action to perform when the option is clicked
def pressAddNewCard(deck_id):
    # Set the selected deck id
    mw.col.decks.select(deck_id)

    # Click Add on this Deck ID
    keyboard = Controller()
    keyboard.press('a')
    keyboard.release('a')



# Define the function to add the option to the menu
def add_option_to_menu(menu, did):
    # Create a new action with the label "My Option"
    action = QAction("Add new card", menu)
    # Connect the action to the function defined above
    action.triggered.connect(lambda b: pressAddNewCard(did))
    # Add the action to the menu
    menu.insertAction(menu.actions()[0], action)


gui_hooks.deck_browser_will_show_options_menu.append(add_option_to_menu)
