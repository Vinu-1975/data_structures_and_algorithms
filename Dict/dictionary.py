my_dict = {}
print(my_dict)

my_dict["name"] = "Vinayak"
my_dict["age"] = 20

print(my_dict["name"])

if "country" in my_dict:
    print("'country' exists")
else:
    print("'country' does not exist")

#delete age
if "age" in my_dict:
    del my_dict["age"]

print(my_dict)
print(len(my_dict))

my_dict["age"]=25
my_dict["address"] = "abc"
my_dict['country'] = "india"

for key in my_dict.keys():
    print(key,end = " ")
print()

for values in my_dict.values():
    print(values,end = " ")
print() 

for key,value in my_dict.items():
    print('{} : {}'.format(key,value))