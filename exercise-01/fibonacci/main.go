package main

import (
	gen "fibonacci/generator"
	"fmt"
)

func main() {
	f := gen.NewFibonacciGenerator()
	result, indices := f.Generate(3)
	fmt.Printf("%d: %v\n", result, indices)
}
