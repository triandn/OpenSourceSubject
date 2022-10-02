def replaceEndValueList(listOne , listTwo):
        listOne[-1:] = listTwo
        print(listOne)
# def replaceEndValueList(listOne , listTwo):
#         del listOne[len(listOne)-1] # Xóa phần tử cuối trong listOne
#         for i in range(len(listTwo)): # Duyệt listTwo
#             listOne.append(listTwo[i]) # Add phần tử listTwo vào listOne
#         print("Ket qua: ", listOne)
listOne = [1,3,5,7,9,10]
listTwo = [2,4,6,8]
replaceEndValueList(listOne,listTwo)