def currency_rates(currency):
    import requests
    req = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    charcode = [element_charcode.split('</CharCode>')[0] for element_charcode in req.split('<CharCode>')[1:]]
    nominal = [element_nominal.split('</Nominal>')[0] for element_nominal in req.split('<Nominal>')[1:]]
    value = [element_value.split('</Value>')[0] for element_value in req.split('<Value>')[1:]]
    dict_kurs = dict(zip(charcode, zip(nominal, value)))
    kurs = dict_kurs.get(currency.upper())
    if kurs is None:
        print('Нет такой валюты')
    else:
        print(f'Курс рубля  за {kurs[0]}  {currency.upper()} равен {kurs[1]}')


currency_rates(input("Ведите валюту:"))