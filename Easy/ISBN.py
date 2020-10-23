checksum=0
test_id="978030640615"

for i in range(0,12,2):
    checksum=checksum+int(test_id[i])+3*int(test_id[i+1])

check=10-(checksum%10)

final_id=test_id+str(check)

print("Initial id: "+test_id)

print("Fianal id: "+final_id)