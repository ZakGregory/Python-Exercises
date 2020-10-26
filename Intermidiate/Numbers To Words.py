###########
#Word list
num_list= {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",15:"fifteen",
20:"twenty",30:"thirty",40:"fourty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninty",100:"hunderd"}

order_list={3:"thousand",6:"million",9:"billion",12:"trillion"}

############
#Num Input
test_num= 1234567890

num = test_num

num_cut=[]

#Split into orders of magnitude MAKE THIS INTO A FUNCTION!

#for i in range(0, (len(str(num))+2)//3):
#    print(i)
#    num_cut.append()



print(num%(10**12)//(10**9))


num_cut=[math.floor((num/10**9)%10**3),math.floor((num/10**6)%10**3),math.floor((num/10**3)%10**3),math.floor(num%10**3)]

print(num_cut)
#num_cut=[num%10**12,num%10**9,num%10**6,num%10**3]





#Convert each section to words
mini_string=""

mini_split=[num_cut[1]//100,num_cut[1]%100]

print(mini_split)

if mini_split[0]!=0:
    mini_string+=num_list[mini_split[0]]+" hundred "



if mini_split[1] in num_list:
    mini_string+=num_list[mini_split[1]]
else:
    micro_split=[(mini_split[1]//10)*10,mini_split[1]%10]
    print(micro_split)
    mini_string+=num_list[micro_split[0]]+" "+num_list[micro_split[1]]

print(mini_string)

#Add all strings together


