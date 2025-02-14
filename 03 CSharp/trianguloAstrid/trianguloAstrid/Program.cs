using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.ExceptionServices;
using System.Text;
using System.Threading.Tasks;

namespace trianguloAstrid
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Se solicita por consola 1 número enteros. Se guardan sobre la variable "cateto".
            int cateto = 0;
            Console.WriteLine("Ingresa un numero mayor a cero: ");
            
            if (int.TryParse(Console.ReadLine(), out cateto) == true)
            {
                if (cateto <= 0)
                {
                    return;                
                }
                else
                {
                    for (int i = cateto; i > 0; i--)
                    {
                        for (int j = 0; j < i; j++)
                        {
                            Console.Write("*");
                        }
                        Console.Write("\n");
                    }
                }
            }
            else
            {
                Console.WriteLine("Numero inválido.");
            }

            //Valida que el número sea mayor que 0.



            //Dibuja en salida un triángulo rectángulo con asteriscos. La longitud de los catetos(lados) deber ser la indicada por entrada

        }
    }
}
