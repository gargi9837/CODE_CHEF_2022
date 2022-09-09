t = int(input("Enter t"))
for i in range(t):
    list_no = int(input("length"))
    a = []
    for j in range(list_no):
        a.append(int(input("elements")))
    a.sort()
    print(a)
    c = list(set(a))
    print(c)
    if list_no % 2 == 1 and a == c:
        print("no")
    else:
        print("yes")
