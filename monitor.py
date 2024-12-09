import os
import time

def main():
    raw_addresses = input("Welcome! please enter the IP addresses you'd like to monitor!(separate by a comma) ")
    address = raw_addresses.split(",")
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
