def contains_anagram(word_set):
    for word in word_set:
        for another_word in word_set:
            if len(word) == len(another_word) and word != another_word:
                contains_all_characters = True
                for ch in word:
                    if ch not in another_word:
                        contains_all_characters = False
                        break
                    else:
                        another_word = another_word.replace(ch, '', 1)
                if contains_all_characters:
                    return True
    return False


valid_line_count = 0
with open('.//input.txt') as txtInputFile:
    for line in txtInputFile:
        words = line.split()
        words_set = set(words)

        if len(words) == len(words_set) and not contains_anagram(words_set):
            valid_line_count += 1

print(valid_line_count)
