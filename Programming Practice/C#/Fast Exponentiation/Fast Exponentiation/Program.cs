using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Fast_Exponentiation
{
    class Program
    {
        static int Exponentiate(int a, int b)
        {
            int pow;

            //Base case
            if (b == 0)
            {
                return 1;
            }
            else
            {
                //b=2k   => a^b = a^(2k) = a^k a^k = a^(b/2) a^(b/2)
                //b=2k+1 => a^b = a^(2k+1) = a a^(2k) = a a^k a^k = a a^(b/2) a^(b/2)
                pow = (int) Math.Pow(a, b / 2);

                if (b % 2 == 0)
                {
                    return pow * pow;
                }
                else
                {
                    return a * pow * pow;
                }
            }
        }
        static void Main(string[] args)
        {
            int a, b, ans;

            //Gather user input
            Console.Write("Enter value for a: ");
            a = int.Parse(Console.ReadLine());
            Console.Write("Enter value for b: ");
            b = int.Parse(Console.ReadLine());

            //Calculate a^b in O(lg n)
            ans = Exponentiate(a, b);
            Console.Write("a^b = " + ans);
            Console.ReadLine();
        }
    }
}
