import requests
import pprint
# import statistics
#
# n = statistics.mean[(5, 6, 9)]
# print(n)

url = 'https://script.google.com/macros/s/AKfycbz-QcvVVk58wGS7TUWFycuxl7HkndDMA1thsO72IFhTpHDIx2NKK5TQepvIxybJwqg/exec'

response = requests.get(url)
data = response.json()
pprint.pprint(data)

def get_data(url=None):
...


