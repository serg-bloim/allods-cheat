from flask_restful import Resource

import cheats

class ResetResource(Resource):
    def get(self):
        cheats.game = None