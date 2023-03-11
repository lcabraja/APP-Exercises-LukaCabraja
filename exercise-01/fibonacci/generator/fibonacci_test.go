package generator

import (
	"reflect"
	"testing"
)

func TestFibonacciGenerator_Generate(t *testing.T) {
	tests := []struct {
		name  string
		input int
		wantN int
		wantS []int
	}{
		{"Zero", 0, 0, []int{0}},
		{"One", 1, 1, []int{0, 1}},
		{"Two", 2, 1, []int{0, 1, 1}},
		{"Three", 3, 2, []int{0, 1, 1, 2}},
		{"Four", 4, 3, []int{0, 1, 1, 2, 3}},
		{"Five", 5, 5, []int{0, 1, 1, 2, 3, 5}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			f := &FibonacciGenerator{}
			gotN, gotS := f.Generate(tt.input)
			if gotN != tt.wantN {
				t.Errorf("FibonacciGenerator.Generate() gotN = %v, want %v", gotN, tt.wantN)
			}
			if !reflect.DeepEqual(gotS, tt.wantS) {
				t.Errorf("FibonacciGenerator.Generate() gotS = %v, want %v", gotS, tt.wantS)
			}
		})
	}
}
