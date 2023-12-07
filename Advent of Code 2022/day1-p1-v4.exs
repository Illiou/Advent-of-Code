problem_file = "input/day1.txt"

result = File.read!(problem_file)
    |> String.split("\n")
    |> Enum.reduce([0], fn(s, [head | tail]) ->
        if s == "",
            do: [0 | [head | tail]],
            else: [head + String.to_integer(s) |tail]
        end)
    |> Enum.max()

IO.inspect(result)

# 1. Group
# 2. Convert values to int
# 3. Sum groups
# 4. Get max
