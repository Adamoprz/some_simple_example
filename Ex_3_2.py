num_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
#n = 0 or 1. To decide about the sorting key

n = 0
num_list.sort(key = lambda x:x[n])
print(num_list)
