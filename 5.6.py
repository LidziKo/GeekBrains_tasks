my_file = open('file56.txt', 'r', encoding='UTF-8')

subject_dict = {}

for line in my_file:
    position2 = line.split()
    subject = position2[0].split(':')[0]
    summary_list = [position2[1].split('(')[0], position2[2].split('(')[0], position2[3].split('(')[0]]
    summary = 0
    for item in summary_list:
        if item.isdigit():
            summary += float(item)
    subject_dict[subject] = summary
print(subject_dict)

my_file.close()
