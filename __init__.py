from os.path import dirname, basename, isfile, join
import glob
modules = glob.glob("*.py")
module_blacklist = ['__init__.py', 'setup.py']
__name__ = "videotools_dev"
__version__ = "0.0.10"
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and f not in module_blacklist]

"""[Removed for packaging]
import init
import extract
import bbox
import image_stabilizer
import transfer_learning
"""

