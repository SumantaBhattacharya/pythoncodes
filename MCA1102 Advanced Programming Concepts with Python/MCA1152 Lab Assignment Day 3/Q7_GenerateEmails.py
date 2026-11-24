# Given a dictionary, which contains domain names as keys, and a list of users as values, 
# generate a list that contains complete email addresses as user@domain. 
# Sample 
# Input: {"gmail.com": ["paul.buchheit", "sanjeev.singh", "kevin.fox"], 
# "yahoo.com":["jerry.yang", "david.filo"], "hotmail.com": ["sabeer.bhatia"]} 
# Output: ['paul.buchheit@gmail.com', 'sanjeev.singh@gmail.com', 'kevin.fox@gmail.com', 
# 'jerry.yang@yahoo.com', 'david.filo@yahoo.com', 'sabeer.bhatia@hotmail.com']

# Given a dictionary, which contains domain names as keys, and a list of users as values,
domains = {
    "gmail.com": ["paul.buchheit", "sanjeev.singh", "kevin.fox"], 
    "yahoo.com":["jerry.yang", "david.filo"], 
    "hotmail.com": ["sabeer.bhatia"]
}

# print(domains.items())

# generate a list that contains complete email addresses as user@domain.
emails = []

for domain in domains:
    print(domain)
    for user in domains[domain]:
        print("user: ", user)
        email = user + "@" + domain
        emails.append(email)

print(emails)
