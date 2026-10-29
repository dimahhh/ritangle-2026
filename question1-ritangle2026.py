import itertools
existingpnt=[(0,3),(2,1),(4,0)]
rows=[2,3,5,7,11,13]
colunms=[17,19,23,29,31,37]
sum=0
grid=[(x,y) for x in range(6) for y in range(6)]
avaliablepoints=[point for point in grid if point not in existingpnt]
for combo in itertools.combinations(avaliablepoints,3):
    sixpoints=existingpnt+list(combo)
    distances=set()
    valid=True
    for i in range(len(sixpoints)):
        for j in range(i+1,len(sixpoints)):
            p1,p2=sixpoints[i],sixpoints[j]
            dis_squared=(p1[0]-p2[0])**2+(p1[1]-p2[1])**2
            
            if dis_squared in distances:
                valid= False
                break
            distances.add(dis_squared)
    if valid:
        print("coordinates are",combo)
        for x,y in combo:
            value=rows[y]*colunms[x]
            print(value)
            sum=sum+value
            print(sum)
