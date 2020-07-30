# Autofill Google Form

import requests
import datetime
import time
import sys

# URL to the form you want to fill. formResponse should be used instead of viewform
url = 'https://docs.google.com/forms/d/e/1FAIpQLScjOJtSuSff900rOUeswVUPKZbpbF4tI4B01yYY3V_KDDn2UA/formResponse'

Medical=['Health issues','Travel History (last 30 days)','Both Travel History and Health issues','None of the above']
Sex={ 'm' : 'Male', 'f' : 'Female' , 't' : 'Transgender'}
print("ZONE : SOUTH")
Zone='SOUTH'
print("WARD : 77")
Ward=77
print("Name")
Name=input()
print("AGE:")
Age=int(input())
print("GENDER --- m:MALE   f:FEMALE   t:TRANSGENDER")
Gender = input()
print("Address:")
Address = input() + " rajarathinam nagar chokampudhur cbe-39"
print("Mobile Number [10 digit]")
Mobile=int(input())
print("Members:")
Members=int(input())
print('HEALTH ISSUES')
print(Medical)
Choice_of_Medical=int(input())


exit()


def get_values():
    """It returns a list of different form data to be submitted by send_attendance method.
    subjects_time is a dictionary with Day as keys and time and subjects in a list as values.
    value_list is a list of lectures' subject and time of current_day."""

    values_list = []


    values = {

            # WARD
	    "entry.1567921313" : 77,
            # NAME
	    "entry.194992209": "siljo",
            # AGE
            "entry.428137887": 54,
            # ADDRESS
            "entry.1530105133": "Raja nagar",
            # MOBILE NO
            "entry.1845386066": 9988998899,
            # ZONE
            "entry.1979438168": "SOUTH",
            # SEX
            "entry.806143800": "Male",
            # MEMBERS
            "entry.1808358772": 1,
            # HOSPITAL RECORD
            "entry.197776048": "None of the above",
    }

    values_list.append(values)

    return values_list


def send_attendance(url, data):
    """It takes google form url which is to be submitted and also data which is a list of data to be submitted in the form iteratively."""

    for d in data:
        try:
            x = requests.post(url, data=d)
            print("Form Submitted.")
            print(x.status_code)
            time.sleep(10)
        except:
            print("Error Occured!")


final_data = get_values()

send_attendance(url, final_data)
