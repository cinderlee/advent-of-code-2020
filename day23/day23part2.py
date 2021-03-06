MAX_NUM = 1000000
NUM_MOVES = 10000000

TEST_INPUT = '389125467'
INPUT = '315679824'


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, input_lst):
        self.access_dict = {}
        self.maxi = 0

        start = input_lst[0]
        prev = None
        for elem in input_lst:
            node = Node(elem)
            self.access_dict[elem] = node
            if prev:
                self.access_dict[prev].next = node
            prev = elem
            self.maxi = max(self.maxi, elem)

        self.access_dict[prev].next = self.access_dict[start]

    def get_cup(self,num):
        return self.access_dict[num]

    def get_max(self):
        return self.maxi

    def get_order(self):
        lst = []
        curr_cup = self.get_cup(1).next

        while curr_cup.data != 1:
            lst.append(str(curr_cup.data))
            curr_cup = curr_cup.next

        return ''.join(lst)

    def get_stars(self):
        first_star = self.get_cup(1).next
        second_star = first_star.next

        return first_star.data, second_star.data

def generate_input_list(input_txt):
    input_lst = [int(elem) for elem in input_txt]
    maxi = max(input_lst)
    for elem in range(maxi + 1, MAX_NUM + 1):
        input_lst.append(elem)

    return input_lst

def play_crab_game(linked_lst, start_cup, num_moves):
    maxi = linked_lst.get_max()
    curr_cup = linked_lst.get_cup(start_cup)
    count = 0

    while count < num_moves:
        first_cup = curr_cup.next
        second_cup = first_cup.next
        third_cup = second_cup.next
        curr_cup.next = third_cup.next

        three_cups_data = [first_cup.data, second_cup.data, third_cup.data]
        next_cup = curr_cup.data 

        while True:
            next_cup -= 1
            if next_cup == 0:
                next_cup = maxi
            if next_cup in three_cups_data:
                continue
            else:
                next_node = linked_lst.get_cup(next_cup)
                after = next_node.next
                next_node.next = first_cup
                third_cup.next = after
                break

        count += 1
        curr_cup = curr_cup.next

def solve(input_txt, num_moves):
    input_lst = generate_input_list(input_txt)
    linked_lst = LinkedList(input_lst)
    start_cup = int(input_txt[0])
    play_crab_game(linked_lst, start_cup, num_moves)

    first_star, second_star = linked_lst.get_stars()
    return first_star * second_star

def main():
    assert(solve(TEST_INPUT, NUM_MOVES) == 149245887792)
    print(solve(INPUT, NUM_MOVES))

main()