# Exercises: Level 1
# . Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

# . Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
# . Insert multiple IT companies at once to the set it_companies
it_companies.update(["Tata Consultancy Services","Infosys","Wipro"])
print(it_companies)
# . Remove one of the companies from the set it_companies
it_companies.remove("IBM")
print(it_companies)
# . What is the difference between remove and discard
# print(it_companies.discard("HCL"))
# print(it_companies.remove("HCL"))

# . Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.update(B)
print(A)

# . Find A intersection B
print(A.intersection(B))
# . Is A subset of B
print(A.issubset(B))

# . Are A and B disjoint sets
print(A.isdisjoint(B))
# . Join A with B and B with A
print(A.union(B))
print(B.union(A))
# . What is the symmetric difference between A and B
print(A.symmetric_difference(B))


# 7. Delete the sets completely
del A
del B

# Exercises: Level 3
# . Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages=[23,54,76,28,87,24]
print(len(ages))    #list length
st=set(ages)
print(len(ages))    #set length
# . Explain the difference between the following data types: string, list, tuple and set
string="difference between the following data types"
lst=['difference between the following data types']
tpl=('difference between the following data types')
st={'difference between the following data types'}
# . I am a teacher and I love to inspire and teach people. How many unique words have been used
sentence=('I am a teacher and I love to inspire and teach people.')
# in the sentence? Use the split methods and set to get the unique words.
print(set(sentence.split()))
unique_words=(sentence)
print(unique_words)
