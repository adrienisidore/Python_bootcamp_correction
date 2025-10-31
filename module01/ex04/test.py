from eval import Evaluator

def main():

	coefs = [2, 3, 1.5]
	words = ["hello", "world", "AI"]

	zip_result = Evaluator.zip_evaluate(coefs, words)
	print("zip_evaluate result:", zip_result)

	enum_result = Evaluator.enumerate_evaluate(coefs, words)
	print("enumerate_evaluate result:", enum_result)

if __name__ == "__main__":
	main()