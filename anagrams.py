
def function_reverse_word(word):
    # the function iterates over the letters in a word and reverses them
    reverse_letter_list = []
    non_letter_list = []

    for every_letter in word:
        if every_letter.isalpha():
            reverse_letter_list.append(every_letter)
            non_letter_list.append(None)
        else:
            non_letter_list.append(every_letter)

    reverse_letter_list = reverse_letter_list[:: -1]

    for element_in_non_letter_list in range(len(word)):
        if non_letter_list[element_in_non_letter_list] is not None:
            pass
        else:
            non_letter_list[element_in_non_letter_list] = reverse_letter_list[0]
            reverse_letter_list.pop(0)

    reversed_word = "".join(non_letter_list)

    return reversed_word


def text_flip_function(text):
    # reverses each word in the text
    reversed_words_list = []
    words_list = list(text.split(" "))

    for elem in words_list:
        reversed_words_list.append(function_reverse_word(elem))

    final_reversed_text = " ".join(reversed_words_list)

    return final_reversed_text


if __name__ == "__main__":
    cases = [
       ("abcd efgh", "dcba hgfe"),
       ("a1bcd efg!h", "d1cba hgf!e"),
       ("", ""),
    ]

    for text, reversed_text in cases:
        assert text_flip_function(text) == reversed_text
