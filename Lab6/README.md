# aplikacje-internetowe-Wicki-185IC

### Autor: Mateusz Wicki Grupa: 185IC_B1

# Lab6 jest kontynuacją zadania z Lab4.
## Dodałem uwierzytelnianie, viewsets, routery oraz licznik wejść przy pomocy cookies

Po zainstalowaniu ***django-rest-auth*** dodałem widok logowania, wylogowania, resetu hasła, rejsetracji, potwierdzenie resetu hasła

Poniżej przedstawione widoki poszeczególnych paneli


![](https://i.imgur.com/Gp0e5Lz.png)
![](https://i.imgur.com/L7lPoaN.png)
![](https://i.imgur.com/a3Kvb3C.png)
![](https://i.imgur.com/ux2esZa.png)
![](https://i.imgur.com/Mnxk3Nu.png)

Aby panel rejstracji działał poprawnie należy dodać w pliku `setting.py` nastepujący kod
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SITE_ID = 1
```

Podaczas rejestracji jest tworzony tokken więc jeżeli w pliku `setting.py` mamy ***SessionAuthentication*** oraz ***TokenAuthentication***
użytkownicy utworzeni wcześniej będą mieli wgląd do postów.

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        #'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticated',
        ],
        
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.SessionAuthentication',
            # 'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.TokenAuthentication', 
        ],
}
```

Jeśli natomiast usuniemy ***SessionAuthentication*** wgląd do postów będą mieli tylko użytkownicy z tokkenem

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        #'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticated',
        ],
        
        'DEFAULT_AUTHENTICATION_CLASSES': [
            # 'rest_framework.authentication.SessionAuthentication',
            # 'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.TokenAuthentication', 
        ],
}
```
## Dodanie licznika przy pomocy cookies

Aby stworzyć licznik należało utworzyć poniższy kod

```python
    # definujemy funkcję post ponieważ odpowiada za formularz dodawania nowych postów
    def post(self, request, *args, **kwargs):
    
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # definujemy funkcję get ponieważ odpowiada ona za wyświetlanie postó na stronie
    def get(self, request, *args, **kwargs):
        snippets = Post.objects.all()
        serializer = PostSerializer(snippets,many=True)  
        #Tworzenie obiektu klasy response przy pomocy danych serializera
        response =  Response(serializer.data)
        # pobieranie ilość "odwiedzin" z cookies jeśli nie ma ustaw na 0
        value =int(request.COOKIES.get('visits', '0'))
        # jeżeli cookis visits istnie to if się wykona
        if request.COOKIES.get('visits' ):
            # ustawienie odpowiednich wartosci do cookies
                response.set_cookie('visits', value + 1 )
                response.set_cookie('last_visit', 'Witaj poraz kolejny')
        else:
            # ustawienie odpowiednich wartosci do cookies
                response.set_cookie('last_visit', 'Witaj poraz pierwszy' )
                response.set_cookie('visits', value + 1 )
        return response
```

Podaczas pierwszego logowania na strone w cookies pojawia się informacja "Witaj poraz pierwsz!"

![](https://i.imgur.com/lb9eMbt.png)

Podaczas każdego następnego logowania na strone w cookies pojawia się informacja "Witaj ponownie"

![](https://i.imgur.com/TJY3WNT.png)

## Dodanie viwevsets oraz router

Aby dodać viewsets należy edytoać plik `viwes.py` i utworzyć w nim funkcję do wyświetlania postów

```python
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

 

class KsiazkaList(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,IsAuthenticated)
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title']
```

Po dodaniu viewsetów pojawił się problem z permissions więc należało dodać do permission_classes, IsAuthorOrReadOnly oraz IsAuthenticated

Viewset nie korzystają z `urlpatterns` tylko z `routers` więc plik urls.py wygląda następująco

```python
from rest_framework.routers import SimpleRouter
from .views import  KsiazkaList
from .views import UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', KsiazkaList, basename='Ksiazki')
urlpatterns = router.urls
```



