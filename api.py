#imports
from websocket_server import WebsocketServer
from flask import Flask, request, json
import manager

#flask init
app = Flask(__name__)

############################
# --- flask routes ---

#run websocket module
@app.route('/runApp')
def run():
    server.run_forever()

@app.route('/createGame')
def createGame():
    return manager.createGame()

@app.route('/getAll')
def getAll():
    return manager.getAll()

@app.route('/getGame')
def getGame():
    id = request.args.get("id")
    return manager.getGame(id)

@app.route('/joinGame')
def joinGame():
    gameID = request.args.get('gameid')
    userID = request.args.get('userid')
    return manager.joinGame(gameID, userID)

###########################
# --- websockets events --- 

#new client in session
def new_client(client, server):
	print('New client connected and was given id %d' % client['id'])

#client left session
def client_left(client, server):
	print('Client(%d) disconnected' % client['id'])

#client send message
def message_received(client, server, message):
    response_json = json.loads(message)
    mess = response_json['mess']
    gameid = response_json['gameid']
    userid = response_json['userid']
    if gameid == 'undefined':
        return server.send_message(client, 'nogameid')
    game = manager.getGame(gameid)
    if userid not in game.players:
        return server.send_message(client, 'http403')
    if client not in game.sessions:
        game.sessions.append(client)
    if len(game.sessions)<2:
        return server.send_message(client, 'single')
    #somefunc(mess)
    i = 0
    for player in game.players:
        if player is not userid:
            return server.send_message(game.sessions[i], mess)
        i += 1

#############################
# --- websocket config ---
PORT=9001
server = WebsocketServer(PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)

#run app
app.run()