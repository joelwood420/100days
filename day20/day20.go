package main

import (
	"fmt"
)

type Triangle struct {
	A, B, C int
}

func main() {
	triangles := []Triangle{
		{3, 5, 9},
		{6, 6, 6},
		{7, 2, 2},
		{1, 5, 5},
		{3, 7, 1},
	}

	for _, v := range triangles {
		if isScalene(v.A, v.B, v.C) {
			perimeter := calculatePerimeter(v.A, v.B, v.C)
			fmt.Printf("Scalene triangle with sides %d, %d, %d has perimeter %d\n", v.A, v.B, v.C, perimeter)
		}
	}
}

func typeOf(a, b, c int) string {
	if a == b && b == c {
		return "Equilateral"
	} else if a == b || b == c || a == c {
		return "Isosceles"
	} else {
		return "Scalene"
	}
}

func isScalene(a, b, c int) bool {
	return typeOf(a, b, c) == "Scalene"
}

func calculatePerimeter(a, b, c int) int {
	return a + b + c
}
