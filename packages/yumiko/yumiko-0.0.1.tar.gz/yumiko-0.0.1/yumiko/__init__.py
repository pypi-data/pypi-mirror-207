__version__ = "0.0.1"
__license__ = "GNU Lesser General Public License v3.0 (LGPL-3.0)"
__copyright__ = "Copyright (C) 2023-present yumiko-api <https://github.com/yumiko-api>"

from yumiko.thumbnails import gen_thumb, create_thumb, generation, creation

def yumiko():
  print(
     f'Yumiko Successfully installed Current version of Yumiko {__version__}' + "\n"
     f'Under {__license__}'
  )
