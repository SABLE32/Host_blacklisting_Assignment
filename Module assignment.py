import os
#I used ChatGPT for each block and individually but i understand every line what the code is doing.

# Defines where the hosts file is located
HOSTS = 'C:\Windows\system32\drivers\etc\hosts'  

 # This block of code checks if the users entry exists in the file located at the location defined in the HOSTS variable
def check_host_exists(host):
    with open(HOSTS, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if host in line:
                return True
    return False

#This block prompts the user for a response and asks what they want done with the file 
def add_host_to_block(host):
    if check_host_exists(host):
        #If the hosts exsists print this.
        print(f"The host '{host}' already exists in the hosts file.") 
        #This prompt the user for what they want done with the entry.
        action = input("Do you want to delete (D) or modify (M) the entry? [D/M]: ").lower()
        #This if block is the action taken from the previous prompt to the user. Delete and modify are defined later.
        if action == 'd':
            delete_host_entry(host)
        elif action == 'm':
            modify_host_entry(host)
        #If the wrong input is selected it will prompt the user again to enter a valid input.
        else:
            print("Invalid option. Please choose 'D' for delete or 'M' for modify.")
    #If the wrong input is selected twice it will default to appending it to the end of the file.
    else:
        append_host_entry(host)

#This block of code will be used to delete the entry in the defined hosts path earlier.
def delete_host_entry(host):
    with open(HOSTS, 'r') as file:
        lines = file.readlines()
    with open(HOSTS, 'w') as file:
        for line in lines:
            if host not in line:
                file.write(line)
    print(f"The host '{host}' has been deleted from the hosts file.")

#This block of code will be used to append the entry to the end of the hosts file in the defined path earlier.
def append_host_entry(host):
    with open(HOSTS, 'a') as file:
        file.write(f"\n0.0.0.0 {host}")
    print(f"The host '{host}' has been added to the hosts file and blacklisted.")

#This block of code will be used to modify the entry defined in the hosts file defined earlier.
def modify_host_entry(host):
    delete_host_entry(host)
    append_host_entry(host)

#This it the first prompt a user will get when using the code. It will ask for a FQDN to be blocked. 
def main():
    print("Host Blacklisting Tool")
    host_to_block = input("Enter the FQDN of the host to be blocked: ")

    add_host_to_block(host_to_block)

if __name__ == "__main__":
    main()
