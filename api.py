#imports
from websocket_server import WebsocketServer
from flask import Flask, request, json
from flask_cors import CORS, cross_origin
import manager

#flask init
app = Flask(__name__)
cors = CORS(app, resources={"*": {"origins": "*"}})

############################
# --- flask routes ---

#run websocket module
@cross_origin
@app.route('/runApp')
def run():
    server.run_forever()

@cross_origin
@app.route('/createGame')
def createGame():
    return manager.createGame()

@cross_origin
@app.route('/getAll')
def getAll():
    return manager.getAll()

@cross_origin
@app.route('/getGame')
def getGame():
    id = request.args.get("id")
    return manager.getGame(id)

@cross_origin
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

    #get response to json
    response_json = json.loads(message)

    #set values to variables
    mess = response_json['mess']
    gameid = response_json['gameid']
    userid = response_json['userid']
    move = response_json['move']

    #check game id
    if gameid == 'undefined':
        return server.send_message(client, 'nogameid')

    #check user is that game player
    if userid not in manager.getGame(gameid).players:
        return server.send_message(client, 'http403')

    #join client ws handler to game sessions
    if client['handler'] not in manager.getGame(gameid).sessions:
        manager.getGame(gameid).sessions.append(client['handler'])

    #check peoples in game session
    if len(manager.getGame(gameid).sessions)<2:
        return server.send_message(client, 'single')

    manager.getGame(gameid).checkSiteCorrect(userid, move)

    #send mess to all players in game session
    for player in manager.getGame(gameid).sessions:
        act_client = server.handler_to_client(player)
        server.send_message(act_client, move)

#############################
# --- websocket config ---
PORT=9001
server = WebsocketServer(PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)

#run app
app.run()