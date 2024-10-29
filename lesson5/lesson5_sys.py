import sys
import requests

print(sys.executable)
print(sys.version)
print(sys.platform)

print("=======================")

for name, path in sys.modules.items():
    print("name = ", name, "path = ", path)