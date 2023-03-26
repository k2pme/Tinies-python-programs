import uuid 
import random
import os

os.system("color a")
while True : 
    id = str(uuid.uuid4())
    trimmed = id[:random.randint(0, len(id) -1)]
    space = " " * random.randint(0, 15)
    
    print(f"{space}{trimmed  }"   )