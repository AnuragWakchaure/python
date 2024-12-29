from brcal import broad
from netcal import nwadd
from rangecal import iprange

def main():
    uservar=192
    uservar1=65
    uservar2=1
    uservar3=int(input("Enter last octat : "))

    print(f"IPv4 add is {uservar}.{uservar1}.{uservar2}.{uservar3}")

    broad.cal_bro_add(uservar,uservar1,uservar2,uservar3)
    nwadd.network_add(uservar,uservar1,uservar2,uservar3)
    iprange.iprange(uservar,uservar1,uservar2,uservar3)
main()