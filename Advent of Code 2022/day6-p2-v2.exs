defmodule Day6_p2_v2 do
    def main() do
        problem_file = "input/day6.txt"

        datastream = File.read!(problem_file)
            |> String.trim()

        result = find_unique_substring_index(datastream, 4)

        IO.puts(result)
    end

    def find_unique_substring_index(str, len) do
        bins = for i <- 97..122, into: %{}, do: {i, 0}
        str_charlist = String.to_charlist(str)

        check_next_letter(str_charlist, str_charlist, bins, len, 0, 0)
    end

    def check_next_letter(_, _, _, streak_needed, pos, streak)
        when streak >= streak_needed, do: pos

    def check_next_letter([], _, _, _, _, _), do: -1

    def check_next_letter([char | str_tail], delayed_str, bins, streak_needed, pos, streak)
    when pos < streak_needed do
        cur_letter_count = bins[char] + 1
        bins = Map.replace!(bins, char, cur_letter_count)
        cond do
            cur_letter_count > 1 -> check_next_letter(str_tail, delayed_str, bins, streak_needed, pos + 1, 1)
            cur_letter_count <= 1 -> check_next_letter(str_tail, delayed_str, bins, streak_needed, pos + 1, streak + 1)
        end
    end

    def check_next_letter([char | str_tail], [first_char | delayed_str_tail], bins, streak_needed, pos, streak) do
        cur_letter_count = bins[char] + 1
        bins = Map.replace!(bins, char, cur_letter_count)
        bins = Map.update!(bins, first_char, &(&1 - 1))
        cond do
            cur_letter_count > 1 -> check_next_letter(str_tail, delayed_str_tail, bins, streak_needed, pos + 1, 1)
            cur_letter_count <= 1 -> check_next_letter(str_tail, delayed_str_tail, bins, streak_needed, pos + 1, streak + 1)
        end
    end
end

Day6_p2_v2.main()
