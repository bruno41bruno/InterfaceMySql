import sys
from cx_Freeze import setup, executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    executable("__main__.py",base=base)
]

setup(
    name="Calculaddora Câmbio",
    version="1.0",
    description="App que calcula o câmbio",
    executables=executable
)