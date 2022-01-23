from cx_Freeze import *
import sys

includefiles = ["settings.json", "Fonts\\"]

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Tells the build script to hide the console.

target = Executable(script="GUI.py", icon="EDSR.ico", base=base)

setup(
    name="EDRadio",
    version="2.0",
    description="",
    options={"build_exe": {"include_files": includefiles, "build_exe": ".//build"}},
    executables=[target],
)
