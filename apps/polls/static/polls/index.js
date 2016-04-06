var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
var socket = new WebSocket(ws_scheme + '://' + window.location.host + "/polls" + window.location.pathname);


function send_msg() {
    socket.send(JSON.stringify('hello ASGI!'));
    return false;
}

function send_http(url) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            console.log(xmlHttp.responseText);
    }
    xmlHttp.open("GET", url, true);
    xmlHttp.send(null);
}

socket.onmessage = function(message) {
    var data = JSON.parse(message.data);
    console.log(data);
};
