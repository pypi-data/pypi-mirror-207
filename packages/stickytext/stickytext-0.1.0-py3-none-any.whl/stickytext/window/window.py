# Imports ##############################################################################################################
import pathlib
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


# Edit Dialog ##########################################################################################################
class Window:
    def __init__(self):
        # GtkBuilder Setup
        self.gtk_builder = Gtk.Builder()
        self.gtk_builder.add_from_file(str((pathlib.Path(__file__).parent / 'window.ui').resolve()))

        # Widgets Setup
        self.window = self.gtk_builder.get_object('window')
        self.textview = self.gtk_builder.get_object("textview")
        self.textbuffer = self.gtk_builder.get_object("textbuffer")
