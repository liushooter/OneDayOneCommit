package main

import (
	"fmt"
	"time"
)

func main() {

	timeUnix := time.Now().Unix()
	fmt.Printf("timeUnix: %d\n", timeUnix)
}
