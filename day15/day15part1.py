TEST_INPUT = [0, 3, 6]
INPUT = [14, 1, 17, 0, 3, 20]
LAST_TURN = 2020


def set_up(input_lst):
    '''
    Returns a dictionary containing number information for memory game.
    Dictionary details:
        curr_num: number to be spoken for the next turn
        spoken_numbers: a dictionary of numbers mapped to the last turn they were said
    '''
    prev_num = None
    curr_num = None
    spoken_numbers = {}
    turn = 0

    for num in input_lst:
        if curr_num is None:
            curr_num = num
        else:
            prev_num, curr_num = curr_num, num
            spoken_numbers[prev_num] = turn
        turn += 1

    return curr_num, spoken_numbers

def get_nth_number(curr_num, spoken_numbers_dict, n):
    '''
    Players take turn saying numbers. For each turn, if it is the first time 
    the most recent number was spoken, the current player says 0. Else,
    current player says how many turns apart ago the number was said previously. 
    '''
    turn = len(spoken_numbers_dict) + 1

    while turn < n:
        if curr_num not in spoken_numbers_dict:
            spoken_numbers_dict[curr_num] = turn
            curr_num = 0
        else:
            last_turn_spoken = spoken_numbers_dict[curr_num]
            spoken_numbers_dict[curr_num] = turn 
            curr_num = turn - last_turn_spoken

        turn += 1

    return curr_num

def solve(input_lst):
    '''
    Play the memory game!
    '''
    curr_num, spoken_numbers = set_up(input_lst)
    return get_nth_number(curr_num, spoken_numbers, LAST_TURN)

def main():
    assert(solve(TEST_INPUT) == 436)
    print(solve(INPUT))

main()
