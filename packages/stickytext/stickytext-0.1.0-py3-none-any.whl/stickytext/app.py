# Imports ##############################################################################################################
import gi
import sys
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio, GLib, GObject
from stickytext.window.window import Window


# GtkApp ###############################################################################################################
class StickyTextGtkApp(Gtk.Application):
    def __init__(self):
        # GTK App Setup
        super().__init__(application_id="com.github.beatlink.stickytext", flags=Gio.ApplicationFlags.HANDLES_OPEN)
        GLib.set_application_name('StickyText')

        self.file = None
        self.file_monitor = None
        self.text_buffer_signal_handler = None
        self.file_monitor_signal_handler = None
        self.autosave_timer = -1
        self.autoload_timer = -1

        # Load Window
        self.window = Window()
        self.window.window.application = self
        self.window.window.connect("close-request", self.on_shutdown)
        self.text_buffer_signal_handler = self.window.textbuffer.connect("changed", self.on_textbuffer_changed)
        self.connect("activate", self.on_activate)
        self.connect("open", self.on_open)

    @staticmethod
    def on_activate(*_):
        print("""
        StickyText
        
        An extremely simple app to show a single text file as a sticky note. 
        
        To Run:
        
        stickytext /path/to/file.txt
                
        """)

    # Startup / Shutdowns ----------------------------------------------------------------------------------------------
    def on_open(self, _application, file_handle, _file_count, _hint):
        self.file = file_handle[0]
        self.monitor_file()
        self.start_sync()
        self.load_file()
        self.add_window(self.window.window)
        self.window.window.present()

    def on_shutdown(self, _):
        self.window.window.close()
        self.quit()

    # File Monitoring --------------------------------------------------------------------------------------------------
    def monitor_file(self):
        self.file_monitor = self.file.monitor_file(
            Gio.FileMonitorFlags.WATCH_MOVES)
        self.file_monitor_signal_handler = self.file_monitor.connect("changed", self.on_file_changed)

    def on_file_changed(self, *_):
        self.autoload_timer = 1

    def on_textbuffer_changed(self, _textbuffer, *_):
        self.autosave_timer = 1

    # Processing -------------------------------------------------------------------------------------------------------
    def start_sync(self):
        GLib.timeout_add(500, self.sync_loop)

    def sync_loop(self):
        if self.autoload_timer == 0:
            self.load_file()
            self.autoload_timer -= 1
        elif self.autoload_timer > 0:
            self.autoload_timer -= 1
        if self.autosave_timer == 0:
            self.save_file()
            self.autosave_timer -= 1
        elif self.autosave_timer > 0:
            self.autosave_timer -= 1
        return True

    # Loading ----------------------------------------------------------------------------------------------------------
    def load_file(self, *_):
        print("Loading file")
        GObject.signal_handler_block(self.window.textbuffer, self.text_buffer_signal_handler)
        success, contents, _etags = self.file.load_contents(None)
        path = self.file.peek_path()
        if not success:
            print(f"Unable to open {path}: {contents}")
            return
        try:
            text = contents.decode('utf-8')
        except UnicodeError:
            print(f"Unable to load the contents of {path}: the file is not encoded with UTF-8")
            return

        self.window.textbuffer.begin_user_action()
        start = self.window.textbuffer.get_start_iter()
        end = self.window.textbuffer.get_end_iter()
        self.window.textbuffer.delete(start, end)
        self.window.textbuffer.insert(start, text)
        end = self.window.textbuffer.get_end_iter()
        self.window.textbuffer.place_cursor(end)
        self.window.textbuffer.end_user_action()
        info = self.file.query_info("standard::display-name", Gio.FileQueryInfoFlags.NONE)
        display_name = info.get_attribute_string("standard::display-name") if info else self.file.get_basename()
        self.window.window.set_title(display_name)
        GLib.timeout_add_seconds(
            1, GObject.signal_handler_unblock, self.window.textbuffer, self.text_buffer_signal_handler)
        print("File loaded")

    # Saving -----------------------------------------------------------------------------------------------------------
    def save_file(self):
        print("Saving file")
        GObject.signal_handler_block(self.file_monitor, self.file_monitor_signal_handler)
        start = self.window.textbuffer.get_start_iter()
        end = self.window.textbuffer.get_end_iter()
        text = self.window.textbuffer.get_text(start, end, False)
        if not text:
            return
        content_bytes = text.encode('utf-8')
        success, _etags = self.file.replace_contents(content_bytes, None, False, Gio.FileCreateFlags.NONE, None)
        info = self.file.query_info("standard::display-name", Gio.FileQueryInfoFlags.NONE)
        display_name = info.get_attribute_string("standard::display-name") if info else self.file.get_basename()
        if not success:
            print(f"Unable to save {display_name}")
            return
        GLib.timeout_add_seconds(1, GObject.signal_handler_unblock, self.file_monitor, self.file_monitor_signal_handler)
        print("File saved")


def run_app():
    app = StickyTextGtkApp()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)


if __name__ == '__main__':
    run_app()
