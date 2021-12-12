let file = open_in "2021/input2.txt"

type entry = Entry of string * int

let rec get_lines buf f =
  try
    let line = input_line file in
    match String.split_on_char ' ' line with
    | [ hd; tl ] -> Entry (hd, int_of_string tl) :: get_lines buf f
    | _ -> failwith "Invalid line"
  with e ->
    close_in_noerr file;
    buf

let entries = get_lines [] file

let solve2_1 entries =
  let rec s21 e dx dy =
    match e with
    | Entry ("down", v) :: tl -> s21 tl dx (dy + v)
    | Entry ("up", v) :: tl -> s21 tl dx (dy - v)
    | Entry ("forward", v) :: tl -> s21 tl (dx + v) dy
    | _ -> dx * dy
  in
  s21 entries 0 0

let rec solve2_2 entries =
  let rec s22 e aim depth pos =
    match e with
    | Entry ("down", v) :: tl -> s22 tl (aim + v) depth pos
    | Entry ("up", v) :: tl -> s22 tl (aim - v) depth pos
    | Entry ("forward", v) :: tl -> s22 tl aim (depth + (aim * v)) (pos + v)
    | _ -> depth * pos
  in
  s22 entries 0 0 0
;;

Sys.command "clear";;

print_int (solve1_2 nums);;

print_newline ();;

print_int (solve1_2 nums);;

print_newline ()
