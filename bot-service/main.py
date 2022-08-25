import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TELEGRAM_TOKEN")
groups = ['test129012skdm', 'melaniatrumpgroup', 'ConservativeTradition']
msg = 'Hello there'


def send_msg(groups, msg):
    if groups:
        for group in groups:
            try:
                if not token:
                    print('No token provided')
                else:
                    url = 'https://api.telegram.org/bot{}/sendMessage?chat_id=@{}&text={}&parse_mode=HTML'.format(token, group, msg)
                    res = requests.get(url)
                    print(res.text)
            except:
                print('Something went wrong')
    else:
        print('Please provide some group ids')


send_msg(groups, msg)
