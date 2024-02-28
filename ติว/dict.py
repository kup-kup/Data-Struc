L = [...] #มีอยู่ n คำ

if "sun" in L #O(n)
.
.
. #หา n ครั้ง
#O(n^2)

d = dict(L)

if "sun" in d #O(1)
.
.
. #หา n ครั้ง
#O(n)