let file = open_in "2021/input1.txt"

let rec get_lines buf f =
  try
    let line = input_line file in
    int_of_string line :: get_lines buf f
  with e ->
    close_in_noerr file;
    buf

let nums = get_lines [] file

let rec solve1_1 l =
  match l with
  | hd :: hd2 :: tl ->
      if hd2 > hd then 1 + solve1_1 (hd2 :: tl) else solve1_1 (hd2 :: tl)
  | _ -> 0

let rec solve1_2 l =
  match l with
  | hd :: hd2 :: hd3 :: hd4 :: tl ->
      if hd4 > hd then 1 + solve1_2 (hd2 :: hd3 :: hd4 :: tl)
      else solve1_2 (hd2 :: hd3 :: hd4 :: tl)
  | _ -> 0
;;

print_int (solve1_1 nums);;

print_newline ();;

print_int (solve1_2 nums);;

print_newline ()
