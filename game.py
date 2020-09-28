import uuid

class Game:
    def __init__(self):
        self.uuid = uuid.uuid1()
        self.players = []
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
        if len(self.players) == 1:
            self.players.append(uuid)
            return 'success'
        else: return 'fail'