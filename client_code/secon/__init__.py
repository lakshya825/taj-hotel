from ._anvil_designer import seconTemplate

from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class secon(seconTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def link_1_click(self, **event_args):
    open_form('menu')

  def button_1_click(self, **event_args):
    open_form('booking')
