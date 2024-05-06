srt_list = ["Emma", "jon", "", "Kelly", None, "Eric", ""]

num = []

for name in srt_list:
    if name and isinstance(name, str):
        num.append(name)

print(srt_list)
print(num)
