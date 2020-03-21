package main

import (
	"fmt"
)

func Sqrt(x float64) float64 {
	if x == 0 {
		return 0
	}
	var z float64 = 1.0
	for y := 0; y < 10; y++ {
		z -= (z*z - x) / (2*z)
		fmt.Println(z)
	}
	return z
}

func main() {
	fmt.Println(Sqrt(10))
}
