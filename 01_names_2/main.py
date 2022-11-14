import os

# with open("people.txt", "w") as file:
# 	file.write("Генадий")
# 	file.write("Владислав")
# 	file.write("АБ")
# 	file.write("Александр")
# 	file.write("Олег")
# 	file.write("Яша")
# 	file.write("Як")


def main_func(count = 0, summ = 0):
	if os.path.exists("errors.txt"):
		txt = open("errors.txt", "w")
		txt.write("")
		txt.close()

	with open("people.txt") as names_file:
		for i_str in names_file:
			count += 1
			sym_count = sym_in_str(i_str, count)
			summ += sym_count

		print(f"В файле {summ} символов")




def sym_in_str(temp_str, str_num, temp_count = 0):
	try:
		if len(temp_str) < 4:
			raise ImportError("Ошибка! В строке меньше 3-х букв")
		temp_count += len(temp_str) - 1

	except ImportError:
		with open("errors.txt", "a") as errors:
			saving_results(errors, str_num)

		print(f"В {str_num} строке меньше 3 символов\n ")

	return temp_count
def saving_results(file_name, str_num):
	file_name.write(f"В {str_num} строке меньше 3 символов\n")




main_func()
