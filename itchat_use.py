import os
import re
import itchat
import sys
import time
import userclass
import imp

def lc():
    print('finish login')
def ec():
    print('exit')

if __name__ == '__main__':
    control=1
    itchat.auto_login(loginCallback=lc, exitCallback=ec)
    while control:
        imp.reload(userclass)
        userset=userclass.user()
        userlist1=userset.user
        userspecial=userset.userSepecial
        userlist2=list(userspecial.keys())
        userlist=set(userlist1+userlist2)
        message=userset.message
        if userlist:
            timecap=userset.time
            if re.search(r'h|H',timecap):
                timecap=float(re.sub(r'h|h',r'',timecap))*3600
            if re.search(r'M|m',timecap):
                timecap=float(re.sub(r'M|m',r'',timecap))*60
            for user in userlist:
                print(user)
                searchF=itchat.search_friends(user)
                if searchF:
                    #itchat.send(message,toUserName=user)
                    aa=searchF[0]
                    message1=message
                    if user in userspecial:
                        print("send special message to %s" % (user))
                        message1=userspecial[user]
                    else:
                        print("send message to %s" % (user))
                    aa.send(message1)
                else:
                    print("no such friends: %s" % user)
            print("sleep %d" % (timecap))
            time.sleep(timecap)
        else:
            control=0

    itchat.logout()



