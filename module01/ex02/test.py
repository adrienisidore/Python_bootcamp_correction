
from vector import Vector

def main():
	vec = Vector([[1., 2., 3.]])
	vec2 = Vector([[1.], [2.], [3.]])
	print(vec.dot(vec2))
	print(vec + vec)
	print(vec - vec)
	print(2 * vec)
	print(vec * 2)
	print(-1 * vec)
	print(vec / 2)

if __name__ == "__main__":
	main()

