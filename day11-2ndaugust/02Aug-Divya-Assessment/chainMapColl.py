import collections

dict1 = {"name":"divya","age":23}
dict2 = {"name":"amar","age":24}
combine_dict = collections.ChainMap(dict1,dict2)
print(combine_dict.maps)                                # to print dict in list
print(list(combine_dict.keys()))
print(list(combine_dict.values()))