import sys
from stats import count_words
from stats import count_characters
from stats import print_report

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
		return file_contents

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		
		#count_words(get_book_text("books/frankenstein.txt"))
		shmeem = count_characters(get_book_text(sys.argv[1]))
		#print(shmeem)
		shmlu = print_report(shmeem)
		print("============ BOOKBOT ============")
		print("Analyzing book found at "+ str(sys.argv[1]) + "...")
		print("----------- Word Count ----------")
		count_words(get_book_text(sys.argv[1]))
		print("--------- Character Count -------")
		for item in shmlu:
			scree = item['letter']
			if scree.isalpha():
				print(item['letter'] + ": " + str(item['num']))
		
		print("============= END ===============")
main()  
