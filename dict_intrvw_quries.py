# 1
'''
input
emails = "john@gmail.com,jane@yahoo.com,bob@gmail.com"

output
{
  "gmail.com": ["john", "bob"],
  "yahoo.com": ["jane"]
}
'''
def groupmails(emails):
    mails=emails.split(",")
    address={}
    for mail in mails:
        name,adr=mail.split("@")
        if adr not in address:
            address.setdefault(adr,[]).append(name)
        else:
            address[adr].append(name)
    print(address)

emails= "john@gmail.com,jane@yahoo.com,bob@gmail.com"
# groupmails(emails)

# 2
'''
input
logs = "ERROR:disk full,INFO:user login,ERROR:file missing"

output:
{
  "ERROR": ["disk full", "file missing"],
  "INFO": ["user login"]
}
'''

def grouplogs(err):
    err_list=err.split(",")
    err_dict=dict()
    for er in err_list:
        er_type,msg=er.split(":")
        if er_type not in err_dict:
            err_dict.setdefault(er_type,[]).append(msg)
        else:
            err_dict[er_type].append(msg)
    print(err_dict)
    return err_dict

logs = "ERROR:disk full,INFO:user login,ERROR:file missing"
grouplogs(logs)

# 3
'''
Group Words by First Letter
words = "apple,banana,avocado,blueberry"
output:
{
  "a": ["apple", "avocado"],
  "b": ["banana", "blueberry"]
}
'''

def groupby_first(words):
    word_list=words.split(",")
    fruits=dict()
    for li in word_list:
        m=li[0]
        if m not in fruits:
            fruits.setdefault(m,[]).append(li)
        else:
            fruits[m].append(li)
    
    return fruits

words = "apple,banana,avocado,blueberry"
print(groupby_first(words))