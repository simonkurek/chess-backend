#imports
from websocket_server import WebsocketServer
from flask import Flask, request
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
    server.send_message_to_all(message)

#############################
# --- websocket config ---
PORT=9001
server = WebsocketServer(PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)

#run app
app.run()
