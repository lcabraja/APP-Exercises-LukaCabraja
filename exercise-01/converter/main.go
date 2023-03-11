package main

import (
	"converter/converter"
	"fmt"
)

func main() {
	f := converter.FahrenheitToCelsiusConverter{}
	c := converter.CelsiusToFahrenheitConverter{}

	fmt.Printf("32°C = %f°F\n", c.Convert(32))
	fmt.Printf("100°F = %f°C\n", f.Convert(100))
}
