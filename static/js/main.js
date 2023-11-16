document.addEventListener('DOMContentLoaded', function() {
    let socket = new WebSocket(`ws://127.0.0.1:8000/ws/?token=${authToken}`);
    socket.onmessage = function (event) {
        let data = JSON.parse(event.data);
        console.log(data)
        addMessage(data.text, 'you')
  };
}, false);


function addMessage(value, author) {
    currentChatElement = document.getElementById("current__chat")
    if (currentChatElement === null) {
        return
    }
    activeChat = document.getElementById("active__chat")
    // if activeChat.
    const newDiv = document.createElement("div");
    newDiv.classList.add('bubble')
    newDiv.classList.add(author)
    newDiv.innerText = value
    currentChatElement.appendChild(newDiv)
}

function clearInputField(message_tag) {
    message_tag.value = ""
}


function submitSend() {
    let message_tag = document.getElementById("message")
    if (message_tag.value.trim() === "") {
        return false
    } else {
        const urlParams = new URLSearchParams(window.location.search);
        const chat = urlParams.get('chat');
        fetch(`/v1/chats/messages/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({'text': message_tag.value, 'chat': chat})
        })
            .then(response => {
                addMessage(message_tag.value, 'me')
                clearInputField(message_tag)
            })
            .catch(error => {
                console.log(error)
        });
    }
}
