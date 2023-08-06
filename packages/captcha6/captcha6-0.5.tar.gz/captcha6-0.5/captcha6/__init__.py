
#  Library developer Omar Style 
from bs4 import BeautifulSoup
import requests
from time import sleep as t
import os





# "https://6captcha.com/apireCAPTCHAv3.php?"
class CAPTCHAv:
    def CAPTCHAv2 (api,websiteKey,websiteURL):
        try:
            URL = f"https://6captcha.com/apireCAPTCHAv2.php?api={api}&websiteKey={websiteKey}&websiteURL={websiteURL}"
            r = requests.get(URL).text
            r4 = r.split(':')[1].split('<')[0].split('"')[1]
            return r4
            exit()
        except:
            return "An error occurred, check online"
            exit()
    
    def CAPTCHAv3(api,websiteKey,websiteURL):
        try:
            URL = f"https://6captcha.com/apireCAPTCHAv3.php?api={api}&websiteKey={websiteKey}&websiteURL={websiteURL}"
            r = requests.get(URL).text
            r4 = r.split(':')[1].split('<')[0].split('"')[1]
            return r4
            exit()
        except:
            return "An error occurred, check online"
            exit()
    
    def help():
        return """
        websiteKey = "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-"
        websiteURL = "https://google.com/recaptcha/api2/demo"
        api =

        from captcha6 import CAPTCHAv  
        CAPTCHAv.CAPTCHAv2(api,websiteKey,websiteURL)
        CAPTCHAv.CAPTCHAv3(api,websiteKey,websiteURL)

        """



