import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person name
    # value: 1
    key = record[0]
    value = 1
    mr.emit_intermediate(key, value)

def reducer(key, value):
    # key: person_name
    # value: a list of 1's (counts)
    mr.emit((key, len(value)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
