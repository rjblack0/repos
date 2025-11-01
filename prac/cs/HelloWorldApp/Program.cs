using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter your name: ");
        string name = Console.ReadLine();
        Console.WriteLine("Hello, " + name + "!");

        Console.Write("How old are you? ");
        string age = Console.ReadLine();

        Console.Write("What month were you born in? ");
        string monthInput = Console.ReadLine();

        int monthNumber = MonConv.ConvertMonth(monthInput);

        if (monthNumber == 0)
        {
            Console.WriteLine("Invalid month entered.");
        }
        else
        {
            int ageInt = int.Parse(age);
            Console.WriteLine($"You were born in month #{monthNumber}.");
            Console.WriteLine($"Your age in months is {ageInt * 12}.");
        }
    }
}

public class MonConv
{
    public static int ConvertMonth(string input)
    {
        if (string.IsNullOrEmpty(input))
            return 0;

        string month = input.Substring(0, 3).ToLower();

        switch (month)
        {
            case "jan": return 1;
            case "feb": return 2;
            case "mar": return 3;
            case "apr": return 4;
            case "may": return 5;
            case "jun": return 6;
            case "jul": return 7;
            case "aug": return 8;
            case "sep": return 9;
            case "oct": return 10;
            case "nov": return 11;
            case "dec": return 12;
            default: return 0;
        }
    }
}