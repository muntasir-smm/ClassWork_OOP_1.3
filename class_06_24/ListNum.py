def bubbleSort(num):
    # return sorted(num)

    for i in range(len(num)):
        for j in range(len(num)-i-1):
            if (num[j]>num[j+1]):
             temp=num[j]
             num[j]=num[j+1]
             num[j+1]=temp

    return num




def main():
    num=[1, 3 , 56, 7, 4, 6, 9, 10]
    print(num)

    sortedNum= bubbleSort(num)
    print(sortedNum)
    num.reverse()
    print(f"Reversed Sort: {num}")

main()