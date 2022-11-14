import os

def f_visuals():
	print("|{::^30}|".format(":"))
	print("|{:-^30}|".format(" MY CHAT "))
	print("|{::^30}|".format(":"))

	print("|{:^30}|".format(""))
	name = input("Введите своё имя: ")
	print("|{:^30}|".format(""))
	print("|{::^30}|".format(""))
	return name

def s_visuals():
	print("|{:^30}|".format(""))
	choose = input("Введите действие:\n- просмотреть\n- написать\n::=>:: ")
	print("|{:^30}|".format(""))
	print("|{::^30}|".format(""))
	return choose

def t_visuals():
	print("|{:^30}|".format(""))
	print("|{:-^30}|".format(">>Ошибка!<<"))
	print("|{:^30}|".format(""))
	print("|{::^30}|".format(":"))


def mail(name):
	with open("chat.txt", "a") as main_chat:
		message = input("Введите своё\nсообщение: ")
		count = 26 - len(name) - len(message)
		full_message = f"{name} :: {message}" + " " * count
		main_chat.write('|{}|\n'.format(full_message))


		print("|{:^30}|".format(""))
		print('|{}|'.format(full_message))
		print("|{:^30}|".format(""))
		print("|{::^30}|".format(""))

def check():
	print("|{:^30}|".format(""))
	with open("chat.txt", "r") as main_chat:
		for i_str in main_chat:
			print(i_str, end = "")
	print("|{:^30}|".format(""))

def main_cycle():
	name = f_visuals()

	while True:
		choose = s_visuals()

		if choose.lower() == "просмотреть":
			check()
		elif choose.lower() == "написать":
			mail(name)
		elif choose.lower() == "break":
			break
		else:
			t_visuals()


def chat_exists():
	if not os.path.exists("chat.txt"):
		with open("chat.txt", "w") as file:
			pass


chat_exists()
main_cycle()