using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace pi_digits
{
    class Program
    {
        static double Truncate(double value, int digits)
        {
            // Truncates a double to specified number of digits
            double multipler = Math.Pow(10, digits);

            return Math.Truncate(value * multipler) / multipler;
        }
        static double EstimateFunction(int k)
        {
            double value;

            //Function used to estimate n decimals of pi
            value = Math.Pow(16, -k) * (((double) 4 / (8 * k + 1)) - ((double) 2 / (8 * k + 4)) - ((double) 1 / (8 * k + 5)) - ((double) 1 / (8 * k + 6)));

            return value;
        }
        static double CalculatePi(int numDigits)
        {
            double value = 0;

            //Calculates pi up to n decimals
            for (int i = 0; i <= numDigits; i++)
            {
                value += EstimateFunction(i);
            }

            return value;
        }
        static void Main(string[] args)
        {
            int numDigits;
            double pi;

            //Get user number of decimals of pi and convert to int
            Console.WriteLine("Enter the number of digits of pi to calculate:");
            numDigits = int.Parse(Console.ReadLine());

            //Calculate digits of pi, format string, and output
            pi = CalculatePi(numDigits);
            pi = Truncate(pi, numDigits);

            //Output
            Console.WriteLine("The requested number of digits of pi: " + pi);
            Console.ReadLine();
        }
    }
}
