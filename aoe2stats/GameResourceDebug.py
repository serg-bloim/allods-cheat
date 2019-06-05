import random

from flask_restful import Resource

start = .7
end = .74


class GameResourceDebug(Resource):
    def get(self):
        return {
                    "playerStats": {
                        "wood": 700.0,
                        "food": 850.0,
                        "stone": 700.0,
                        "gold": 700.0,
                        "pop": 4.0,
                        "popMax": 200.0,
                        "popFree": 1.0,
                        "unitsCreating": 1.0,
                        "unitsQueued": 3.0
                    },
                    "tcs": [
                        {
                            "addr": "0xfadea20",
                            "type": 109,
                            "typeName": "TC",
                            "health": 2400.0,
                            "queue": [
                                {
                                    "type": 83,
                                    "progress": 0,
                                    "remainingTime": 0,
                                    "iconId": 15,
                                    "kind": 1
                                },
                                {
                                    "type": 83,
                                    "progress": 0,
                                    "remainingTime": 0,
                                    "iconId": 15,
                                    "kind": 1
                                },
                                {
                                    "type": 83,
                                    "progress": 0,
                                    "remainingTime": 0,
                                    "iconId": 15,
                                    "kind": 1
                                }
                            ],
                            "prodProgress": 0.6148809814453124,
                            "prodRemaining": 9.627975463867188,
                            "techInProd": {
                                "type": -1,
                                "progress": 0,
                                "remainingTime": 0,
                                "iconId": -1,
                                "kind": 3
                            }
                        }
                    ]
                }

