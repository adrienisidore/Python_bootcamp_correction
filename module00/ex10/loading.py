# Notions
# yield
# Print in terminal

from time import sleep
import time
import sys

def ft_progress(lst):
	total = len(lst)
	start = time.time()
	for i, num in enumerate(lst):
		percent = (i + 1) / total * 100
		elapsed = time.time() - start
		eta = (elapsed / (i + 1)) * (total - (i + 1)) if i > 0 else 0

		bar = "=" * int(percent // 4) + ">"
		sys.stdout.write(f"\rETA: {eta:.2f}s [{percent:.0f}%] [{bar:<25}] {i}/{total} | elapsed time {elapsed:.2f}s")
		sys.stdout.flush()
		yield num

def main():
	listy = range(1000)
	ret = 0
	for elem in ft_progress(listy):
		ret += (elem + 3) % 5
		sleep(0.01)
	print()
	print(ret)

if __name__ == "__main__":
	try:
		main()
	except:
		pass