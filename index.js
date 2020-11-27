//fichier serveur 
const express = require("express"); //server
const { listen } = require("socket.io");
const socket = require("socket.io");
const listUsers = new Set();
//server setup
const PORT = 5000;
const app = express();
const server = app.listen(PORT, function() {
    console.log(`http://localhost:${PORT}`);
});
app.use(express.static('client'));
// socket setup 

const io = socket(server);
// creer la connexion
io.on("connection", function(socket) {
    console.log("User connected");
    socket.on("newUser", function(data) {
        socket.userId = data; //user id = id unique d'un client
        listUsers.add(data);
        io.emit("newUser", [...listUsers]);
    });

    socket.on("disconnect", () => {
        listUsers.delete(socket.userId);
        io.emit("userDisconnect", socket.userId);
    });
    socket.on("chatMessage", function(data) {
        io.emit("chatMessage", data);
    });

    socket.on("typing", function(data) {
        //envoie à tt le monde sauf l'envoyeur
        socket.broadcast.emit("typing", data);
    });
});