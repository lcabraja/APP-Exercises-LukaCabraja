package converter

import (
	"math"
	"testing"
)

func TestFahrenheitToCelsiusConverter_Convert(t *testing.T) {
	tests := []struct {
		name  string
		input float64
		want  float64
	}{
		{"Freezing", 32, 0},
		{"Boiling", 212, 100},
		{"Room Temperature", 68, 20},
		{"Negative", -22, -30},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			f := FahrenheitToCelsiusConverter{}
			got := f.Convert(tt.input)
			if math.Abs(got-tt.want) > 0.01 {
				t.Errorf("FahrenheitToCelsiusConverter.Convert() = %v, want %v", got, tt.want)
			}
		})
	}
}
