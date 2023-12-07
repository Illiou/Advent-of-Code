defmodule AVS do
    def main do
        problem_file = "input/day1.txt"

        lines = File.read!(problem_file) |> String.split("\n")
        food = sum_by_group(lines)
        result = Enum.sort(food) |> Enum.take(-3) |> Enum.sum()
        IO.inspect(result)
    end

    def sum_by_group(lines, sum \\ 0)

    def sum_by_group([], _), do: []

    def sum_by_group([line | lines], sum) do
        if String.trim(line) === "" do
            [sum | sum_by_group(lines)]
        else
            sum_by_group(lines, sum + String.to_integer(line))
        end
    end
end

AVS.main()
