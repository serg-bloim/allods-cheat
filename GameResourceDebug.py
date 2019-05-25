import random

from flask_restful import Resource

start = .7
end = 1


class GameResourceDebug(Resource):
    def get(self):
        return {
            'tcs': [
                {
                    'prodProgress': random.uniform(start, end),
                    'queue': [83]
                },
                {
                    'prodProgress': random.uniform(start, end),
                    'queue': [83]
                },
                # {
                #     'prodProgress': 0,
                #     'queue': []
                # }
            ]
        }
