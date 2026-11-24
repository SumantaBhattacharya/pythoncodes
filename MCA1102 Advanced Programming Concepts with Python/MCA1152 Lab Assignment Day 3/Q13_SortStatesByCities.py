# 13. Given a dictionary as stated in the sample input, 
# (i) Sort the states in order by the first city name. (Sample Output: ['West Bengal', 
# 'Maharastra','Kerala']) 
# (ii) Sort the states by the length of the second city name, break ties of equal length by 
# name of the second cities. (Sample Output: ['Maharastra', 'West Bengal', 'Kerala']) 
# (iii) Sort the states in order by the number of cities having length greater than 6. 
# (Sample  
# Output: ['Maharastra', 'Kerala', 'West Bengal']) 
# Sample 
# Input: {"Kerala": ["Kannur", "Palakkad", "Thalassery"], 
# "Maharastra": ["Bhandara", "Nagpur", "Wardha"],  
# "West Bengal": ["Asansol", "Basirhat", "Bardhaman"]}

state_cities = {
    "Kerala": ["Kannur", "Palakkad", "Thalassery"],
    "Maharastra": ["Bhandara", "Nagpur", "Wardha"],
    "West Bengal": ["Asansol", "Basirhat", "Bardhaman"]
}

def getFirst_city(state):
    return state_cities[state][0]

# (i) Sort the states in order by the first city name.
sort_i = sorted(state_cities, key= lambda s: state_cities[s][0])

print(sort_i)

# (ii) Sort by the length of the second city name, 
# tie-break by name of the second city.
sort_ii = sorted(state_cities, key= lambda s: (len(state_cities[s][1]), state_cities[s][1]))

print(sort_ii)

# (iii) Sort the states in order by the number of cities having length greater than 6. 
# Kerala 
#     "Kannur" → 6 >6 No
#     "Palakkad" → 8 >6 Yes
#     "Thalassery" → 10 >6 Yes
# = 2

# Maharastra 
#     "Bhandara" → 8 >6 Yes
#     "Nagpur" → 6 >6 No
#     "Wardha" → 6 >6 No
# = 1

# West Bengal 
#     "Asansol" → 7 >6 Yes
#     "Basirhat" → 8 >6 Yes
#     "Bardhaman" → 9 >6 Yes
# = 3

# Kerala = 2, Maharastra = 1, West Bengal = 3
# sort
# Maharastra, Kerala, West Bengal

def cityCounter_greaterThan6(s):
    count = 0
    for i in state_cities[s]:
            len_city = i.__len__()
            if len_city > 6:
                count = count+1

    return count

sort_iii = sorted(state_cities, key= cityCounter_greaterThan6)

print(sort_iii)