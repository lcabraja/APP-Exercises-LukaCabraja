package converter

type FahrenheitToCelsiusConverter struct{}

func (f FahrenheitToCelsiusConverter) Convert(value float64) float64 {
	return (value - 32) * 5 / 9
}
