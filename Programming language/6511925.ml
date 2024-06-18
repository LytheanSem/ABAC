(*Name: Lythean Sem*)
(*ID: 6511925*)

(*1*)

(*a*)
datatype suit = Hearts | Diamonds | Clubs | Spades;

(*b*)
datatype rank = Ace | One | Two | Three | Four | Five | Six | Seven | Eight | Nine | Jack | Queen | King;


(*2*)

(*a*)



(*b*)
fun cardname s: suit => r: rank => "s" ^ "of" ^ "r";

(*c*)
datatype coin = Penny of int | Nickel of int | Dime of int | Quarter of int;

fun sumcoins (a: coin, b: coin, c: coin, d: coin) =
    case (a, b, c, d) of
        (Quarter a, Dime b, Nickel c, Penny d) => (0.25*real a)+(0.10*real b)+(0.05*real c)+(0.01*real d);

(*d*)
datatype day = Mon | Tue | Thu | Fri | Sat | Sun;


(*e*)
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