from src import api

from src.main.resources.image import Images

# We define all the endpoints handled by this service
api.add_resource(Images, '/preprocessed-images')
