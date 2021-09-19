import math
from datetime import datetime

print(f"# set accuracy after decimal point {math.pi:.5f}")

for i in range(1, 11):
    print(f"{i:02}")  # set at least 2 digits

date = datetime(2000, 10, 25)
print(f"my birthday is in {date:%B %d, %Y}")
