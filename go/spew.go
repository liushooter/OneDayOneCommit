package main

import (
	"fmt"

	"github.com/davecgh/go-spew/spew"
)

func main() {
	scs := spew.ConfigState{Indent: "\t"}

	// Output using the ConfigState instance.
	v := map[string]int{"one": 1}
	fmt.Printf("v: %v\n", v)
	scs.Dump(v)
}
