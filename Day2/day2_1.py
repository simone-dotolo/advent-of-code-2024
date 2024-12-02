with open('input.txt') as f:
	reports = [[int(level) for level in report.split()] for report in f.readlines()]
	
	res = 0

	for j, report in enumerate(reports):
		increasing = report[0] < report[1]
		is_safe = ((abs(report[1] - report[0]) >= 1) and (abs(report[1] - report[0]) <= 3))
		i = 2
		while is_safe and i < len(report):
			if increasing:
				is_safe = ((report[i] > report[i-1]) and (abs(report[i] - report[i-1]) >= 1) and (abs(report[i] - report[i-1]) <= 3))
			else:
				is_safe = ((report[i] < report[i-1]) and (abs(report[i] - report[i-1]) >= 1) and (abs(report[i] - report[i-1]) <= 3))
			i += 1

		print(f'Report {j} is safe? {is_safe}')
		res += (is_safe == True)

	print(res)