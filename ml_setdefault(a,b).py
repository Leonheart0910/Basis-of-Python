
# Returns the key value available in the dictionary and if given key is not
# available then it will return provided default value.

ml = {'Name': 'Zara', 'Age':7, 1: 95478089}
print('Age=', ml.setdefault('Age', None))
print('Sex=', ml.setdefault('Sex', None))
print(1, dict.setdefault(1, 'we do not find this'))