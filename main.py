import pandas as pd


print("\t\tBlood Donor Organization\n")
a = int(input("If Admin press 1\nIf User press 2\n"))
HospitalName = []
BloodGroupAvailable = []
Phno = []
Donorname = []
Donorphno = []
DonorBloodgroup = []
Address=[]
Email=[]


def addhospital():
    a = input("HospitalName")
    b = input("Enter BloodGroup available in words")
    c = int(input("Phno"))
    j=input("Enter Address")
    p=input("Enter Email address")
    d=dict(HospitalName=a,BloodGroupAvailable=b,Phno=[c],Address=j,Email=p)
    global r
    r=pd.DataFrame(d)
    print("Data updated successfully")

def printhospitals():
    fh=open('HospitalData','r')
    filecontents=fh.read()
    print(filecontents)
    fh.close()



def donateblood():
    print("Please submit your full health report before donating blood unless it's an emergency")
    a = input("Please enter your name")
    b = int(input("Please enter your phone number"))
    c = input("Please enter your blood group in words")
    x = c.upper()
    Donorname.append(a)
    Donorphno.append(b)
    if (x == "ABNEGATIVE"):
        print("Your blood group is rare thanks for coming forward to donate")
    DonorBloodgroup.append(c)
    print("Thanks for coming forward to donate blood")

def displaydonorlist():
    fh=open('DonorData','r')
    filecontents=fh.read()
    print(filecontents)
    fh.close()


def rspb():
    notifyblooddonor()


def bloodrequests():
    a=input("Enter Blood Group to search")
    fh=open('HospitalData','r')
    f=0
    h=0

    for line in fh:
        h+=1

        if a in line:
            f=1
            break
    if f==0:
        print("Enter Valid Blood Group to search")
    else:
        content=fh.readlines()
        print(content[h])



def notifyblooddonor():
    a = input("Enter Blood Group to search")
    fh=open('DonorData','r')
    f = 0
    h = 0

    for line in fh:
        h += 1

        if a in line:
            f = 1
            break
    if f == 0:
        print("Enter Valid Blood Group to search")
    else:
        content = fh.readlines()
        print(content[h-1])
        print("Blood Donor has been notified...")


if (a == 1):
    print("Welcome Admin\n")
    b = int(input(
        "Please select what would you like to do\n1.Add Hospitals having bloodbanks\n2.View donors list\n3.View Hospitals list\n4.Check for blood requests\n5.Notify Blood donor"))
    if (b == 1):
        addhospital()
    if (b == 2):
        displaydonorlist()
    if(b==3):
        printhospitals()
    if (b == 4):
        bloodrequests()
    if (b == 5):
        notifyblooddonor()


if (a == 2):
    print("\n\tHello User\nWhat would you like to do")
    d = int(input("1.Request specific blood group\n2.Donate blood\n3.Find blood Donation camps nearby"))
    if (d == 1):
        rspb()  # Request Specific Blood Group
    if (d == 2):
        donateblood()
    if(d==3):
        a = input("Enter the area you live in")
        fh = open('HospitalData', 'r')
        f = 0
        h = 0

        for line in fh:
            h += 1

            if a in line:
                f = 1
                break
        if f == 0:
            print("There are no bloodcamps in your area.Please try another area")
        else:
            content = fh.readlines()
            print(content[h-1])
else:
    print("Please select valid option")




