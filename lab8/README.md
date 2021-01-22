# aplikacje-internetowe-Wicki-185IC

### Autor: Mateusz Wicki Grupa: 185IC_B1
 
# Lab 8 Czat z użyciem Web Socket + Web Workers

### Realizacja kodu z preozytorium

![](https://i.imgur.com/uC5wq33.png)

![](https://i.imgur.com/KiFoxtP.png)

Do realizajci należy w stworzonej aplikacji wprowadzić poniższy kod:

Plik `chat/views.py`

```python
from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

```

Plik `urls.py` 

```python
from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
]
```

Plik `chat/urls.py` 

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]

```

Należało również utworzyć plik  `routing.py` 

```python
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
```

Oraz plik  `consumer.py` 

```python
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
```
Wygląd plików `index.html` oraz `room.html`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>Chat Rooms</title>
</head>
<body>
    What chat room would you like to enter?<br>
    <input id="room-name-input" type="text" size="100"><br>
    <input id="room-name-submit" type="button" value="Enter">

    <script>
        document.querySelector('#room-name-input').focus();
        document.querySelector('#room-name-input').onkeyup = function(e) {
            if (e.keyCode === 13) { 
                document.querySelector('#room-name-submit').click();
            }
        };

        document.querySelector('#room-name-submit').onclick = function(e) {
            var roomName = document.querySelector('#room-name-input').value;
            window.location.pathname = '/chat/' + roomName + '/';
        };
    </script>
</body>
</html>
```

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>Chat Room</title>
</head>
<body>
    <textarea id="chat-log" cols="100" rows="20"></textarea><br>
    <input id="chat-message-input" type="text" size="100"><br>
    <input id="chat-message-submit" type="button" value="Send">
    {{ room_name|json_script:"room-name" }}
    <script>
        const roomName = JSON.parse(document.getElementById('room-name').textContent);

        const chatSocket = new WebSocket(
            'ws://'
            + window.location.host
            + '/ws/chat/'
            + roomName
            + '/'
        );

        chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);
            document.querySelector('#chat-log').value += (data.message + '\n');
        };

        chatSocket.onclose = function(e) {
            console.error('Chat socket closed unexpectedly');
        };

        document.querySelector('#chat-message-input').focus();
        document.querySelector('#chat-message-input').onkeyup = function(e) {
            if (e.keyCode === 13) { 
                document.querySelector('#chat-message-submit').click();
            }
        };

        document.querySelector('#chat-message-submit').onclick = function(e) {
            const messageInputDom = document.querySelector('#chat-message-input');
            const message = messageInputDom.value;
            chatSocket.send(JSON.stringify({
                'message': message
            }));
            messageInputDom.value = '';
        };
    </script>
</body>
</html>

```
## Chat przy użyciu socket.io

Należy pamiętać aby najpierw zainstalować `Node.js`

W pierwszej kolejności tworzymy plik `package.json`, który opisuje nasz projekt

```json
{
  "name": "socket-chat-example",
  "version": "0.0.1",
  "description": "my first socket.io app",
  "dependencies": {}
}
```

Instalujemy pakiet `express` przy pomocy polecenia

```
npm install express@4
```

Tworzymy plik `index.js`

```javascript
const app = require('express')();
const http = require('http').createServer(app);

app.get('/', (req, res) => {
  res.send('<h1>Hello world</h1>');
});

http.listen(3000, () => {
  console.log('listening on *:3000');
});
```

Po uruchomieniu przy pomocy polecenia `node index.js` otrzymujemy następujacy widok

![](https://i.imgur.com/BqDFYFS.png)

Widok konsoli

![](https://i.imgur.com/2hQNM1k.png)

Jeżeli chcempy pracować z socke.io należy go zainstalować poleceniem

```
npm install socket.io

```

```javascript
const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', (socket) => {
  console.log('a user connected');
});

http.listen(3000, () => {
  console.log('listening on *:3000');
});
```
Po przeanalizowaniu powyższego kodu można dostrzec że io jest instancją socket.io która nasłuchuje zdarzenia `connection`. Po nawiązaniu połączenia w consoli pojawi się komunikat że użytkownik dołączył

![](https://i.imgur.com/wjZWoEL.png)

Elemnt jaki otrzymuje `io.on` to socket może on otrzymywać pewne parametry wtedy wywołuje odpowiedną funkcję przy pomocy atrybutu `on`. Może również wysyłać pewne zgłoszenia przy pomocy atrybutu `emit`. Dzięki połączeniu ze stroną przy pomocy 

```html
<script src="/socket.io/socket.io.js"></script>
<script>
  var socket = io();
</script>
```

Można łatwo łączyć się z serwerem

Sam `socekt.io` nie wymaga wielu funkcji więcej zależy od tago jak zostanie to wykorzystane na stronie przy pomocy odpowiednich skryptów.

Poniżej utworzony przeze mnie plik `index.js`

```javascript
const express = require('express');
const app = require('express')();
const path = require('path');
const http = require('http').Server(app);
const io = require('socket.io')(http);

//dodanie plików razem ze staticami
app.use(express.static(path.join(__dirname, '/')));


io.on('connection', (socket) => {
    let addedUser = false;
  
    // Tworznie nowej wiadomości
    socket.on('chat message', (data) => {
      socket.broadcast.emit('chat message', {
        username: socket.username,
        message: data
      });
    });
  
    // Tworznie nowego użytkownika
    socket.on('add user', (username) => {
      if (addedUser) return;
  
      // Przypisanie podanej nazwy do secket
      socket.username = username;
      addedUser = true;
      socket.emit('login');
    });
  
    // Wyświetlanie inforamicji o tym czy kotś pisze
    socket.on('typing', () => {
      socket.broadcast.emit('typing', {
        username: socket.username
      });
    });
  
    // Zakonczenie wyświetlania "pisze"
    socket.on('stop typing', () => {
      socket.broadcast.emit('stop typing', {
        username: socket.username
      });
    });
  });
  

http.listen(3000, () => {
  console.log('listening on *:3000');
});
```

Większy problem sprawiło odpowiednie skonfikgurowanie `jQuery` na stronie

```javascript
$(function() {

  const $window = $(window);
  const $usernameInput = $('.usernameInput'); 
  const $messages = $('.messages');           
  const $inputMessage = $('.inputMessage');  
  const $loginPage = $('.login.page');        
  const $chatPage = $('.chat.page');     

  const socket = io();

  let username;
  let connected = false;
  let typing = false;


  // Ustawienie nazwy użytkownika
  const setUsername = () => {
    username = $usernameInput.val().trim();
    console.log(username)
    if (username) {
      $loginPage.hide();
      $chatPage.show();
      $currentInput = $inputMessage.focus();

      // Wysłanie informacji do servera przy pomocy socketa
      socket.emit('add user', username);
    }
  }

  // Wysyłanie wiadomości
  const sendMessage = () => {
    let message = $inputMessage.val().trim();
    if (message && connected) {
      $inputMessage.val('');
      addChatMessage({ username, message });
      // Wysłanie informacji do servera przy pomocy socketa uruchomienie funkcji chat message
      socket.emit('chat message', message);
    }
  }

  // Wyśietlanie wiadmości
  const addChatMessage = (data, options) => {
    
    if (!options) {
      options = {};
    }
    const $usernameDiv = $('<span class="username"/>')
      .text(data.username)
    const $messageBodyDiv = $('<span class="messageBody">')
      .text(data.message);

    const typingClass = data.typing ? 'typing' : '';
    const $messageDiv = $('<li class="message"/>')
      .data('username', data.username)
      .addClass(typingClass)
      .append($usernameDiv, $messageBodyDiv);

    addMessageElement($messageDiv, options);
  }

  // Wyświetlenie wiadmoci "pisze"
  const addChatTyping = (data) => {
    data.typing = true;
    data.message = 'pisze';
    addChatMessage(data);
  }

  // Usuwanie wiadmości "pisze"
  const removeChatTyping = (data) => {
    getTypingMessages(data).fadeOut(function () {
      $(this).remove();
    });
  }

  // Dodawanie wiadomości na strone
  const addMessageElement = (el, options) => {
    const $el = $(el);
    if (!options) {
      options = {};
    }
    if (typeof options.prepend === 'undefined') {
      options.prepend = false;
    }
    if (options.prepend) {
      $messages.prepend($el);
    } else {
      $messages.append($el);
    }

    $messages[0].scrollTop = $messages[0].scrollHeight;
  }


  // Ustawienie wiadmości "pisze"
  const updateTyping = () => {
    if (connected) {
      if (!typing) {
        typing = true;
        socket.emit('typing');
      }
    }
  }

  // Pobranie nazwy użytkownika który aktualnie pisze
  const getTypingMessages = (data) => {
    return $('.typing.message').filter(function (i) {
      return $(this).data('username') === data.username;
    });
  }

  $window.keydown(event => {

    // Wysyłąnie przy pomocy entera
    if (event.which === 13) {
      if (username) {
        sendMessage();
        socket.emit('stop typing');
        typing = false;
      } else {
        setUsername();
      }
    }
  });

  $inputMessage.on('input', () => {
    updateTyping();
  });


  // Wywołania odpowiednich fukcji socketa
  socket.on('login', (data) => {
    connected = true;
  });

  socket.on('chat message', (data) => {
    addChatMessage(data);
  });

  socket.on('typing', (data) => {
    addChatTyping(data);
  });

  socket.on('stop typing', (data) => {
    removeChatTyping(data);
  });

});
```

Ostatecznie strona prezentuje się następująco

![](https://i.imgur.com/UGerqMn.png)

Podajemy różne nazwy użytkownków

![](https://i.imgur.com/AA4LeTl.png)

W momencie w którym jakiś użytkownik zaczyna pisać pozostałym użytkownikom wyświetla się komunikat o tym

![](https://i.imgur.com/Kjj1l4l.png)

![](https://i.imgur.com/h5ASl5P.png)

Po wysłaniu wiadomości pojawia się ona w odpowiednim sektorze i znika informacja, że któryś z użytkowników aktualnie coś pisze

## WebWorkers

Worker liczący ciąg Fibonacziego

![](https://i.imgur.com/SJSKTKz.png)

Należało zastosować poniższe skrypty

```html
<script id="fibonacci" type="javascript/worker">
    self.onmessage = function(e) {
    let userNum = Number(e.data);
    fibonacci(userNum);
    }


    function fibonacci(num){
        let arr =[];
        let a = 1, b = 0, temp;
        while (num >= 0){
            temp = a;
            a = a + b;
            b = temp;
            arr.push(a)
            num--;
        }

        self.postMessage(arr);
        }
</script>
<script>
    var blob = new Blob([document.querySelector('#fibonacci').textContent]);
    blobURL = window.URL.createObjectURL(blob);
    var form = document.querySelector('form');
    var input = document.querySelector('input[type="number"]');
    var result = document.querySelector('p#result');
    var worker = new Worker(blobURL);

    worker.onmessage = function(event) {
      result.textContent = event.data;
    };

    form.onsubmit = function(e) {
      e.preventDefault();
      worker.postMessage(input.value);
      input.value = '';
    }
 
</script>
```
Worker przyjmuje jako parametr plik js np:
```
    var worker = new Worker('worker.js');
```

Jednak przy tworzeniu workera na naszynie wirualnej pojawia się problem że worker nie importuje pliku więc można to ominąć przekazując skrypt ze strony w następujący sposób

```html
    var blob = new Blob([document.querySelector('#fibonacci').textContent]);
    blobURL = window.URL.createObjectURL(blob);
    var worker = new Worker(blobURL);
```
Tworzymy obiekt Blob następnie tworzymy url do nie i następnie tak stworzony url przekazujemy workerowi

Pojawił się również prolem przy tworzeniu workera bez uruchomionego serwera. Przegladarka Google Chrom wyświetlałą błąd zabezpieczeń.

Worker liczący silnie

![](https://i.imgur.com/Wnavh7m.png)
![](https://i.imgur.com/fWGiZM5.png)

Skrypt workera

```html
<script id="factorial" type="javascript/worker">
  var factorial
    self.onmessage = function(e) {
    let userNum = Number(e.data);
    factorial(userNum);
    }


    function factorial(num){
        let temp;
        factorial = num;
        console.log(factorial)
        while (num > 1){
            num--;
            factorial *= num;
        }
        console.log(factorial)
        self.postMessage(factorial);
        }
</script>
<script>
    var blob = new Blob([document.querySelector('#factorial').textContent]);
    blobURL = window.URL.createObjectURL(blob);
    var form = document.querySelector('form');
    var input = document.querySelector('input[type="number"]');
    var result = document.querySelector('p#result');
    var worker = new Worker(blobURL);

    worker.onmessage = function(event) {
      result.textContent = event.data;
    };

    form.onsubmit = function(e) {
      e.preventDefault();
      worker.postMessage(input.value);
      input.value = '';
    }
 
</script>
```
