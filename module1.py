# is wali file ham module ko improt karte hai end than fr ham function ko run karege 
import module
print(module.sum(10,20))
print(module.mul(40,55))
# this is one more option isse ham file se function ka name leke srif use function ko coll kara sakte hai or print kara sakte hai 
from module import sum,mul
print(sum(20,30))
print(mul(30,40))


print("*****************")

from module import *

print(sum(100,40))
print(mul(100,40))




