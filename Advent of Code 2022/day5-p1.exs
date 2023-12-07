problem_file = "input/day5.txt"

[stacks_string, rearrangements_string] = File.read!(problem_file)
    |> String.split("\n\n", trim: true)

{stacks_list, [stack_indices]} = stacks_string
    |> String.split("\n", trim: true)
    |> Enum.split(-1)

stacks_list = stacks_list
    |> Enum.map(&String.to_charlist/1)
    |> Enum.map(&Enum.drop(&1, 1))
    |> Enum.map(&Enum.chunk_every(&1, 1, 4, :discard))

stacks = stacks_list |> Enum.zip_with(fn l -> Enum.reject(l, &(&1 == ' ')) end)
stacks = for {val, i} <- Enum.with_index(stacks), into: %{}, do: {i + 1, val}

rearrangements_list = rearrangements_string |> String.split("\n", trim: true)

rearrangements_list = rearrangements_list
    |> Enum.map(fn (elem) ->
        Regex.run(~r".+?(\d+).+?(\d+).+?(\d+)", elem, capture: :all_but_first) |> Enum.map(&String.to_integer/1)
    end)

stacks = Enum.reduce(rearrangements_list, stacks, fn ([count, from, to], stacks_) ->
    stacks_
        |> Map.put(to, Enum.reverse(Enum.take(stacks_[from], count)) ++ stacks_[to])
        |> Map.put(from, Enum.drop(stacks_[from], count))
    end)

IO.inspect(stacks)

solution = Enum.reduce(Map.values(stacks), [], &([List.first(&1, "") | &2])) |> Enum.reverse

IO.puts(solution)
