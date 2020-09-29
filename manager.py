import game

gameList = []

def createGame():
    newGame = game.Game()
    gameList.append(newGame)
    return str(newGame.uuid)

def getAll():
    return gameList

def getGame(id):
    for i in gameList:
        if id == i.uuid:
            return i

def joinGame(gameID, userID):
    return getGame(gameID).join(userID)