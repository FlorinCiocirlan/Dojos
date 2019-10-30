doors=[]
every_door=0
for a in range(1,100):
    doors.append(every_door)

a=0
pass_doors=1
for i in range(1,100):
    while a<len(doors)-1:
        a=a+pass_doors
        pass_doors+=1
        if doors[a] == 0:
            doors[a] = 1
        else:
            doors[a] = 0
        print(pass_doors)
print(doors)
        
        
