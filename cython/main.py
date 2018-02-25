from cython_class import Solver
import sys

s = Solver()
s.init(sys.argv[1])

if len(sys.argv) >= 3 and sys.argv[2] == "full":
    s.compute_hash_full()
else:
    s.compute_hash()
