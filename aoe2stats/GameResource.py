from flask_restful import Resource
from aoe2stats.cheats import *

class GameResource(Resource):
    def get(self):
        return getOrCreateGame().getState()
