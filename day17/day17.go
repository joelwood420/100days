package main

import (
	"fmt"
)

func main() {
	var a int
	var b int
	fmt.Println("Enter a number: ")
	fmt.Scan(&a)
	fmt.Println("Enter another number: ")
	fmt.Scan(&b)
	sum := a + b
	fmt.Printf("%v + %v = %v\n", a, b, sum)

}
