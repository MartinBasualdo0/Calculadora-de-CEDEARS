import os
from threading import Timer
import webbrowser

def _open_browser():
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:8050/')

def open_default_browser():
    Timer(1, _open_browser).start()