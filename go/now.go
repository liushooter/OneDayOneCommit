package main

import (
	"fmt"
	"time"

	"github.com/jinzhu/now"
)

var (
	format    = "2006-01-02 15:04:05"
	allformat = "2006-01-02 15:04:05.999999999"
)

func main() {
	t := time.Now()
	fmt.Println("now: ", format)
	fmt.Println("now: ", allformat)

	fmt.Println(now.BeginningOfMinute())
	fmt.Println(now.BeginningOfHour())
	fmt.Println(now.BeginningOfDay())
	fmt.Println(now.BeginningOfWeek())
	fmt.Println(now.BeginningOfMonth())
	fmt.Println(now.BeginningOfQuarter())
	fmt.Println(now.BeginningOfYear())
	fmt.Println(now.BeginningOfWeek())

	fmt.Println(now.EndOfMinute())
	fmt.Println(now.EndOfHour())
	fmt.Println(now.EndOfDay())
	fmt.Println(now.EndOfWeek())
	fmt.Println(now.EndOfMonth())
	fmt.Println(now.EndOfQuarter())
	fmt.Println(now.EndOfYear())

	fmt.Println(now.Monday())
	fmt.Println(now.Sunday())

	fmt.Println("Friday: ", now.Monday().AddDate(0, 0, 4))
	fmt.Println("GetFriday: ", GetFriday(t))

}

func GetFriday(date time.Time) time.Time {
	return now.New(date).Monday().AddDate(0, 0, 4)
}
