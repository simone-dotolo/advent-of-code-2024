with open('input.txt') as f:
	lines = f.readlines()

	list_1 = [int(el.split()[0]) for el in lines]
	list_2 = [int(el.split()[1]) for el in lines]

	list_1.sort()
	list_2.sort()

	res = 0

	for i in range(len(list_1)):
		res += abs(list_1[i] - list_2[i])

	print(res)
