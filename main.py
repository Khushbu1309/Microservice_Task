from func import *

url = "https://example.com/"
result = count_words(url)
print(result)

word_counts = count_words(url)
with open('output.json', 'w') as f:
     f.write(word_counts)
