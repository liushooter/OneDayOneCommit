package main

import "fmt"

func main() {

	s := []int{1, 2, 3}
	fmt.Println(s) //[1 2 3]
	copy(s, []int{4, 5, 6, 7, 8, 9})
	fmt.Println(s) //[4 5 6]

	bytes := []byte("hello world")
	copy(bytes, "ha ha")

	fmt.Printf("%s\n", bytes)

}
