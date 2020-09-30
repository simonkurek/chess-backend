//server config
const PROTOCOL = 'http'
const IP = 'localhost'
const PORT = 5000
const SRV = PROTOCOL + '://' + IP + ':' + PORT

//client variables
let my_uuid
let game_id

const connection = () => {
    //create websocket connection
    ws = new WebSocket('ws://' + IP + ':9001') 

    //on message event
    ws.onmessage = (event) => { 
        console.log(event.data)
    } 

    //on open event
    ws.onopen = () => {
        console.log('open')
    } 

    //on close event
    ws.onclose = () => {
        console.log('close')
    }

    //on error event
    ws.onerror = () => {
        console.log('error')
    }
}

const sendMess = (mess) => {
    const json = `{
        "userid":"${my_uuid}",
        "gameid":"${game_id}",
        "mess":"${mess}"
    }`
    ws.send(json)
}

const cls = () => {
    console.clear()
}

const setGameID = (gameid) => {
    game_id = gameid
}

const getID = () => {
    let dt = new Date().getTime()
    let uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (dt + Math.random()*16)%16 | 0
        dt = Math.floor(dt/16)
        return (c=='x' ? r :(r&0x3|0x8)).toString(16)
    });
    return uuid
}

const createGame = () => {
    fetch(SRV + '/createGame')
    .then(resp => resp.json())
    .then(resp => {
        game_id = resp.uuid
        console.log(resp)
        joinGame()
    })
}

const joinGame = () => {
    fetch(SRV + '/joinGame?gameid=' + game_id + '&userid=' + my_uuid)
    .then(resp => resp.json())
    .then(resp => {
        if(resp.status != 'success') console.error('join game failure')
    })
}

window.onload = () => {
    my_uuid = getID()
    cls()
}

// on start page:
// 1. create connection by "connection()" in console
// 2. create game by /createGame
// 3. second player /joingame?gameid=jd&userid=jd
// 4. go "sendMess('jd')" to send mess jd with your id and gameid to server
