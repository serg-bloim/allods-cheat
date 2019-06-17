from flask_restful import Resource

from aoe2stats import cheats

class ResetResource(Resource):
    def get(self):
        cheats.game = None