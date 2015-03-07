import sys
import argparse
# Usage: 'python hashing_trick.py path_to_data [flag]'
# The format of the data should be the same as libsvm
# Flag:
#   1(default) unsigned_hashing
#   2 signed_hashing
#   3 multiple_hashing

class hashing_trick:
    '''

    Hashing trick is used to decrease the feature dimension such that the features can be stored into memory.

    Parameters
    ----------
    
    path : string, 
        Input path of data with format like libsvm

    N : int, optional(default 10000)
        The feature dimension after being hashed

    flag : int, optional(default 1)
        The flag tells which kind of hashing trick algorithm is used
        1: unsigned hashing
        2: signed hashing
        3: multiple hashing

    '''
    
    def __init__(self, path, N, flag):
        self.path = path
        self.N = N
        self.flag = flag
        self.res_lst = []

    def hash_features(self):
        for line in open(self.path):
            row = line.strip().split(' ')
            d = {}
            if self.flag == 1:
                d = self.unsigned_hashing(row[1:])
            elif self.flag == 2:
                d = self.signed_hashing(row[1:])
            elif self.flag == 3:
                d = self.multiple_hashing(row[1:])
            sort = sorted(d.iteritems(), key = lambda dd: dd[0])
            self.res_lst.append([row[0], sort])
        for res in self.res_lst:
            print res

    def unsigned_hashing(self, lst):
        d = {}
        for l in lst:
            (index, value) = map(float, l.split(':'))
            index_hashed = hash('feature' + str(index)) % self.N
            d.setdefault(index_hashed, 0.0)
            d[index_hashed] += value
        return d


    def signed_hashing(self, lst):
        d = {}
        for l in lst:
            (index, value) = map(float, l.split(':'))
            index_hashed = hash('feature' + str(index)) % self.N
            sign = hash('sign' + str(index)) % 2
            d.setdefault(index_hashed, 0.0)
            d[index_hashed] += (2 * sign - 1) * value
        return d
parser = argparse.ArgumentParser(description = 'Options for this script')
parser.add_argument('-i', dest = 'path_input', help = 'input path')
parser.add_argument('-N', default = 10000, type = int, help = 'number of indexes after hashing')
parser.add_argument('-f', dest = 'flag', default = 1, type = int, help = 'flag, 1 is unsigned hashing, 2 is signed hashing, 3 is multiple hashing')

args = parser.parse_args(sys.argv[1:])
ht = hashing_trick(args.path_input, args.N, args.flag)
ht.hash_features()
