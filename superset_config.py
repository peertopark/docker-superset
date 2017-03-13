import os

MAPBOX_API_KEY = os.getenv("MAPBOX_API_KEY", "")
CACHE_CONFIG = {'CACHE_TYPE': 'simple'}
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "")
SECRET_KEY = os.getenv("SECRET_KEY", "")
