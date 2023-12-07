problem_file = "input/day4.txt"

pairs = File.read!(problem_file)
    |> String.split("\n", trim: true)
    |> Enum.map(fn (list) ->
        Regex.run(~r"(\d+)-(\d+),(\d+)-(\d+)", list, capture: :all_but_first)
            |> Enum.map(&String.to_integer/1)
    end)

overlaps = Enum.count(pairs, fn ([s1, e1, s2, e2]) -> (s1 <= s2 and s2 <= e1) or (s2 <= s1 and s1 <= e2) end)

IO.inspect(overlaps)
