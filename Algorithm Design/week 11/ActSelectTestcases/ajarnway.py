n = int(input())
act = []
for i in range(n):
    s, f = map(int, input().split())
    act.append((s,f))
   
def getKey(x):
    return(x[1])
 
act.sort(key=getKey)
#set busy as deadline
busy = -1
#if the activity is done, count
count = 0
for s,f in act:
    #if start time is after busy time
    if s > busy:
        count += 1
        busy = f
print(count)