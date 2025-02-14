using System;


namespace pacDesarrollo_SecuenciaFibonacci
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /* ---- Enunciados Ejercicio
            Recoger por consola un número entero y validar su valor:
            el número introducido debe tener un valor comprendido entre 7 y 22
            ambos valores incluidos.*/

            // - Declaramos el numero entero, cogemos el input y validamos
            int _valor = 0;
            string _parserInput = "";

            // - Tambien las variables para la secuencia
            int[] _sec;


            // - Ponemos mensaje de bienvenida y preguntamos.
            Console.WriteLine("Hola, bienvenido a la PAC de desarrollo.");
            Console.Write("Por favor, inserta los números de la secuencia de Fibonacci a calcular entre 7-22: ");

            // - Estaba sin return, pero no sabia si queria que saliera el programa cuando fuese incorrecto o no la entrada.
            do
            {
                _parserInput = Console.ReadLine();

                // - Comprobamos si podemos convertir el string en un int y si esta entre 7 y 22
                if (int.TryParse(_parserInput, out _valor) == false)
                {
                    Console.WriteLine("El valor {0} no es válido", _parserInput);
                    break;
                }
                else if (_valor < 7 || _valor > 22)
                {
                    // - Se establece un valor invalido para seguir dentro del bucle.
                    _parserInput = "numInvalido";
                    Console.WriteLine("El valor {0} no es válido", _valor);
                    break;
                }

            } while (int.TryParse(_parserInput, out _valor) == false);

            /* ---- Enunciados Ejercicio
            //Crear la secuencia Fibonacci: se compondrá de tantos elementos como indique el valor del número introducido
            //(NOTA: la secuencia debe comenzar con el valor "0").*/

            // - Sabiendo que el número introducido es correcto, declaramos la array con esas posiciones
            _sec = new int [_valor];

            for (int i = 0; i < _valor; i++) 
            {
                // - Tenemos de condicion que 0 y 1 no suman en la secuencia.
                if (i > 1)
                {
                    _sec[i] = _sec[i - 1] + _sec[i - 2];
                }
                else
                {
                    _sec[i] = i;
                }
                
            }

            // - Imprimimos en pantalla la array.
            foreach (int numero in _sec)
            {
                Console.Write("{0} ",numero);
            }

            /* ---- Enunciados Ejercicio
            //Crear la secuencia Fibonacci con los valores en orden invertido:
            //se toma como referencia la secuencia Fibonacci generada y se invierte su orden.*/
            
            Console.Write("\n");

            for (int i = _valor - 1; i >= 0; i--)
            {
                Console.Write("{0} ",_sec[i]);
            }


        }
    }
}
