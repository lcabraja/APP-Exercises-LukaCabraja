package generator

type FibonacciGenerator struct{}

func NewFibonacciGenerator() *FibonacciGenerator {
	return &FibonacciGenerator{}
}

func (f *FibonacciGenerator) Generate(i int) (int, []int) {
	result := []int{0, 1}
	if i == 0 {
		return 0, result[:1]
	} else if i == 1 {
		return 1, result
	}

	for j := 2; j <= i; j++ {
		next := result[j-1] + result[j-2]
		result = append(result, next)
	}
	return result[i], result
}
