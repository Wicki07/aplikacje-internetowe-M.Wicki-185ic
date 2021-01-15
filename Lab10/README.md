# aplikacje-internetowe-Wicki-185IC

### Autor: Mateusz Wicki Grupa: 185IC_B1
 
# Lab10 


### Główny wygląd strony

![](https://github.com/Wicki07/aplikacje-internetowe-M.Wicki-185ic/blob/master/Lab10/zrzuty/1.PNG?raw=true)

![](https://github.com/Wicki07/aplikacje-internetowe-M.Wicki-185ic/blob/master/Lab10/zrzuty/2.PNG?raw=true)

![](https://github.com/Wicki07/aplikacje-internetowe-M.Wicki-185ic/blob/master/Lab10/zrzuty/3.PNG?raw=true)

![](https://github.com/Wicki07/aplikacje-internetowe-M.Wicki-185ic/blob/master/Lab10/zrzuty/4.PNG?raw=true)

![](https://github.com/Wicki07/aplikacje-internetowe-M.Wicki-185ic/blob/master/Lab10/zrzuty/5.PNG?raw=true)

![](https://github.com/Wicki07/aplikacje-internetowe-M.Wicki-185ic/blob/master/Lab10/zrzuty/6.PNG?raw=true)

Jak widać na zaprezentowanych screenach powyżej elemnty listy `To-do` dodają się prawidłowo oraz prawidło się wyświetlają

Zaczynając od pliku `setting.py` co należało dodać

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',          # należy dodać 
    'rest_framework',         # należy dodać  
    'todo',      # należy dodać 
  ]
  
  MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',      # należy dodać 
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
Należy pamiętać aby linie `'corsheaders.middleware.CorsMiddleware',` umieścić na samej górze aby uniknąć problemów z działaniem

### Uwaga

Zastoswany fragmenty z poradnika:

```python
CORS_ORIGIN_WHITELIST = (
     'http://localhost:3000/'
 )
```

Od wersji Django 3.0.0 przyjmuje inny format a dokładniej: 

```python
CORS_ORIGIN_WHITELIST = (
     'http://example.com'
 )
```

Lub

```python
CORS_ORIGIN_WHITELIST = (
     'example.com'
 )
```

Więc aby wykonać polecenie należy albo zaistalować starszą wersję `Django` albo zastosować pewną modyfikację w pliku `models.py`

```python
from django.db import models


class Todo(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  completed = models.BooleanField(default=False)

  def _str_(self):
    return self.title
    assert errors[0].msg.startswith("CORS_ORIGIN_ALLOW_ALL should be") # to należy dodać
```

Oczywiście tworzymy również plik `serializers.py` oraz `views.py` w celu wyświetlania/zwracania obiektów oraz pracy z nimi.

```python
#serializers.py

from rest_framework import serializers
from .models import Todo
      
class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = ('id', 'title', 'description', 'completed')
```

```python
#views.py

from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import TodoSerializer      
from .models import Todo                 

class TodoView(viewsets.ModelViewSet):      
  serializer_class = TodoSerializer         
  queryset = Todo.objects.all()     
```

Jeśli wszystko zostało prawidłowo skonfigurowane możemy uruchomić serwer otrzymamy wtedy widok znany z poprzednich laborek czy wygląd z pakietu `rest_framework`

Należy również pamiętać o instalacji owych pakietów przy pomocy poleceń

```
pip install django-cors-headers
```

Oraz

```
pip install djangorestframework
```

## Tworznie Frontendu przy pomocy React

Zaczynamy od stworzenia nowej aplikacji przy pomocy poleceń

```
npm install -g create-react-app
```
Oraz
```
create-react-app frontend
```

Dla efektowniejszego formatowania dodajemy `bootstrapa` przy pomocy polecenia

```
npm add bootstrap reactstrap
```

Duże zmiany można dostrzec w pliku `index.js`

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css';   
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(<App />, document.getElementById('root'));

serviceWorker.unregister();
```

Aby aplikacja działa szybciej można zmienić `serviceWorker.unregister();` na `serviceWorker.register();` jednak może to wywołać kilka nieoczekiwanych problemów.

Dodatkowo należy załączyć plik `serviceWorker.js` nie zawraty w poradniki. Jego zawartość prezentuje się następująco

```javascript
// This optional code is used to register a service worker.
// register() is not called by default.

// This lets the app load faster on subsequent visits in production, and gives
// it offline capabilities. However, it also means that developers (and users)
// will only see deployed updates on subsequent visits to a page, after all the
// existing tabs open on the page have been closed, since previously cached
// resources are updated in the background.

// To learn more about the benefits of this model and instructions on how to
// opt-in, read http://bit.ly/CRA-PWA

const isLocalhost = Boolean(
  window.location.hostname === 'localhost' ||
    // [::1] is the IPv6 localhost address.
    window.location.hostname === '[::1]' ||
    // 127.0.0.1/8 is considered localhost for IPv4.
    window.location.hostname.match(
      /^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/
    )
);

export function register(config) {
  if (process.env.NODE_ENV === 'production' && 'serviceWorker' in navigator) {
    // The URL constructor is available in all browsers that support SW.
    const publicUrl = new URL(process.env.PUBLIC_URL, window.location.href);
    if (publicUrl.origin !== window.location.origin) {
      // Our service worker won't work if PUBLIC_URL is on a different origin
      // from what our page is served on. This might happen if a CDN is used to
      // serve assets; see https://github.com/facebook/create-react-app/issues/2374
      return;
    }

    window.addEventListener('load', () => {
      const swUrl = `${process.env.PUBLIC_URL}/service-worker.js`;

      if (isLocalhost) {
        // This is running on localhost. Let's check if a service worker still exists or not.
        checkValidServiceWorker(swUrl, config);

        // Add some additional logging to localhost, pointing developers to the
        // service worker/PWA documentation.
        navigator.serviceWorker.ready.then(() => {
          console.log(
            'This web app is being served cache-first by a service ' +
              'worker. To learn more, visit http://bit.ly/CRA-PWA'
          );
        });
      } else {
        // Is not localhost. Just register service worker
        registerValidSW(swUrl, config);
      }
    });
  }
}

function registerValidSW(swUrl, config) {
  navigator.serviceWorker
    .register(swUrl)
    .then(registration => {
      registration.onupdatefound = () => {
        const installingWorker = registration.installing;
        if (installingWorker == null) {
          return;
        }
        installingWorker.onstatechange = () => {
          if (installingWorker.state === 'installed') {
            if (navigator.serviceWorker.controller) {
              // At this point, the updated precached content has been fetched,
              // but the previous service worker will still serve the older
              // content until all client tabs are closed.
              console.log(
                'New content is available and will be used when all ' +
                  'tabs for this page are closed. See http://bit.ly/CRA-PWA.'
              );

              // Execute callback
              if (config && config.onUpdate) {
                config.onUpdate(registration);
              }
            } else {
              // At this point, everything has been precached.
              // It's the perfect time to display a
              // "Content is cached for offline use." message.
              console.log('Content is cached for offline use.');

              // Execute callback
              if (config && config.onSuccess) {
                config.onSuccess(registration);
              }
            }
          }
        };
      };
    })
    .catch(error => {
      console.error('Error during service worker registration:', error);
    });
}

function checkValidServiceWorker(swUrl, config) {
  // Check if the service worker can be found. If it can't reload the page.
  fetch(swUrl)
    .then(response => {
      // Ensure service worker exists, and that we really are getting a JS file.
      const contentType = response.headers.get('content-type');
      if (
        response.status === 404 ||
        (contentType != null && contentType.indexOf('javascript') === -1)
      ) {
        // No service worker found. Probably a different app. Reload the page.
        navigator.serviceWorker.ready.then(registration => {
          registration.unregister().then(() => {
            window.location.reload();
          });
        });
      } else {
        // Service worker found. Proceed as normal.
        registerValidSW(swUrl, config);
      }
    })
    .catch(() => {
      console.log(
        'No internet connection found. App is running in offline mode.'
      );
    });
}

export function unregister() {
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.ready.then(registration => {
      registration.unregister();
    });
  }
}

```

Po przejściu przez cały poradnik ostateczny wygląd `App.js`

```javascript

 import React, { Component } from "react";
 import Modal from "./components/Modal";
 import axios from "axios";

 class App extends Component {
   constructor(props) {
     super(props);
     this.state = {
       viewCompleted: false,
       activeItem: {
         title: "",
         description: "",
         completed: false
       },
       todoList: []
     };
   }
   componentDidMount() {
     this.refreshList();
   }
   refreshList = () => {
     axios
       .get("http://localhost:8000/api/todos/")
       .then(res => this.setState({ todoList: res.data }))
       .catch(err => console.log(err));
   };
   displayCompleted = status => {
     if (status) {
       return this.setState({ viewCompleted: true });
     }
     return this.setState({ viewCompleted: false });
   };
   renderTabList = () => {
     return (
       <div className="my-5 tab-list">
         <span
           onClick={() => this.displayCompleted(true)}
           className={this.state.viewCompleted ? "active" : ""}
         >
           complete
         </span>
         <span
           onClick={() => this.displayCompleted(false)}
           className={this.state.viewCompleted ? "" : "active"}
         >
           Incomplete
         </span>
       </div>
     );
   };
   renderItems = () => {
     const { viewCompleted } = this.state;
     const newItems = this.state.todoList.filter(
       item => item.completed === viewCompleted
     );
     return newItems.map(item => (
       <li
         key={item.id}
         className="list-group-item d-flex justify-content-between align-items-center"
       >
         <span
           className={`todo-title mr-2 ${
             this.state.viewCompleted ? "completed-todo" : ""
           }`}
           title={item.description}
         >
           {item.title}
         </span>
         <span>
           <button
             onClick={() => this.editItem(item)}
             className="btn btn-secondary mr-2"
           >
             {" "}
             Edit{" "}
           </button>
           <button
             onClick={() => this.handleDelete(item)}
             className="btn btn-danger"
           >
             Delete{" "}
           </button>
         </span>
       </li>
     ));
   };
   toggle = () => {
     this.setState({ modal: !this.state.modal });
   };
   handleSubmit = item => {
     this.toggle();
     if (item.id) {
       axios
         .put(`http://localhost:8000/api/todos/${item.id}/`, item)
         .then(res => this.refreshList());
       return;
     }
     axios
       .post("http://localhost:8000/api/todos/", item)
       .then(res => this.refreshList());
   };
   handleDelete = item => {
     axios
       .delete(`http://localhost:8000/api/todos/${item.id}`)
       .then(res => this.refreshList());
   };
   createItem = () => {
     const item = { title: "", description: "", completed: false };
     this.setState({ activeItem: item, modal: !this.state.modal });
   };
   editItem = item => {
     this.setState({ activeItem: item, modal: !this.state.modal });
   };
   render() {
     return (
       <main className="content">
         <h1 className="text-white text-uppercase text-center my-4">Todo app</h1>
         <div className="row ">
           <div className="col-md-6 col-sm-10 mx-auto p-0">
             <div className="card p-3">
               <div className="">
                 <button onClick={this.createItem} className="btn btn-primary">
                   Add task
                 </button>
               </div>
               {this.renderTabList()}
               <ul className="list-group list-group-flush">
                 {this.renderItems()}
               </ul>
             </div>
           </div>
         </div>
         {this.state.modal ? (
           <Modal
             activeItem={this.state.activeItem}
             toggle={this.toggle}
             onSave={this.handleSubmit}
           />
         ) : null}
       </main>
     );
   }
 }
 export default App;
```

Oraz pliku `Modal.js`

```javascript
import React, { Component } from "react";
    import {
      Button,
      Modal,
      ModalHeader,
      ModalBody,
      ModalFooter,
      Form,
      FormGroup,
      Input,
      Label
    } from "reactstrap";

    export default class CustomModal extends Component {
      constructor(props) {
        super(props);
        this.state = {
          activeItem: this.props.activeItem
        };
      }
      handleChange = e => {
        let { name, value } = e.target;
        if (e.target.type === "checkbox") {
          value = e.target.checked;
        }
        const activeItem = { ...this.state.activeItem, [name]: value };
        this.setState({ activeItem });
      };
      render() {
        const { toggle, onSave } = this.props;
        return (
          <Modal isOpen={true} toggle={toggle}>
            <ModalHeader toggle={toggle}> Todo Item </ModalHeader>
            <ModalBody>
              <Form>
                <FormGroup>
                  <Label for="title">Title</Label>
                  <Input
                    type="text"
                    name="title"
                    value={this.state.activeItem.title}
                    onChange={this.handleChange}
                    placeholder="Enter Todo Title"
                  />
                </FormGroup>
                <FormGroup>
                  <Label for="description">Description</Label>
                  <Input
                    type="text"
                    name="description"
                    value={this.state.activeItem.description}
                    onChange={this.handleChange}
                    placeholder="Enter Todo description"
                  />
                </FormGroup>
                <FormGroup check>
                  <Label for="completed">
                    <Input
                      type="checkbox"
                      name="completed"
                      checked={this.state.activeItem.completed}
                      onChange={this.handleChange}
                    />
                    Completed
                  </Label>
                </FormGroup>
              </Form>
            </ModalBody>
            <ModalFooter>
              <Button color="success" onClick={() => onSave(this.state.activeItem)}>
                Save
              </Button>
            </ModalFooter>
          </Modal>
        );
      }
    }
```

### Uwaga

Ponownie jeżeli chcemy uniknąć błędu który pojawia się przy próbie łącznie Reacta z Django i który bolkuje przesył inforamci między nimi

```error
Access to XMLHttpRequest at 'http://localhost:8000/api/todos/' from origin 'http://localhost:3000' has been blocked by CORS policy: Response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present on the requested resource.
```
Należy zainstalować następujące roszerzenie do przeglądarki google chrome: [Moesif Origin & CORS Changer](https://chrome.google.com/webstore/detail/moesif-origin-cors-change/digfbfaphojjndkpccljibejjbppifbc?hl=en-US)
