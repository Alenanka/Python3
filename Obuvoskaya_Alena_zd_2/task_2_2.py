spisok = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(spisok):
    if ((spisok[i][0] in '+-') and spisok[i][1:].isdigit()) or (spisok[i]).isdigit():
        if spisok[i][0] in '+-' and len(spisok[i][1:]) < 2:
            spisok[i] = spisok[i][0] + "0" + spisok[i][1:]
        if len(spisok[i]) < 2:
            spisok[i] = "0" + spisok[i]
        spisok.insert(i, '"')
        spisok.insert(i + 2, '"')
        i = i + 2
    i = i+1
print(spisok)

stt = ' '.join(spisok)
print(stt)