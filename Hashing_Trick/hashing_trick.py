import sys
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


if len(sys.argv) < 3 or len(sys.argv) > 4:
    print "Usage python hashing_trick.py path_to_data [N] [flag]"

flag = 1
if len(sys.argv) == 4:
    flag = int(sys.argv[3])

N =  10000
if len(sys.argv) >= 3:
    N = int(sys.argv[2])

if flag == 1:
    data = unsigned_hashing(sys.argv[1], N)
