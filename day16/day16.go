// Go Challenge 1 – Simple Greeter
// Write a Go program that:
// 	•	Asks the user for their name.
// 	•	Reads the input from the terminal.
// 	•	Prints: `Hello, <name>!` on its own line.

package main

import (
	"fmt"
)

func greet() {
	var name string
	fmt.Print("What's your name? ")
	fmt.Scan(&name)
	fmt.Println("Hello,", name)
}

func main() {
	greet()
}
