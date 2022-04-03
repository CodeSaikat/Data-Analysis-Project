import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=e43a01deb2c84faeaf9f05f7c2898c68')
response = requests.get(url)
#print(response.json())
pk=response.json()
article = pk['articles']
results = []
for ar in article:
    results.append(ar['title']+ar['description'])
for i in range(len(results)):
    # printing all trending news
    print(i + 1, results[i])
def speek():
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(results)

if __name__ == '__main__':
    speek()
