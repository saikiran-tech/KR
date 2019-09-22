

import random
a = random.sample(range(1,20), 14)
b = random.sample(range(1,14), 8)
c = []
result = [i for i in a if i in b]
c.append(result)
c