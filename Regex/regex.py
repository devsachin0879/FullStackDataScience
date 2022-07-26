import re

test_string = '123abc456789abc123ABC'

pattern = re.compile(r"abc")
matches = pattern.finditer(test_string)
print(type(matches))

for i in matches:
    print(i)

#############################################

test_string = '123abc456789abc123ABC'
matches = re.finditer(r"abc",test_string)
for i in matches:
    print(i)

################################################

#findall()

test_string = '123abc456789abc123ABC'
pattern = re.compile(r"abc")
matches = pattern.findall(test_string)
for i in matches:
    print(i)


################################################

#match()
#match looks for the pattern only in the beginning of the string as abc is not at begining it will give None
test_string = '123abc456789abc123ABC'
pattern = re.compile(r"abc")
matches = pattern.match(test_string)
print(matches)

# ## chaging the string
test_string = 'abc123456789abc123ABC'
pattern = re.compile(r"abc")
matches = pattern.match(test_string)
print(matches)

################################################

##search():- It scans through the string and looks for any location whether re matches

test_string = '123abc456789abc123ABC'
pattern = re.compile(r"abc")
matches = pattern.search(test_string)
print(matches)

################################################

# span,start,end
test_string = '123abc456789abc123ABC'
pattern = re.compile(r"abc")
matches = pattern.finditer(test_string)
for i in matches:
    print(i.span(), i.start(), i.end())

# group

test_string = '123abc456789abc123ABC'
pattern = re.compile(r"abc")
matches = pattern.finditer(test_string)
for i in matches:
    print(i.group())


#################################################
################ Meta Characters ################
#################################################


# All meta characters: . ^ $ * + ? { } [ ] \ | ( )

# . Any character (except newline character) "he..o"
# ^ Starts with "^hello"
# $ Ends with "world$"
# * Zero or more occurrences "aix*"
# + One or more occurrences "aix+"
# { } Exactly the specified number of occurrences "al{2}"
# [] A set of characters "[a-m]"
# \ Signals a special sequence (can also be used to escape special characters) "\d"
# | Either or "falls|stays"
# ( ) Capture and group


# More Metacharacters / Special Sequences
# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
#
# \d :Matches any decimal digit; this is equivalent to the class [0-9].
# \D : Matches any non-digit character; this is equivalent to the class [^0-9].
# \s : Matches any whitespace character; (space " " tab "\t" newline "\n")
# \S : Matches any non-whitespace character;
# \w : Matches any alphanumeric (word) character; this is equivalent to the class [a-zA-Z0-9_].
# \W : Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].
# \b Returns a match where the specified characters are at the beginning or at the end of a word r"\bain" r"ain\b"
# \B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word r"\Bain" r"ain\B"
# \A Returns a match if the specified characters are at the beginning of the string "\AThe"
# \Z Returns a match if the specified characters are at the end of the string "Spain\Z"




# test_string = '123abc456789abc123ABC'
pattern = re.compile(r".")
matches = pattern.finditer(test_string)
for i in matches:
    print(i.group())

test_string = '123abc456789abc123ABC....'
pattern = re.compile(r"\.")
matches = pattern.finditer(test_string)
for i in matches:
    print(i)


test_string = '123abc456789abc123ABC....'
pattern = re.compile(r"^123") ## starting with 123
matches = pattern.finditer(test_string)
for i in matches:
    print(i.group())
    print(i)

test_string = '123abc456789abc123ABC'
pattern = re.compile(r"ABC$") ## ending with ABC
matches = pattern.finditer(test_string)
for i in matches:
    print(i.group())
    print(i)



# test_string = 'hello 123_ heyho hohey'
pattern = re.compile(r"\d") ##digits
matches = pattern.finditer(test_string)
for i in matches:
    print(i)

test_string = 'hello 123_ heyho hohey'
pattern = re.compile(r"\D") ##non digit characters
matches = pattern.finditer(test_string)
for i in matches:
    print(i)


test_string = 'hello 123_ heyho hohey'
pattern = re.compile(r"\s") ##whitespace
matches = pattern.finditer(test_string)
for i in matches:
    print(i)

test_string = 'hello 123_ heyho hohey'
pattern = re.compile(r"\S") ##non-whitespace character
matches = pattern.finditer(test_string)
for i in matches:
    print(i)


test_string = 'hello 123_ heyho hohey'
pattern = re.compile(r"\w") ##alpha-numeric
matches = pattern.finditer(test_string)
for i in matches:
    print(i)

test_string = 'hello 123_ heyho hohey'
pattern = re.compile(r"\W") ## non-alphanumeric characters
matches = pattern.finditer(test_string)
for i in matches:
    print(i)



test_string = 'hello 123_ heyho hohey heyho'
pattern = re.compile(r"\bhey")
matches = pattern.finditer(test_string)
for i in matches:
    print(i)




#######################################################
#                          Sets

# A set is a set of characters inside a pair of square brackets [] with a special meaning. Append multiple conditions back-to back, e.g. [aA-Z].
# A ^ (caret) inside a set negates the expression.
# A - (dash) in a set specifies a range if it is in between, otherwise the dash itself.
#
# Examples:
# - [arn] Returns a match where one of the specified characters (a, r, or n) are present
# - [a-n] Returns a match for any lower case character, alphabetically between a and n
# - [^arn] Returns a match for any character EXCEPT a, r, and n
# - [0123] Returns a match where any of the specified digits (0, 1, 2, or 3) are present
# - [0-9] Returns a match for any digit between 0 and 9
# - 0-5 Returns a match for any two-digit numbers from 00 and 59
# - [a-zA-Z] Returns a match for any character alphabetically between a and z, lower case OR upper case


test_string = 'hello 123_'
pattern = re.compile(r"[lo]")
matches = pattern.finditer(test_string)
for i in matches:
    print(i)


test_string = 'hello 123_'
pattern = re.compile(r"[a-z]") ## all lowercase character a to z
matches = pattern.finditer(test_string)
for i in matches:
    print(i)


test_string = 'hello 1023_'
pattern = re.compile(r"[1-9]") ## nums from 1 to 9
matches = pattern.finditer(test_string)
for i in matches:
    print(i)


test_string = 'helloHELLO 1023_'
pattern = re.compile(r"[a-zA-F0-2]") ## all lowercase, uppercase A to F and nums from 0 to 2
matches = pattern.finditer(test_string)
for i in matches:
    print(i)


#################################################################
# Quantifier
# * : 0 or more
# + : 1 or more
# ? : 0 or 1, used when a character can be optional
# {4} : exact number
# {4,6} : range numbers (min, max)


test_string = 'hello_123'
pattern = re.compile(r'\d*')
matches = pattern.finditer(test_string)
for i in matches:
    print(i)


test_string = 'hello_123'
pattern = re.compile(r'\d+')
matches = pattern.finditer(test_string)
for i in matches:
    print(i)


test_string = 'hello_123'
pattern = re.compile(r'_\d')
matches = pattern.finditer(test_string)
for i in matches:
    print(i)


test_string = 'hello123'
pattern = re.compile(r'_?\d') ## here _ is optional
matches = pattern.finditer(test_string)
for i in matches:
    print(i)

test_string = 'hello_1_2_3'
pattern = re.compile(r'_?\d') ## here _ is optional
matches = pattern.finditer(test_string)
for i in matches:
    print(i)


test_string = 'hello123'
pattern = re.compile(r'\d{3}') ## exactly 3 digits
matches = pattern.finditer(test_string)
for i in matches:
    print(i)

test_string = 'hello123'
# here we have only 3 digits so it will return nothing
pattern = re.compile(r'\d{4}') ## 4 digits
matches = pattern.finditer(test_string)
for i in matches:
    print(i)


test_string = 'hello123'
pattern = re.compile(r'\d{1,5}') ### there can be 1 to 5 digits in the string
matches = pattern.finditer(test_string)
for i in matches:
    print(i)

########################################################################

dates = '''
hello
01.04.2020

2020-04-01
2020-05-23
2020-06-11
2020-07-11
2020-08-11

2020/04/02

2020_04_04
2020_04_04
'''

pattern = re.compile("\d{4}.\d{2}.\d{2}") ## 4digits .(any character) 2digits .(any character) 2characters
matches = pattern.finditer(dates)
for i in matches:
    print(i.group())



# ## find dates with - format
pattern = re.compile("\d{4}-\d{2}-\d{2}")
matches = pattern.finditer(dates)
for i in matches:
    print(i.group())



# ## find dates with - and / format
pattern = re.compile("\d{4}[-/]\d{2}[-/]\d{2}")
matches = pattern.finditer(dates)
for i in matches:
    print(i.group())


##   find dates for month may,june and july
pattern = re.compile("\d{4}[-/]0[5-7][-/]\d{2}")
matches = pattern.finditer(dates)
for i in matches:
    print(i.group())


######################################################################
## CONDITIONS

my_string = """
hello world
123
2020-05-20
Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T
"""

## extract only names from the above string
pattern = re.compile(r"(Mr|Mrs|Ms)\.?\s\w+")
matches = pattern.finditer(my_string)
for i in matches:
    print(i)




emails = """
pythonengineer@gmail.com
Python-engineer@gmx.de
python-engineer123@my-domain.org
"""

# pattern = re.compile(r'[a-zA-Z0-9-]+@[a-z-]+\.[a-z]+')
# matches = pattern.finditer(emails)
# for i in matches:
#     print(i.group())

##grouping === use () for grouping
pattern = re.compile(r'([a-zA-Z0-9-]+)@([a-z-]+)\.([a-z]+)')
matches = pattern.finditer(emails)
for i in matches:
    print("group0")
    print(i.group(0))
    print("------------")
    print("group1")
    print(i.group(1))
    print("------------")
    print("group2")
    print(i.group(2))
    print("------------")
    print("group3")
    print(i.group(3))
    print("------------")



###################################################
##### Modify string

## split:- split string into a list wherever character matches
## sub:- finds the substring where character matches and replaces them with a different string

##split()
test_string = '123abc456789abc123ABC'
pattern = re.compile(r"abc")
splitted = pattern.split(test_string)
print(splitted)


##sub()
test_string = 'hello world, you are the best world'
pattern = re.compile(r"world")
mysub = pattern.sub("planet",test_string)
print(mysub)


urls = """
hello
2020-05-20
http://python-engineer.com
https://www.python-engineer.org
http://www.pyeng.net
"""

pattern = re.compile(r"(https?://)(www\.)?([a-zA-Z-]+)(\.[a-zA-Z]+)")
matches = pattern.finditer(urls)
for i in matches:
    print(i.group(1))

sub = pattern.sub(r"\2\3\4",urls)
print(sub)