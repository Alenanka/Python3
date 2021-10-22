number_from_1_to_100 = []
for i in range(100):
    number_from_1_to_100.append(i+1)
for each_number in number_from_1_to_100:
    if 10 < each_number < 15:
        print(each_number, "процентов")
    else:
        if each_number % 10 == 1:
            print(each_number, "процент")
        if 1 < each_number % 10 < 5:
            print(each_number, "процента")
        if 4 < each_number % 10 < 10 or each_number % 10 == 0:
            print(each_number, "процентов")