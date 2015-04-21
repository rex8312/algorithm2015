__author__ = 'Hyunsoo'


def process(states):
    next_states = list()
    for state in states:
        next_states.append(state + 1)
        next_states.append(state + 2)
        #next_states.append(state + 0)
    return next_states


def print_count(states):
    count = dict()
    for state in states:
        count.setdefault(state, 0)
        count[state] += 1

    from pprint import pprint
    pprint(count)
    return count

if __name__ == '__main__':
    init_states = [0]
    states = init_states
    for i in range(5):
        states = process(states)
        print i + 1,
        print_count(states)
