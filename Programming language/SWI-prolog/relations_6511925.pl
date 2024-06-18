male(kim).
male(kent).
male(herbert).
female(holly).
female(esther).
female(jean).

parent(kim, holly).
parent(margaret, kim).
parent(margaret, kent).
parent(esther, margaret).
parent(herbert, margarent).
parent(herbert, jean).

mother(X, Y) :- female(X), parent(X,Y).
father(X, Y) :- male(X), parent(X, Y).
sister(X, Y) :- female(X), parent(Z, X), parent(Z, Y), X = Y.
brother(X, Y) :- male(X), parent(Z, X), parent(Z, Y), X = Y.
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X = Y.
cousin(X, Y) :- parent(A, X), parent(B, Y), sibling(A, B).