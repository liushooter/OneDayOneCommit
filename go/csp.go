package main

import (
	"fmt"
	"time"
)

func main() {
	retCh := asyncServer()

	otherTask()

	fmt.Println(<-retCh) // 取数据
	time.Sleep(time.Millisecond * 500)

}

func server() string {
	time.Sleep(time.Millisecond * 50)
	return "Done"
}

func otherTask() {
	fmt.Println("working on something")
	time.Sleep(time.Millisecond * 100)

	fmt.Println("Task is Done")
}

func asyncServer() chan string {
	retCh := make(chan string)
	// retCh := make(chan string, 1) // buffer channel

	go func() {
		ret := server()
		fmt.Println("returned result")
		retCh <- ret // 放数据
		fmt.Println("server exited")
	}()

	return retCh

}
