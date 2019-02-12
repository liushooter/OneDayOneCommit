package main

import (
	"fmt"
	"os"
	"os/user"
)

func main() {
	fmt.Printf("user home: %s\n", homeDir())
}

func homeDir() string {
	if home := os.Getenv("HOME"); home != "" {
		return home
	}

	if usr, err := user.Current(); err == nil {
		return usr.HomeDir
	}

	return ""
}
