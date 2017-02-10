# def run():
# 	file_name = 'url_list.txt'
# 	with open(file_name, 'wb') as wfile:
# 		for i in range(1, 741):
# 			wfile.write("http://www.cafc.uscourts.gov/opinions-orders?populate=&field_origin_value=All&field_report_type_value=All&field_date_value_1[min][value]=2002-01-24%2012%3A01%3A11&field_date_value_1[max][value]=2017-01-24%2012%3A01%3A11&field_date_dropdown=date_range&page=" + str(i) + ' ' + str(i + 1) + '\n')

# run()


# def dirList():
# 	file_name = 'dirList.txt'
# 	with open(file_name, 'wb') as wfile:
# 		for i in range(1, 742):
# 			wfile.write('Lists/list' + str(i) + '.txt')
# 			wfile.write('\n')

# dirList()


def dirList():
	file_name = 'dirList.txt'
	count = 0
	count2 = 0
	with open(file_name, 'rb') as rfile:
		for line in rfile:
			line = line.strip().split('\n')[0]
			with open(line, 'rb') as rfile2:
				for line2 in rfile2:
					line2 = line2.strip().split('\n')[0]
					line2 = str(line2) + '.txt'
					count2 += 1
					try:
						with open(line2, 'rb') as rfile3:
							if 'patent' or 'patents' in rfile3:
								count += 1
					except:
						print('error')
	print(count)
	print(count2)

dirList()