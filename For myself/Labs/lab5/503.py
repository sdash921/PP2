import re
a = input("Tell me how was your day going: ")
pattern_bad_words = re.compile("(bad|terrible|awful|horrible|worst)") #we can prepare pattern by compiling its and then use it to search in the string
pattern_good_words = re.compile("(wonderful|amazing|perfect|great)")
pattern_mid_words = re.compile("(good|okay)")



find_b = re.findall(pattern_bad_words,a) #findall returns the amount with view of list like ['bad', 'awful', 'worst']
find_g = re.findall(pattern_good_words,a) #finds words like ['amazing','wonderful']
find_m = re.findall(pattern_mid_words,a) #finds words like ['good','amazing']

b,g,m = 0, 0, 0

for i in find_b:#simple function to use after we got list
    b = b + 1
for i in find_g:
    g = g + 1
for i in find_m:
    m = m + 1
print("Bad words:", b," Good woords:", g," Mid words:", m)