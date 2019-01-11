package main

import (
	"encoding/hex"
	"fmt"
	"hash/fnv"
)

func main() {

	fmt.Printf("%s\n", genFnv("hi"))
	fmt.Printf("%s\n", genFnv("shooter"))
	fmt.Printf("%s\n", genFnv("shoooter"))

}

func genFnv(val string) string {
	a := fnv.New32()
	a.Write([]byte(val))
	return hex.EncodeToString(a.Sum(nil))
}

// http://blog.cyeam.com/hash/2014/07/28/fnv_md5
// http://www.hiwzc.com/post/55be3259.html
