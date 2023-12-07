problem_file = "input/day3.txt"

compartments = File.read!(problem_file)
    |> String.split("\n", trim: true)
    |> Enum.map(&(String.split_at(&1, div(String.length(&1), 2))))
    |> Enum.map(fn({left, right}) -> {String.to_charlist(left), String.to_charlist(right)} end)

wrong_items = Enum.map(compartments, fn({left, right}) -> hd(left -- (left -- right)) end)

priorities = Enum.map(wrong_items, &(if &1 > 90, do: &1 - 96, else: &1 - 38))

IO.puts(Enum.sum(priorities))
