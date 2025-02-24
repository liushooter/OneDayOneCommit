package main

import (
	"fmt"
	"net"
)

func main() {
	conn, err := net.ListenUDP("udp", &net.UDPAddr{
		IP:   net.ParseIP("0.0.0.0"),
		Port: 1820,
	})
	if err != nil {
		fmt.Printf("Error starting UDP server: %v\n", err)
		return
	}
	defer conn.Close()

	fmt.Printf("UDP server listening\n")

	buffer := make([]byte, 1228) // 1228 - udp shred size

	// Continuously read data
	for {
		n, addr, err := conn.ReadFromUDP(buffer)
		if err != nil {
			fmt.Printf("Error reading from UDP connection: %v\n", err)
			continue
		}

		// or process it generally
		fmt.Printf("Received message from %s: %s\n", addr.String(), string(buffer[:n]))
	}
}
