 CREATE TABLE `dato_opcion` (
  `iddato` int(11) NOT NULL AUTO_INCREMENT,
  `idpagina` int(11) DEFAULT NULL,
  `posicion` int(11) DEFAULT NULL,
  `nombre` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`iddato`),
  KEY `fk_dato_opcion_pagina_idx` (`idpagina`),
  CONSTRAINT `fk_dato_opcion_pagina` FOREIGN KEY (`idpagina`) REFERENCES `pagina` (`idpagina`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `texto_dato` (
  `idtexto` int(11) NOT NULL AUTO_INCREMENT,
  `iddato` int(11) NOT NULL,
  `ididioma` int(11) DEFAULT NULL,
  `titulo` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `direccion` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`idtexto`),
  KEY `fk_texto_dato_idx` (`iddato`),
  KEY `fk_texto_idioma_idx` (`ididioma`),
  CONSTRAINT `fk_texto_idioma` FOREIGN KEY (`ididioma`) REFERENCES `idioma` (`ididioma`),
  CONSTRAINT `fk_texto_dato` FOREIGN KEY (`iddato`) REFERENCES `dato_opcion` (`iddato`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
 
alter table opcion add column iddato int(11);

update opcion set iddato = idopcion;

alter table opcion modify column iddato int(11) not null;

insert into dato_opcion (iddato, idpagina, posicion, nombre) select idopcion,idpagina,posicion,nombre from opcion;

alter table texto_subopcion drop foreign key `fk_texto_subopcion_subopcion1`;

update subopcion set idsubopcion=7 where idsubopcion=3;

update texto_subopcion set idsubopcion=7 where idsubopcion=3;

update subopcion set idsubopcion=8 where idsubopcion=2;

update texto_subopcion set idsubopcion=8 where idsubopcion=2;
