namespace AdventOfCode;

public class Day2
{
    public static void Main(string[] args)
    {
        Console.WriteLine('A' - 27);
        Console.WriteLine($"answer for part_1: {Part1()}");
        Console.WriteLine($"answer for part_2: {Part2()}");
    }
    
    static int Part1()
    {
        string[] lines = File.ReadAllLines(@"input");
        int sum = 0;
        foreach(string line in lines)
        {
            Char item = line.Substring(line.Length/2).Intersect(line.Substring(0, line.Length/2)).First();
            sum += Char.IsUpper(item) ? item - 'A' + 27 : item - 'a' + 1;
        }

        return sum;
    }

    static int Part2()
    {
        string[] lines = File.ReadAllLines(@"input");
        int sum = 0;
        for (int i = 0; i < lines.Length / 3; i++)
        {
            Char item = lines[i * 3 + 2].Intersect(lines[i * 3].Intersect(lines[i * 3 + 1])).First();
            sum += Char.IsUpper(item) ? item - 'A' + 27 : item - 'a' + 1;
        }

        return sum;
    }
}