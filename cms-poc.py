from optparse import OptionParser
import threading
import requests
import imp
import os
import sys
import Queue
Q=Queue.Queue()
threads=[]
lock=threading.Lock()
def poc(module): 
    while True:
        lock.acquire()
        if Q.qsize()>0:
            target=Q.get()
            lock.release()
        else:
            lock.release()
            break
        status=module.poc(target.rstrip('\n'))
        if status:
            lock.acquire()
            print "[*] %s" %target.rstrip('\n')
            lock.release()

def setMulThread(module):
    for i in range(10):
        t=threading.Thread(target=poc,args=(module,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

def setImp(name):
    print "[+] Loading custom script: %s" %name
    script=os.getcwd()+'\\script\\'
    fp, pathname, description = imp.find_module(os.path.splitext(name)[0], [script])
    module=imp.load_module("_", fp, pathname, description)
    if not hasattr(module,'poc'):
        print "can't find poc function,please check your script"
        sys.exit(0)
    else:
        return module
    
def singleThread(module):
    module.poc()

def setPayloads():
    print "[+] Loading payloads..."
    with open(os.getcwd()+"\\data\\"+options.filename,'r') as file:
            for line in file:
                Q.put(line)
    
if __name__=="__main__":
    parser=OptionParser()
    parser.add_option("-f","--file",dest="filename",help="load file of targets")
    parser.add_option("-s","--script",dest="script",help="load script of attack")
    parser.add_option("-t","--target",dest="target",help="single target")
    (options,args)=parser.parse_args()
    if options.filename:
        module=setImp(options.script)
        setPayloads()
        setMulThread(module)
    elif options.target:
        module=setImp(options.script)
        singleThread(module)
    else:
        print "please check your input format"
       

        
    




