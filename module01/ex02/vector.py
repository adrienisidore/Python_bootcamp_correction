import numpy as numpy
import math as math
# Erreur dans le sujet
# NaN and inf not supported
class Vector:

	def __init__(self, values=None, shape=None):

		if values is None:
			raise TypeError("Vector's value must be a finite real number")
		
		if not isinstance(values, list):
			raise TypeError("Vector() must contain a list")

		# values = [[int1, int2, int3]]
		if len(values) == 1 and isinstance(values[0], list) and all(isinstance(val, float) for val in values[0]):
			self.values = values
		# values = [[int1], [int2], [int3]]
		elif len(values) > 1 and all(
			isinstance(sub_values, list)
			and len(sub_values) == 1
			and isinstance(sub_values[0], float)
			for sub_values in values
		):
			self.values = values
		else:
			raise TypeError("Invalid type argument: list in Vector() contains a list of finite floats, or finite floats in list")

		# shape is neither None nor a tuple
		if shape is not None and shape is not isinstance(shape, tuple):
			TypeError("shape argument must be a tuple")

		# Compute automatically shape
		if shape is None:
			if len(values) == 1:
				shape = (1, len(values[0]))
			else:
				shape = (len(values), 1)

		if len(shape) != 2 or not all(isinstance(val, int) for val in shape):
			raise TypeError("Invalid type argument: Vector's shape contains int and is either <(1, n)> or <(n, 1)>")

		if len(values) != shape[0] or len(values[0]) != shape[1]:
			raise ValueError("Argument <shape> does not match the Vector's shape")

		self.shape = shape

	# v1.dot(v2)
	def dot(self, vec2):
		"""produces a dot product between two vectors of same shape"""
		if not isinstance(vec2, Vector):
			raise TypeError("Invalid type argument for dot()")
		
		if self.shape[0] != vec2.shape[1] or self.shape[1] != vec2.shape[0]:
			raise ValueError("Vectors must have the same shape for dot product")

		result = 0.0
		if self.shape[0] == 1:  # self = [[1., 2., 3.]] , vec2 = [[1.], [2.], [3.]]
			for i in range(self.shape[1]):
				result += self.values[0][i] * vec2.values[i][0]
		else:  # self = [[1.], [2.], [3.]] , vec2 = [[1., 2., 3.]]
			for i in range(vec2.shape[1]):
				result += self.values[i][0] * vec2.values[0][i]
		return result

	# v1.T()
	def T(self):
		"""transpose vector"""
		result = []
		if self.shape[0] == 1:# self = [[1., 2., 3.]]
			for i in range(self.shape[1]):
				result[i] = [self.values[0][i]]
		else:
			for i in range(self.shape[1]):# self = [[1.], [2.], [3.]]
				result[i] = self.values[i][0]

	def __str__(self):
		"""Returns the string to print with the Vector"""
		return f"{self.values}"





# __add__
# __radd__
# # add & radd : only vectors of the same shape.
# __sub__
# __rsub__
# # sub & rsub: only vectors of the same shape.
# __truediv__
# # truediv : only with scalars (to perform division of a Vector by a scalar).
# __rtruediv__
# # rtruediv : raises an NotImplementedError with the message "Division of a scalar by a Vector is not defined here."
# __mul__
# __rmul__
# # mul & rmul: only scalars (to perform multiplication of a Vector by a scalar).
# __str__
# __repr__
# # must be identical, i.e we expect that print(vector) and vector within python interpretor to behave the same, see correspo