import pizza as p

p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushroom','green peppers','extra cheese')

#如果只想导入函数可以
from pizza import make_pizza as mp
mp(16,'pepperoni')
mp(12,'mushroom','green peppers','extra cheese')

#导入模块中所有函数
from pizza import *