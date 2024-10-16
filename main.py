import re

path_to_file = './books/frankenstein.txt'

def get_book_text(path):
    with open(path) as f:
        return f.read()
def get_num_words(text):
    words = text.split()
    return len(words)
def get_char_occurence(text):
    occurences = dict()
    for char in text:
      lowered_char = char.lower()
      if lowered_char in occurences:
          occurences[lowered_char] += 1
      else:
          occurences[lowered_char] = 1
    return occurences
def format_char_occurence(dict):
    occurences_list = []
    for i in dict:
      if i.isalpha():
        occurences_list.append({'char': i, 'occurences': dict[i]})
    occurences_list.sort(key=lambda x: x['occurences'], reverse=True)
    return occurences_list

def main():
    with open(path_to_file) as f:
        text = get_book_text(path_to_file)
        num_words = get_num_words(text)
        character_occurence = get_char_occurence(text)
        sorted_character_occurence = format_char_occurence(character_occurence)

        print(f'--- Begin report of {path_to_file} ---')
        print(f'{num_words} words found in the document')
        print('')
        for char_occ in sorted_character_occurence:
            print(f'The \'{char_occ["char"]}\' character was found {char_occ["occurences"]} times')
        print('--- End report ---')

main()