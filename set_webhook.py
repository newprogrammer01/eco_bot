import requests
import os
url='http://jasurbek777.pythonanywhere.com/webhook'
TOKEN=os.environ['TOKEN']
payload={
    'url':url
}
r=requests.get(f'https://api.telegram.org/bot{TOKEN}/setWebhook', params=payload)
print(r.status_code)