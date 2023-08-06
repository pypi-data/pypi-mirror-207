
from bs4 import BeautifulSoup
import requests
from time import sleep as t



# "https://6captcha.com/apireCAPTCHAv3.php?"
class CAPTCHAv:
    def CAPTCHAv2 (api,websiteKey,websiteURL):
        try:
            URL = f"https://6captcha.com/apireCAPTCHAv2.php?api={api}&websiteKey={websiteKey}&websiteURL={websiteURL}"
            r = requests.get(URL).text
            soup1 = BeautifulSoup(r,'html.parser')
            t(5)
            form_tokon = soup1.find('font', attrs={'color':'black'}).text
            r2 = form_tokon.split('":"')
            r3 = r2[1]
            r4 =r3.split('"')
            t(20)
            return r4[0]
        except:
            return ""
    
    def CAPTCHAv3(api,websiteKey,websiteURL):
        try:
            URL = f"https://6captcha.com/apireCAPTCHAv3.php?api={api}&websiteKey={websiteKey}&websiteURL={websiteURL}"
            r = requests.get(URL).text
            soup1 = BeautifulSoup(r,'html.parser')
            t(5)
            form_tokon = soup1.find('font', attrs={'color':'black'}).text
            r2 = form_tokon.split('":"')
            r3 = r2[1]
            r4 =r3.split('"')
            t(20)
            return r4[0]
        except:
            return ""
    
    def help():
        return """

        from captcha6 import CAPTCHAv  
        CAPTCHAv.CAPTCHAv2(api,websiteKey,websiteURL)
        CAPTCHAv.CAPTCHAv3(api,websiteKey,websiteURL)

        """



