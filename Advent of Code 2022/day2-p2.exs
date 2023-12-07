problem_file = "input/day2.txt"

points = %{
    "AX" => 3+0,
    "BX" => 1+0,
    "CX" => 2+0,
    "AY" => 1+3,
    "BY" => 2+3,
    "CY" => 3+3,
    "AZ" => 2+6,
    "BZ" => 3+6,
    "CZ" => 1+6,
}

rounds = File.read!(problem_file)
    |> String.split("\n", trim: true)
    |> Enum.map(&(String.split(&1) |> Enum.join("")))

score = Enum.map(rounds, &(points[&1])) |> Enum.sum()

IO.puts(score)
