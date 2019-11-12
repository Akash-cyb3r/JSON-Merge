import glob
import json
try:
    import json
except ImportError:
    import simplejson as json
result = []
for f in glob.glob("*.json"):
    with open(f, "rb") as infile:
        try:
            result.append(json.load(infile))
        except ValueError:
            print(f)

with open("merge1.json", "wb") as outfile:
    json.dump(result, outfile)
