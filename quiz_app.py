import sys
import random
import itertools


def create_question(text):
    text = text.strip()
    question, correct_answer, options_str = text.split(";")
    
    options = options_str.split(',')
    options.append(correct_answer)
    random.shuffle(options)

    print(question)

    correct_index = None
    for i, item in enumerate(options, start=1):
        print(f'{i}. {item}')

        if item == correct_answer:
            correct_index = i

    return question, options, correct_index



def isGood(answer, correct_index):
     if answer == correct_index:
        return 1
     else: return 0

def main():
    profession = sys.argv[1]
    num_of_question = int(sys.argv[2])

    with open(f'questions/{profession}.txt', mode='r', encoding='utf-8') as read_file:
        numGoodAnswers = 0

        for line in itertools.islice(read_file, num_of_question):
            question, options, correct_index = create_question(line)
            answer = int(input())
            numGoodAnswers += isGood(answer, correct_index)
        

        print(f'You answered {numGoodAnswers} / {num_of_question} good answers!!!')

if __name__ == '__main__':
    main()








