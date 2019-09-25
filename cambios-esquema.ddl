alter table opcion add column tipo int(11);

alter table texto_subopcion drop foreign key `fk_texto_subopcion_subopcion1`;

update subopcion set idsubopcion=7 where idsubopcion=3;

update texto_subopcion set idsubopcion=7 where idsubopcion=3;

update subopcion set idsubopcion=8 where idsubopcion=2;

update texto_subopcion set idsubopcion=8 where idsubopcion=2;

