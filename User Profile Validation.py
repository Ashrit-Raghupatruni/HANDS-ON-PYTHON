import copy
def generate_data():
    return [
        {"id": 1, "data": {"files": ["a.txt"], "usage": 500}},
        {"id": 2, "data": {"files": ["b.txt","c.txt"], "usage": 300}}
    ]
def replicate_data(data):
    return data, copy.copy(data), copy.deepcopy(data)

def modify_data(assign, shallow, deep):
    for i in range(len(assign)):
        assign[i]["data"]["files"].append("A.txt")
        shallow[i]["data"]["files"].append("P.txt")
        deep[i]["data"]["files"].append("D.txt")
        shallow[i]["data"]["usage"] += 50
        deep[i]["data"]["usage"] += 100

    if len(shallow[0]["data"]["files"]) > 0:
        shallow[0]["data"]["files"].pop(0)

def check_integrity(original, shallow, deep):
    leakage = 0
    safe = 0

    if "S.txt" in original[0]["data"]["files"] or "A.txt" in original[0]["data"]["files"]:
        leakage = 1

    if "D.txt" not in original[0]["data"]["files"]:
        safe = 1

    original_files = set()
    shallow_files = set()

    for user in original:
        for f in user["data"]["files"]:
            original_files.add(f)

    for user in shallow:
        for f in user["data"]["files"]:
            shallow_files.add(f)

    overlap = len(original_files & shallow_files)

    if original[0]["data"]["files"] != deep[0]["data"]["files"]:
        mutation = "Inner level mutation"
    else:
        mutation = "No mutation"

    return leakage, safe, overlap, mutation

original = generate_data()

print("BEFORE:", original)

assign, shallow, deep = replicate_data(original)

modify_data(assign, shallow, deep)

print("\nAFTER:")
print("Original:", original)
print("Shallow:", shallow)
print("Deep:", deep)

leakage, safe, overlap, mutation = check_integrity(original, shallow, deep)

print("\nINTEGRITY REPORT:")
print("Leakage:", leakage)
print("Safe:", safe)
print("Overlap:", overlap)
print("Mutation:", mutation)

print("\nFinal Tuple:", ("leakage:",leakage,"safe", safe,"overlap", overlap))
