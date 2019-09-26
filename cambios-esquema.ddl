alter table opcion add column tipo int(11);

alter table texto_subopcion drop foreign key `fk_texto_subopcion_subopcion1`;

update subopcion set idsubopcion=7 where idsubopcion=3;

update texto_subopcion set idsubopcion=7 where idsubopcion=3;

update subopcion set idsubopcion=8 where idsubopcion=2;

update texto_subopcion set idsubopcion=8 where idsubopcion=2;

insert into opcion (idopcion, posicion, nombre, idpagina, tipo) select idsubopcion,posicion,nombre,idpagina,2 from subopcion;

update texto_subopcion set idtexto=idtexto+20;

insert into texto_opcion (idtexto,idopcion,ididioma,titulo,direccion) select idtexto,idsubopcion,ididioma,titulo,direccion from texto_subopcion;

alter table opcion add column idpadre int(11) null;

update opcion set tipo=1 where tipo is null;

update opcion set idpadre=5 where idopcion in (7,8);


