read_location(kitchen). read_location(living_room).
glasses_location(kitchen_table). glasses_location(coffee_table).



not(glasses_on_kitchen_table) :- read_location(kitchen), not(saw_glasses_at_breakfast).


saw_glasses_at_breakfast :- glasses_on(kitchen_table).
saw_glasses_at_breakfast :- fail.


glasses_on(coffee_table) :- read_location(living_room).


where_are_glasses(Location) :-
    (glasses_on(kitchen_table), Location = kitchen_table, !);
    (glasses_on(coffee_table), Location = coffee_table, !);
    (Location = unknown).


query(Location) :- where_are_glasses(Location), write('Glasses are on the '), write(Location), nl.
