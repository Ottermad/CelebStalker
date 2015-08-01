import requests
import base64

keyBing = base64.b64encode(bytes('YIKl8ICqhOIjAr5P+A08DfxXwVocmvWCTzbdYnQyADU=', 'utf-8'))

#keyBing = 'YIKl8ICqhOIjAr5P+A08DfxXwVocmvWCTzbdYnQyADU='

credentialBing = 'Basic :{}'.format(keyBing) # the "-1" is to remove the trailing "\n" which encode adds

print(credentialBing)
searchString = '%27Xbox+One%27'
top = 20
offset = 0

url = 'https://api.datamarket.azure.com/Bing/Search/Image?' + \
      'Query={}&$format=json'.format(searchString, top, offset)

headers = {'Authorization': credentialBing}
request = requests.get(url, headers=headers)
print(request.status_code)