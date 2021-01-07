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

Pod dodaniu warunku przy tworzeniu połączenia ``decode-responses=True``  znika z wynki `b'  '`

![](https://i.imgur.com/dqA0J1Y.png)

Opcja `append` dodaje wartość do wartości podanego klucza natomiast `delete` usuwa klucz 

![](https://i.imgur.com/yGZn17b.png)

Opcja `set` ustawia wartość podanego klucza natomiast `incr` oraz `decr` odpowiednio zwiękaszają i zmniejszają wartość klucza 

![](https://i.imgur.com/Ec9TPES.png) 





