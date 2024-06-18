(*1*)
fun exist (a, nill) = false
|   exist (a, x::xs) = if a=x then true else exist (a, xs);

(*2*)
fun lessthan (a, nil) = nil
|   lessthan (a, x::xs) = 
        if a>x then x::lessthan (a,xs);
        else lessthan (a, xs);

(*3*)
fun repeats (a::b::rest) = a = b orelse repeats (b::rest)
|   repeats _ = false;

(*4*)
fun member (a, nill) = false
|   member (a, x::xs) = if a=x then true else member (a, xs);

(*5*)
fun union (xs, nill) = xs
|   union (xs, y::ys) = if member (y,xs) then union (xs, ys)
                                        else y::union(xs, ys);

(*6*)
fun intersection (xs, nill) = nil
|   intersection (xs, y::ys) = if member(y, xs) then y::intersection (xs, ys)
                                                else intersection (xs, ys);

(*7*)
fun powerset nill = [nill]
|   powerset (head::rest) = 
    let
        fun addToEach (e, nill) = nill
        |   addToEach (e, x::xs) = (e::x)::addToEach(e, xs);
        val a = powerset rest;
    in
        addToeach(head, a) @ a
    end;