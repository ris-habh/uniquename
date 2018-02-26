import csv
import operator
import itertools

data=[[]]
keys = []
groups = []
flag=0
with open('training_data.csv','r') as td:
    cr=csv.reader(td, delimiter=',')
    td.__next__()
    sr=sorted(cr, key=operator.itemgetter(0))
    with open('sorted_data.csv', 'w') as sdw:
        for x in sr:
            data.append([x[0],x[1],x[2],x[3]])
            sdw.write(str(x)+'\n')



sortd=sorted(data[0])

with open("key_names.csv",'w') as kn:

    with open("same_set_of_names.csv",'w') as sson:

        for k,g in itertools.groupby(data):
            keys.append(k)
            groups.append(list(g))


        for i in groups:
            sson.write(str(i)+'\n')
        for i in keys:
            kn.write(str(i)+'\n')


value_input=[]
print('Enter dob')
d=input()
d=" '"+d+"'"
print('Enter gender')
g=input()
g=" '"+g+"'"
print('Enter first name')
f=input()
f=" '"+f+"']"
print('Enter last name')
l=input()
l="['"+l+"'"

value_input=[l,d,g,f]



with open('key_names.csv','r') as rkn:
    rkn_reader= csv.reader(rkn,delimiter=',')
    rkn.__next__()


    for row in rkn_reader:
        if value_input[1] == row[1] and value_input[2] == row[2] :
            if (value_input[3] == row[3] and value_input[0] == row[0]) or (value_input[0][2]==row[0][2] and value_input[3]==row[3]) or (value_input[3][2]==row[3][2] and value_input[0]==row[0]):
                print("unique name :" + row[0]+" "+row[3])
                flag=1
    if flag==0:
        print("NO SUCH ENTRY BEFORE")
        
