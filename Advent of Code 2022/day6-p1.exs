problem_file = "input/day6.txt"

datastream = File.read!(problem_file) |> String.trim()

result = datastream
    |> String.to_charlist()
    |> Enum.chunk_every(4, 1)
    |> Enum.reduce_while(4, fn (chunk, acc) ->
        cond do
            chunk == Enum.uniq(chunk) -> {:halt, acc}
            true -> {:cont, acc + 1}
        end
    end)

IO.puts(result)
