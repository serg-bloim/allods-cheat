from flask_restful import Resource
from flask import request

from aoe2stats import cheats

class ResetResource(Resource):
    def get(self):
        cheats.proc_name = request.args['proc_name']
        cheats.game = None