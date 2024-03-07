import enchant

def correct_spelling(text):
    checker = enchant.Dict("en_US")  # Creating a spell checker instance for US English
    words = text.split()
    corrected_words = []
    for word in words:
        if not checker.check(word):
            suggestions = checker.suggest(word)
            if suggestions:
                corrected_words.append(suggestions[0])  # Choosing the first suggestion as correction
            else:
                corrected_words.append(word)  # If no suggestion is available, keep the word unchanged
        else:
            corrected_words.append(word)  # If the word is already correct, keep it unchanged
    return ' '.join(corrected_words)

def main():
    input_file_path = "D:/port/work-1/work/파이썬연습2월/16.맞춤법 검사기/틀린맞춤법.txt"
    output_file_path = "D:/port/work-1/work/파이썬연습2월/16.맞춤법 검사기/수정맞춤법.txt"

    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    corrected_content = correct_spelling(content)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(corrected_content)

if __name__ == "__main__":
    main()