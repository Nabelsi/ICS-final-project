email_id =input("enter please your Email").strip()

user_name= email_id[:email_id.index('@')]

domain= email_id [email_id.index('@')+1:]

print(f"your user_name :{user_name} and your domain should be {domain}")
