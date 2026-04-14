import random
from collections import defaultdict


# rand_list =

# list_comprehension_below_10 =

# list_comprehension_below_10 =

def flatten_dict(d, key='', sep=''):
    items={}
    for k, v in d.items():
        key_new= f"{key}{sep}{k}" if key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, key_new, sep=sep))
        else:
            items[key_new]= v
    return items


## deduplicate an array
arr= [3,1,2,3,2,4,1]
unique=[]
def deduplicate_array(arr):
    unique=[]
    for x in arr:
        if x not in unique:
            unique.append(x)
    return unique


##group a list of dicts by key
def group_by_key(data, key):
    grouped= defaultdict(list)
    for item in data:
        grouped[item[key]].append(item)

    return dict(grouped)
