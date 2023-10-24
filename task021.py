# task021. Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
a = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
     {"VII": " S005 "}, {" V ": " S009 "}, {" VIII ": " S007 "}]
b = set()
for i in a:
    for v in i.values():
        b.add(v.strip())
print(b)