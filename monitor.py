import os
import time


def inputIP(prompt):
    success = False
    while not success:
        rawAddress = input(prompt)
        try:
            address = rawAddress.split(".")
            addressValueSuccess = True
            for i in range(len(address)):
                address[i] = int(address[i])
            for i in address:
                if i > 255 or i < 0:
                    addressValueSuccess = False
            if len(address) > 4:
                addressValueSuccess = False
            if addressValueSuccess:
                success = True
            else:
                print("[ERROR] invalid IPv4 Value")
        except:
                print("[ERROR] invalid IPv4 Value")
    addressValue = ""
    for i in range(4):
        if i < 3:
            addressValue = addressValue + str(address[i]) +"."
        else:
            addressValue += str(address[i])
    return addressValue

def inputBin(prompt):
    success = False
    value = 15
    while not success:
        value = input(prompt)
        try:
            value = int(value)
            if value == 0 or value == 1:
                success = True
            else:
                print("[Error] Invalid Option ")
        except:
            print("[ERROR] Invalid Input ")
    if value == 0:
        return False
    elif value == 1:
        return True
    else:
        print("unknown error")
        exit(0)

def inputAddresses():
    moreAddresses = True
    addressList = []
    while moreAddresses:
        addressList.append(inputIP("please enter the IPv4 Address for the service you'd like to monitor "))
        moreAddresses = inputBin("add more addresses? (1=yes/0=no) ")
    return addressList


def main():
    address = inputAddresses()
    index = 0
    while True:
        time.sleep(0.1)
        os.system("ping " + address[index] + " -c 4 > output.txt")
        with open("output.txt", "r") as infile:
            lines = infile.readlines()
        serviceDown = False
        time.sleep(0.1)
        for i in range(len(lines)):
            if "Destination Host Unreachable" in lines[i] or "timeout" in lines[i]:
                serviceDown = True
        if serviceDown:
            print("\aWARNING! service at "+ address[index] + " is down!")
            time.sleep(1)
            print("\a")
            time.sleep(1)
            print("\a")
            os.system("rm output.txt")
            exit(0)
        else:
            print("Service at "+ address[index] +" appears to be available")
        time.sleep(0.1)
        if index < len(address)-1:
            index += 1
        else:
            index = 0
        os.system("rm output.txt")

if __name__ == "__main__":
    main()
