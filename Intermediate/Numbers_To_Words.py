#Word list:
#Dictionarys of the nane of each unique number and order
num_list= {0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",15:"fifteen",
20:"twenty",30:"thirty",40:"fourty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninty",100:"hunderd"}

order_list={0:"", 1:" thousand ",2:" million ",3:" billion ",4:" trillion "}

############
#Num Input

num = int(input("Input nuber here: "))

#Split into orders of magnitude

def num_split(number):
    num_cut=[]
    for i in range(0, len(str(number)),3):
        num_cut.append(number%(10**(i+3))//(10**i))
    return num_cut[::-1]

num_cut=num_split(abs(num))

#Convert each section to words
def block_to_sting(block_int):
    block_string=""
    block_split_1=[block_int//100,block_int%100]
    
    if block_split_1[0]!=0:
        block_string+=num_list[block_split_1[0]]+" hundred "

    if block_split_1[0]!=0 and block_split_1[1]!=0:
        block_string+="and "

    if block_split_1[1] in num_list:
        block_string+=num_list[block_split_1[1]]
    else:
        block_split_2=[(block_split_1[1]//10)*10,block_split_1[1]%10]
        block_string+=num_list[block_split_2[0]]+" "+num_list[block_split_2[1]]
    return block_string+""

#Add all strings together
def blocks_to_string():
    to_string=""
    for j in range(0, (len(str(num))+2)//3):
        last_block_string=block_to_sting(num_cut[j])
        to_string+=last_block_string
        if last_block_string!= "":
            to_string+=order_list[(len(str(num))+2)//3-j-1]
    return to_string

#Sort edge cases and output
num_string=""
if len(str(num))<=15:  
    if num==0:
        num_string="zero"
    elif num <0:
        num_string="negative "
        num_string+=blocks_to_string()
    else:
        num_string=blocks_to_string()
    print(num_string)
else:
    print("Number too long")
