a={"nathan":['nidhi', 'dinesh', 'nila'], "sharma":['sheila', 'madan', 'rakesh']}
for i in a:
	print("Key :",i,"Values :",a[i])
	print("the length of values :",len(a[i]))
	j=int(input("Enter the number 0 to 2 to get the data:"))
	print("the 2nd value in the list:",a[i][j])
