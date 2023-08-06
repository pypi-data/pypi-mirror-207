

""""""# start delvewheel patch
def _delvewheel_init_patch_1_3_6():
    import os
    import sys
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'light_curve.libs'))
    is_pyinstaller = getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')
    if not is_pyinstaller or os.path.isdir(libs_dir):
        os.add_dll_directory(libs_dir)


_delvewheel_init_patch_1_3_6()
del _delvewheel_init_patch_1_3_6
# end delvewheel patch

# Import all Python features
from .light_curve_py import *

# Hide Python features with Rust equivalents
from .light_curve_ext import *

# Hide Rust Extractor with universal Python Extractor
from .light_curve_py import Extractor

from .light_curve_ext import __version__
