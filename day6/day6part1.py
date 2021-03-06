FILE_TEST_NM = 'day6testinput.txt'
FILE_NM = 'day6input.txt'

def count_total_answers(file_nm):
    '''
    Returns the sum of the sum of questions to which anyone 
    answered yes for each group. 
    '''
    file = open(file_nm, 'r')
    total_answers = 0
    answers = set()

    for line in file:
        line = line.strip('\n')
        if not line:
            # collect group answers
            total_answers += len(answers)
            answers = set()
        else:
            for ans in line:
                answers.add(ans)

    file.close()

    # last group also needs to be accounted for!
    total_answers += len(answers)
    return total_answers

def main():
    assert(count_total_answers(FILE_TEST_NM) == 11)
    print(count_total_answers(FILE_NM))

main()