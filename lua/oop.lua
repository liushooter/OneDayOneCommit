-- 元类
Rectangle = {area = 0, length = 0, breadth = 0}

-- 派生类的方法 new
function Rectangle:new (o,length,breadth)
  o = o or {}
  setmetatable(o, self)
  self.__index = self
  self.length = length or 0
  self.breadth = breadth or 0
  self.area = length*breadth;
  return o
end

-- 派生类的方法 printArea
function Rectangle:printArea ()
  print("矩形面积为 ",self.area)
end

r = Rectangle:new(nil,10,20)
print(r.length)
r:printArea()
-- . 与 : 的区别在于使用 : 定义的函数隐含 self 参数，使用 : 调用函数会自动传入 table 至 self 参数
