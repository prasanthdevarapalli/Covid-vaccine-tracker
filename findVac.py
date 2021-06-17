import json
import requests
from playsound import playsound
import time


from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

district_id = 4 # for Krishna district Andhra Pradesh

URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date=17-06-2021".format(district_id)


print("searching...")
while(True):
    json_result=requests.get(URL).json()
    found = False
    if json_result['sessions']:
        #print(json_result)
        for session in json_result['sessions']:
            if(session['min_age_limit']>17 and session['available_capacity']>0):
                found = True
                print("===============================================")
                print("center name: ",session['name'])
                print("vaccine type:",session['vaccine'])
                print('Address: ',session['address'])
                print('pin code: ',session['pincode'])
                print('slots; ',session['available_capacity'])
                
                
                now = datetime.now()

                current_time = now.strftime("%H:%M:%S")
                print("Current Time =", current_time)
        print(".",end="")
        if(not found):
            time.sleep(10)
                
        
        #alert
        if(found):
            while True:
                playsound("siren.wav")

    else:
        print(".",end='')
        time.sleep(10)
