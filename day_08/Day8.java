package day_08;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

public class Day8 {

    static ArrayList<int[]> readInput() {
        ArrayList<int[]> tree_lines = new ArrayList<>();
        try {
            FileReader file = new FileReader("/Users/lorenz/IdeaProjects/advent_of_code/src/day_08/input");
            BufferedReader reader = new BufferedReader(file);

            String line;
            while ((line = reader.readLine()) != null) {
                int[] trees = new int[line.length()];
                for (int i = 0; i < line.length(); i++) {
                    trees[i] = line.charAt(i) - '0';
                }
                tree_lines.add(trees);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
        return tree_lines;
    }

    static int part1() {
        ArrayList<int[]> tree_lines = readInput();
        int visible = tree_lines.size() * 2 + tree_lines.get(0).length * 2 - 4;
        for (int row = 1; row < tree_lines.size() - 1; row++) {
            int[] trees = tree_lines.get(row);
            for (int col = 1; col < trees.length - 1; col++) {
                // To-Do better solution - this is very unsexy
                boolean left = false;
                for (int i = 0; i < col; i++) {
                    if (trees[i] >= trees[col]) {
                        left = true;
                        break;
                    }
                }
                if (!left) {
                    visible++;
                    continue;
                }

                boolean right = false;
                for (int i = col + 1; i < trees.length; i++) {
                    if (trees[i] >= trees[col]) {
                        right = true;
                        break;
                    }
                }
                if (!right) {
                    visible++;
                    continue;
                }

                boolean up = false;
                for (int i = 0; i < row; i++) {
                    if (tree_lines.get(i)[col] >= trees[col]) {
                        up = true;
                        break;
                    }
                }
                if (!up) {
                    visible++;
                    continue;
                }

                boolean down = false;
                for (int i = row + 1; i < tree_lines.size(); i++) {
                    if (tree_lines.get(i)[col] >= trees[col]) {
                        down = true;
                        break;
                    }
                }
                if (!down) {
                    visible++;
                }
            }
        }
        return visible;
    }

    static int part2() {
        ArrayList<int[]> tree_lines = readInput();
        int biggest_scenic_score = 0;
        for (int row = 1; row < tree_lines.size() - 1; row++) {
            int[] trees = tree_lines.get(row);
            for (int col = 1; col < trees.length - 1; col++) {
                int left = 0;
                for (int i = col - 1; i >= 0; i--) {
                    left++;
                    if (trees[i] >= trees[col]) {
                        break;
                    }
                }

                int right = 0;
                for (int i = col + 1; i < trees.length; i++) {
                    right++;
                    if (trees[i] >= trees[col]) {
                        break;
                    }
                }

                int up = 0;
                for (int i = row - 1; i >= 0; i--) {
                    up++;
                    if (tree_lines.get(i)[col] >= trees[col]) {
                        break;
                    }
                }

                int down = 0;
                for (int i = row + 1; i < tree_lines.size(); i++) {
                    down++;
                    if (tree_lines.get(i)[col] >= trees[col]) {
                        break;
                    }
                }
                int scenic_score = left * right * up * down;
                if (scenic_score > biggest_scenic_score) biggest_scenic_score = scenic_score;
            }
        }
        return biggest_scenic_score;
    }

    public static void main(String[] args) {
        System.out.println("the solution for part_1 is: " + part1());
        System.out.println("the solution for part_2 is: " + part2());
    }
}
