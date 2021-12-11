jm = int(input())
name = input()
list = ["สมหญิง", "ศรีนวล", "ชาติชาย"]
a = list[0]
b = list[1]
c = list[2]
print(list[jm])

if(name.__eq__(a) or name.__eq__(b) or name.__eq__(c)):
    print("มี",name, "ในรายชื่อ")
else:
    print("ไม่มีชื่อ",name,"ในรายชื่อ")

