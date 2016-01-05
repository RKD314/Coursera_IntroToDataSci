import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order_id
    # value: whole record
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, value):
    # key: order_id
    # value: a list of lists (the records of 'order' and all matching 'line_items')
    # find the list in value that has element 0 == 'order'
    for orders in value:
        if orders[0] != "order":                            # if the first element of the list is 'order', 
            continue                                        # move to the next list
        for line_items in value:                            # iterate over the list of lists again
            join_list = []
            if not line_items[0] == "line_item":            # if the first element of the list is not 'line_item'
                continue                                    # go to the next list
            else:                                           # otherwise
                join_list.append(orders)
                join_list.append(line_items)                # add the list to join_list
                mr.emit(([val for subl in join_list for val in subl]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
