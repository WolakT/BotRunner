import requests
import json

botUrl = 'https://demo.uipath.com'
authenticateUrl = "https://demo.uipath.com/api/account/authenticate"
processesUrl = "https://demo.uipath.com/odata/Releases"
robotUrl = "https://demo.uipath.com/odata/Robots"


resp = requests.post(authenticateUrl,data= {'tenancyName': "Infosys_rpa_bot", 'usernameOrEmailAddress': "admin",
                                            'password': "Borowka*4"})
respJson = resp.json()
token = respJson['result']
print(resp)
#get release key
headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}
print(headers)
resp = requests.get(processesUrl,headers=headers)
rawresp = resp.json()
value = rawresp['value']
key = value[0]['Key']
print(key)
# print(key)

#get robot id
resp = requests.get(robotUrl, headers=headers)
robotId = resp.json()['value'][0]['Id']
print(robotId)
