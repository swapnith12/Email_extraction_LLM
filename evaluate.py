import json

with open("output.json") as f:
    pred = json.load(f)

with open("ground_truth.json") as f:
    truth = {x["id"]: x for x in json.load(f)}

correct = 0
total = 0

for p in pred:
    t = truth[p["id"]]
    for k in t:
        if k == "id":
            continue
        total += 1
        if p.get(k) == t.get(k):
            correct += 1

print("Overall accuracy:", round(correct / total * 100, 2), "%")
