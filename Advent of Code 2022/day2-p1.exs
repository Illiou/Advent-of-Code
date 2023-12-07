problem_file = "input/day2.txt"

points = %{
    "AX" => 1+3,
    "BX" => 1+0,
    "CX" => 1+6,
    "AY" => 2+6,
    "BY" => 2+3,
    "CY" => 2+0,
    "AZ" => 3+0,
    "BZ" => 3+6,
    "CZ" => 3+3,
}

rounds = File.read!(problem_file)
    |> String.split("\n", trim: true)
    |> Enum.map(&(String.split(&1) |> Enum.join("")))

score = Enum.map(rounds, &(points[&1])) |> Enum.sum()

IO.puts(score)
