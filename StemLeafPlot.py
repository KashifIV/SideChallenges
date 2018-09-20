x = [6.1,12.6,34.7,1.6,18.8,2.2,3,2.2,5.6,3.8,2.2,3.1,1.3,1.1,14.1,4,21,6.1,1.3,20.4,7.5,3.9,10.1,8.1,19.5,5.2,12,15.8,10.4,5.2,6.4,10.8,83.1,3.6,6.2,6.3,16.3,12.7,1.3,0.8,8.8,5.1,3.7,26.3,6,48,8.2,11.7,7.2,3.9,15.3,16.6,8.8,12,4.7,14.7,6.4,17,2.5,16.2]

DIVISONS = 5
ADD = 10/DIVISONS
x.sort()
counter = 0
plot = []      
maxstem = 0 
for i in x:
    stem = int(i/10)
    plot.append((stem,int(i%10)))
    if maxstem < stem:
        maxstem = stem
a = []
for i in range(maxstem+1):
    for j in range(DIVISONS):
        while(len(plot) > 0):
            p = plot[0]
            if p[1] >= j*ADD+ADD or p[0] > i:
                print(str(i) + "|" + str(a))
                a = []
                break
            else:
                plot.pop(0)
                a.append(p[1])
        if len(a) > 0:
            print(str(i) + "|" + str(a))
            a = []
                
            
        
    
