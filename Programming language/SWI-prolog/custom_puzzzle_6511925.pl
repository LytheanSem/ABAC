kid(neo).
kid(eva).
kid(albert).

costume(dracula).
costume(little_mermaid).
costume(spiderman).


dressed_as(neo, dracula, 6).
dressed_as(albert, little_mermaid, 8).
dressed_as(eva, spiderman, 10).


solve :- 
    dressed_as(neo, CostumeNeo, AgeNeo),
    write('Neo is '), write(AgeNeo), write(' years old and dressed as '), writeln(CostumeNeo),
    
    dressed_as(albert, CostumeAlbert, AgeAlbert),
    write('Albert is '), write(AgeAlbert), write(' years old and dressed as '), writeln(CostumeAlbert),
    
    dressed_as(eva, CostumeEva, AgeEva),
    write('Eva is '), write(AgeEva), write(' years old and dressed as '), writeln(CostumeEva).
