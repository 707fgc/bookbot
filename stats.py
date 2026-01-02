def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents

def total_word_count(filepath):
    with open(filepath) as file:
        num_words = len(file.read().split())
        return (f"Found {num_words} total words")

def total_char_appearance(filepath):
    counts = {}
    with open(filepath) as file:
        file_contents = file.read().lower()
        for char in file_contents:
            if char in counts:
                counts[char] += 1
            elif char.isalpha():
                counts[char] = 1
    return counts

def sort_on(items):
    return items["num"]

def sorted_chars(filepath):
    total_chars = total_char_appearance(filepath)
    out = []

    for item in total_chars:
        appendage = {"char": item, "num":total_chars[item]}
        out.append(appendage)

    out.sort(reverse=True, key=sort_on)
    return out

def print_list(filepath):
    sorted_list = sorted_chars(filepath)
    return sorted_list


