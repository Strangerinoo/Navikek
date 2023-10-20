import requests
from faker import Faker
import warnings
fake = Faker()
warnings.filterwarnings("ignore", message="Unverified HTTPS request")
headers = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Cookie' : 'cf_chl_2=6f5eec6c94423a8; cf_clearance=iR_BAfxmoXAXibUlROEniOCs3xMUtd9TYvyZvbLnMmA-1697832887-0-1-c7d02d36.1edbc80f.90d172d6-250.0.0; PHPSESSID=75j97u9lctc8eh0baqg6kbqn1t'
    }   

#################
#On génère les PDF comme Osirus Jack
def genPostData():
   data = { 'ccnum' : fake.credit_card_number(), 'ccexp' : fake.credit_card_expire(), 'ccvv' : fake.credit_card_security_code() }
   return data

def makeNavikekRequest():
   URL = 'https://client.navigo-remboursements.com/connection/auth/remboursement.php'
   r = requests.post(URL, data=genPostData(), headers=headers, verify=False, json=None)
   if r.status_code == 200: 
      print("Navikeked")
   else: 
      print("C cassé chef >.<")





while True:
   makeNavikekRequest()