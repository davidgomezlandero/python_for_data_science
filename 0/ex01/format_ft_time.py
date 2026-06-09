import time as tm
from datetime import datetime

ts = tm.time()

print (f"Seconds since January 1, 1970: {ts:,.4f} or {ts:.2e} in scientific notation")
dt = datetime.fromtimestamp(ts)
print(dt.strftime("%b %d %Y"))