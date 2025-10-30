
from vector import Vector

def main():
	vec = Vector([[1., 2., 3.]])
	vec2 = Vector([[1.], [2.], [3.]])
	print(vec.dot(vec2))


if __name__ == "__main__":
	main()


# import numpy as np

# v1 = np.array([1., 2., 3.])   # vecteur ligne implicite
# v2 = np.array([4., 5., 6.])

# res = np.dot(v1, v2)
# print(res)
