import random

from flask_restful import Resource

start = .7
end = .74


class GameResourceDebug(Resource):
    def get(self):
        return {
            "playerStats": {
                "wood": 150.0,
                "food": 4100.0,
                "stone": 200.0,
                "gold": 100.0,
                "pop": 5.0,
                "popMax": 200.0,
                "popFree": 3.0,
                "unitsCreating": 1.0,
                "unitsQueued": 1.0
            },
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
