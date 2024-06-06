import json

Person = {"nombre": "Juan", "edad": 25, "trabajo": "Ingeniero"}

json_person = json.dumps(Person)
json_person = json.loads(json_person)

print(json_person['nombre'])