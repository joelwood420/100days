// Go Challenge 1 – Simple Greeter
// Write a Go program that:
// 	•	Asks the user for their name.
// 	•	Reads the input from the terminal.
// 	•	Prints: `Hello, <name>!` on its own line.

package main

import (
	"fmt"
)

func main() {
	var name string
	fmt.Println("whats your name? ")
	fmt.Scan(&name)
	fmt.Println("hello ,", name)

}
