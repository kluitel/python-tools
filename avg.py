listk = [
            [
                {"x":"asdfa", "y":3},{"x":"ss", "y":8},{"x":"ss", "y":8}
            ], 
            [
                {"x":"asdf", "y":3}, {"x":"gg", "y":9},	{"x":"gg", "y":9}
            ],
            [
                {"x":"sss", "y":5}, {"x":"ddd", "y":10}, {"x":"ddd", "y":10}
            ]
]



def get_y_from_list(list1):
    rt=[]
    for l in list1:
        rt.append(l["y"])
    return rt


test = []        
for j in range(len(listk)):
    #kk = get_y_from_list(listk[j])
    kk = [l["y"] for l in listk[j]]
    print(kk)
    temp = []
    for i in range(len(kk)):
        temp.append(kk[i])
    test.append(temp)

#print(test)

def func1(nestedList, index):
    ss = []
    for ll in nestedList:
        ss.append(ll[index])
    #print(ss)
    return ss

for i in range(len(test[0])):
    print(func1(test, i))

'''

temp_list=[]
for j in range(len(listk)):
    for i in range(len(listk[0][0])+1):
        temp_list.append(listk[j][0]["y"])
print(temp_list)
print(temp_list1)
'''
