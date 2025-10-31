# a = [1, 2, 3]
# b = ['x', 'y', 'z']

# zip() : generator of tuples from 2 iterables
# zip(a, b) = (1, 'x'), (2, 'y'), (3, 'z')

# enumerate() : generator of tuples(idx, val) from an iterable
# enumerate(b) = (0, 'x'), (1, 'y'), (2, 'z')

class Evaluator:

	@staticmethod
	def parsing(coefs=None, words=None):
		if not hasattr(coefs, '__iter__') or not hasattr(words, '__iter__'):
			raise TypeError("coefs and words must be iterables")
		if not all(isinstance(c, (int, float)) for c in coefs):
			raise TypeError("coefs must contain only int or float")
		if not all(isinstance(w, str) for w in words):
			raise TypeError("words must contain only str")
		if len(coefs) != len(words):
			raise ValueError("Two arguments must have the same length")

	@staticmethod
	def zip_evaluate(coefs=None, words=None):
		Evaluator.parsing(coefs, words)
		return sum(c * len(w) for c, w in zip(coefs, words))

	@staticmethod
	def enumerate_evaluate(coefs=None, words=None):
		Evaluator.parsing(coefs, words)
		return sum(c * len(words[i]) for i, c in enumerate(coefs))
