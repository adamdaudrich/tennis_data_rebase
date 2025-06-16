
# any
(year in filename for year in years) 

evaluates to **True** if at least one element in the iterable returns True, otherwise it returns False.
Breaking it down:

year in filename for year in years is a generator expression that checks 

if any string in the years list appears as a substring within filename
any() returns True as soon as it finds the first match