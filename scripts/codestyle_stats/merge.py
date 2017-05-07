import json


with open("fine_codestyle.json", "r") as cs_bad_stats:
    cs_bad_data = cs_bad_stats.read().replace('\n', ' ')
    parsed_cs_bad = json.loads(cs_bad_data)
    print parsed_cs_bad[:10]
with open("fine_custom.json", "r") as custom_bad_stats:
    custom_bad_data = custom_bad_stats.read().replace('\n', ' ')
    parsed_custom_bad = json.loads(custom_bad_data)
    print parsed_custom_bad[:10]
res = open("fine_res.json", "w+")
merged_bad = []
for i in range(0, len(parsed_custom_bad)):
    if (parsed_custom_bad[i]["filename"] == parsed_cs_bad[i]["filename"]):
        print parsed_custom_bad[i]["filename"]
        if "errors" in parsed_cs_bad[i]:
            parsed_custom_bad[i]["errors"] = parsed_cs_bad[i]["errors"]
        else:
            parsed_custom_bad[i]["errors"] = None
res.write(json.dumps(parsed_custom_bad, indent=4))
res.close()