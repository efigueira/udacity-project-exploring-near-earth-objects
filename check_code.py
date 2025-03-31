# TASK 1

from models import NearEarthObject, CloseApproach
from datetime import datetime
from helpers import cd_to_datetime


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
