import json


f = open("shit_codestyle.out", "r")
res = open("shit_codestyle.json", "a+")
begin_coord = 0
lines_count = []
filenames = []
i = 0
for line in f:
    if (line[0] == "f"):
        begin_coord = i
        filenames.append(line[10:-1])
    if (line[0] == "\n"):
        lines_count.append(i - begin_coord)
    i += 1
mid = 0
for i in range(0, len(lines_count)):
    mid += lines_count[i]
for i in range(0, len(filenames)):
    print filenames[i]
    res.write(json.dumps({"filename: ", filenames[i]}))
print mid/len(lines_count)
f.close()
res.close()