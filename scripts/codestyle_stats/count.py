import json


f = open("fine_codestyle.out", "r")
res = open("fine_codestyle.json", "a+")
begin_coord = 0
lines_count = []
file_info = []

i = 0 
for line in f:
    errors = {"E101": 0, "E191": 0,"E122": 0,"E305": 0,"E302": 0,"E111": 0, "E112": 0,
            "E113": 0,"E114": 0,"E116": 0,"E115": 0,"E121": 0,"E123": 0,"E124": 0, 
            "E129": 0,"E126": 0,"E127": 0,"E128": 0,"E131": 0,"W291": 0,"E125": 0,
            "W503": 0,"E701": 0,"E203": 0,"E201": 0,"E202": 0,"E702": 0,"E211": 0,
            "E221": 0,"E222": 0,"E223": 0,"E224": 0,"E225": 0,"E226": 0,"E227": 0,
            "E228": 0,"E231": 0,"E241": 0,"E242": 0,"E251": 0,"E272": 0,"E261": 0,
            "E262": 0, "E265": 0, "E266": 0, "E271": 0, "E273": 0, "E274": 0, 
             "E402": 0, "E275": 0, "E301": 0, "E303": 0, "E304": 0, "E306": 0, "E401": 0,
             "E501": 0, "E502": 0, "E703": 0, "E704": 0, "E711": 0, "E712": 0, "E713": 0, "E714": 0, "E721": 0,
            "E722": 0, "E731": 0, "E901": 0,"W293": 0,"W601": 0,"W602":0,"W603":0,"W604":0, "W191":0, "W292":0, "W391":0} 
    if (line[0] == "f"):
        info = {}
        filename = line[10:-1]
        info["filename"] = filename
        i += 1
        continue
    if (line[0]) == "\n":
    	file_info.append(info)
    	i += 1
    	continue
    amount = line.split("   ")
#	print "123"
    print amount[0]
    errno = amount[-1].lstrip()[:4]
    info["errors"] = errors
    errors[errno] = int(amount[0])
    i += 1
mid = 0
print len(file_info)
res.write(json.dumps(file_info, indent=4))
print "OK\n"
f.close()
res.close()
