import requests 

while True:

    url = 'https://uselessfacts.jsph.pl/random.json?language=en'

    response = requests.get(url)
    bored = response.json()['text']

    print(bored)

    again = input('you want again :')

    if again != 'yes'.lower():
        break
