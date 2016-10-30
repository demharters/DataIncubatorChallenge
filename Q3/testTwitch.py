import requests
from requests_oauthlib import OAuth1
import time

def main():

    auth = OAuth1('67iv7yg7px3z36o7mmyb0o9vz2nssmq','net28dh0yf998ost1af9uzyknumwpyf')
    while True:

        #r = requests.get('https://api.twitch.tv/kraken/channels/david_toroczkai/follows', headers = {'Authorization': 'access_token 67iv7yg7px3z36o7mmyb0o9vz2nssmq'})
        r = requests.get('https://api.twitch.tv/kraken', auth=auth)
        print r.json()

if __name__ == '__main__':
    main()
