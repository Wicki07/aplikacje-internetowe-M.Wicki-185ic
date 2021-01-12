# aplikacje-internetowe-Wicki-185IC

### Autor: Mateusz Wicki Grupa: 185IC_B1
 
# Lab9 Django + React (aplikacja CRUD)


### Główny wygląd strony

![](https://github.com/Wicki07/aplikacje-internetowe-M.Wicki-185ic/blob/master/lab9/zrzuty/1.PNG?raw=true)

### Wygląd strony dodwania

![](https://github.com/Wicki07/aplikacje-internetowe-M.Wicki-185ic/blob/master/lab9/zrzuty/2.PNG?raw=true)

Jak widać elemnt został dodany

![](https://github.com/Wicki07/aplikacje-internetowe-M.Wicki-185ic/blob/master/lab9/zrzuty/3.PNG?raw=true)

W `setting.py` należy wprowadzić następujące zmiany

```javascript
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',      #<-------- Należy dodać
    'tutorials.apps.TutorialsConfig',   #<-------- Należy dodać
    'corsheaders',    #<-------- Należy dodać
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',    #<-------- Należy dodać
    'django.middleware.common.CommonMiddleware',   #<-------- Należy dodać
]

CORS_ORIGIN_ALLOW_ALL = False   #<-------- Należy dodać
CORS_ORIGIN_WHITELIST = (    #<-------- Należy dodać
    'http://localhost:8081',   #<-------- Należy dodać
)
```

Należy również utworzyć plik `models.py`

```javascript
class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)
    data_publikacji = models.DateField(blank=True, default=timezone.now)
```

Oraz `serializers.py`

```javascript
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'data_publikacji',
                  'published')
```

Należy zauważyć że żeby stworzyć poprawnie views należy skorzystać z [poradnka](https://bezkoder.com/django-crud-mysql-rest-framework/), niestety nie wszystko działa poprawianie.

Gotowe `views.py`

```javascript
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tutorials.models import Tutorial
from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try: 
        tutorial = Tutorial.objects.get(pk=pk) 
    except Tutorial.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = TutorialSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = Tutorial.objects.filter(published=True)
        
    if request.method == 'GET': 
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
```

## React-CRUD

Aby połączyć się z stworzoną aplikacją w Django należy stworzyć plik `http-common.js`

```javascript
import axios from "axios";

export default axios.create({
  baseURL: "http://localhost:8080/api",
  headers: {
    "Content-type": "application/json"
  }
});
```

W zaprezentowanym poradniku zabrakło `serviceWorker.js`. Jego kod prezentuje się następująco

```javascript
const isLocalhost = Boolean(
    window.location.hostname === 'localhost' ||
      window.location.hostname === '[::1]' ||
      window.location.hostname.match(
        /^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/
      )
  );
  
  export function register(config) {
    if (process.env.NODE_ENV === 'production' && 'serviceWorker' in navigator) {
      const publicUrl = new URL(process.env.PUBLIC_URL, window.location.href);
      if (publicUrl.origin !== window.location.origin) {
        return;
      }
  
      window.addEventListener('load', () => {
        const swUrl = `${process.env.PUBLIC_URL}/service-worker.js`;
  
        if (isLocalhost) {
          checkValidServiceWorker(swUrl, config);
  
          navigator.serviceWorker.ready.then(() => {
            console.log(
              'This web app is being served cache-first by a service ' +
                'worker. To learn more, visit https://bit.ly/CRA-PWA'
            );
          });
        } else {
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
                console.log(
                  'New content is available and will be used when all ' +
                    'tabs for this page are closed. See https://bit.ly/CRA-PWA.'
                );
  
                if (config && config.onUpdate) {
                  config.onUpdate(registration);
                }
              } else {
                console.log('Content is cached for offline use.');
  
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
    fetch(swUrl, {
      headers: { 'Service-Worker': 'script' }
    })
      .then(response => {
        const contentType = response.headers.get('content-type');
        if (
          response.status === 404 ||
          (contentType != null && contentType.indexOf('javascript') === -1)
        ) {
          navigator.serviceWorker.ready.then(registration => {
            registration.unregister().then(() => {
              window.location.reload();
            });
          });
        } else {
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
      navigator.serviceWorker.ready
        .then(registration => {
          registration.unregister();
        })
        .catch(error => {
          console.error(error.message);
        });
    }
  }
```

Aby dodać brakujące komponenty należy skorzystać z poradnika ze [strony](https://bezkoder.com/react-crud-web-api/)

## Dodane dodatkowo

Pod doadniu panelu Administratora widać zmiany jakie zachodzą można tam również edytować utworzone już tutoriale. Oraz dodałem datę publikacji.

![](https://github.com/Wicki07/aplikacje-internetowe-M.Wicki-185ic/blob/master/lab9/zrzuty/4.PNG?raw=true)

![](https://github.com/Wicki07/aplikacje-internetowe-M.Wicki-185ic/blob/master/lab9/zrzuty/5.PNG?raw=true)

 Zmainy na stronie
 
 ![](https://github.com/Wicki07/aplikacje-internetowe-M.Wicki-185ic/blob/master/lab9/zrzuty/6.PNG?raw=true)
 
 ![](https://github.com/Wicki07/aplikacje-internetowe-M.Wicki-185ic/blob/master/lab9/zrzuty/7.PNG?raw=true)
 
 Wyświetlanie log marek odbywa się automatycznie dzięki zastosowaniu `switch` w react
 
 ```javascript

 
   renderSwitch(param) {
    switch(param) {
      case 'BMW':
        return (<img src={logo1} />);
      case 'Audi':
        return (<img src={logo3} />);;
      case 'Mercedes':
        return (<img src={logo2} />);;
      case 'Skoda':
        return (<img src={logo4} />);;
      default:
        return 'brak zdjecia';
    }
  }
  ...
  //Następnie w kodzie należy wywołać następującą funkcje
  
  {this.renderSwitch(tutorial.marka)}
 ```
 Pod dodaniu nowego modelu należy edytować fukcje które dodają dane do bazy
 Nowy kod strony
 
 ```javascript
  // App.js
 
 class App extends Component {
  render() {
    return (
      <div>
        <img src={tlo} className="mx-auto d-block"/>
        <h1 className="text-center">Ewidencja pojazdów</h1>
        <nav className="navbar navbar-expand navbar-dark bg-dark">
          <a href="/tutorials" className="navbar-brand">
            Mateusz Wicki
          </a>
          <div className="navbar-nav mr-auto">
            <li className="nav-item">
              <Link to={"/tutorials"} className="nav-link">
                Pojazdy
              </Link>
            </li>
            <li className="nav-item">
              <Link to={"/add"} className="nav-link">
                Dodaj
              </Link>
            </li>
          </div>
        </nav>

        <div className="container mt-3 mx-auto">
          <Switch>
            <Route exact path={["/", "/tutorials"]} component={TutorialsList} />
            <Route exact path="/add" component={AddTutorial} />
            <Route path="/tutorials/:id" component={Tutorial} />
          </Switch>
        </div>
      </div>
    );
  }
}
 ```
 
 ```javascript
//pojazdy-list.component.js

import React, { Component } from "react";
import PojazdyDataService from "../services/tutorial.service";
import { Link } from "react-router-dom";
import logo1 from './logo.jpg';
import logo2 from './merc.jpg';
import logo3 from './audi.jpg';
import logo4 from './skoda.jpg';

export default class PojazdyList extends Component {
  constructor(props) {
    super(props);
    this.onChangeSearchMarka = this.onChangeSearchMarka.bind(this);
    this.retrievePojazdy = this.retrievePojazdy.bind(this);
    this.refreshList = this.refreshList.bind(this);
    this.setActivePojazdy = this.setActivePojazdy.bind(this);
    this.removeAllPojazdy = this.removeAllPojazdy.bind(this);
    this.searchMarka = this.searchMarka.bind(this);

    this.state = {
      pojazdy: [],
      currentPojazdy: null,
      currentIndex: -1,
      searchTitle: ""
    };
  }

  componentDidMount() {
    this.retrievePojazdy();
  }

  onChangeSearchMarka(e) {
    const searchMarka = e.target.value;

    this.setState({
      searchTitle: searchMarka
    });
  }

  retrievePojazdy() {
    TutorialDataService.getAll()
      .then(response => {
        this.setState({
          pojazdy: response.data
        });
        console.log(response.data);
      })
      .catch(e => {
        console.log(e);
      });
  }

  refreshList() {
    this.retrievePojazdy();
    this.setState({
      currentPojazdy: null,
      currentIndex: -1
    });
  }

  setActivePojazdy(pojazdy, index) {
    this.setState({
      currentPojazdy: pojazdy,
      currentIndex: index
    });
  }

  removeAllPojazdy() {
    TutorialDataService.deleteAll()
      .then(response => {
        console.log(response.data);
        this.refreshList();
      })
      .catch(e => {
        console.log(e);
      });
  }

  searchMarka() {
    PojazdyDataService.findByMarka(this.state.searchMarka)
      .then(response => {
        this.setState({
          pojazdy: response.data
        });
        console.log(response.data);
      })
      .catch(e => {
        console.log(e);
      });
  }
  renderSwitch(param) {
    switch(param) {
      case 'BMW':
        return (<img src={logo1} />);
      case 'Audi':
        return (<img src={logo3} />);;
      case 'Mercedes':
        return (<img src={logo2} />);;
      case 'Skoda':
        return (<img src={logo4} />);;
      default:
        return 'brak zdjecia';
    }
  }
  render() {
    const { searchMarka, pojazdy, currentTutorial, currentIndex } = this.state;

    return (
      <div className="list row">
        <div className="col-md-8">
          <div className="input-group mb-3">
            <input
              type="text"
              className="form-control"
              placeholder="Szukaj po marce"
              value={searchMarka}
              onChange={this.onChangeSearchMarka}
            />
            <div className="input-group-append">
              <button
                className="btn btn-outline-secondary"
                type="button"
                onClick={this.searchMarka}
              >
                Search
              </button>
            </div>
          </div>
        </div>
        <div className="col-md-12">
          <h4>Lista pojazdów</h4>

          <ul className="list-group">
            {pojazdy &&
              pojazdy.map((pojazdy, index) => (
                <li
                  className={
                    "list-group-item " +
                    (index === currentIndex ? "active" : "")
                  }
                  onClick={() => this.setActivePojazdy(pojazdy, index)}
                  key={index}
                >
                  {this.renderSwitch(pojazdy.marka)}
                  <b>     {pojazdy.marka}</b> {pojazdy.model}
                  <br></br>
                  <br></br>
                  Rejestracja: {pojazdy.rejestracja}<p className="">Data rejestracji: {pojazdy.data_publikacji}</p>
                  <div>
                    <Link
                      to={"/pojazdy/" + pojazdy.id}
                      className="badge badge-pill badge-success"
                    >
                      Edytuj
                    </Link>
                  </div>

                </li>
              ))}
          </ul>

          <button
            className="m-3 btn btn-sm btn-danger"
            onClick={this.removeAllPojazdy}
          >
            Remove All
          </button>
        </div>
      </div>
    );
  }
}
 ```
 
## Błąd

Po nawet poprawnym zrealizowaniu labolatorium pojawiał się błąd polegający na odmowie dostępu przez co na stronie nie pojawiały się żadne tutoriale oraz nie można ich było dodać.
Można to rozwiązać instalując rozszerzenie [Moesif Origin & CORS Changer](https://chrome.google.com/webstore/detail/moesif-origin-cors-change/digfbfaphojjndkpccljibejjbppifbc?hl=en-US)
