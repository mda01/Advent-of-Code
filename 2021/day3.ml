let file = open_in "2021/input3.txt"

let explode s = List.init (String.length s) (String.get s)

let rec get_lines buf f =
  try
    let line = input_line file in
    explode line :: get_lines buf f
  with e ->
    close_in_noerr file;
    buf

let lines = get_lines [] file

let rec pow a = function
  | 0 -> 1
  | 1 -> a
  | n ->
      let b = pow a (n / 2) in
      b * b * if n mod 2 = 0 then 1 else a

let norm l n =
  let rec nor li nli n =
    match li with
    | hd :: tl -> nor tl (nli @ [ (if hd >= n / 2 then 1 else 0) ]) n
    | [] -> nli
  in
  nor (Array.to_list l) [] n

let compute num =
  let rec comrec num cnt exp =
    match num with
    | hd :: tl -> comrec tl (cnt + (hd * pow 2 exp)) (exp - 1)
    | [] -> cnt
  in
  comrec num 0 (List.length num - 1)

let solve3_1 nums =
  let rec s31 nums2 epsilon gamma n =
    match nums2 with
    | hd :: tl ->
        let rec update entry epsilons gammas i =
          match entry with
          | hd2 :: tl2 ->
              if hd2 == '0' then Array.set epsilons i (Array.get epsilons i + 1)
              else Array.set gammas i (Array.get gammas i + 1);
              update tl2 epsilons gammas (i + 1)
          | [] -> s31 tl epsilons gammas n
        in
        update hd epsilon gamma 0
    | [] -> compute (norm gamma n) * compute (norm epsilon n)
  in
  s31 nums
    (Array.make (List.length (List.nth nums 0)) 0)
    (Array.make (List.length (List.nth nums 0)) 0)
    (List.length nums)

let winner list index =
  let rec winrec list ind =
    match list with
    | hd :: tl -> (if List.nth hd ind == '1' then 1 else 0) + winrec tl ind
    | [] -> 0
  in
  if 2 * winrec list index >= List.length list then '1' else '0'

let rec convert list =
  match list with
  | hd :: tl -> (if hd == '1' then 1 else 0) :: convert tl
  | [] -> []

let solve3_2 nums =
  let rec s32 nums2 nums3 it =
    match (nums2, nums3) with
    | [], y -> 0
    | x, [] -> 0
    | [ x ], [ y ] -> compute (convert x) * compute (convert y)
    | [ x ], n3 ->
        let w3 = winner n3 it in
        s32 [ x ] (List.filter (fun x -> w3 != List.nth x it) n3) (it + 1)
    | n2, [ y ] ->
        let w2 = winner n2 it in
        s32 (List.filter (fun x -> w2 == List.nth x it) n2) [ y ] (it + 1)
    | n2, n3 ->
        let w2, w3 = (winner n2 it, winner n3 it) in
        s32
          (List.filter (fun x -> w2 == List.nth x it) n2)
          (List.filter (fun x -> w3 != List.nth x it) n3)
          (it + 1)
  in
  s32 nums nums 0
;;

Sys.command "clear";;

solve3_1 lines;;

solve3_2 lines;;
