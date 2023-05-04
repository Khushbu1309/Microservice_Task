from bs4 import BeautifulSoup
import requests
import json

def count_words(url):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    words = soup.get_text().split()

    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    freq_list = [(k, v) for k, v in freq.items()]
    freq_list.sort(key=lambda x: x[1], reverse=True)

    return json.dumps(freq_list)


