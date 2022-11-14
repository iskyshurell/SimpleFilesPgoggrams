import os

def main(str_count = 0):
	with open("result.txt", "w") as result_file:
		with open("calc.txt") as txt:
			for i_str in txt:
				str_count += 1
				result_file.write(f"{action(i_str, str_count)}\n")
	return sum_count()


def action(i_str, str_count):
	try:
		info = i_str.split()
		if len(info) != 3:
			raise ValueError

		return counting(i_str, info, str_count)

	except ValueError:
		error = f"В {str_count} строке не хватает елементов"
		print(error)
		flag = error_choise(i_str)
		return new_str(flag, str_count, error)

def counting(i_str, temp_list, str_count, actions = ["+", "-", "*", "/", "//", "%", "**"]):
	action = temp_list[1]
	f_num = temp_list[0]
	s_num = temp_list[-1]

	try:
		int(f_num)     #Очистка входных данных
		int(s_num)
		if not action in actions:
			raise ValueError

		return eval(f"{f_num} {action} {s_num}")

	except ZeroDivisionError:
		error = f"В строке {str_count} нельзя делить на 0!"
		print(error)
		flag = error_choise(i_str)
		return new_str(flag, str_count, error)
	except ValueError:
		error = f"Один из элементов в {str_count} строке не соответствует ожиданиям"
		print(error)
		flag = error_choise(i_str)
		return new_str(flag, str_count, error)

def error_choise(i_str):
	choise = input(f"Хотите исправить ошибку в строке? {i_str}")
	if choise.lower() == "да":
		return True
	elif choise.lower() == "нет":
		return False

def new_str(flag, str_count, error):
	if flag:
		i_str = input("Введите исправленную строку: ")
		return action(i_str, str_count)
	return error


def sum_count(summ = 0):
	with open("result.txt") as result:
		for i_str in result:
			try:
				if float(i_str):
					summ += float(i_str)
			except ValueError:
				pass

		return summ

print(f"Сумма результатов: {main()}")


