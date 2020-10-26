list=[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

new_list =[0]

next_start=0

def nexthighest(start, end, ignore, iteration): #find the next higest value, add it to new list, return position of next highest
    for i in range(start,end):
        if list[i] > new_list[iteration]:
            new_list.append(list[i])
            return i
    return end 
        

i_iteration=0

while next_start < len(list):   #untill end of list
    next_start= nexthighest(next_start,len(list),0 , i_iteration)    
    i_iteration+=1
    print(next_start)


#for i_iteration in range(5):
#    next_start= nexthighest(next_start,len(list),0 , i_iteration)    
#    print(next_start)

print(new_list) #prints new list



