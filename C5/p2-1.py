__author__ = 'Hyunsoo'


def process(states):
    next_states = list()
    for state in states:
        next_states.append(state + 1)
        next_states.append(state + 2)
    return next_states


def print_prob(states):
    prob = dict()
    for state in states:
        prob.setdefault(state, 0.0)
        prob[state] += 1. / len(states)

    from pprint import pprint
    pprint(prob)
    return prob

if __name__ == '__main__':
    init_states = [0]
    states = init_states
    for i in range(20):
        states = process(states)
        print i + 1,
        prob = print_prob(states)

    xs, ys = zip(*sorted(prob.items()))
    print ys
    import pylab as pl
    pl.plot(xs, ys)
    pl.show()
