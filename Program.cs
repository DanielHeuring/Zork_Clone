using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Csharp
{
    internal class Program
    {
        static void Main(string[] args)
        {   


            Console.WriteLine("Enter a Number.");
            int number = Convert.ToInt32(Console.ReadLine());
            bool run = true;
            int allow = 0;
            int increase = 1;



            while (allow < 5) ;
            {
                Console.WriteLine("Guess the Number!");
                int gnumber = Convert.ToInt32(Console.ReadLine());

                if (number == gnumber)
                {
                    Console.WriteLine("You guessed it!!!");
                    allow += increase;
                }
                else if (number > gnumber)
                {
                    Console.WriteLine("Your too low");
                    allow += increase;

                }
                else if (number < gnumber)
                {
                    Console.WriteLine("Your too high");
                    allow += increase;

                }
            }




        }
    }
}
