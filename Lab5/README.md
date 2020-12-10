# aplikacje-internetowe-Wicki-185IC

### Autor: Mateusz Wicki Grupa: 185IC_B1

# Lab5 Web Scaraping
## W pierwszel kolejności zrealizowałem kod z laboratoriów.

Do stworzenia szablonu wykorzystałem wygląd strony z projektowania serwisów internetowych.
Na stronie głównej pojawiają się zrealizowane przykłady

![](https://i.imgur.com/0z809Ha.png)
![](https://i.imgur.com/GCiDaTc.png)

Aby przykłady wyświetlały się na stronie należało do funkcji dodać `return render()`. Ostatecznie funkcja prezentuje się następująco

```python
def zajecia(request):
    #Przykład 1
    page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
    soup = BeautifulSoup(page.content, "html.parser")

    all_span_tags = []
    for element in soup.select("span"):
        all_span_tags.append(element.text)

    pierwszy = all_span_tags[0]
    trzeci = all_span_tags[3]
    ostatni = len(all_span_tags)
    #Przykład 2
    top_items = []

    products = soup.select("div.thumbnail")
    print("Liczba top items = ", len(products))
    for elem in products:
        title = elem.select("h4 > a.title")[0].text
        review_label = elem.select("div.ratings")[0].text
        info = {"title": title.strip(), "review": review_label.strip()}
        top_items.append(info)

    #Przykład 3
    # Create top_items as empty list
    image_data = []

    # Extract and store in top_items according to instructions on the left
    images = soup.select("img")
    print("Liczba obrazków =", len(images))
    for image in images:
        src = image.get("src")
        alt = image.get("alt")
        image_data.append({"src": src, "alt": alt})

    #Przykład 4
    all_products = []

    # Extract and store in top_items according to instructions on the left
    products = soup.select('div.thumbnail')
    for product in products:
        name = product.select('h4 > a')[0].text.strip()
        description = product.select('p.description')[0].text.strip()
        price = product.select('h4.price')[0].text.strip()
        reviews = product.select('div.ratings')[0].text.strip()
        image = product.select('img')[0].get('src')

        all_products.append({
            "name": name,
            "description": description,
            "price": price,
            "reviews": reviews,
            "image": image
        })

 
    return render(request,'home.html',{'pierwszy':pierwszy, 'trzeci':trzeci, 'ostatni':ostatni, 'top_items':top_items, 'image_data':image_data, 'all_products':all_products})
```

## Formularz do Web Scrapingu

Wygląd fomularza 

![](https://i.imgur.com/VH83mDa.png)

Pola w formularzu są wymagane

![](https://i.imgur.com/WrTItDX.png)

Do fomularza wpisujemy link strony oraz elemnt jakiego chcemy wyszukać. Po wyszukaniu elemnty wyświetlają się jeden pod drugim.

![](https://i.imgur.com/IkwGZfe.png)

W tym przypadku elemnt ***p*** zawiera tylko tekst więc tylko on jest wyświetlany. Jeżeli elemnet posiada więcej atrybutów jak np klasę, będą one wyświetlane.

![](https://i.imgur.com/ruAVCS8.png)

Kolejny przykładem jest wyszukanie elemntów ***img***

![](https://i.imgur.com/ID6SMaC.png)

Jak widać te elemnty zawierają więcej atrybutów. Atrybut `Tekst` nie wyświtla nic ponieważ taktuje on zdjęcie jako tekst.

### Funkcja zwracająca wyszukane elemnty

```python
def szukaj(request):
    if request.method == "POST":
        url = request.POST.get('web_link', None)
        element = request.POST.get('element', None)
        source=requests.get(url).text 
        all_elements = []
        
        soup = BeautifulSoup(source, "html.parser")

        items = soup.find_all(element)
        amount = len(items)    

        index = 1 

        for i in items:
            # Szukanie klasy
            find_class = i.get('class')
            if find_class is None:
                find_class = "Brak"   
            
            # Szukanie id
            find_id = i.get('id')
            find_id = find_id.strip() if find_id is not None else "Brak"

            # Szukanie linków
            find_href = i.get('href')
            find_href = find_href.strip() if find_href is not None else "Brak"

            # Szukanie tekstu
            get_text = i.text
            get_text = get_text.strip() if get_text is not None else "Brak"

            # Szukanie źródeł
            find_src = i.get('src')            
            if find_src is None:
                find_src = "Brak"
            # Szukanie atrybutu
            find_alt = i.get('alt')
            find_alt = find_alt.strip() if find_alt is not None else "Brak"

            all_elements.append({"find_id": find_id, "find_class": find_class, "find_href": find_href, "get_text": get_text, 'find_alt':find_alt, 'find_src': find_src, 'index': index})
            index += 1
        return render(request, 'scrap.html', {'all_elements':all_elements, 'amount': amount, 'url': url, 'element':element})
    return render(request, 'scrap.html')
```

## Szuaknie elemntów ze strony przy pomocy xml

Wygląd na stronie
![](https://i.imgur.com/d2ydEPB.png)

Aby znaleźć elemnt przy pomocy xPath potrzebuje adresu strony oraz xPath szukanego elemntu. Pobieramy go poprzez naciśnięcia na elemnt prawym przyciskiem myszki następnie ``Zbadaj`` najeżdżamy na wybrany elemnt i wybieramy ``Copy -> Copy xPath``


