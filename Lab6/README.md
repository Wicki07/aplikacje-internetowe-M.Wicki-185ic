# aplikacje-internetowe-Wicki-185IC

### Autor: Mateusz Wicki Grupa: 185IC_B1

# Lab6 jest kontynuacją zadania z Lab4.
### Dodałem uwierzytelnianie, viewsets, routery oraz licznik wejść przy pomocy cookies

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
