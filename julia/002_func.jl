function mysum(arr)
    s = 0.0

    for i in arr
        s+=i
    end
    s #最后一行默认返回值
end

println(rand(Bool, 3, 3)) #矩阵

A = rand(1000)
println(mysum(A))

arr = rand(Int,10)
println(mysum(arr))

'''
    is_even(x::Int) -> Bool
判断一个整数`x`是不是偶数

'''
is_even(x::Int)= x % 2 == 0
println(is_even(7))

println(is_even(2.0)) # 强类型
