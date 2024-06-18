(*Write a datatype definition for a type suit whose values are the four suits of deck of playing cards.*)

datatype suit = Hearts | Diamonds | Clubs | Spades;

val mySuit = Hearts;  (* Assigns the Hearts suit to the variable mySuit *)

(*Using your definition from previous exercise, write a function suitname of type suit -> string that returns a string giving the name of a suit.*)

fun suitname(s: suit) =
    case s of
        Hearts => "Hearts"
      | Diamonds => "Diamonds"
      | Clubs => "Clubs"
      | Spades => "Spades";

val mySuit = Hearts;
val name = suitname mySuit;  (* Assigns "Hearts" to the variable name *)

(*Write a datatype definition for a type number whose values are either integers or real numbers.*)

datatype number = Int of int | Real of real;

val intNumber = Int 42;        (* Represents an integer value 42 *)
val realNumber = Real 3.14;    (* Represents a real number value 3.14 *)

(*Using your definition from previous exercise, write a function plus of type number -> number -> number that adds two numbers, coercing int to real only if necessary.*)

fun plus(a: number, b: number) =
    case (a, b) of
        (Int x, Int y) => Int (x + y)       (* Add two integers, result is an Int *)
      | (Int x, Real y) => Real (real x + y) (* Add int to real, result is a Real *)
      | (Real x, Int y) => Real (x + real y) (* Add real to int, result is a Real *)
      | (Real x, Real y) => Real (x + y);    (* Add two real numbers, result is a Real *)

(*Write a function addup of type intnest -> int that adds up all the integers in an intnest. Use this definition for intnest. (Be careful as you type. INT is not the same as int!)
datatype intnest = 
    INT of int |
    LIST of intnest list;*)


datatype intnest = INT of int | LIST of intnest list;

fun addup(nest: intnest): int =
    case nest of
        INT x => x               (* If it's an INT, return the integer *)
      | LIST [] => 0             (* If it's an empty list, return 0 *)
      | LIST (hd::tl) =>         (* If it's a non-empty list, recurse on each element *)
          addup hd + addup (LIST tl);

(*Write a function prod of type int myList -> int that takes an int mylist x and returns the product of all the elements of x. If the list is NIL your function should return 1. Here again is the definition of myList
datatype 'element mylist = 
    NIL | 
    CONS of 'element * ' element  mylist;*)


datatype 'element mylist = NIL | CONS of 'element * 'element mylist;

fun prod(x: int mylist): int =
    case x of
        NIL => 1                           (* Base case: if list is empty, return 1 *)
      | CONS (head, tail) => head * prod(tail);  (* Multiply head with product of tail *)




(*Write a function reverse of type ' a mylist -> 'a mylist ->  'a mylist that takes two mylist values, a and b, and 
returns the mylist containing all the elements of a followed by all the elements of b. (Use the mylist definition from previous exercise).*)

datatype 'a mylist = NIL | CONS of 'a * 'a mylist;

fun reverse(a: 'a mylist, b: 'a mylist): 'a mylist =
    case a of
        NIL => b                         (* If 'a' is empty, return 'b' as is *)
      | CONS (x, xs) => CONS (x, reverse(xs, b));  (* Add 'x' to 'b' and recurse on 'xs' and 'b' *)


(*Write a function append of type ' a mylist -> ' a mylist -> ' a mylist that takes two mylist values, a and b, and returns the mylist 
containinng all the elements of a followed by all the elements of b. (Use the mylist definition from previous exercise).*)

datatype 'a mylist = NIL | CONS of 'a * 'a mylist;

fun append(a: 'a mylist, b: 'a mylist): 'a mylist =
    case a of
        NIL => b                             (* If 'a' is empty, return 'b' as is *)
      | CONS (x, xs) => CONS (x, append(xs, b));  (* Add 'x' to the result of appending 'xs' and 'b' *)

(*Write a function appendall of type ' a list tree -> ' a list that takes a tress of lists and returns the result of appending all the lists together. 
Put the list for a node together in this order: first the contents of the left subtree, then the list at this node, and then the contents of the right subtree. Here again is the definition of tree.
datatype 'data tree = 
    Empty |
    Node of 'data tree * ' data * ' data tree;*)

datatype 'a tree = Empty | Node of 'a tree * 'a * 'a tree;

fun appendall(t: 'a tree): 'a list =
    case t of
        Empty => []  (* If it's an empty tree, return an empty list *)
      | Node (left, lst, right) => 
            appendall(left) @ lst @ appendall(right);  (* Concatenate lists in the desired order *)

(*A complete binary tree is one in which every Node has either two Empty children 
or two Node children but not one of each. Write a function isComplete of type ' a tree -> bool that tests whether a tree is complete. Use the tree definition from previous exercise.*)

datatype 'a tree = Empty | Node of 'a tree * 'a * 'a tree;

fun isComplete(t: 'a tree): bool =
    let
        (* Helper function to check if a tree is complete from a specific depth *)
        fun isCompleteDepth(t: 'a tree, depth: int): bool =
            case t of
                Empty => true  (* Empty tree is complete by definition *)
              | Node (left, _, right) =>
                    (* Check if left and right subtrees are complete up to the same depth *)
                    isCompleteDepth(left, depth - 1) andalso isCompleteDepth(right, depth - 1)
    in
        (* Helper function to calculate the depth of the tree *)
        fun depth(t: 'a tree): int =
            case t of
                Empty => 0
              | Node (left, _, right) => 1 + Int.max(depth(left), depth(right))

        (* Check if the tree is complete up to its maximum depth *)
        isCompleteDepth(t, depth(t))
    end;

(*A binary search tree is a binary tree with special properties. It may be Empty. 
It may be a Node containing a left subtree, a data item x, and a right subtree. In this case all the data items in the tree are different, 
all the items in the left subtree are smaller than x, all the items in the right subtree are greater than x, and the left and right subtrees are also binary search trees. Write a function makeBST of type ' a list -> (' a * ' a -> bool) -> ' a tree that organizes the items in the list into a binary search tree. 
The tree need not be balanced. You may assume that no item in the list is repeated.*)

datatype 'a tree = Empty | Node of 'a tree * 'a * 'a tree;

fun makeBST(lst: 'a list, cmp: 'a * 'a -> bool): 'a tree =
    let
        (* Helper function to insert an item into a BST *)
        fun insert(item: 'a, tree: 'a tree): 'a tree =
            case tree of
                Empty => Node(Empty, item, Empty)  (* Create a new node if the tree is empty *)
              | Node(left, value, right) =>
                    if cmp(item, value) then
                        Node(insert(item, left), value, right)  (* Insert into the left subtree if item is smaller *)
                    else
                        Node(left, value, insert(item, right))  (* Insert into the right subtree if item is greater *)

        (* Fold over the list to insert items into the tree *)
        fun insertAll(items: 'a list, tree: 'a tree): 'a tree =
            foldl (fn (item, t) => insert(item, t)) tree items
    in
        insertAll(lst, Empty)  (* Start with an empty tree and insert all items from the list *)
    end;

(*Write a function searchBST of type ' ' a tree -> (' ' a * ' ' a -> bool) -> bool that searches a binary search tree for a given data element. (Refer to previous exercise for the definition of a binary search tree). 
You should not search every node in the tree, but only those nodes that, according to the definition, might contain the element you are looking for.*)

datatype 'a tree = Empty | Node of 'a tree * 'a * 'a tree;

fun searchBST(tree: 'a tree, cmp: 'a * 'a -> bool, elem: 'a): bool =
    case tree of
        Empty => false  (* If the tree is empty, the element is not found *)
      | Node(left, value, right) =>
            if cmp(elem, value) then
                searchBST(left, cmp, elem)  (* Search in the left subtree if the element is smaller *)
            else if cmp(value, elem) then
                searchBST(right, cmp, elem)  (* Search in the right subtree if the element is greater *)
            else
                true  (* Found the element in the current node *)
