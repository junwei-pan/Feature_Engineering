import sys
import argparse
# Usage: 'python hashing_trick.py path_to_data [flag]'
# The format of the data should be the same as libsvm
# Flag:
#   1(default) unsigned_hashing
#   2 signed_hashing
#   3 multiple_hashing

def unsigned_hashing(path, N):
    res_lst = []
    for line in open(path):
        d = {}
        row = line.strip().split(' ')
        for r in row[1:]:
            print r
            (index, value) = map(float, r.split(':'))
            index_hashed = hash('feature ' + str(index)) % N
            d.setdefault(index_hashed, 0.0)
            d[index_hashed] += value
        sort = sorted(d.iteritems(), key = lambda dd: dd[0])
        res_lst.append([row[0], sort])
    for res in res_lst:
        print res
    return res_lst


parser = argparse.ArgumentParser(description = 'Options for this script')
parser.add_argument('-i', dest = 'path_input', help = 'input path')
parser.add_argument('-N', default = 10000, type = int, help = 'number of indexes after hashing')
parser.add_argument('-f', dest = 'flag', default = 1, type = int, help = 'flag, 1 is unsigned hashing, 2 is signed hashing, 3 is multiple hashing')

args = parser.parse_args(sys.argv[1:])
if args.flag == 1:
    unsigned_hashing(args.path_input, args.N)
