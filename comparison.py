set1 = set(line.strip() for line in open('profile1.txt'))
set2 = set(line.strip() for line in open('profile2.txt'))
result = set.intersection(set1, set2)

f1 = open('common_follower.txt', 'w')
for list in result:
    f1.write(list + '\n')
