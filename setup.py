import sys
from cx_Freeze import setup, Executable
from PyQt5 import uic,QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable("__main__.py",base=base)
]

setup(
    name="Calculaddora Câmbio",
    version="1.0",
    description="App que calcula o câmbio",
    executables=Executable
)