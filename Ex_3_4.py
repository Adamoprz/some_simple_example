#count()

lines = ['10000101011', '111111', '01010101010010', '011001100001', '001010101011']

for element in lines:
    if(element.count('11')) < 1:
        print(element)
a = list(filter(lambda x:not x.count('11'), lines))
print(a)