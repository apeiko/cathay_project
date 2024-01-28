num = int(input("請輸入 (0-100) 的數字: "))

peopleList = list(range(1, num + 1))

# Continue the process until only one person remains
index = 0
while len(peopleList) > 1:
    # The person to be deleted
    index = (index + 2) % len(peopleList)
    
    # Delete the person at the index
    peopleList.pop(index)

finalPosition = peopleList[0]

print(f"最後的同事是在第{finalPosition} 位置")