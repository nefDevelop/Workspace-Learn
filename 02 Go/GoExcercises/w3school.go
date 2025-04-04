package main

import (
	"fmt"
)

var c = 3

func main() {
	// Variables
	// var number = 12
	// var number2 = -273465928
	// var f = 3.14159265358979323846264338327950288419716939937510582097494
	// var a bool = true
	// var hola string = "Hola"

	// // FORMATO
	// fmt.Printf("t:  %T  %v \n", number, number)
	// fmt.Printf("t:  %T  %v \n", number2, number2)

	var array1 = [3]int{2, 6, 0}
	arr4 := [4]int{2: 4, 3: 5}

	fmt.Println(len(array1))
	fmt.Println(arr4)

}
