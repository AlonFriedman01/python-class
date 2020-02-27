# Create a new <list>
a = [5]

# Create an alias identifier for this list
b = a
print id(a), id(b)

# Now change the <list> b in-place
b.append(1)

# And observe how this also changes a
# The alias is not broken by in-place operations
print a,b
print id(a),id(b)

# Create a <list>
a = [5]
 
# Create a new <list> with the same value
b = list(a)
 
# We now have two separate variables with identical but separate values
print a,b
print id(a), id(b)
 
# Same with the full slice technique:
b = a[:]
print a,b
print id(a), id(b)

# Create <tuple>
a = (5,)
 
# Try to force a copy
b = tuple(a)
 
# It didn't work...
print id(a), id(b)
 
# Neither does this
b = a[:]
print id(a), id(b)

v_list = [1,2,3]
 
for i in v_list:
    i = i+1
    print i
 
print v_list
v_list = [[1],[2],[3]]
 
for i in v_list:
    i.append(0)
    print i
 
print v_list
# copy and more
v_list = [[1],[2],[3]]

for i in v_list:
    i.append(0)
    print i
   
print v_list

