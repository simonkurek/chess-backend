window.onload = () => {
    //create websocket connection
    ws = new WebSocket('ws://localhost:9001') 

    //on message event
    ws.onmessage = (event) => {
        console.log('message received') 
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
    ws.send(mess)
}

const cls = () => {
    console.clear()
}