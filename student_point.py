di = {"Arthur" : 93,
      "George" : 92,
      "Bob" : 94
     }
print("Our original dictionary is:", di, "\n")
di.update({"Sofia" : 95})
print("Our updated dictionary is:")
for i in di:
    print(i, ":", di.get(i), "\n")
di.update({"Bob" : 96})
di.pop("George")
print("Our second updated dictionary is:")
for i in di:
    print(i, ":", di.get(i))
