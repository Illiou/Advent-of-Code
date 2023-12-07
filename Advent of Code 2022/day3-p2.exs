problem_file = "input/day3.txt"

groups = File.read!(problem_file)
    |> String.split("\n", trim: true)
    |> Enum.map(&String.to_charlist/1)
    |> Enum.chunk_every(3)

badges = Enum.map(groups, fn([first, second, third]) -> hd(Enum.filter(first, &(&1 in second and &1 in third))) end)

priorities = Enum.map(badges, &(if &1 > 90, do: &1 - 96, else: &1 - 38))

IO.puts(Enum.sum(priorities))
