word = input()
cro_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

count = len(word)

for cro_char in cro_list:
    count -= word.count(cro_char)

print(count)