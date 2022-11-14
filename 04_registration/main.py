def main_func():
	with open("registrations.txt", encoding = "utf-8") as names_list:
		with open("registrations_good.log", "w") as g_info:
			with open("registrations_bad.log", "w") as b_info:
				for i_info in names_list:
					try:
						temp = i_info.split()
						error = error_check(temp)

						if len(str(error)) > 0:
							raise error


					except:
						b_info.write(f'{" ".join(temp)}  ---  {error} \n')
					else:
						g_info.write(f'{" ".join(temp)}\n')


def error_check(temp):
	if len(temp) != 3:
		return IndexError
	elif not temp[0].isalpha():
		return NameError

	elif not "@" in temp[1] and not "." in temp[1]:
		return SyntaxError

	elif (int(temp[2]) < 10 or int(temp[2]) > 99):
		return ValueError

	else:
		return ""

main_func()
