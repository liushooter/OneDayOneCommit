package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var s, sep string
	for i := 1; i < len(os.Args); i++ {
		s += sep + os.Args[i]
		sep = ""
	}

	fmt.Println(strings.Join(os.Args[1:], " "))

	fmt.Println(s)

	for true { // while
		fmt.Println("zqw")
	}

	for {
		fmt.Println("shooter")
	}
}
