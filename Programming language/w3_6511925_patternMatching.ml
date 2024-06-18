(*Week 3 Worksheet*)
(*Lythean Sem*)

(*1*)
fun iseven n = n mod 2 = 0;

(*2*)
fun cube n = n*n*n;

(*3*)
fun cuber n:real = n*n*n;

(*4*)
fun third l = (hd (tl (tl l)));

(*5*)
fun max3(x,y,z) =
    if x > y then if x > z then x else z
        else if y > z then y else z;

(*6*)
fun remove2 (x,y,z) = (x,z);

(*7*)
fun fourthch s = hd (tl (tl (tl (explode s))));

(*8*)
fun rotate1 l = (tl l) @ [hd l];
fun rotate (l, 0) = l
|   rotate (l, n) = rotate (rotate1 l, n-1);

(*9*)
fun minhelper (nil, n) = n
|   minhelper (x::xs, n) =
      if x > n then
        minhelper (xs, n)
      else
        minhelper (xs, x);
fun min l = minhelper (tl l, hd l);

(*10*)
(* helper function *)
fun selecthelper (nil, f, outlist) = outlist
|   selecthelper (x::xs, f, outlist) =
      if f x then
        selecthelper (xs, f, x::outlist)
      else
        selecthelper (xs, f, outlist);
fun select (l, f) = selecthelper (l, f, nil);