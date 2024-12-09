import os

def main():
    raw_addresses = input("Welcome! please enter the IP addresses you'd like to monitor!(separate by a comma) ")
    address = raw_addresses.split(",")
    index = 0
    while True:
        os.system("ping " + address[index] + " -c 4 > output.txt")
        with open("output.txt", "r") as infile:
            lines = infile.readlines()
        serviceDown = False
        for i in range(len(lines)):
            if "Destination Host Unreachable" in lines[i]:
                serviceDown = True
        if serviceDown:
            print("WARNING! service at "+ address[index] + " is down!")
            os.system("rm output.txt")
            exit(0)
        else:
            print("Service at "+ address[index] +" appears to be available")
        if index < len(address)-1:
            index += 1
        else:
            index = 0



if __name__ == "__main__":
    main()
