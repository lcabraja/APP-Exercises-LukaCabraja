package converter

type CelsiusToFahrenheitConverter struct{}

func (c CelsiusToFahrenheitConverter) Convert(value float64) float64 {
	return (value * 9 / 5) + 32
}
