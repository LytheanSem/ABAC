(*Write a function cube of type int - > int that returns the cube of
its parameter. *)

fun cube (x: int) : int = x * x * x;

val result1 = cube 3;   (* Returns 27 *)
val result2 = cube ~2;  (* Returns -8 *)


(*Write a function cuber of type real -> real that returns the cube
of its parameter*)

fun cuber (x: real) : real = x * x * x;

val result3 = cuber 2.5;      (* Returns 15.625 *)
val result4 = cuber ~1.5;     (* Returns -3.375 *)


(*Write a function fourth of type * a list - > ' a that returns the
fourth element of a list. Your function need not behave well on lists with less than
four elements.*)

fun fourth (x::y::z::w::xs) = w
  | fourth _ = raise Fail "List has less than four elements";

val result5 = fourth [1, 2, 3, 4, 5];     (* Returns 4 *)
val result6 = fourth ["a", "b", "c", "d"]; (* Returns "d" *)


(*Write a function min3 of type int * int * int - > int that returns the smallest of three integers.*)

fun min3 (a: int, b: int, c: int) : int =
    if a < b then
        if a < c then a else c
    else
        if b < c then b else c;

val result7 = min3 (5, 2, 8);     (* Returns 2 *)
val result8 = min3 (~3, ~5, ~1);  (* Returns ~5 *)


(*Write a function red3 of type 'a * 'b * 'c  -> 'a * 'c that converts a tuple with 
three elements into one with two by eliminating the second element .*)

fun red3 (a, _, c) = (a, c);

val result9 = red3 (1, "two", 3.0);       (* Returns (1, 3.0) *)
val result10 = red3 ("apple", 2, false);   (* Returns ("apple", false) *)


(*Write a function thirds of type string - > char that retums
the third character of a string. Your function need not behave well on strings with lengths less than 3.*)

fun thirds s = String.sub (s, 2);

val result11 = thirds "abcdef";  (* Returns #"c" *)
val result12 = thirds "12";      (* Returns #"2" *)


(*Write a function cyclel of type 'a list -> 'a list whose
output list is the same as the input list, but with the first element of the list moved to the end. 
For example, cyclel [1,2 ,3 ,4 ] should return [2,3,4,l].*)

fun cyclel (x::xs) = xs @ [x]
  | cyclel [] = [];

val result13 = cyclel [1, 2, 3, 4];    (* Returns [2, 3, 4, 1] *)
val result14 = cyclel ["a", "b", "c"]; (* Returns ["b", "c", "a"] *)


(*Write a function sort3 of real * real * real -> real list that returns a list of three real numbers, 
in sorted order with the smallest first.*)

fun sort3 (a: real, b: real, c: real) : real list =
    if a <= b then
        if b <= c then [a, b, c]
        else if a <= c then [a, c, b]
        else [c, a, b]
    else
        if a <= c then [b, a, c]
        else if b <= c then [b, c, a]
        else [c, b, a];

val result15 = sort3 (3.0, 1.5, 2.0);   (* Returns [1.5, 2.0, 3.0] *)
val result16 = sort3 (~2.0, ~1.0, ~3.0); (* Returns [~3.0, ~2.0, ~1.0] *)


(*Write a function del3 of type 'a list -> 'a list whose output list is the same as the input  list, but with the third element deleted. 
Your function need not behave well on lists with lengths less than 3.*)

fun del3 (x::y::z::xs) = x::y::xs
  | del3 _ = [];

val result17 = del3 [10, 20, 30, 40];     (* Returns [10, 20, 40] *)
val result18 = del3 ["a", "b", "c", "d"]; (* Returns ["a", "b", "d"] *)


(*Write a function sqsum of type int -> int that takes a non-negative integer n and returns the sum of the squares of all the integers 0 through n. 
Your function need not behave well on inputs less than zero.*)

fun sqsum n =
    if n = 0 then 0
    else n * n + sqsum (n - 1);

val result19 = sqsum 3;  (* Returns 14 *)
val result20 = sqsum 0;  (* Returns 0 *)


(*Write a function cycle of type 'a list * int -> 'a list that takes a list and an integer n as input and returns the same list, 
but with the first element cycled to the end of the list n times. (Make use of your cyclel function from a previous exercise). 
For example, cycle ([1,2,3,4,5,6], 2) should return the list [3,4,5,6,1,2].*)

(* Assuming cyclel is defined as follows: *)
fun cyclel (x::xs) = xs @ [x]
  | cyclel [] = [];

(* Definition of cycle function *)
fun cycle (lst, n) =
    if n = 0 then lst
    else cycle (cyclel lst, n - 1);

val result21 = cycle ([1, 2, 3, 4, 5], 2);  (* Returns [3, 4, 5, 1, 2] *)
val result22 = cycle (["a", "b", "c"], 1);   (* Returns ["b", "c", "a"] *)


(*Write a function pow of type real * int -> real that raises a real number to an integer power. 
Your function need not behave well if the integer power is negative.*)

fun pow (x: real, n: int) : real =
    if n = 0 then 1.0
    else if n = 1 then x
    else x * pow (x, n - 1);

val result23 = pow (2.0, 3);   (* Returns 8.0 *)
val result24 = pow (~2.0, 2);  (* Returns 4.0 *)


(*Write a function max of type int list -> int that returns the largest element of a list of integers. 
Your function need not behave well if the list is empty. Hint: write a helper function maxhelper that takes as a second parameter the largest element seen so far. 
Then you can complete the exercise by defining 
fun max x = maxhelper (tl x, hd x);*)

(* Helper function that takes a list and the current maximum *)
fun maxhelper ([], curMax) = curMax
  | maxhelper (x::xs, curMax) = maxhelper (xs, if x > curMax then x else curMax);

(* Main function that initiates the process with the first element as the current maximum *)
fun max x = maxhelper (tl x, hd x);

val result25 = max [5, 2, 8, 1];    (* Returns 8 *)
val result26 = max [~3, ~5, ~1];    (* Returns ~1 *)


(*Write a function isPrime of type int -> bool that returns true if and only if its integer parameter is a prime number. 
Your function need not behave well if the parameter is negative.*)

(* Helper function to check divisibility *)
fun isDivisible (n, divisor) =
    if divisor * divisor > n then false
    else if n mod divisor = 0 then true
    else isDivisible (n, divisor + 1);

(* Main function to check if a number is prime *)
fun isPrime n =
    if n <= 1 then false
    else not (isDivisible (n, 2));

val result27 = isPrime 7;   (* Returns true *)
val result28 = isPrime 10;  (* Returns false *)


(*' a list * ('a -> bool) -> ' a list 
that takes a list and a function f as parameters. Your function should apply f to each element of the list and should return a new list containing only those elements of the original list for which f returned true. ( The elements of the new list may be given in any order). 
For example, evaluating select ([1,2,3,4,5,6,7,8,9,10], isPrime) should result in a list lke [7,5,3,2]. 
This is an example of a higher-order function, since it takes another function as a parameter .*)

fun select ([], _) = []
  | select (x::xs, f) = if f x then x :: select (xs, f) else select (xs, f);

val result29 = select ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], isPrime);
(* Returns [2, 3, 5, 7] *)



