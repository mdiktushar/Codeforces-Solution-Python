
t = int(input())
while t:
    arr = input()
    arr = arr.split()
    a = int(arr[1])

    arr1 = input()
    list = arr1.split()

    sum = 0
    for i in list:
        sum += int(i)

    if sum == a:
        print("YES")
    else:
        print("NO")
    t-=1