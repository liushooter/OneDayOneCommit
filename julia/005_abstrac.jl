using InteractiveUtils # 0.7 之后需要调用这个标准库

function view_tree(T, depth=0)
    println("  "^depth, T)
    for each in subtypes(T)
        view_tree(each, depth+1)
    end
end

abstract type AbstractAnimal end

abstract type AbstractBird <: AbstractAnimal end
abstract type AbstractDog <: AbstractAnimal end
abstract type AbstractCat <: AbstractAnimal end

struct Sparrow <: AbstractBird end
struct Kitty <: AbstractCat end
struct Snoope <: AbstractDog end

view_tree(AbstractAnimal)