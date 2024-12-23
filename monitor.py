import os
import time
import _thread
import subprocess

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

def inputInt(prompt):
    success = False
    while not success:
        value = input(prompt)
        try:
            value = int(value)
            success = True
        except:
            print("[ERROR] input must be an integer")
    return value


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

def input_thread(a_list):
    input()
    a_list.append(True)

def monitor(address):
    print("press ENTER key to return to menu")
    serviceDown = False
    index = 0
    output = ""
    a_list = []
    _thread.start_new_thread(input_thread, (a_list,))
    while not a_list:
        if not serviceDown:
            time.sleep(0.1)
            if os.name == 'nt':
                output = subprocess.run(['ping', address[index]], stdout=subprocess.PIPE)
                output = str(output)
            else:
                output = subprocess.run(['ping',address[index], '-c', '4'], stdout=subprocess.PIPE)
                output = str(output)
            serviceDown = False
            time.sleep(0.1)
            if "destination host unreachable" in output.lower() or "timeout" in output.lower():
                serviceDown = True
        if serviceDown:
            print("\r\aWARNING! service at "+ address[index] + " is down! (press ENTER key to return to menu)", end='')
            time.sleep(1)
        else:
            print("Service at "+ address[index] +" appears to be available")
        time.sleep(0.1)
        if index < len(address)-1 and not serviceDown:
            index += 1
            serviceDown = False
        elif serviceDown:
            pass
        else:
            for i in range(len(address)):
                print("\033[F", end='')
            index = 0
            



def main():
    while True:
        print("Welcome!")
        address = []
        while True:
            print("Please select an option below.")
            print("1. Input addresses of services to monitor")
            print("2. Monitor Services")
            print("3. Exit")
            choice = inputInt("option: ")
            if choice == 1:
                address = inputAddresses()
            elif choice == 2:
                if len(address) > 0:
                    monitor(address)
                else:
                    print("[ERROR] no addresses to monitor, please select option 1")
            elif choice == 3:
                exit(0)
            else:
                print("[ERROR] Invalid Selection")



if __name__ == "__main__":
    main()
