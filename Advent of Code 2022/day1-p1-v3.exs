problem_file = "input/day1.txt"

result = File.read!(problem_file)
    |> String.split("\n")
    |> Enum.chunk_by(&(&1 != ""))
    |> Enum.reject(&(&1 == [""]))
    |> Enum.map(fn(s) -> s
        |> Enum.map(&String.to_integer/1)
        |> Enum.sum()
    end)
    |> Enum.max()

IO.puts(result)
