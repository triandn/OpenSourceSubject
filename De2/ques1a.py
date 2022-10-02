def replaceFirstValueList(listOne , listTwo):
        listOne[:-5] = listTwo
        print(listOne)
        
listOne = [1,3,5,7,9,10]
listTwo = [2,4,6,8]

replaceFirstValueList(listOne,listTwo)