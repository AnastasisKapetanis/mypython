ck = 0
txt = input("Give 6 Numbers: ")
if(len(txt)==6):
    ck = 1
while(ck ==0): 
    txt = input("Error Give 6 Numbers: ")
    if(len(txt)==6):
        ck = 1
with open('nums.txt') as f:
    for x in range(6):
        if txt[x:x+4] in f.read():
            print("There is a quadruple available")
