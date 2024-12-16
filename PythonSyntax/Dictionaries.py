capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(capitals.get("USA"))
# print(capitals.get("India"))

# if capitals.get("Russia"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")
    
capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
# capitals.clear()

# keys = capitals.keys()

# for key in capitals.keys():
#     print(key)
    
# values = capitals.values()
# print(values)

# for value in capitals.values():
#     print(value)

# items = capitals.items()
# print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")
