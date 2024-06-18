/*1*/
lcm(X, Y, Z) :- gcd(X, Y, G), Z is abs(X*Y) // G.

/*2*/
max(X, Y, X) :- X >= Y.
max(X, Y, Y) :- X < Y.

/*3*/
maxlist([X], X). % Base case: the max of a single-element list is the element itself.
maxlist([X|Xs], M) :- maxlist(Xs, M1), max(X, M1, M).