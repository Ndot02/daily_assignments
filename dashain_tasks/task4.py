
trip = ("Pokhara", 3, "bus")
city, days, by = trip
print(f"Going to {city} for {days} days by {by}")


sita = {"mama", "kaka", "hajurba", "fupu"}
ram = {"kaka", "hajurba", "maiju"}
print("Both:", sorted(sita & ram))
print("Everyone:", sorted(sita | ram))
print("Only Sita:", sorted(sita - ram))

guests = ["mama", "kaka", "mama", "fupu", "kaka"]
print("Unique guests:", len(set(guests)))
\
tika = {"hajurba": 500, "mama": 1000}
tika["kaka"] = 200
tika["mama"] = 1100
tika.update({"fupu": 300})
print("Maiju gave:", tika.get("maiju", 0))
removed = tika.pop("kaka")
print("Removed kaka:", removed)
print(tika)
print("People:", list(tika.keys()))
print("Total:", sum(tika.values()))

family = {"hajurba": {"city": "Kathmandu", "tika": 500}}
print(family["hajurba"]["city"])