// Variables llamadas

package main

import (
	"fmt"
)

func main() {

	// Variables
	var number = 12
	var f = 13.141516171819101238472529346923874659283465923876
	var txt = "Hola"
	var a bool = true

	// General
	fmt.Printf("%v \n", number)
	fmt.Printf("%#v \n", number)
	fmt.Printf("%T\n", number)

	// int
	fmt.Printf("b:  %b \n", number)
	fmt.Printf("d:  %d \n", number)
	fmt.Printf("d+: %d+ \n", number)
	fmt.Printf("o: %o \n", number)
	fmt.Printf("O: %O \n", number)
	fmt.Printf("x: %x \n", number)
	fmt.Printf("X: %X \n", number)
	fmt.Printf("#X: %#X \n", number)

	// Float
	fmt.Printf("e: %e \n", f)
	fmt.Printf("E: %E \n", f)
	fmt.Printf("f: %f \n", f)
	fmt.Printf(".2f: %.2f \n", f)
	fmt.Printf("6.2f: %6.2f \n", f)
	fmt.Printf("g: %g \n", f)

	//string
	fmt.Printf("s: %s \n", txt)
	fmt.Printf("q: %q \n", txt)
	fmt.Printf("8s: %8s \n", txt)
	fmt.Printf("-8s: %-8s \n", txt)
	fmt.Printf("x: %x \n", txt)
	fmt.Printf(" x: % x \n", txt)

	// Bool
	fmt.Printf("%t \n", a)
}
