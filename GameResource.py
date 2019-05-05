from flask_restful import Resource
from cheats import *

class GameResource(Resource):
    def get(self):
        return getOrCreateGame().getState()
