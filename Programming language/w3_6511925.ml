(*Lythean Sem*)
(*6511925*)
(*CSX3004*)

(*Q1*)  
fun iseven(n: int): bool =
  n mod 2 = 0;

(*Example of Q1*)
val test1 = iseven 4;     (* Should return true *)
val test2 = iseven 7;     (* Should return false *)


(*Q2*)
fun cube(n: int): int =
  n * n * n;

(*Example of Q2*)
val test3 = cube 2;       (* Should return 8 *)
val test4 = cube 5;       (* Should return 125 *)


(*Q3*)
fun cuber(x: real): real =
  x * x * x;

(*Example of Q3*)
val test5 = cuber 2.0;    (* Should return 8.0 *)
val test6 = cuber 3.5;    (* Should return 42.875 *)


(*Q4*)
fun third(lst: 'a list): 'a =
  hd(tl(tl lst));

(*Example of Q4*)
val test7 = third [1, 2, 3, 4, 5];    (* Should return 3 *)
val test8 = third ["apple", "banana", "cherry", "date"];   (* Should return "cherry" *)


(*Q5*)
fun max3(a: int, b: int, c: int): int =
  if a >= b andalso a >= c then
    a
  else if b >= c then
    b
  else
    c;

(*Example of Q5*)
val test9 = max3(5, 9, 3);    (* Should return 9 *)
val test10 = max3(12, 8, 15);  (* Should return 15 *)


(*Q6*)
fun remove2(x: 'a * 'b * 'c): 'a * 'c =
  let
    val (first, _, third) = x
  in
    (first, third)
  end;

(*Example of Q6*)
val test11 = remove2 (1, "two", 3.0);   (* Should return (1, 3.0) *)
val test12 = remove2 (2, "Three", 5); (* Should return (2, 5) *)


(*Q7*)
fun fourthch(s: string): char =
  String.sub(s, 3);

(*Example of Q7*)
val test13 = fourthch "example";    (* Should return 'm' *)
val test14 = fourthch "abcd";        (* Should return 'd' *)


(*Q8*)
fun rotate([], _) = []
  | rotate(lst, n) =
    let
      val len = length lst
      val n' = n mod len
    in
      List.drop (lst, n') @ List.take (lst, n')
    end;

(*Example of Q8*)
val test15 = rotate([1, 2, 3, 4, 5], 3);   (* Should return [4, 5, 1, 2, 3] *)
val test16 = rotate(["apple", "orange", "banana", "grape"], 2);  (* Should return ["banana", "grape", "apple", "orange"] *)


(*9*)
fun min(lst: int list): int =
  let
    fun minhelper([], smallest) = smallest
      | minhelper(x::xs, smallest) =
        if x < smallest then
          minhelper(xs, x)
        else
          minhelper(xs, smallest)
  in
    minhelper(lst, hd lst)
  end;

(*Example of Q9*)
val test17 = min [5, 8, 2, 1, 9];      (* Should return 1 *)
val test18 = min [15, 7, 12, 18, 3];    (* Should return 3 *)


(*Q10*)
fun select(lst: 'a list, f: 'a -> bool): 'a list =
  let
    fun filter([], acc) = rev acc
      | filter(x::xs, acc) =
        if f x then
          filter(xs, x::acc)
        else
          filter(xs, acc)
  in
    filter(lst, [])
  end;

(*Example of Q10*)
val isodd = fn x => x mod 2 = 1;
val test19 = select([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], isodd);  (* Should return [1, 3, 5, 7, 9] *)
val test20 = select(["apple", "orange", "banana", "grape"], fn s => String.size s > 5); (* Should return ["orange", "banana"] *)


