import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # record is [sequence id (string), nucleotides (string)]
    # key: nucleotide - the last 10 characters
    # value: 1
    key = record[1][0:(len(record[1])-10)]
    value = 1
    mr.emit_intermediate(key, value)

def reducer(key, value):
    # key: a trimmed nucleotide
    # value: a list of 1s (counts)
    mr.emit((key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
