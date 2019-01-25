package main

import (
	"fmt"

	"github.com/robertkrimen/otto"
)

func greet(name string) {
	fmt.Printf("hello, %s!\n", name)
}

func main() {
	vm := otto.New()

	if err := vm.Set("greetFromGo", greet); err != nil { // js方法与golang方法关联
		panic(err)
	}

	// `hello, Golang!`
	// set -> run
	if _, err := vm.Run(`greetFromGo('Golang')`); err != nil {
		panic(err)
	}

	if _, err := vm.Run(`function greetFromJS(name) {
    console.log('hello, ' + name + '!');
  }`); err != nil {
		panic(err)
	}

	// `hello, JS!`
	// run -> call
	if _, err := vm.Call(`greetFromJS`, nil, "JS"); err != nil {
		panic(err)
	}

	if _, err := vm.Run("var x = 1 + 1"); err != nil {
		panic(err)
	}

	// run -> get
	val, err := vm.Get("x")
	if err != nil {
		panic(err)
	}

	v, err := val.Export()
	if err != nil {
		panic(err)
	}

	// (all numbers in JavaScript are floats!)
	// `float64: 2`
	fmt.Printf("%T: %v\n", v, v)

	if _, err := vm.Run(`function add(a, b) {
    return a + b;
  }`); err != nil {
		panic(err)
	}

	// run -> call
	r, err := vm.Call("add", nil, 2, 3)
	if err != nil {
		panic(err)
	}

	// `5`
	fmt.Printf("%s\n", r)
}

// run定义js方法, call调用js方法

// https://www.fknsrs.biz/blog/otto-getting-started.html
