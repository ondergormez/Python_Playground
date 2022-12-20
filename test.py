# TODO: Add shebang
import json

string_obj =  '{ "name":"Kean", "city":"Istanbul", "age":80}'
dictionary_obj = json.loads(string_obj)

print(dictionary_obj["city"])

bytes_to_be_signed = bytes(json.dumps(string_obj, sort_keys=True, separators=(",", ":")),"ascii")
# TODO: Remove this
print(type(bytes_to_be_signed))

print(bytes_to_be_signed)



