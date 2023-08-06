import os
import dotenv
import inspect

from .tile_io import *

if os.path.exists('.env.shared'):
    dotenv.load_dotenv('.env.shared')

try:
    os.environ['EARTHDATA_USERNAME']
    os.environ['EARTHDATA_PASSWORD']
except KeyError as e:
    print("\nEnvironmental variables 'EARTHDATA_USERNAME' and 'EARTHDATA_PASSWORD' must be set!\nRegister at https://urs.earthdata.nasa.gov/users/new and set them with either:\n    - os.environ['EARTHDATA_USERNAME'] = '<your_username>'\n      os.environ['EARTHDATA_PASSWORD'] = '<your_password>'\n    - Create a .env.shared file in the calling directory containing\nEARTHDATA_USERNAME=<your_username>\nEARTHDATA_PASSWORD=<your_password>")
    raise
    

os.environ['TERRAIN_SRC'] = os.path.dirname(
    os.path.abspath(inspect.getsourcefile(lambda: 0))
)
os.environ['TERRAIN_DATA'] = os.path.join(os.environ['TERRAIN_SRC'], 'data')
_DATA_PRODUCT_TYPES = ["aerosol", "cloud", "terrain"]

if not os.path.exists(os.environ['TERRAIN_DATA']):
    os.mkdir(os.environ['TERRAIN_DATA'])
for product in _DATA_PRODUCT_TYPES:
    product_data_path = os.path.join(os.environ['TERRAIN_DATA'], product)
    if not os.path.exists(product_data_path):
        os.mkdir(product_data_path)