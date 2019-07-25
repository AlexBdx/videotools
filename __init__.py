from os.path import dirname, basename, isfile, join
import glob
modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
__name__ = "videotools"
__version__ = "0.0.6"

"""[Removed for packaging]
import init
import extract
import bbox
import image_stabilizer
import transfer_learning
"""

