num = [1, 2, 5, 4]

def duplicate(num):
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i] == num[j]:
                return True
    return False

print(duplicate(num))