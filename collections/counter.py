from collections import Counter

a = "aaaaaaabbbbbbbbccccccccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1)[0][0])