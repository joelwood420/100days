package main

import (
	"fmt"
)

func main() {
	var a float64
	var b float64
	var c string
	fmt.Print("Enter a number :")
	fmt.Scan(&a)
	fmt.Print("Enter another Number :")
	fmt.Scan(&b)
	fmt.Print("Enter an operator :")
	fmt.Scan(&c)
	fmt.Println(Calculator(a, b, c))
}

func Calculator(a float64, b float64, c string) float64 {
	switch c {
	case "+":
		return a + b
	case "-":
		return a - b
	case "*":
		return a * b
	case "/":
		if b != 0 {
			return a / b
		}
		fmt.Println("Error: Division by zero")
		return 0
	default:
		fmt.Println("Invalid operator")
		return 0
	}
}
