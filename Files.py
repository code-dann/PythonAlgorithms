def read():
    #numbers=[]
    #with open('./Archivos/numbers.txt', 'r', encoding='utf-8') as f:
    #    for i in f:
   #         numbers.append(int(i))
   numbers =  list(map(lambda x: int(x),  open('./Archivos/numbers.txt', 'r', encoding='utf-8')))
   print(numbers)        


def write():
    names=['Facundo','Miguel','Chucho','Christian','Majo']
    with open('./Archivos/names.txt', 'w', encoding='utf-8') as f:
        for i in names:
            f.write(i)
            f.write('\n')


def run():
    write()


if __name__ == '__main__':
    run()