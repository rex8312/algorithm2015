__author__ = 'rex8312'

import pylab as pl
import shelve


if __name__ == '__main__':
    db = shelve.open('results.pkl')
    for key in db.keys():
        puzzle = db[key]
        pl.imshow(puzzle, interpolation='none', cmap='hsv')
        pl.savefig('data2/{}.png'.format(key))
    db.close()