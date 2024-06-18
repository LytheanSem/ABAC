(*Write a function il2rl of type int list - > real list
that takes a list of integers and returns a list of the same numbers converted
to type real. For example, if you evaluate il2rl [1, 2, 3] you should get
[1.0 , 2.0, 3, 0].*)

fun il2rl(lst: int list) = List.map Real.fromInt lst;

(*Write a function ordlist of type char list -> int list that takes a list of characters and returns the list of the integer codes of those character. For example, 
if you evaluate ordlist [#"A", #"b", #'C"] you should get [65, 98, 67]*)

fun ordlist(lst: char list) = List.map Char.ord lst;

(*Write a function squarelist of type int list -> list that takes a list of integers and returns the list of squares of those integers. 
For example, if you evaluate squarelist [1,2,3,4] you should get [1,4,9,16].*)

fun squarelist(lst: int list) = List.map (fn x => x * x) lst;

(*Write a function multpairs of type (int * int) list -> int list that takes a list of pairs of integers and returns a list of the product of each pair. 
For example, if the input is [(1,2) , (3,4)], your function should return  [2,12].
*)

fun multpairs(lst: (int * int) list) = List.map (fn (x, y) => x * y) lst;

(*Write a function inclist of type int list -> int -> int list that takes a list of integers and an integer increment, and return the same list of integers but with integer increment added to each one. For example, 
if you evaluate inclist [1,2,3,4] 10 you should get [11,12,13,14]. Note that the function is curried. *)

fun inclist(lst: int list) (increment: int) = List.map (fn x => x + increment) lst;

(*Write a function bor of type bool list -> bool that takes a list of boolean values and returns the logical OR of all of them. 
If the list is empty, your function should return false.*)

fun bor(lst: bool list) = List.foldl (fn (x, acc) => x orelse acc) false lst;

(*Write a function band of type bool list -> bool that takes a list of boolean values and returns the logical AND of all of them. 
If the list is empty, your function should return true.*)

fun band(lst: bool list) = List.foldl (fn (x, acc) => x andalso acc) true lst;

(*Write a function bxor of type bool list -> bool that takes a list of boolean values and returns the logical exclusive OR of all of them. 
(It should return true if the number of true values in the list is odd and false if the number of true values is even.) If the list is empty, your function should return false.
*)

fun bxor(lst: bool list) = List.foldl (fn (x, acc) => (x orelse acc) andalso not (x andalso acc)) false lst;

(*Write function dupList of type 'a list -> ' a list whose output list is the same as the input list, but with each element of the input list repeated twice in a row. 
For example, if the input list is [1,3,2], the output list should be [1,1,3,3,2,2]. If the input list is [], the output list should be [].*)

fun dupList(lst: 'a list) = List.map (fn x => [x, x]) lst |> List.concat;

(*Write a function myLength of type 'a list -> int that returns the length of a list. 
(Of course, you may not use the predefined length function to do it).*)

fun myLength(lst: 'a list) = List.foldl (fn (_, acc) => acc + 1) 0 lst;

(*Write a function il2absrl of type int list -> real list that takes a list of integers and returns and returns a list containing the absolute values of those integers, converted to real numbers.*)

fun il2absrl(lst: int list) = List.map (fn x => Real.fromInt (abs x)) lst;

(*Write a function truecount of type bool list -> int that takes a list of boolean values and returns the number of trues in the list.*)

fun truecount(lst: bool list) = List.foldl (fn (x, acc) => if x then acc + 1 else acc) 0 lst;

(*Write a function maxpairs of type (int * int) list -> int list that takes a list of pairs of integers and returns the list of the max elements from each pair. 
For example, if you evaluate maxpairs [(1,3), (4,2), (-3,-4)] you should get [3,4,-3]*)

fun maxpairs(lst: (int * int) list) = List.map (fn (x, y) => Int.max(x, y)) lst;

(*Write a function myimplode that works just like the predefined implde. In other words, it should be a function of type char list -> string that takes a list of character and returns the string containing those same character in that same order.*)

fun myimplode(lst: char list) = String.implode(List.map str [lst]);

(*Write a function lconcat of type 'a list list -> 'a list that takes a list of lists as input and returns the list formed by appending the input lists together in order. For example, if the input is [[1,2], [3,4,5,6], [7]], our function should return [1,2,3,4,5,6,7]. 
(There is a predefined function like this called concat, which of course you should not use).*)

fun lconcat(lst: 'a list list) = List.foldl (fn (sublist, acc) => sublist @ acc) [] lst;

(*Write a function max of type int list -> int that returns the largest element of a list of integers. Your function need not behave well if the list is empty.*)

fun max(lst: int list) = List.foldl Int.max (hd lst) (tl lst);

(*Write a function min of type int list -> int that returns the smallest element of a list of integers. Your function need not behave well if the list is empty.*)

fun min(lst: int list) = List.foldl Int.min (hd lst) (tl lst);

(*Write a function member of type ' 'a * ' 'a list -> bool so that member (e, L) is true if and only if e is an element of list L.*)

fun member (e, lst: 'a list) = List.exists (fn x => x = e) lst;

(*Write a function append of type ' a list -> ' a list -> ' a list that takes two lists and returns the result of appending the second one onto the end of the first. For example, append [1,2,3] [4,5,6] should evaluate to [1,2,3,4,5,6]. 
Do not use predefined appending utilities, like the @ operator or the concat function. Note that the function is curried.*)

fun append(lst1: 'a list) (lst2: 'a list) =
    List.foldr (fn (x, acc) => x :: acc) lst2 lst1;

(*Define a function less of type int * int list -> int list so that lees (e, L) is a list of all the integers in L that are less than e (in any order).*)

fun less(e, lst: int list) =
    List.filter (fn x => x < e) lst;

(*Write a function evens of type int list -> int list that takes a list of integers and returns the list of all the even elements from the original list (int the original order). 
For example, if you evaluate evens [1,2,3,4] you should get [2,4].*)

fun evens(lst: int list) =
    List.filter (fn x => x mod 2 = 0) lst;

(*Write a function convert of type (' a * ' b) list -> ' a list * ' b list, that converts a list of pairs into a pair of lists, preserving the order of the elements. 
For example, convert [ (1,2), (3,4), (5,6) ] should evaluate to ([1,3,5], [2,4,6]).*)

fun convert(lst: ('a * 'b) list) =
    let
        val (list1, list2) = List.foldr (fn ((x, y), (acc1, acc2)) => (x :: acc1, y :: acc2)) ([], []) lst
    in
        (list1, list2)
    end;

(*Define a function mymap with the same type and behavior as map, but without using map. ( Note this should be a one-liner: use foldl or foldr).*)

fun mymap (f: 'a -> 'b) (lst: 'a list) = List.foldr (fn (x, acc) => (f x) :: acc) [] lst;

(*Represent a polynomial using a list of its (real) coefficients, starting with the constant coefficient and going only as high as necessary. For example, 3x^2 + 5x + 1 would be represented as the list [1.0,2.0,3.0] and x^3 - 2x as [0.0, -2.0, 0.0, 1.0]. 
Write a function eval of type rea list -> real -> real that takes a polynomial at the given x. 
For example, eval [1.0, 5.0, 3.0] 2.0 should evaluate to 23.0, because when x = 2, 3x^2 + 5x + 1 = 23.*)

fun eval(coefficients: real list) (x: real) =
    let
        val n = length coefficients - 1  (* Get the highest degree of the polynomial *)
        fun evalTerm (coeff, degree) = coeff * (Math.pow(x, Real.fromInt degree))
    in
        List.foldl (fn (coeff, acc) => acc + evalTerm(coeff, n)) 0.0 (coefficients)
    end;

(*Define a function mymap2 with the same type and behavior as map.*)

fun mymap2 (f: 'a -> 'b) (lst: 'a list) =
    case lst of
        [] => []
      | x::xs => f x :: mymap2 f xs;

(*Define a function myfoldr with the same type and behavior as foldr.*)

fun myfoldr (f: 'a * 'b -> 'b) (acc: 'b) (lst: 'a list) =
    case lst of
        [] => acc
      | x::xs => f (x, myfoldr f acc xs);

(*Define a function myfoldl with the same type and behavior as foldl.*)

fun myfoldl (f: 'a * 'b -> 'a) (acc: 'a) (lst: 'b list) =
    case lst of
        [] => acc
      | x::xs => myfoldl f (f (acc, x)) xs;

