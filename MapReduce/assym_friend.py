import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: (A,B)
    # value: 1
    names=sorted(record)
    key = names[0]+","+names[1]
    value = 1
    mr.emit_intermediate(key, value)
    
def reducer(key, list_of_values):
    # key: personApersonB
    # value: a list of 1s (counts)
    total = 0
    for v in list_of_values:
      total += v
    if total==1:
        two_names=key.split(",",2)
        out_list = [[two_names[0],two_names[1]], [two_names[1],two_names[0]]]
        for pair in out_list:
            mr.emit(tuple(pair))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
