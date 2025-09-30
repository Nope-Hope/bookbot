from stats import get_num_words

def get_book_text(filepath):
	with open(filepath) as f:
		# do something with f (the file) here
		# f is a file object
		file_contents = f.read()
		return file_contents
def main():
	num_words = get_num_words(get_book_text("./books/frankenstein.txt"))
	print(f"Found {num_words} total words")

main()
