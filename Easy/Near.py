print("Can the second word be made from the first by removing one letter?")
a=str(input("Input first word: "))
b=str(input("Input second word: "))

try:
    def near(str1,str2):
        if len(str2) >= len(str1) or len(str2)<len(str1)-1:
            return False

        l_str2=str2+" "
        r_str2=" "+str2

        matching_letters=0
        
        for i in range(0,len(str1)):
            if l_str2[i]==str1[i] or r_str2[i]==str1[i]:
                matching_letters=matching_letters+1

        if matching_letters>=len(str2):
            return True
        else:
            return False
except:
    print("somthing went wrong")

print("Computer says: "+str(near(a,b)))

#print(near("reset", "rest"))
#print(near("dragoon", "dragon"))
#print(near("eave", "leave"))
#print(near("sleet", "lets"))
