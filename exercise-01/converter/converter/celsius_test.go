package converter

import (
	"math"
	"testing"
)

func TestCelsiusToFahrenheitConverter_Convert(t *testing.T) {
	tests := []struct {
		name  string
		input float64
		want  float64
	}{
		{"Freezing", 0, 32},
		{"Boiling", 100, 212},
		{"Room Temperature", 20, 68},
		{"Negative", -30, -22},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			c := CelsiusToFahrenheitConverter{}
			got := c.Convert(tt.input)
			if math.Abs(got-tt.want) > 0.01 {
				t.Errorf("CelsiusToFahrenheitConverter.Convert() = %v, want %v", got, tt.want)
			}
		})
	}
}
