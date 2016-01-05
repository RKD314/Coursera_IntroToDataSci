import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: if MatrixA, key = (row, j=0:4)   if MatrixB, key = (i=0:4, col)
    # value: if MatrixA, value = ('a',col,a_ik) if MatrixB, value = ('b',row,b_kj)
    if record[0]=='a':                                      # MatrixA
        for x in range (0,5):
            key=(record[1],x)
            value = ('a',record[2],record[3])
            mr.emit_intermediate(key,value)
    else:                                                   # MatrixB
        for x in range (0,5):
            key=(x,record[2])
            value = ('b',record[1],record[3])
            mr.emit_intermediate(key,value)

def reducer(key, value):
    # key: a row nimber or b col number
    # value: a list of lists (the records of 'a' and all matching 'b')
    # find the list in value that has element 0 == 'a'
    
    number = 0
    for a_entry in value:
        if a_entry[0] == 'b':
            continue
        for b_entry in value:
            if b_entry[0] == 'a':
                continue
            else:
                if a_entry[1] == b_entry[1]:
                    number += a_entry[2]*b_entry[2]
                
    mr.emit((key[0],key[1],number))
    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
