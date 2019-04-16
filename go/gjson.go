package main

import (
	"fmt"

	"github.com/tidwall/gjson"
)

const json = `{
  "name": { "first": "Tom", "last": "Sara"},
  "age": 37,
  "children": ["Alice", "Bob", "Carol", "David"],
  "fav.movie": "Deer Hunter",
  "friends": [
 		{"first": "Dale", "last": "Murphy", "age": 44},
 		{"first": "Roger", "last": "Craig", "age": 68},
 		{"first": "Jane", "last": "Murphy", "age": 47}
  ]
}`

var putf = fmt.Printf

func main() {
	name := gjson.Get(json, "name.last")
	age := gjson.Get(json, "age")
	children := gjson.Get(json, "children")
	movie := gjson.Get(json, "fav\\.movie")
	friends := gjson.Get(json, "friends.#")
	friend := gjson.Get(json, "friends.1.last")

	println(name.String())
	println(age.Int())
	putf("children: %v\n", children)
	println(movie.String())
	putf("friends num: %v\n", friends)
	putf("friend: %v\n", friend)
}
