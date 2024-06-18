(*Define a function member of type ' 'a * list -> bool 
so that member (e. L) is true if and only if e is an element of the list L.*)

fun member (_, []) = false
  | member (e, x::xs) = if e = x then true else member (e, xs);

(*Define a function less of type int * int list - > int list
so that less ( e, L) is a list of all the integers in L that are less than e.*)

fun less (e, []) = []
  | less (e, x::xs) = if x < e then x :: less (e, xs) else less (e, xs);

(*Define a function repeats of type ' ' a list -> bool so that repeats (L) is true if  and only if the list L has two equal elements next to each other.*)

fun repeats [] = false
  | repeats [_] = false
  | repeats (x::y::xs) = if x = y then true else repeats (y::xs);

(*Represent a polynomial using a list of its (real) coefficients, starting with the constant coefficient and going only as high as necessary. 
For example, 3x^2 + 5x + 1 would be represented as the list [1.0, 5.0, 3.0] and x^3 - 2x as [0.0, ~0.0, 1.0]. Write a function eval of type real list * real -> real that takes a polynomial represented this way and a value for x and returns the value of that polynomial represented this way and a value for x and returns the value of that polynomial at the given x. 
For example, eval ([1.0, 5.0, 3.0], 2.0) should evaluate to 23.0, because when x = 2, 3x^2 + 5x + 1 = 23.*)

fun eval (coeffs, x) =
    let
        fun evalHelper ([], acc) = acc
          | evalHelper (c::rest, acc) = evalHelper(rest, acc * x + c)
    in
        evalHelper(coeffs, 0.0)
    end;


(*Write a quicksort function of type int list - > int list.
Here's a review of the quicksort algorithm. First pick an element and call it the
pivot. (The head of the list is an easy choice for the pivot.) Partition the rest of the
list into two sublists, one with all the elements less than the pivot and another with all the elements not less than the pivot .Recursively sort the sublists. Combing the two sublists (and the pivot) into a final sorted list.
*)

fun quicksort([]: int list) = []
  | quicksort(pivot::rest: int list) =
    let
        fun partition([], left, right) = (left, right)
          | partition(x::xs, left, right) =
            if x < pivot then partition(xs, x::left, right)
            else partition(xs, left, x::right)
        
        val (lesser, greater) = partition(rest, [], [])
    in
        (quicksort(lesser) @ [pivot] @ quicksort(greater))
    end;

(*Function can be passed as parameters just like other values in ML. For example, consider these function definitions:
    fun square a = a * a ;
    fun double a = a + a;
    fun compute (n, f) = f n;
The functions square and double take a single int parameter and return an int result. The function compute takes a value n and a function f, and returns the result of calling that function f with n as its parameter. So compute(3, square) evaluates to 9, while compute (3, double) evaluates to 6. 
Make another version of your quicksort function, but this time of type 
    ' a list * ('a * 'a -> bool) -> 'a list. The second parameter should be a function that performs the role of the < comparison in your original function. (Hint: This should require only minor changes to your previous quicksort definition).
Why would you want to define such a function? Because it is much more useful than the orginal one. For example, suppose you defined icmp and rcmp like this:
    fun icmp (a, b) = a < b;
    fun rcmp (a : real, b) = a < b;
You could now use quicksort (L, icmp) to sort an integer list L, and you could use quicksort (M, rcmp) to sort a real list M. And if you defined
    fun ircmp (a,b) = a > b;
then you could use quick sort (L, ircmp) to sort the integer list L in reverse order.*)

fun quicksort([], _) = []
  | quicksort(pivot::rest, cmp) =
    let
        fun partition([], left, right) = (left, right)
          | partition(x::xs, left, right) =
            if cmp(x, pivot) then partition(xs, x::left, right)
            else partition(xs, left, x::right)
        
        val (lesser, greater) = partition(rest, [], [])
    in
        (quicksort(lesser, cmp) @ [pivot] @ quicksort(greater, cmp))
    end;

(*In the following exercises, implement sets as Usls, where each element of a set
appears exactly once in the list and the elements appear in no particular order. Do not assume you can sort the lists, Do assume that input lists have no duplicate elements, 
and do guarantee that output lists have no duplicate elements.*)

(*Write a function to test whether an element is a member of a set.*)

fun isMember(_, []) = false
  | isMember(x, (y::ys)) = x = y orelse isMember(x, ys);

(*Write a function to construct the union of two sets.*)

fun union([], setB) = setB
  | union(setA, []) = setA
  | union(setA, setB) =
    let
        fun addUnique([], acc) = acc
          | addUnique(x::xs, acc) =
            if isMember(x, acc) then addUnique(xs, acc)
            else addUnique(xs, x::acc)
    in
        addUnique(setA, setB)
    end;

(*Write a function to construe the intersection of two sets.*)

fun intersection([], _) = []
  | intersection(_, []) = []
  | intersection(setA, setB) =
    let
        fun isCommon(x, ys) =
            List.exists (fn y => x = y) ys
        
        fun findIntersection([], acc) = acc
          | findIntersection(x::xs, acc) =
            if isCommon(x, setB) then findIntersection(xs, x::acc)
            else findIntersection(xs, acc)
    in
        rev (findIntersection(setA, []))
    end;

(*Write a function to construct the powerset of any set. A set's powerset is the set of all of its subsets. Consider the set A = {1,2,3}. It has various subsets: {1}, {1,2}, and so on. Of course the empty set, is a subset of every set. The power set of A is the set of all subsets of A: 
(x| x<= A) = {empty, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}
Your powerset function should take a list (representing the set) and return a list of lists (representing the set of all subsets of the original set). powerset [1,2] should return [ [1,2], [1], [2], [1]] (in any order). Your powerset function need not work on the untyped empty list; it may give an error message when evaluating powerset nil.
But it should work on a typed empty list, so powerset (nil : int list) should give the right answer ([[]]).*)

fun powerset([]) = [[]]
  | powerset(x::xs) =
    let
        val subsetsWithoutX = powerset(xs)
        val subsetsWithX = List.map (fn s => x :: s) subsetsWithoutX
    in
        subsetsWithX @ subsetsWithoutX
    end;
