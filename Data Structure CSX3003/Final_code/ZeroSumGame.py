import time

Input1 = list(map(int,input().split()))
Input2 = list(map(int,input().split()))
Input3 = list(map(int,input().split()))
Input4 = list(map(int,input().split()))


st = time.process_time()
oneTwoDict = {}

for i in range(len(Input1)):
    for j in range(len(Input2)):
        key = Input1[i] + Input2[j]
        oneTwoDict[key] = [Input1[i], Input2[j]]


for i in range(len(Input3)):
    for j in range(len(Input4)):
        negKey = (-1) * (Input3[i] + Input4[j])
        if negKey in oneTwoDict:
            element1, element2 = oneTwoDict.get(negKey)
            break
    else: #break out nested loop when a quadruple is found
        continue
    break
else:
    print("No pair Exist")

et = time.process_time()

print(f"{element1} {element2} {Input3[i]} {Input4[j]}")
print(element1 + element2 + Input3[i] + Input4[j])
print(et-st)
