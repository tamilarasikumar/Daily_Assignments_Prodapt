import collections
dict1={"name":"renuka","age":22}
dict2={"nam":"dharani","ag":25}
comb_dict=collections.ChainMap(dict1,dict2)
print(comb_dict.maps)
print(list(comb_dict.keys()))
print(list(comb_dict.values()))
# create a simple menu driven application 1.add employee2.view employees 
# 1.we have to read empid,empname,designation,salary,address,phone number,pincode
# create a dictinary for this data and when i click on view employees we have to merge all dictionries and print
# it as an api