problem_file = "input/day1.txt"

result = File.read!(problem_file)
    |> String.split("\n\n")
    |> Enum.map(fn(s) -> s
        |> String.split("\n", trim: true)
        |> Enum.map(&String.to_integer/1)
        |> Enum.sum()
    end)
    |> Enum.max()

IO.puts(result)
