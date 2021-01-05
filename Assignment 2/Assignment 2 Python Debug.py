# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Assignment 2 - Alejandro Vera
# %% [markdown]
# Mutable Objects are objects that can be changed such as lists, while Immutable Objects are objects that cannot be changed such as tuples. 
# 
# You would want to use a mutable object when dealing with a list you want to transform into something else. 
# You would want to use an immutable object when you're wanting sometihng that's more static in nature and don't need to worry about changing.
# 
# By: Alejandro Vera
# 
# %% [markdown]
# ## Lists

# %%
list1 = []

# here we will work backwords from 10 and append a random number to the list
for i in range(10, 0, -1):
    list1.append((i * 64) % 15)

# sort the list 
list1.sort();

print(list1)

# %% [markdown]
# ## Tuples

# %%
# take the first 5 values in list1 and put them in tuple1
tuple1 = list1[:5]
# take the last 5 values in list1 and put them in tuple2
tuple2 = list1[5:]

print(tuple1)
print(tuple2)

# combine the two tuples into another tuple
combined = (tuple1, tuple2)

print(combined)

# %% [markdown]
# ## Dictionaries

# %%
favorateFoods = {
    "Enchiladas" : ['cheese', 'tortillas', 'salsa', 'potatos'],
    "Three Milk Cake" : ['condensed milk', 'sugar', 'eggs'],
    "Chicken Alfredo" : ['chicken', 'cheese', 'pasta']
}

# print the ingredients from the dic using the key
print(favorateFoods["Enchiladas"])
print(favorateFoods["Three Milk Cake"])
print(favorateFoods["Chicken Alfredo"])


# %%
fav_animals = ['shark', 'otter', 'platypus', 'bear', 'dolphin']

# for every animal in fav_animals print animal
for animal in fav_animals:
    print(animal)

animal_rankings = [2,4,5,3,1]

# zip fav_animals with animal rankings so they correctly correspond
zipped = dict(zip(animal_rankings, fav_animals))

print(zipped)

hobbies_list = ['longboarding', 'soccer']

# enumerate my hobbies list
fav_hobbies = enumerate(hobbies_list)

for counter, value in enumerate(hobbies_list):
    print(counter, value)

# %% [markdown]
# ## Data Cleaning and Dictionary Building

# %%
# importing list
data = [' chase!', 'on', 'wednesday', 'reported', 'an', 'unexpected', 'drop', 'in', 'profit', 'during', 'a', 'sluggish', 'fourth', 'quarter', 'the', 'bank', 'said', 'its', 'earnings', 'fell', '7', 'percent', 'to', '4.9', 'billion', 'or', '1.19', 'a', 'share', 'from', '5.6', 'billion', 'or', '1.30', 'a', 'share', 'in', 'the', 'period', 'a', 'year', 'earlier', 'the', 'most', 'recent', 'results', 'fell', 'short', 'of', 'the', '1.31', 'a', 'share', 'expected', 'by', 'analysts', 'surveyed', 'by', 'THOMSON??', 'reuters', 'net', 'revenue', 'at', 'the', 'bank', 'dropped', '3', 'percent', 'to', '22.5', 'billion', 'from', 'the', 'fourth', 'quarter', 'of', '2013', 'on', 'a', 'so-called', 'managed', 'basis', 'revenue', '#was', '23.55', 'billion', 'slightly', 'below', 'the', '23.6', 'billion', 'anticipated', 'by', 'analysts', 'the', 'bank', '’', 's', 'SHARES', 'were', 'down', '4', 'percent', 'in', 'midmorning', 'trading', 'for', '2014', 'as', 'a', 'whole', 'jpmorgan!', ' reported', 'profit!', 'of', '21.8', 'billion', 'a', '21', 'percent', 'increase', 'and', 'the', 'highest', 'ever', 'annual', 'profit?', 'for', 'the', 'company', 'the', 'bank', '’', 's', 'quarterly', 'profit', 'was', 'hurt', 'by', '900', 'million', 'in', 'new', 'legal', 'expenses', 'or', '1.1', 'billion', 'on', 'a',  'pretax ', 'basis', 'as', 'the', 'company', 'prepared', 'to', 'SETTLE', 'an', 'investigation', 'into', 'manipulation', 'of', 'the', 'foreign', 'currency', 'markets', 'by', 'the', 'big', 'banks', 'these', 'are', 'the', 'latest', 'big', 'legal', 'costs', 'being', 'absorbed', 'by', ' jpmorgan ', 'in', 'the', 'wake', 'of', 'the', 'financial', 'crisis']

# %% [markdown]
# here is where all the magic happens 
# 
# we take the word then remove the punctuation
# 
# we convert it to lowercase
# 
# finally we append it to the clean_list only if it isn't empty
# 
# trims the string removing spaces

# %%
import re
import string

def clean_words(data_list):
    clean_list = []
    for word in data_list:
        temp = str.lower(re.sub(r'[^\w\s]', '', word))
        if (len(temp) > 0):
            clean_list.append(temp.strip())
    return clean_list


# %%
data = clean_words(data)

# %% [markdown]
# The following code tell you which is the 58th item in the list
# 

# %%
print('The 58th value is: ' + data[57])

# %% [markdown]
# Here is a for loop that checks if the value is already in the list and if its not then it is added. 

# %%
unique = []

for x in data:
    if x not in unique:
        unique.append(x)

print(unique)


# %%



# %%
letter_dict = dict()

for word in unique:
    # create the new key value pairs
    if word[0] in letter_dict:
        temp = []
        # if isinstance(letter_dict[word[0]], list):
        #     temp = letter_dict[word[0]].copy()
        # else: 
        temp.append(letter_dict[word[0]])
        temp.append(word)
        letter_dict[word[0]] = temp
    else:
        letter_dict[word[0]] = word

# print(letter_dict)


# %%
letter_dict['b']


