__author__ = 'rex8312'

import pylab as pl
import shelve


if __name__ == '__main__':
    db = shelve.open('results.pkl')
    for key in db.keys():
        puzzle = db[key]
        #pl.imshow(puzzle, interpolation='none', cmap='hsv')
        pl.imshow(puzzle, interpolation='none', cmap='gray')
        pl.savefig('data3/{}.png'.format(key))
    db.close()