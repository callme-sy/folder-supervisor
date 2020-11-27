const socket = io();
const divUsers = document.querySelector(".div_users");
let userName = "";

const newUser = function(user) {
    userName = user || prompt("Entrez votre nom:", "user");
    `User${Math.floor(Math.random()*10000)}`;
    socket.emit("newUser", userName);
    addUserDiv(userName);
}

const addUserDiv = function(userName) {
    if (document.querySelector(`.${userName}-UserList`)) {
        return;
    }
    const addUser = `
    <div class="${userName}-UserList">
        <h5>${userName}</h5>
    </div>`;

    divUsers.innerHTML += addUser;
}

messageForm = document.querySelector(".form_message");
inputFormMessage = document.querySelector(".input_form_message");
messagesDiv = document.querySelector(".div_messages");
typingDiv = document.querySelector(".div_typing");

inputFormMessage.addEventListener("keyup", () => {
    socket.emit("typing", {
        isTyping: inputFormMessage.value.length > 0,
        user: userName,
    });
});

socket.on("typing", function(data) {
    const { isTyping, user } = data;
    if (!isTyping) {
        typingDiv.innerHTML + "";
        return;
    }

    typingDiv.innerHTML = `<p>${user} is typing...</p>`;
});

//affiche le msg
const addNewMessage = ({ user, message }) => {
    const receivedMessage = `
    <div class="receivedMessage">
        <span class="author">${user}</span>
        <p>${message}</p>
    </div>`;

    const myMessage = `
    <div class="sentMessage">
        <p>${message}</p>
    </div>`;

    messagesDiv.innerHTML += user === userName ? myMessage : receivedMessage;
};

//quand le msg est envoyé
messageForm.addEventListener("submit", (e) => {
    e.preventDefault();

    if (!inputFormMessage.value) {
        return;
    }

    socket.emit("chatMessage", {
        message: inputFormMessage.value,
        user: userName,
    });
    inputFormMessage.value = "";
});

socket.on("chatMessage", function(data) {
    addNewMessage({ user: data.user, message: data.message });
});

socket.on("newUser", function(data) {
    data.map((user) => addUserDiv(user));
});

socket.on("userDisconnect", function(userName) {
    console.log("userDisconnect");
    document.querySelector(`.${userName}-UserList`).remove();
});

newUser();