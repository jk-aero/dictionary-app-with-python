import requests

def randomword():
    response = requests.get("https://api.urbandictionary.com/v0/random")
    api_data=response.json()['list'][3]
    print(api_data)
    word_defenition=api_data['definition']
    word=api_data['word']
    print('\n'+word+'\n')
    print(word_defenition+'\n')

def wordData(word):
    response = requests.get(f"http://api.urbandictionary.com/v0/define?term={word}")
    api_data=response.json()
    for defenition in (api_data)['list']:
        print(defenition['definition'])


