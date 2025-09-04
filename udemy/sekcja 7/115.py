# email parts

def getEmailParts(email):
    dotIndex = email.find('.')
    monkeyIndex = email.find('@')
    user = email[0:monkeyIndex]
    domainName = email[monkeyIndex+1:dotIndex]
    domainExt = email[dotIndex+1:]
    user_mail = {
        'user': user,
        'domain': domainName,
        'domainExt': domainExt
    }
    return user_mail



mail1 = 'ola@domena.com'
print(getEmailParts(mail1))





#   return 'user: ' + user + ' domainName: ' + domainName + ' domainExt: ' + domainExt