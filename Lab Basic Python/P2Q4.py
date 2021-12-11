ohm = []
while True:
    a = int(input())
    ohm.append(a)
    if a == 0:      
        break
plus =0
min = 0
if ohm[0]==0:
    print("ไม่มีข้อมูล")
else:
    for x in range(len(ohm)):
        if ohm[x] > 0:
            plus+=1
        elif ohm[x] <0:
            min+=1
    print("จำนวนตัวเลขที่มีค่าเป็นบวก",plus)
    print("จำนวนตัวเลขที่มีค่าเป็นลบ",min)