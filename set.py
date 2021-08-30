utensils = {"fork","spoon","knife"}
dinnerset= {"plate","cup"," bowl","knife"}
utensils.add("babyspoon")
dinnerset.remove("plate")
for i in utensils:
    print(i)
x= utensils.union(dinnerset)
y= utensils.intersection(dinnerset)
print("The results of the intersection of the two sets")
print(x)
print(y)
