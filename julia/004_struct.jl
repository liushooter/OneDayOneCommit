struct MyComplex
    real::Float64
    imag::Float64
end

a = MyComplex(1.0, 2.0)

println(a.real, a.imag)
