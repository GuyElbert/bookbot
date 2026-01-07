def count_words(text):
	words = text.split()
	num_words = len(words)
	print(f"Found {num_words} total words")

def count_characters(text):
    my_dict = {}
    for ch in text:
        ch = ch.lower()
        if ch in my_dict:
            my_dict[ch] += 1
        else:
            my_dict[ch] = 1
    return my_dict 

def sort_on(item):
    return item["num"]

def print_report(count_characters(text)):
    items = []
    for key in my_dict:
        num = my_dict[key]
        new_dict = {'letter': key, 'num': num}
        items.append(new_dict)
    items.sort(reverse=True, key=sort_on)
    return items
