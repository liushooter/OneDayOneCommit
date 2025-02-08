package main

import (
	"fmt"

	"github.com/expr-lang/expr"
)

type User struct {
	Name string
	Age  int
}

func main() {

	// 表达式计算
	env := map[string]interface{}{
		"foo": 1,
		"bar": 2,
	}

	out, err := expr.Eval("foo + bar", env)

	if err != nil {
		panic(err)
	}
	fmt.Println(out)

	// 自定义函数
	env2 := map[string]interface{}{
		"x":      3,
		"double": func(i int) int { return i * 2 },
	}

	out2, err2 := expr.Eval("double(x)", env2)

	if err2 != nil {
		panic(err2)
	}

	fmt.Println(out2)

	env3 := map[string]interface{}{
		"user": User{Name: "Alice", Age: 18},
	}

	code3 := `user.Name`

	program3, _ := expr.Compile(code3, expr.Env(env3))

	output3, err3 := expr.Run(program3, env3)
	if err != nil {
		panic(err3)
	}

	fmt.Println(output3)

}
