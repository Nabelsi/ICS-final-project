import sys

import socket   
                                                             


email_id =input("enter please your Email").strip()

user_name= email_id[:email_id.index('@')]

domain= email_id [email_id.index('@')+1:]

ip_site = socket.gethostbyname(domain)  
name = socket.gethostname()                                                                                     
print (name)                                            
print(ip_site) 

sys.stdout = open("output.txt", "w")

print(f"your user_name :{user_name} and your domain should be {domain}")

sys.stdout.close()