import re

def email_parse(email_address):
    email_dict = {'username': '', 'domain': ''}
    user = re.findall(r'(^[a-zA-Z0-9\.\-]+)@([a-zA-Z0-9]+\.[a-zA-Z\.]{2,}$)',email_address)
    if not user:
        raise ValueError(f"wrong email: {email_address}")
    email_dict['username'], email_dict['domain'] = user[0][0],user[0][1]
    print(email_dict)


email_parse('lena@mts.by')
email_parse('daily@mail.co.uk')
email_parse('le.na@mts.by')
email_parse('lena@m.b') # недопустим один символ после точки

