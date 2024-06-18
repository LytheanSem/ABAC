fun iseven n = n mod 2 = 0;

fun cube n = n*n*n;

fun cuber n:real = n*n*n;

fun third l = (hd (tl (tl l)));

fun max3(x,y,z) =
    if x > y then if x > z then x else z
        else if y > z then y else z;

fun remove2 (x,y,z) = (x,z);

fun fourthch s = hd (tl (tl (tl (explode s))));

(* helper function*)
fun rotate1 l = (tl l) @ [hd l];
fun rotate (l, n) = 
    if n = 0 then l
    else rotate (rotate1 l, n-1);

(* helper function*)
fun minhelper (l, n) =
    if (null l) then n
    else if (hd l > n) then minhelper (tl l, n)
        else minhelper (tl l, hd l);
fun min l = minhelper (tl l, hd l);

(*helper function*)
fun selecthelper (inlist, f, outlist) =
    if null inlist then outlist
    else if f (hd inlist) then selecthelper (tl inlist, f, hd inlist::outlist)
        else selecthelper (tl inlist, f, outlist);
fun select (l, f) = selecthelper(l, f, nil);

