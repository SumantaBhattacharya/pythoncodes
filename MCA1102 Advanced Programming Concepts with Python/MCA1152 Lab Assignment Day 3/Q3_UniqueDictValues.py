# Write Python scripts to: 3. Extract unique values from a dictionary.

dictionary = {"name": "SUMANTA BHATTACHARYA", "roll no": 2682005, "course": "Master of Computer Applications"}

val = dictionary.values()

# unique - as nothing mentioned regarding mentaining the order
# uniVal = set(val)

uniVal = []

# this maintain the order and ensures unique values
for i in val:
    if i not in uniVal:
        uniVal.append(i)

print(uniVal)