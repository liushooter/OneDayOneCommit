package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {

	mutexCounter()
	wgCounter()
}

func mutexCounter() {

	var mut sync.Mutex
	counter := 0
	for i := 0; i < 5000; i++ {

		go func() {

			defer func() {
				mut.Unlock()
			}()
			mut.Lock()
			counter += 1

		}()

	}
	time.Sleep(time.Second * 1) //sleep 后数据才会正确， 但sleep 并不是真正的 所有goroutine 执行完的时间
	fmt.Println(counter)
}

func wgCounter() {
	var mut sync.Mutex
	var wg sync.WaitGroup
	counter := 0
	for i := 0; i < 5000; i++ {
		wg.Add(1)

		go func() {
			defer func() {
				mut.Unlock()
			}()
			mut.Lock()
			counter++
			wg.Done()

		}()

		wg.Wait()
	}

	fmt.Println(counter)
}
