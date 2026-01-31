package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Println("Enter a number :")
	fmt.Scan(&n)
	fmt.Println(evenOrOdd(n))
}

func evenOrOdd(n int) string {
	switch {
	case n%2 == 0:
		return "this is even"
	case n%2 != 0:
		return "this is odd"
	}
	return ""
}
