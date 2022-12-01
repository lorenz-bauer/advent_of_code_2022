package day_1;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Arrays;

public class Day_1 {
    public static void main(String[] args) {
        int[] best_elves = new int[]{0,0,0,0};
        int current_calories = 0;

        try {
            FileReader in = new FileReader("/Users/lorenz/IdeaProjects/advent_of_code/src/day_1/input");
            BufferedReader br = new BufferedReader(in);
            String line;
            while ((line = br.readLine()) != null) {
                if (!line.isBlank()) {
                    current_calories += Integer.parseInt(line);
                } else {
                    best_elves[0] = current_calories;
                    Arrays.sort(best_elves);
                    current_calories = 0;
                }
            }
            in.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

        int erg = best_elves[1]+best_elves[2]+best_elves[3];
        System.out.printf("number 1: %d, number 2: %d, number 3: %d\n", best_elves[3],best_elves[2],best_elves[1]);
        System.out.println("calories of top 3: " + erg);
    }
}