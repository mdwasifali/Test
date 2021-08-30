utensils = {"fork","spoon","knife"}
dinnerset= {"plate","cup"," bowl","knife"}
utensils.add("babyspoon")
dinnerset.remove("plate")
for i in utensils:
    print(i)
x= utensils.union(dinnerset)
y= utensils.intersection(dinnerset)
print(x)
print(y)
