(*
Lythean Sem
6511925
CSX3004
*)

(*Q1*)
fun exist (e, []) = false
  | exist (e, x::xs) = (e = x) orelse exist(e, xs);

(*Q2*)
fun lessthan(e,[]) = []
  | lessthan (e, x::xs) = 
  if (x < e) then x :: lessthan(e,xs) 
  else lessthan(e,xs);

(*Q3*)
fun repeats ([]) = false
  | repeats([first]) = false
  | repeats(first::second::rest) =
  if (first=second) then true
  else repeats(second::rest);

(*Q4*)
fun quicksort ([]) = []
  | quicksort (pivot::rest) =
  let
    val smaller = List.filter (fn x => x < pivot) rest
    val larger = List.filter (fn x => x >= pivot) rest
  in
    quicksort(smaller) @ [pivot] @ quicksort(larger)
  end;

(*Q5*)
fun member(x, []) = false
  | member(x, y::ys) = if x = y then true else member(x, ys);

(*Q6*)
fun member(x, []) = false
  | member(x, y::ys) = x = y orelse member(x, ys);

fun union([], ys) = ys
  | union(x::xs, ys) =
      if member(x, ys) then union(xs, ys)
      else x :: union(xs, ys);

(*Q7*)
fun member(x, []) = false
  | member(x, y::ys) = x = y orelse member(x, ys);

fun intersection([], _) = []
  | intersection(_, []) = []
  | intersection(x::xs, ys) =
      if member(x, ys) then
        x :: intersection(xs, ys)
      else
        intersection(xs, ys);

(*Q8*)
fun powerset([]) = [[]]
  | powerset(x::xs) =
      let
        val subsetsWithoutX = powerset xs
        val subsetsWithX = List.map (fn s => x :: s) subsetsWithoutX
      in
        subsetsWithoutX @ subsetsWithX
      end;
