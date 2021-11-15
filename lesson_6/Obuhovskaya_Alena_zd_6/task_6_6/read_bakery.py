
def bakery_sales_read(argv):
   program, *args = argv
   tuple_of_args = tuple(args)
   if len(tuple_of_args) > 2:
       sys.exit('Введено неверное число аргументов')
   with open('bakery.csv', 'r', encoding='utf-8') as f:
       if len(tuple_of_args) == 0:
           for line in f:
               print(line.strip())
       elif len(tuple_of_args) == 1:
           start = int(tuple_of_args[0]) - 1
           lines = f.readlines()
           for line in lines[start:]:
               print(line.strip())
       elif len(tuple_of_args) == 2:
           start = int(tuple_of_args[0]) - 1
           end = int(tuple_of_args[1]) - 1
           lines = f.readlines()
           for line in lines[start:end]:
               print(line.strip())


if __name__ == '__main__':
   import sys

   exit(bakery_sales_read(sys.argv))