from models import NearEarthObject, CloseApproach
from datetime import datetime
from helpers import cd_to_datetime
import subprocess


# TASK 1
print("Task 1: Check attributes of NearEarthObject and CloseApproach instance\n")
neo = NearEarthObject(
    designation='2020 FK',
    name='One REALLY BIG fake asteroid',
    diameter=12.345,
    hazardous=True
)


if neo.designation == '2020 FK':
    print("✅ designation is correct")
else:
    print("❌ designation is incorrect")

if neo.name == 'One REALLY BIG fake asteroid':
    print("✅ name is correct")
else:
    print("❌ name is incorrect")

if abs(neo.diameter - 12.345) < 0.001:
    print("✅ diameter is correct")
else:
    print("❌ diameter is incorrect")

if neo.hazardous is True:
    print("✅ hazardous is correct")
else:
    print(f"❌ hazardous is incorrect: {neo.hazardous}")

if neo.fullname == '2020 FK (One REALLY BIG fake asteroid)':
    print("✅ fullname is correct")
else:
    print(f"❌ fullname is incorrect: {neo.fullname}")


ca = CloseApproach(
    designation='2020 FK',
    time='2020-Jan-01 12:30',
    distance=0.25,
    velocity=56.78,
    neo=neo
)


if isinstance(ca.time, datetime):
    print("✅ time is a datetime object")
else:
    print("❌ time is not a datetime object")

if ca.time == cd_to_datetime('2020-Jan-01 12:30'):
    print("✅ time value is correct")
else:
    print("❌ time value is incorrect")

if abs(ca.distance - 0.25) < 0.001:
    print("✅ distance is correct")
else:
    print("❌ distance is incorrect")

if abs(ca.velocity - 56.78) < 0.01:
    print("✅ velocity is correct")
else:
    print("❌ velocity is incorrect")

if ca.neo is neo:
    print("✅ neo reference is correct")
else:
    print("❌ neo reference is incorrect")

if ca.time_str == '2020-01-01 12:30':
    print("✅ time_str is correct")
else:
    print(f"❌ time_str is incorrect: {ca.time_str}")

# TASK 2
print("\nTask 2: Check command line arguments\n")
def run_command(args):
    print(f"\n$ python main.py {' '.join(args)}")
    result = subprocess.run(
        ["python", "main.py"] + args,
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.stderr:
        print("stderr:", result.stderr)

# Test cases
run_command(["inspect", "--name", "Halley"])
run_command(["inspect", "--pdes", "433"])
run_command(["inspect", "--verbose", "--name", "Ganymed"])
run_command(["inspect", "--name", "DoesNotExist"])


# TASK 3
print("\nTask 3: Check filters.py\n")
def run_query(*args):
    print(f"\n$ python3 main.py query {' '.join(args)}")
    result = subprocess.run(
        ["python3", "main.py", "query", *args],
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.stderr:
        print("stderr:", result.stderr)

# 1. Query for close approaches on 2020-01-01
run_query("--date", "2020-01-01")
# 2. Query for close approaches in 2020
run_query("--start-date", "2020-01-01", "--end-date", "2020-12-31")
# 3. In 2020 with a distance of <=0.1 au
run_query("--start-date", "2020-01-01", "--end-date", "2020-12-31", "--max-distance", "0.1")
# 4. In 2020 with a distance of >=0.3 au
run_query("--start-date", "2020-01-01", "--end-date", "2020-12-31", "--min-distance", "0.3")
# 5. In 2020 with a velocity of <=50 km/s
run_query("--start-date", "2020-01-01", "--end-date", "2020-12-31", "--max-velocity", "50")
# 6. In 2020 with a velocity of >=25 km/s
run_query("--start-date", "2020-01-01", "--end-date", "2020-12-31", "--min-velocity", "25")
# 7. Not hazardous NEOs between 0.5km and 0.6km in diameter
run_query("--min-diameter", "0.5", "--max-diameter", "0.6", "--not-hazardous")
# 8. Rare: hazardous, large, fast, and close
run_query("--max-distance", "0.1", "--min-velocity", "35", "--min-diameter", "2.5", "--hazardous")