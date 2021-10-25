list_weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(list_weather):
    if ((list_weather[i][0] in '+-') and list_weather[i][1:].isdigit()) or (list_weather[i]).isdigit():
        if list_weather[i][0] in '+-' and len(list_weather[i][1:]) < 2:
            list_weather[i] = list_weather[i][0] + "0" + list_weather[i][1:]
        if len(list_weather[i]) < 2:
            list_weather[i] = "0" + list_weather[i]
        list_weather.insert(i, '"')
        list_weather.insert(i + 2, '"')
        i = i + 2
    i = i+1
print(list_weather)

str_weather = ' '.join(list_weather)
print(str_weather)
