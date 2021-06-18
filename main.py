import requests
from colorama import Fore, Style
from datetime import datetime
from typing import List
import threading
from numpy import array_split


INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def check(names: List) -> None:

	with open(OUTPUT_FILE, "a") as output:
		for name in names:
			name = name[:-1]

			try:
				r = requests.get(f"https://github.com/{name}")
			
			except: # There is a bug that i can't fix lol. Maybe i'm sending too many requests too quickly. I will try to add support for proxies later
				pass

			time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

			if r.text == "Not Found":
				print(f"{Style.BRIGHT + Fore.GREEN}| {name} Is Available | https://github.com/{name} | Checked: {time} |")

				output.write(f"| {name} Is Available | https://github.com/{name} | Checked: {time} |\n")

			else:
				print(f"{Style.BRIGHT + Fore.RED}| {name} Is Not Available | https://github.com/{name} | Checked: {time} |")
				pass

def main():
	with open(INPUT_FILE, "r") as file:
		file = file.readlines()


	threads = int(input("How many threads do you want? (less than file length): "))
	lists = array_split(file, threads)

	for i in range(0, threads):
		t = threading.Thread(target = check, args = (lists[i],))
		t.start()


if __name__ == '__main__':
	try:
		main()

	except KeyboardInterrupt:
		print("\nSee you later!")
