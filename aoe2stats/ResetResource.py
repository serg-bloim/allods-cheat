from flask_restful import Resource

import aoe2stats.cheats

class ResetResource(Resource):
    def get(self):
        cheats.game = None