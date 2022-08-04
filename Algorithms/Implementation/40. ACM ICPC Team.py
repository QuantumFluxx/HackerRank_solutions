line = input()
line = line.split()
n = int(line[0])
m = int(line[1])

people = [input() for i  in range(n)]
skills = []
max_skills = 0

for i in range(len(people)):
    j = i
    while j < n:
        first_person = people[i]
        second_person = people[j]
        
        skill = bin(int(first_person, 2) | int(second_person, 2))[2:].count('1')
        if (skill > max_skills):
            max_skills = skill
        skills.append(str(skill))
        
        j += 1

print(max_skills)
print(skills.count(str(max_skills)))