package main

import (
	"fmt"
)

func main() {
	var temp float64
	fmt.Println("Enter Temp(celcius): ")
	fmt.Scan(&temp)
	fmt.Printf("%.2f° C = %.2f° F\n", temp, convertTempToFahrenheit(temp))
}

func convertTempToFahrenheit(temp float64) float64 {
	f := temp*9/5 + 32
	return float64(f)
}
