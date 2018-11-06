package main

import (
	"fmt"
	"runtime"
	"syscall/js"
)

func main() {
	println("Hello, WebAssembly")
	fmt.Printf("OS: %s, Architecture: %s\n", runtime.GOOS, runtime.GOARCH)

	c := make(chan struct{}, 0)
	registerCallbacks()
	<-c
}

func sum(args []js.Value) {
	var sum int

	for _, val := range args {
		sum += val.Int()
	}

	println(sum)
}

func registerCallbacks() {
	js.Global().Set("sum", js.NewCallback(sum))
}
