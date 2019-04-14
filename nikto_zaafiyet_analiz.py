import os

def isIp(hedef_ip):
    global flag
    flag = False

    for i in hedef_ip:
        if (i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i=="0" or i=="."):
            flag = True
        else:
            flag = False
            break

os.system("apt-get install nikto")
os.system("apt-get install figlet")
os.system("clear")

os.system("figlet ZAAFIYET ANALIZI")

try:
    hedef_ip = input("Hedef Ip Adresini Girin : ")
    isIp(hedef_ip)
    if(flag):
        print("\nanaliz yapılıyor..\n")
        os.system("nikto -h " + hedef_ip + " >> /root/"+hedef_ip+".txt")
        print("Kayıt Edildi /root/"+hedef_ip+".txt\n")
    else:
        print("\n\033[93mHATA\n")
except:
    print("\n\n\033[93mHATA\n")