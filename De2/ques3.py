def Sort_Tuple(tup):
	
	len_tuple = len(tup)
	for i in range(0, len_tuple):
		for j in range(0, len_tuple-i-1):
			if (tup[j][1] < tup[j + 1][1]):
				temp = tup[j]
				tup[j]= tup[j + 1]
				tup[j + 1]= temp

	return tup

tup =[('item1', 12.20), ('item2', 15.10), ('item3', 24.5)]
print(Sort_Tuple(tup))