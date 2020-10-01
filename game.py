import uuid
import json

class Game:
    def __init__(self):
        self.uuid = str(uuid.uuid1())
        self.players = []
        self.sessions = []
        self.table = [
            [2, 3, 4, 5, 6, 4, 3, 2],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [7, 7, 7, 7, 7, 7, 7, 7],
            [8, 9, 10, 11, 12, 10, 9, 8],
        ]

    def join(self, uuid):
        playersSize = len(self.players)
        if playersSize<2:
            self.players.append(uuid)
            return json.dumps({'status':'success'})
        return json.dumps({'status':'failure'})

    def checkSiteCorrect(self, userid, move):
        fx = int(move[3])
        fy = int(move[1])
        tx = int(move[8])
        ty = int(move[6])
        print(self.table[fx][fy])