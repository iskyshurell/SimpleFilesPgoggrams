import os
import random


def main_func(summ = 0):
	errors_list = [BaseException, SystemExit, KeyboardInterrupt, GeneratorExit, Exception, StopIteration, ArithmeticError, FloatingPointError,
	               OverflowError, ZeroDivisionError, AssertionError , AttributeError, BufferError, EOFError, ImportError, LookupError, IndexError,
	               KeyError, MemoryError, NameError, UnboundLocalError, OSError, BlockingIOError, ChildProcessError, ConnectionError, BrokenPipeError,
	               ConnectionAbortedError, ConnectionResetError, ConnectionRefusedError, FileExistsError, FileNotFoundError, InterruptedError, IsADirectoryError,
	               NotADirectoryError, PermissionError, ProcessLookupError, TimeoutError, ReferenceError, RuntimeError, NotImplementedError, SyntaxError,
	               IndentationError, TabError, SystemError, TypeError, ValueError, UnicodeError, UnicodeEncodeError, UnicodeDecodeError, UnicodeTranslateError]

	while summ < 777:
		try:
			new_num = int(input("Введите число: "))
			chanse = random.randint(1, 13)
			if chanse == 1: #Вместо 1 можно поставить другое любое число от 1 до 13
				error = random.choice(errors_list)
				raise error("Упс! Неповезло)")

			summ += new_num
			saving_num(new_num)

		except errors_list:
			print("Ошибка!")
			break
	print("Победа)")
def saving_num(num):
	with open("result.txt", "a") as result:
		result.write(f"{str(num)}\n")

main_func()