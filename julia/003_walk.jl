"""
    walk(T) -> trajectory

模拟随机行走
"""

function walk(T)
    x = 0
    trajectory = [x] #轨迹, 数组

    for t in 1:T
        if rand()< 0.5
            x += 1
        else
            x -= 1
        end
        push!(trajectory, x)
    end

    trajectory
end



# using GR,Interact
# T = 100
# plot(0:T,walk(T))

# @manioulate for T in 10:100
#     plot(0:T, walk(T))
# end