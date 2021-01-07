# aplikacje-internetowe-Wicki-185IC

### Autor: Mateusz Wicki Grupa: 185IC_B1

# Lab7 Python + Redis + Django

## Przerobienie przykładów ze [strony](https://mmazurek.dev/tag/redis-i-python/?order=asc)

### 2

![](https://i.imgur.com/37sRe0u.png) 

Gdy nie wprowadzimy zmian w ``redis_coennection = Redis() `` redis uruchomi się na standardowym porcie czyli 6379

![](https://i.imgur.com/SydxxCT.png) 

Redis jest poprawnie skonfigurowany i zainstalowany jeżeli na zapytanie `ping` otrzymamy odpowiedź `pong`

![](https://i.imgur.com/Ot01EQo.png) 

W pierwszej linijce kodu nawiązujemy połączeni z redisem następnie tworzymy własną wartość i klucz do niej na koniec odczytujemy.

![](https://i.imgur.com/MxWRzuF.png)



![](https://i.imgur.com/dqA0J1Y.png)

Pod dodaniu warunku przy tworzeniu połączenia ``decode-responses=True``  znika z wynki `b'  '`

![](https://i.imgur.com/yGZn17b.png)

Opcja `append` dodaje wartość do wartości podanego klucza natomiast `delete` usuwa klucz 

![](https://i.imgur.com/Ec9TPES.png) 

Opcja `set` ustawia wartość podanego klucza natomiast `incr` oraz `decr` odpowiednio zwiękaszają i zmniejszają wartość klucza 

## Listy

![](https://i.imgur.com/xlo3kuR.png)

`rpush` dodaje elemnty do listy natomiast `lrange` zwraca elemnty listy w określonym przedziale w tym przypadku od 0 do -1 co oznacze wszystkie elemnty

![](https://i.imgur.com/6MS88ya.png)

Jak widać po zmianie wartośći wyświetlane są elemnty od 1 do 3 należy pamiętać że iterację zaczynamy od 0

![](https://i.imgur.com/5pCc43r.png)

`brpop` działa w pentli z zwraca ostatni elemnt listy. W momencie w którym lista jest pusta blokuje on program.

![](https://i.imgur.com/IEfsBHe.png)

Dodanie opcji `db` pozwala nam wybrać z którą z dostępnych baz chcemy nawiązać połączenie jest ich 16 zaczynając od 0. DB0 jest bazą domyślną

![](https://i.imgur.com/iJcpGk7.png)

Polecenie `setex` ustawia wartość klucza i jego TTL(Time to live) czyli czas  życia klucza, potem klucz jest automatycznie usuwany.

![](https://i.imgur.com/cgHUyvn.png)

Powyższe polecenie powstało z połączenia SET i EXPIRE działanie powyższego kodu jest takie samo jak poprzedniego.

## Zbiory

![](https://i.imgur.com/PsmbnAL.png)

Po utworzeniu zbioru, gdy chcemy go wyświetlić powtarza się schemat wyświetlania i co 3 raz otrzymujemy to sami w innym przypadku kolejność jest różna

![](https://i.imgur.com/mzPz5AZ.png)

`zrange` wyświetla klucze posrotwane według wartość

![](https://i.imgur.com/7kpcYeu.png)

Dodanie paremetru `withscores=True` sprawi że klucze będą wyświetlały się razem z wartościami

![](https://i.imgur.com/nqHaNYE.png)

Hashe to mapy, słowniki lub tablice asocjacyjne czyli struktura danych przechowująca klucze i odpowiadające im wartości

## Pubsub

![](https://i.imgur.com/4W2OFdE.png)

Przedstawiony proces pokazuje twornie użytkownika z kluczem `testowa_kanal_tekstowy` program po utuchomienu oczekuje na wiadomość 

![](https://i.imgur.com/7NQc8Rw.png)

Dodanie `_*` umożliwia się podłączenie kilku kanałów 

## Strumienie

![](https://i.imgur.com/0Y4iSln.png)

Tworzenie strumienia. liczby przed kluczem to ilość sekund od dnia 1 stycznia 1970r.

![](https://i.imgur.com/mc33ryO.png)

Dodanie elemntu do strumienia.

![](https://i.imgur.com/Z0ETSvl.png)

Powyższy kod przedstawia utrzymanie elemntów tak aby nie ginęły

![](https://i.imgur.com/t2xcx9o.png)

## Pipelining

![](https://i.imgur.com/tKRW7qV.png)

Powyższy okd sprawdza czy klucze nie zostały zmienione. Błąd który się pojawia oznacza że klucze zostały zmienione

## Lua

![](https://i.imgur.com/MbWhjHV.png)

Komendą eval przekazujemy redisowi ciało skrytpu. Redis wykonuje operację i zwraca rezulatat. Drugi argument eval to 0, określa ilość argumentów które można przekazać do skryptu.

![](https://i.imgur.com/umejsrY.png)

Pierwsza dwa przekazane parametry to klucze następne to wartości.

![](https://i.imgur.com/XYcumjN.png)

Przedstawiony kod poniżej zawraca tablicę 10 elemntową

![](https://i.imgur.com/YM96fEC.png)

Powyższy kod przedstawia wykorzystanie JSONA do dodania 2 liczb

![](https://i.imgur.com/RXy3rtl.png)

Wykoanie dodawani liczby 10 i 5. Pierwsze wyświetlane jest none ponieważ fukcja eval zwarac nil  natomiast w kluczu key2 przechowywana jest wartość wyniku.

![](https://i.imgur.com/xOxHMJs.png)

Zczytywanie z cache


# Django-Redis-Celery

### Wygląd strony
![](https://i.imgur.com/fBbfJ8o.png)
![](https://i.imgur.com/TVCFxzh.png)

dołączony plik 


![](https://i.imgur.com/CMVcKXf.png)

Po utworzeniu pliku `celery.py` wykonujemy test


Do Do pliku settings.py należy dodać następujący kod

```javascript
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'media'))
IMAGES_DIR = os.path.join(MEDIA_ROOT, 'images')

if not os.path.exists(MEDIA_ROOT) or not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)

# celery
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Warsaw' 
```
oraz:

```javascript
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'thumbnailer.apps.ThumbnailerConfig',
    'widget_tweaks',
    'django_celery_beat',
]
```
Kod na systemie Windows działa poprawnie dopiero po odpowiednim zmodyfikowaniu kodu

```javascript
import os
from zipfile import ZipFile
from celery import shared_task
from PIL import Image
from django.conf import settings

@shared_task
def make_thumbnails(file_path, thumbnails=[]):
    os.chdir(settings.IMAGES_DIR)
    path, file = os.path.split(file_path)
    file_name, ext = os.path.splitext(file)

    zip_file = f"{file_name}.zip"
    results = {'archive_path': f"{settings.MEDIA_URL}images/{zip_file}"}
    try:
        img = Image.open(file_path)
        zipper = ZipFile(zip_file, 'w')
        zipper.write(file)
        for w, h in thumbnails:
            img_copy = img.copy()
            img_copy.thumbnail((w, h))
            thumbnail_file = f'{file_name}_{w}x{h}.{ext}'
            img_copy.save(thumbnail_file)
            zipper.write(thumbnail_file)

        img.close()
        zipper.close()
    except IOError as e:
        print(e)

    return results
```

![](https://i.imgur.com/lRLMnGx.png)

Wynikiem jest zmiania obrazka na obrazek o wymiarach 128x128 

## Tworznie tasków

W pliku task wprawadzamy kod

```javascript

@shared_task(name='test')
def send_notifiction():
     print('Hello World')
     # Another trick


@shared_task(name='summary') 
def send_import_summary():
    print('Hello every 10 sec')
```

Następnie w pliku setting wprowadzamy ustawianie do tasków

```javascript
from celery.schedules import crontab
CELERY_BEAT_SCHEDULE = {
    # ustawienie taska cyklicznie co 10 sekund
    'minelo 10 sekund': { 
       'task': 'summary',
       'schedule': 10.0
    },
    # Ustawienie taska tak by wykonał się o konktretnej godzinie
    'Witaj o 15:05': {  
         'task': 'test', 
         'schedule': crontab(hour=17, minute=35), 
    },
}
```
Następnie uruchamiamy celery poleceniami 

`
celery -A lab7 beat -l INFO --scheduler 
django_celery_beat.schedulers:DatabaseScheduler
celery -A lab7 worker -l info -P gevent
`
![](https://i.imgur.com/ds077AD.png)
