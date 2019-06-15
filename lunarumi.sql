-- MySQL dump 10.13  Distrib 5.6.26, for osx10.8 (x86_64)
--
-- Host: uuubuntu    Database: lunarumi
-- ------------------------------------------------------
-- Server version	5.5.5-10.3.10-MariaDB-1:10.3.10+maria~bionic-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$150000$WEoWfTNgjC6K$KbfOSI212qmAVg//wXoGN/mJe8DTsSBgQMM62s1eoqI=','2019-06-15 19:41:10.536965',1,'admin','','','miguelpayet@gmail.com',1,1,'2019-06-03 01:29:09.963055');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contacto`
--

DROP TABLE IF EXISTS `contacto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contacto` (
  `idcontacto` int(11) NOT NULL AUTO_INCREMENT,
  `mail` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `direccion` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `telefonos` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`idcontacto`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacto`
--

LOCK TABLES `contacto` WRITE;
/*!40000 ALTER TABLE `contacto` DISABLE KEYS */;
INSERT INTO `contacto` VALUES (1,'contacto@lunarumi.com','Camino Ccotohuincho s/n \r\n\r\nUrubamba - Cusco - Perú','**CUSCO**\r\n\r\nTel. (51-84) 20-1797 Fax: (51-84) 20-1235\r\n\r\n**LIMA**\r\n\r\nTel. (51-1) 242-0548 Fax: (51-1) 446-5668');
/*!40000 ALTER TABLE `contacto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-06-03 01:39:38.649408','1','Español',1,'[{\"added\": {}}]',7,1),(2,'2019-06-03 01:39:47.387972','2','Inglés',1,'[{\"added\": {}}]',7,1),(3,'2019-06-04 03:06:54.049248','1','Inicio',1,'[{\"added\": {}}, {\"added\": {\"name\": \"Texto Imagen\", \"object\": \"1\"}}, {\"added\": {\"name\": \"Texto Imagen\", \"object\": \"2\"}}]',9,1),(4,'2019-06-04 18:14:33.739885','1','2014x768-1.png',1,'[{\"added\": {}}, {\"added\": {\"name\": \"Texto Imagen\", \"object\": \"1\"}}, {\"added\": {\"name\": \"Texto Imagen\", \"object\": \"2\"}}]',8,1),(5,'2019-06-04 18:15:12.153986','2','2014x768-2.png',1,'[{\"added\": {}}, {\"added\": {\"name\": \"Texto Imagen\", \"object\": \"3\"}}, {\"added\": {\"name\": \"Texto Imagen\", \"object\": \"4\"}}]',8,1),(6,'2019-06-04 18:15:38.584314','1','2014x768-1.png',2,'[{\"changed\": {\"name\": \"Texto Imagen\", \"object\": \"2\", \"fields\": [\"texto\"]}}]',8,1),(7,'2019-06-05 03:14:12.386747','2','Inglés',2,'[{\"changed\": {\"fields\": [\"codigo\"]}}]',7,1),(8,'2019-06-05 03:14:18.254687','1','Español',2,'[{\"changed\": {\"fields\": [\"codigo\"]}}]',7,1),(9,'2019-06-06 02:31:15.726711','2','Inglés',2,'[{\"changed\": {\"fields\": [\"codigo\"]}}]',7,1),(10,'2019-06-06 02:31:24.333870','2','Inglés',2,'[]',7,1),(11,'2019-06-06 02:31:33.001101','1','Español',2,'[{\"changed\": {\"fields\": [\"codigo\"]}}]',7,1),(12,'2019-06-06 03:19:16.510666','1','Inicio',2,'[{\"changed\": {\"name\": \"Texto Opci\\u00f3n\", \"object\": \"Inicio\", \"fields\": [\"direccion\"]}}, {\"changed\": {\"name\": \"Texto Opci\\u00f3n\", \"object\": \"Home\", \"fields\": [\"direccion\"]}}]',9,1),(13,'2019-06-06 03:20:09.112874','2','Quienes Somos',1,'[{\"added\": {}}, {\"added\": {\"name\": \"Texto Opci\\u00f3n\", \"object\": \"Quienes Somos\"}}, {\"added\": {\"name\": \"Texto Opci\\u00f3n\", \"object\": \"Who We Are\"}}]',9,1),(14,'2019-06-06 03:20:48.941130','3','Instalaciones',1,'[{\"added\": {}}, {\"added\": {\"name\": \"Texto Opci\\u00f3n\", \"object\": \"Instalaciones\"}}, {\"added\": {\"name\": \"Texto Opci\\u00f3n\", \"object\": \"Facilities\"}}]',9,1),(15,'2019-06-06 03:21:12.075241','4','Tours',1,'[{\"added\": {}}, {\"added\": {\"name\": \"Texto Opci\\u00f3n\", \"object\": \"Tours\"}}, {\"added\": {\"name\": \"Texto Opci\\u00f3n\", \"object\": \"Tours\"}}]',9,1),(16,'2019-06-06 03:21:33.660739','5','Servicios',1,'[{\"added\": {}}, {\"added\": {\"name\": \"Texto Opci\\u00f3n\", \"object\": \"Servicios\"}}, {\"added\": {\"name\": \"Texto Opci\\u00f3n\", \"object\": \"Services\"}}]',9,1),(17,'2019-06-06 03:22:08.182556','6','Contacto',1,'[{\"added\": {}}, {\"added\": {\"name\": \"Texto Opci\\u00f3n\", \"object\": \"Contacto\"}}, {\"added\": {\"name\": \"Texto Opci\\u00f3n\", \"object\": \"Contact\"}}]',9,1),(18,'2019-06-08 19:34:11.512243','8','Quienes Somos',1,'[{\"added\": {}}]',10,1),(19,'2019-06-08 19:37:31.169850','8','Quienes Somos',2,'[{\"added\": {\"name\": \"Secci\\u00f3n Texto con Foto\", \"object\": \"1\"}}, {\"added\": {\"name\": \"Secci\\u00f3n Texto con Foto\", \"object\": \"2\"}}]',10,1),(20,'2019-06-09 14:10:02.676547','6','Fotos Página Inicial - 1',1,'[{\"added\": {}}, {\"added\": {\"name\": \"Foto de Secci\\u00f3n Foto\", \"object\": \"matrimonial_jMteVDV.jpg\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Habitaci\\u00f3n Matrimonial\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Double Room\"}}]',11,1),(21,'2019-06-09 14:10:52.324418','6','Fotos Página Inicial - 1',2,'[{\"added\": {\"name\": \"Foto de Secci\\u00f3n Foto\", \"object\": \"doble-1.jpg\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Habitaci\\u00f3n Doble\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Twin Room\"}}]',11,1),(22,'2019-06-09 14:11:22.046734','6','Fotos Página Inicial - 1',2,'[{\"added\": {\"name\": \"Foto de Secci\\u00f3n Foto\", \"object\": \"doble-2.jpg\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Habitaci\\u00f3n Doble\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Twin Room\"}}]',11,1),(23,'2019-06-09 14:11:44.326069','6','Fotos Página Inicial - 1',2,'[{\"added\": {\"name\": \"Foto de Secci\\u00f3n Foto\", \"object\": \"triple.jpg\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Habitaci\\u00f3n Triple\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Triple Room\"}}]',11,1),(24,'2019-06-09 14:17:59.514099','6','Fotos Página Inicial - 1',2,'[]',11,1),(25,'2019-06-10 04:24:29.943264','6','Fotos Página Inicial - 1',2,'[{\"added\": {\"name\": \"Fila Secci\\u00f3n Foto\", \"object\": \"1\"}}, {\"added\": {\"name\": \"Foto de Fila Secci\\u00f3n Foto\", \"object\": \"1\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Double room\"}}]',11,1),(26,'2019-06-10 04:25:44.269398','6','Fotos Página Inicial - 1',2,'[{\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Double room\"}}, {\"changed\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Double room\", \"fields\": [\"texto\"]}}]',11,1),(27,'2019-06-11 02:00:40.367751','6','Fotos Página Inicial - 1',2,'[{\"added\": {\"name\": \"Foto de Fila Secci\\u00f3n Foto\", \"object\": \"2\"}}, {\"added\": {\"name\": \"Foto de Fila Secci\\u00f3n Foto\", \"object\": \"3\"}}, {\"changed\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Double room\", \"fields\": [\"texto\"]}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Habitaci\\u00f3n Doble\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Twin Room\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Habitaci\\u00f3n Doble\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Twin Room\"}}]',11,1),(28,'2019-06-11 02:01:53.330730','6','Fotos Página Inicial - 1',2,'[{\"added\": {\"name\": \"Foto de Fila Secci\\u00f3n Foto\", \"object\": \"4\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Habitaci\\u00f3n Triple\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Triple Room\"}}]',11,1),(29,'2019-06-11 02:10:58.431563','6','Fotos Página Inicial - 1',2,'[{\"added\": {\"name\": \"Fila Secci\\u00f3n Foto\", \"object\": \"2\"}}, {\"added\": {\"name\": \"Foto de Fila Secci\\u00f3n Foto\", \"object\": \"1\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Vereda Interior\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Inner Walkway\"}}]',11,1),(30,'2019-06-11 02:12:31.049082','6','Fotos Página Inicial - 1',2,'[{\"added\": {\"name\": \"Foto de Fila Secci\\u00f3n Foto\", \"object\": \"2\"}}, {\"added\": {\"name\": \"Foto de Fila Secci\\u00f3n Foto\", \"object\": \"3\"}}, {\"added\": {\"name\": \"Foto de Fila Secci\\u00f3n Foto\", \"object\": \"4\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Jardines\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Gardens\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Comedor\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Dining Room\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Ave\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Bird\"}}]',11,1),(31,'2019-06-11 02:14:24.029073','6','Fotos Página Inicial - 1',2,'[{\"added\": {\"name\": \"Fila Secci\\u00f3n Foto\", \"object\": \"2\"}}, {\"added\": {\"name\": \"Foto de Fila Secci\\u00f3n Foto\", \"object\": \"1\"}}, {\"changed\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Inner Walkway\", \"fields\": [\"texto\"]}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Balcones\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Balconies\"}}]',11,1),(32,'2019-06-11 02:15:01.271471','6','Fotos Página Inicial - 1',2,'[{\"added\": {\"name\": \"Foto de Fila Secci\\u00f3n Foto\", \"object\": \"1\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Arboles Frutales\"}}, {\"added\": {\"name\": \"Texto de Foto de Secci\\u00f3n Foto\", \"object\": \"Fruit Trees\"}}]',11,1),(33,'2019-06-11 03:28:15.365809','2','Carrusel Página Inicial',1,'[{\"added\": {}}]',15,1),(34,'2019-06-11 03:28:36.474041','2','Carrusel Página Inicial',2,'[{\"changed\": {\"fields\": [\"posicion\"]}}, {\"added\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"4\"}}]',15,1),(35,'2019-06-11 03:30:06.846675','2','Carrusel Página Inicial',2,'[{\"changed\": {\"fields\": [\"posicion\"]}}, {\"added\": {\"name\": \"Texto de Imagen de Secci\\u00f3n Carrusel\", \"object\": \"5\"}}, {\"added\": {\"name\": \"Texto de Imagen de Secci\\u00f3n Carrusel\", \"object\": \"6\"}}]',15,1),(36,'2019-06-11 03:30:37.835328','2','Carrusel Página Inicial',2,'[{\"changed\": {\"fields\": [\"posicion\"]}}, {\"added\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"5\"}}, {\"added\": {\"name\": \"Texto de Imagen de Secci\\u00f3n Carrusel\", \"object\": \"7\"}}, {\"added\": {\"name\": \"Texto de Imagen de Secci\\u00f3n Carrusel\", \"object\": \"8\"}}]',15,1),(37,'2019-06-12 00:36:11.439804','8','Quienes Somos',2,'[]',10,1),(38,'2019-06-12 00:36:18.007510','8','Quienes Somos',2,'[{\"changed\": {\"fields\": [\"posicion\"]}}]',10,1),(39,'2019-06-12 00:37:36.120037','6','Fotos Página Inicial - 1',2,'[{\"changed\": {\"fields\": [\"posicion\"]}}]',11,1),(40,'2019-06-12 01:06:13.658478','2','Carrusel Página Inicial',2,'[{\"changed\": {\"fields\": [\"fotos_fila\"]}}]',15,1),(41,'2019-06-12 01:07:56.289384','3','Caminatas y Tours',1,'[{\"added\": {}}, {\"added\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"6\"}}, {\"added\": {\"name\": \"Texto de Imagen de Secci\\u00f3n Carrusel\", \"object\": \"9\"}}, {\"added\": {\"name\": \"Texto de Imagen de Secci\\u00f3n Carrusel\", \"object\": \"10\"}}]',15,1),(42,'2019-06-12 01:08:51.486106','3','Caminatas y Tours',2,'[{\"added\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"7\"}}, {\"added\": {\"name\": \"Texto de Imagen de Secci\\u00f3n Carrusel\", \"object\": \"11\"}}, {\"added\": {\"name\": \"Texto de Imagen de Secci\\u00f3n Carrusel\", \"object\": \"12\"}}]',15,1),(43,'2019-06-12 03:53:11.959861','9','Servicios',1,'[{\"added\": {}}, {\"added\": {\"name\": \"Secci\\u00f3n Texto con Foto\", \"object\": \"3\"}}, {\"added\": {\"name\": \"Secci\\u00f3n Texto con Foto\", \"object\": \"4\"}}]',10,1),(44,'2019-06-13 00:09:17.954811','1','Parametro object (1)',1,'[{\"added\": {}}]',17,1),(45,'2019-06-13 00:18:12.213257','1','Parámetro 1',2,'[{\"added\": {\"name\": \"Texto de Par\\u00e1metro\", \"object\": \"<class \'app.models.Parametro.TextoParametro\'> 1\"}}, {\"added\": {\"name\": \"Texto de Par\\u00e1metro\", \"object\": \"<class \'app.models.Parametro.TextoParametro\'> 2\"}}]',17,1),(46,'2019-06-13 00:19:55.307559','1','Parámetro 1',2,'[{\"changed\": {\"name\": \"Texto de Par\\u00e1metro\", \"object\": \"<class \'app.models.Parametro.TextoParametro\'> 1\", \"fields\": [\"copyright\"]}}]',17,1),(47,'2019-06-13 01:02:22.143643','1','Parámetro 1',2,'[]',17,1),(48,'2019-06-13 01:03:36.359033','1','1',1,'[{\"added\": {}}]',18,1),(49,'2019-06-13 01:06:32.271322','1','1',2,'[{\"added\": {\"name\": \"Texto de Contacto\", \"object\": \"<class \'app.models.Contacto.TextoContacto\'> 1\"}}, {\"added\": {\"name\": \"Texto de Contacto\", \"object\": \"<class \'app.models.Contacto.TextoContacto\'> 2\"}}]',18,1),(50,'2019-06-13 02:05:54.455782','1','Facebook',1,'[{\"added\": {}}]',19,1),(51,'2019-06-13 02:06:11.546834','2','Instagram',1,'[{\"added\": {}}]',19,1),(52,'2019-06-13 02:29:05.514618','8','Quienes Somos',2,'[{\"changed\": {\"fields\": [\"estilo\"]}}]',10,1),(53,'2019-06-13 02:29:14.345932','9','Servicios',2,'[{\"changed\": {\"fields\": [\"estilo\"]}}]',10,1),(54,'2019-06-14 02:16:15.001062','1','Inicio',2,'[{\"changed\": {\"name\": \"Texto Opci\\u00f3n\", \"object\": \"Inicio\", \"fields\": [\"direccion\"]}}, {\"changed\": {\"name\": \"Texto Opci\\u00f3n\", \"object\": \"Home\", \"fields\": [\"direccion\"]}}]',9,1),(55,'2019-06-14 02:49:58.056040','2','Carrusel Página Inicial',2,'[{\"changed\": {\"name\": \"Texto de Imagen de Secci\\u00f3n Carrusel\", \"object\": \"<class \'app.models.SeccionCarrusel.TextoImagenSeccionCarrusel\'> 5\", \"fields\": [\"texto\"]}}, {\"changed\": {\"name\": \"Texto de Imagen de Secci\\u00f3n Carrusel\", \"object\": \"<class \'app.models.SeccionCarrusel.TextoImagenSeccionCarrusel\'> 6\", \"fields\": [\"texto\"]}}]',15,1),(56,'2019-06-14 03:02:56.296348','2','Carrusel Página Inicial',2,'[{\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"4\", \"fields\": [\"posx\", \"posy\", \"ancho\", \"color\"]}}, {\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"5\", \"fields\": [\"posx\", \"posy\", \"ancho\", \"color\"]}}]',15,1),(57,'2019-06-14 23:42:42.619471','2','Carrusel Página Inicial',2,'[{\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"4\", \"fields\": [\"imagen\"]}}, {\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"5\", \"fields\": [\"imagen\"]}}]',15,1),(58,'2019-06-14 23:44:22.120615','2','Carrusel Página Inicial',2,'[{\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"4\", \"fields\": [\"posx\", \"posy\", \"ancho\"]}}, {\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"5\", \"fields\": [\"posx\", \"posy\", \"ancho\"]}}, {\"changed\": {\"name\": \"Texto de Imagen de Secci\\u00f3n Carrusel\", \"object\": \"<class \'app.models.SeccionCarrusel.TextoImagenSeccionCarrusel\'> 5\", \"fields\": [\"texto\"]}}, {\"changed\": {\"name\": \"Texto de Imagen de Secci\\u00f3n Carrusel\", \"object\": \"<class \'app.models.SeccionCarrusel.TextoImagenSeccionCarrusel\'> 6\", \"fields\": [\"texto\"]}}, {\"changed\": {\"name\": \"Texto de Imagen de Secci\\u00f3n Carrusel\", \"object\": \"<class \'app.models.SeccionCarrusel.TextoImagenSeccionCarrusel\'> 7\", \"fields\": [\"texto\"]}}, {\"changed\": {\"name\": \"Texto de Imagen de Secci\\u00f3n Carrusel\", \"object\": \"<class \'app.models.SeccionCarrusel.TextoImagenSeccionCarrusel\'> 8\", \"fields\": [\"texto\"]}}]',15,1),(59,'2019-06-14 23:48:38.862800','2','Carrusel Página Inicial',2,'[{\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"4\", \"fields\": [\"posx\", \"posy\"]}}, {\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"5\", \"fields\": [\"posx\", \"posy\", \"ancho\"]}}]',15,1),(60,'2019-06-14 23:49:08.816334','2','Carrusel Página Inicial',2,'[{\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"4\", \"fields\": [\"posy\"]}}, {\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"5\", \"fields\": [\"posy\"]}}]',15,1),(61,'2019-06-14 23:49:52.269039','2','Carrusel Página Inicial',2,'[{\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"5\", \"fields\": [\"posx\", \"posy\"]}}]',15,1),(62,'2019-06-14 23:50:23.030506','2','Carrusel Página Inicial',2,'[{\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"4\", \"fields\": [\"posy\"]}}, {\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"5\", \"fields\": [\"posy\"]}}]',15,1),(63,'2019-06-14 23:50:43.484933','2','Carrusel Página Inicial',2,'[{\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"4\", \"fields\": [\"posy\"]}}]',15,1),(64,'2019-06-14 23:51:33.177113','2','Carrusel Página Inicial',2,'[{\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"4\", \"fields\": [\"posx\", \"posy\"]}}, {\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"5\", \"fields\": [\"posx\", \"posy\"]}}]',15,1),(65,'2019-06-14 23:53:35.650456','2','Carrusel Página Inicial',2,'[{\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"5\", \"fields\": [\"ancho\"]}}]',15,1),(66,'2019-06-14 23:53:40.272710','2','Carrusel Página Inicial',2,'[{\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"5\", \"fields\": [\"posy\"]}}]',15,1),(67,'2019-06-14 23:54:09.555145','2','Carrusel Página Inicial',2,'[{\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"5\", \"fields\": [\"posx\"]}}]',15,1),(68,'2019-06-14 23:54:39.822889','2','Carrusel Página Inicial',2,'[{\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"5\", \"fields\": [\"posx\"]}}]',15,1),(69,'2019-06-14 23:55:23.456862','2','Carrusel Página Inicial',2,'[{\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"5\", \"fields\": [\"ancho\"]}}]',15,1),(70,'2019-06-14 23:55:47.778634','2','Carrusel Página Inicial',2,'[{\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"5\", \"fields\": [\"ancho\"]}}]',15,1),(71,'2019-06-14 23:56:14.123099','2','Carrusel Página Inicial',2,'[{\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"5\", \"fields\": [\"posx\"]}}]',15,1),(72,'2019-06-14 23:56:43.897564','2','Carrusel Página Inicial',2,'[{\"changed\": {\"name\": \"Im\\u00e1gen Secci\\u00f3n Carrusel\", \"object\": \"5\", \"fields\": [\"posx\"]}}]',15,1),(73,'2019-06-15 00:09:07.869546','8','Quienes Somos',2,'[{\"changed\": {\"name\": \"Secci\\u00f3n Texto con Foto\", \"object\": \"<class \'app.models.TextoSeccionTextoFoto.TextoSeccionTextoFoto\'> 1\", \"fields\": [\"texto\"]}}, {\"changed\": {\"name\": \"Secci\\u00f3n Texto con Foto\", \"object\": \"<class \'app.models.TextoSeccionTextoFoto.TextoSeccionTextoFoto\'> 2\", \"fields\": [\"texto\"]}}]',10,1),(74,'2019-06-15 00:57:25.386428','6','Fotos Página Inicial - 1',2,'[{\"added\": {\"name\": \"Texto de Secci\\u00f3n Foto\", \"object\": \"<class \'app.models.SeccionFoto.TextoSeccionFoto\'> 1\"}}, {\"added\": {\"name\": \"Texto de Secci\\u00f3n Foto\", \"object\": \"<class \'app.models.SeccionFoto.TextoSeccionFoto\'> 2\"}}]',11,1),(75,'2019-06-15 17:04:05.972695','2','Carrusel Página Inicial',2,'[{\"changed\": {\"fields\": [\"tipo\"]}}, {\"added\": {\"name\": \"T\\u00edtulo\", \"object\": \"<class \'app.models.SeccionCarrusel.TextoSeccionCarrusel\'> 1\"}}, {\"added\": {\"name\": \"T\\u00edtulo\", \"object\": \"<class \'app.models.SeccionCarrusel.TextoSeccionCarrusel\'> 2\"}}]',15,1),(76,'2019-06-15 17:06:26.941496','3','Caminatas y Tours',2,'[{\"changed\": {\"fields\": [\"tipo\"]}}, {\"added\": {\"name\": \"T\\u00edtulo\", \"object\": \"<class \'app.models.SeccionCarrusel.TextoSeccionCarrusel\'> 3\"}}, {\"added\": {\"name\": \"T\\u00edtulo\", \"object\": \"<class \'app.models.SeccionCarrusel.TextoSeccionCarrusel\'> 4\"}}, {\"changed\": {\"name\": \"Im\\u00e1gen\", \"object\": \"6\", \"fields\": [\"ancho\", \"color\"]}}, {\"changed\": {\"name\": \"Im\\u00e1gen\", \"object\": \"7\", \"fields\": [\"ancho\", \"color\"]}}]',15,1),(77,'2019-06-15 17:19:32.737207','2','Carrusel Página Inicial',2,'[{\"changed\": {\"fields\": [\"tipo\"]}}, {\"changed\": {\"name\": \"Im\\u00e1gen\", \"object\": \"4\", \"fields\": [\"posx\"]}}]',15,1),(78,'2019-06-15 17:20:38.685802','2','Carrusel Página Inicial',2,'[{\"changed\": {\"fields\": [\"tipo\"]}}, {\"changed\": {\"name\": \"Im\\u00e1gen\", \"object\": \"4\", \"fields\": [\"posx\"]}}]',15,1),(79,'2019-06-15 18:21:55.057585','8','Quienes Somos',2,'[{\"changed\": {\"fields\": [\"color\"]}}]',10,1),(80,'2019-06-15 18:22:16.389554','8','Quienes Somos',2,'[{\"changed\": {\"fields\": [\"color\"]}}]',10,1),(81,'2019-06-15 18:22:25.216767','9','Servicios',2,'[{\"changed\": {\"fields\": [\"color\"]}}]',10,1),(82,'2019-06-15 19:52:03.251659','1','Parámetro 1',2,'[{\"changed\": {\"name\": \"Valores\", \"object\": \"<class \'app.models.Parametro.TextoParametro\'> 1\", \"fields\": [\"titulosocial\"]}}, {\"changed\": {\"name\": \"Valores\", \"object\": \"<class \'app.models.Parametro.TextoParametro\'> 2\", \"fields\": [\"titulosocial\"]}}]',17,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(18,'app','contacto'),(13,'app','filaseccionfoto'),(14,'app','fotofilaseccionfoto'),(7,'app','idioma'),(8,'app','imageninicio'),(16,'app','imagenseccioncarrusel'),(9,'app','opcion'),(17,'app','parametro'),(15,'app','seccioncarrusel'),(11,'app','seccionfoto'),(12,'app','seccionfotofoto'),(10,'app','secciontextofoto'),(19,'app','social'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-06-02 01:40:25.204414'),(2,'auth','0001_initial','2019-06-02 01:40:25.470292'),(3,'admin','0001_initial','2019-06-02 01:40:26.624034'),(4,'admin','0002_logentry_remove_auto_add','2019-06-02 01:40:26.868618'),(5,'admin','0003_logentry_add_action_flag_choices','2019-06-02 01:40:26.878012'),(6,'contenttypes','0002_remove_content_type_name','2019-06-02 01:40:27.040146'),(7,'auth','0002_alter_permission_name_max_length','2019-06-02 01:40:27.166127'),(8,'auth','0003_alter_user_email_max_length','2019-06-02 01:40:27.179070'),(9,'auth','0004_alter_user_username_opts','2019-06-02 01:40:27.190544'),(10,'auth','0005_alter_user_last_login_null','2019-06-02 01:40:27.260908'),(11,'auth','0006_require_contenttypes_0002','2019-06-02 01:40:27.271800'),(12,'auth','0007_alter_validators_add_error_messages','2019-06-02 01:40:27.281628'),(13,'auth','0008_alter_user_username_max_length','2019-06-02 01:40:27.391874'),(14,'auth','0009_alter_user_last_name_max_length','2019-06-02 01:40:27.531599'),(15,'auth','0010_alter_group_name_max_length','2019-06-02 01:40:27.580038'),(16,'auth','0011_update_proxy_permissions','2019-06-02 01:40:27.599207'),(17,'sessions','0001_initial','2019-06-02 01:40:27.638428');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0flahheh0imdyvwh8n47begvcaf5dqt5','NjMyYzk5YWYxNTkxZTQ2M2I0ZmJhMjAyNjYzZWI1MmE3MTgzMjU2Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYTEzMjI0MTYxNWNjOGUwNDE5YTNiMWVlNGNjNzQxNzNmMDA3YzdiIn0=','2019-06-29 17:00:44.372589'),('0yr6bak367ucvurne5zdei4ljh819bu9','YzZhYTNiY2MwNzA1NDc4MjIwYTM2NTliMDAwZGU0OTcxOGNiZjU2Mzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYTEzMjI0MTYxNWNjOGUwNDE5YTNiMWVlNGNjNzQxNzNmMDA3YzdiIiwiX2xhbmd1YWdlIjoiZW4ifQ==','2019-06-28 03:10:05.162226'),('2wirwmkuszs0gvo8usflw353pkqsnckk','ZWNmNTM0NWRiOGYxNzdmZDk5YzIzNTI1OWMzMTcwNTU1Yjk5ZTUyYjp7Il9sYW5ndWFnZSI6ImVzIn0=','2019-06-28 02:07:00.733924'),('3u35w6f91bnng8tzno9uh7psti8d1e4h','NjMyYzk5YWYxNTkxZTQ2M2I0ZmJhMjAyNjYzZWI1MmE3MTgzMjU2Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYTEzMjI0MTYxNWNjOGUwNDE5YTNiMWVlNGNjNzQxNzNmMDA3YzdiIn0=','2019-06-18 18:12:01.849159'),('4kg4qq2vxok9v1n4ohutyts2pf60oih8','YzZhYTNiY2MwNzA1NDc4MjIwYTM2NTliMDAwZGU0OTcxOGNiZjU2Mzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYTEzMjI0MTYxNWNjOGUwNDE5YTNiMWVlNGNjNzQxNzNmMDA3YzdiIiwiX2xhbmd1YWdlIjoiZW4ifQ==','2019-06-23 15:55:03.366329'),('8709rwy67jh3hx7g2rvi76s8ahujqdiy','NjMyYzk5YWYxNTkxZTQ2M2I0ZmJhMjAyNjYzZWI1MmE3MTgzMjU2Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYTEzMjI0MTYxNWNjOGUwNDE5YTNiMWVlNGNjNzQxNzNmMDA3YzdiIn0=','2019-06-22 18:32:34.020672'),('bdsgm297brwhwwe794txgr2e3xc175eb','YzZhYTNiY2MwNzA1NDc4MjIwYTM2NTliMDAwZGU0OTcxOGNiZjU2Mzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYTEzMjI0MTYxNWNjOGUwNDE5YTNiMWVlNGNjNzQxNzNmMDA3YzdiIiwiX2xhbmd1YWdlIjoiZW4ifQ==','2019-06-29 19:41:20.066367'),('bfj72lzqo02zgxjrbj3kflst8b1l3icp','NjMyYzk5YWYxNTkxZTQ2M2I0ZmJhMjAyNjYzZWI1MmE3MTgzMjU2Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYTEzMjI0MTYxNWNjOGUwNDE5YTNiMWVlNGNjNzQxNzNmMDA3YzdiIn0=','2019-06-19 02:53:02.151332'),('fgk88sbe9qkndx1yhb1kpe3xk8hhi7cq','NjMyYzk5YWYxNTkxZTQ2M2I0ZmJhMjAyNjYzZWI1MmE3MTgzMjU2Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYTEzMjI0MTYxNWNjOGUwNDE5YTNiMWVlNGNjNzQxNzNmMDA3YzdiIn0=','2019-06-18 03:05:53.047655'),('ga3f4ry9nybntszu719ifts2egsrcccj','NjMyYzk5YWYxNTkxZTQ2M2I0ZmJhMjAyNjYzZWI1MmE3MTgzMjU2Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYTEzMjI0MTYxNWNjOGUwNDE5YTNiMWVlNGNjNzQxNzNmMDA3YzdiIn0=','2019-06-25 01:59:17.416579'),('jx4a5zihbcjasywzrzpgy4xn0ob3v89q','NGJhYTEwZTNjNTc2NTc1NjQwNTBjMzViNDYwZGJkODNkOTBhZDcyNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYTEzMjI0MTYxNWNjOGUwNDE5YTNiMWVlNGNjNzQxNzNmMDA3YzdiIiwiX2xhbmd1YWdlIjoiZXMifQ==','2019-06-26 03:55:57.888973'),('le68difepykgumjsipugkd0dt88gq5k2','NGJhYTEwZTNjNTc2NTc1NjQwNTBjMzViNDYwZGJkODNkOTBhZDcyNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYTEzMjI0MTYxNWNjOGUwNDE5YTNiMWVlNGNjNzQxNzNmMDA3YzdiIiwiX2xhbmd1YWdlIjoiZXMifQ==','2019-06-28 23:57:41.045364'),('s6bywo81pes5iuihk8s9ch84i3e5vvwt','NGJhYTEwZTNjNTc2NTc1NjQwNTBjMzViNDYwZGJkODNkOTBhZDcyNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYTEzMjI0MTYxNWNjOGUwNDE5YTNiMWVlNGNjNzQxNzNmMDA3YzdiIiwiX2xhbmd1YWdlIjoiZXMifQ==','2019-06-20 03:50:00.699542'),('tnin79ynnhr99z048a18q1x38scu9pos','NjMyYzk5YWYxNTkxZTQ2M2I0ZmJhMjAyNjYzZWI1MmE3MTgzMjU2Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjYTEzMjI0MTYxNWNjOGUwNDE5YTNiMWVlNGNjNzQxNzNmMDA3YzdiIn0=','2019-06-17 01:29:17.646386'),('vai46cdhvxvdzdkatcv25ae4je8813tj','YTA0MmM5ZDY4NWFhODgyMDRiYTZkZGIzZjZiYTI5NDJiZTNiNWRlNDp7Il9sYW5ndWFnZSI6ImZ5In0=','2019-06-20 01:58:26.438447');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fila_seccion_foto`
--

DROP TABLE IF EXISTS `fila_seccion_foto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fila_seccion_foto` (
  `idfila` int(11) NOT NULL AUTO_INCREMENT,
  `idseccion` int(11) NOT NULL,
  `posicion` int(11) DEFAULT NULL,
  PRIMARY KEY (`idfila`),
  KEY `fk_fila_seccion_foto_seccion_foto1_idx` (`idseccion`),
  CONSTRAINT `fk_fila_seccion_foto_seccion_foto1` FOREIGN KEY (`idseccion`) REFERENCES `seccion_foto` (`idseccion`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fila_seccion_foto`
--

LOCK TABLES `fila_seccion_foto` WRITE;
/*!40000 ALTER TABLE `fila_seccion_foto` DISABLE KEYS */;
INSERT INTO `fila_seccion_foto` VALUES (2,6,1),(3,6,2),(4,6,2);
/*!40000 ALTER TABLE `fila_seccion_foto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `foto_fila`
--

DROP TABLE IF EXISTS `foto_fila`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `foto_fila` (
  `idfoto` int(11) NOT NULL AUTO_INCREMENT,
  `imagen` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `posicion` int(11) DEFAULT NULL,
  `idfila` int(11) NOT NULL,
  PRIMARY KEY (`idfoto`),
  KEY `fk_foto_fila_fila_seccion_foto1_idx1` (`idfila`),
  CONSTRAINT `fk_foto_fila_fila_seccion_foto1` FOREIGN KEY (`idfila`) REFERENCES `fila_seccion_foto` (`idfila`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `foto_fila`
--

LOCK TABLES `foto_fila` WRITE;
/*!40000 ALTER TABLE `foto_fila` DISABLE KEYS */;
INSERT INTO `foto_fila` VALUES (2,'matrimonial_fQEA1uY.jpg',1,2),(3,'doble-1_p83XM8r.jpg',2,2),(4,'doble-2_VGK2vzn.jpg',3,2),(5,'triple_O54JScE.jpg',4,2),(6,'1-vereda-interior.jpg',1,3),(7,'2-jardines.jpg',2,3),(8,'3-comedor.jpg',3,3),(9,'4-ave.jpg',4,3),(10,'5-balcones.jpg',1,4),(11,'7-frutales.jpg',1,4);
/*!40000 ALTER TABLE `foto_fila` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `idioma`
--

DROP TABLE IF EXISTS `idioma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `idioma` (
  `ididioma` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(5) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `nombre` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `imagen` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `directorio` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `posicion` int(11) DEFAULT NULL,
  PRIMARY KEY (`ididioma`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `idioma`
--

LOCK TABLES `idioma` WRITE;
/*!40000 ALTER TABLE `idioma` DISABLE KEYS */;
INSERT INTO `idioma` VALUES (1,'es','Español','','/Users/miguel/Python/lunarumi/static/imagenes/',NULL),(2,'en','English','','/Users/miguel/Python/lunarumi/static/imagenes/',NULL);
/*!40000 ALTER TABLE `idioma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `imagen_seccion_carrusel`
--

DROP TABLE IF EXISTS `imagen_seccion_carrusel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `imagen_seccion_carrusel` (
  `idimagen` int(11) NOT NULL AUTO_INCREMENT,
  `idseccion` int(11) NOT NULL,
  `posicion` int(11) NOT NULL,
  `imagen` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `posx` int(11) DEFAULT NULL,
  `posy` int(11) DEFAULT NULL,
  `ancho` int(11) DEFAULT NULL,
  `color` varchar(6) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`idimagen`),
  KEY `fk_carrusel_idseccion_seccion_idx` (`idseccion`),
  CONSTRAINT `fk_carrusel_idseccion_seccion` FOREIGN KEY (`idseccion`) REFERENCES `seccion_carrusel` (`idseccion`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `imagen_seccion_carrusel`
--

LOCK TABLES `imagen_seccion_carrusel` WRITE;
/*!40000 ALTER TABLE `imagen_seccion_carrusel` DISABLE KEYS */;
INSERT INTO `imagen_seccion_carrusel` VALUES (4,2,1,'CARRUSEL-1.jpg',12,8,20,'ffffff'),(5,2,2,'CARRUSEL-2.jpg',7,6,25,'858279'),(6,3,0,'machupicchu.jpg',0,0,0,'000000'),(7,3,0,'maras-moray.jpg',0,0,0,'000000');
/*!40000 ALTER TABLE `imagen_seccion_carrusel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `opcion`
--

DROP TABLE IF EXISTS `opcion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `opcion` (
  `idopcion` int(11) NOT NULL AUTO_INCREMENT,
  `posicion` int(11) DEFAULT NULL,
  `nombre` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`idopcion`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opcion`
--

LOCK TABLES `opcion` WRITE;
/*!40000 ALTER TABLE `opcion` DISABLE KEYS */;
INSERT INTO `opcion` VALUES (1,1,'Inicio'),(2,2,'Quienes Somos'),(3,3,'Instalaciones'),(4,4,'Tours'),(5,5,'Servicios'),(6,6,'Contacto');
/*!40000 ALTER TABLE `opcion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parametro`
--

DROP TABLE IF EXISTS `parametro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parametro` (
  `idparametro` int(11) NOT NULL AUTO_INCREMENT,
  `logoblanco` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `logomarron` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `copyright` varchar(128) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`idparametro`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parametro`
--

LOCK TABLES `parametro` WRITE;
/*!40000 ALTER TABLE `parametro` DISABLE KEYS */;
INSERT INTO `parametro` VALUES (1,'logo-fondo-blanco.jpg','logo-fondo-beige.jpg',NULL);
/*!40000 ALTER TABLE `parametro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seccion_carrusel`
--

DROP TABLE IF EXISTS `seccion_carrusel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `seccion_carrusel` (
  `idseccion` int(11) NOT NULL AUTO_INCREMENT,
  `idopcion` int(11) NOT NULL,
  `nombre` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `posicion` int(11) DEFAULT NULL,
  `fotosfila` int(11) DEFAULT NULL,
  `tipo` int(11) DEFAULT NULL,
  PRIMARY KEY (`idseccion`),
  KEY `fk_seccion_carrusel_opcion1_idx` (`idopcion`),
  CONSTRAINT `fk_seccion_carrusel_opcion1` FOREIGN KEY (`idopcion`) REFERENCES `opcion` (`idopcion`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seccion_carrusel`
--

LOCK TABLES `seccion_carrusel` WRITE;
/*!40000 ALTER TABLE `seccion_carrusel` DISABLE KEYS */;
INSERT INTO `seccion_carrusel` VALUES (2,1,'Carrusel Página Inicial',1,1,1),(3,1,'Caminatas y Tours',4,2,2);
/*!40000 ALTER TABLE `seccion_carrusel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seccion_foto`
--

DROP TABLE IF EXISTS `seccion_foto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `seccion_foto` (
  `idseccion` int(11) NOT NULL AUTO_INCREMENT,
  `idopcion` int(11) NOT NULL,
  `nombre` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `posicion` int(11) DEFAULT NULL,
  PRIMARY KEY (`idseccion`),
  KEY `fk_seccion_foto_opcion1_idx` (`idopcion`),
  CONSTRAINT `fk_seccion_foto_opcion1` FOREIGN KEY (`idopcion`) REFERENCES `opcion` (`idopcion`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seccion_foto`
--

LOCK TABLES `seccion_foto` WRITE;
/*!40000 ALTER TABLE `seccion_foto` DISABLE KEYS */;
INSERT INTO `seccion_foto` VALUES (6,1,'Fotos Página Inicial - 1',3);
/*!40000 ALTER TABLE `seccion_foto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seccion_foto_foto`
--

DROP TABLE IF EXISTS `seccion_foto_foto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `seccion_foto_foto` (
  `idfoto` int(11) NOT NULL AUTO_INCREMENT,
  `imagen` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `posicion` int(11) DEFAULT NULL,
  `fila_seccion_foto_idfila` int(11) NOT NULL,
  PRIMARY KEY (`idfoto`),
  KEY `fk_foto_fila_fila_seccion_foto1_idx` (`fila_seccion_foto_idfila`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seccion_foto_foto`
--

LOCK TABLES `seccion_foto_foto` WRITE;
/*!40000 ALTER TABLE `seccion_foto_foto` DISABLE KEYS */;
INSERT INTO `seccion_foto_foto` VALUES (1,'matrimonial_jMteVDV.jpg',NULL,0),(2,'doble-1.jpg',NULL,0),(3,'doble-2.jpg',NULL,0),(4,'triple.jpg',NULL,0);
/*!40000 ALTER TABLE `seccion_foto_foto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seccion_texto_foto`
--

DROP TABLE IF EXISTS `seccion_texto_foto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `seccion_texto_foto` (
  `idseccion` int(11) NOT NULL AUTO_INCREMENT,
  `idopcion` int(11) NOT NULL,
  `nombre` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `posicion` int(11) NOT NULL,
  `imagen` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tipo` int(11) NOT NULL,
  `color` varchar(6) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`idseccion`),
  KEY `fk_seccion_texto_foto_opcion1_idx` (`idopcion`),
  CONSTRAINT `fk_seccion_texto_foto_opcion1` FOREIGN KEY (`idopcion`) REFERENCES `opcion` (`idopcion`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seccion_texto_foto`
--

LOCK TABLES `seccion_texto_foto` WRITE;
/*!40000 ALTER TABLE `seccion_texto_foto` DISABLE KEYS */;
INSERT INTO `seccion_texto_foto` VALUES (8,1,'Quienes Somos',2,'vista-jardin-interior_xIJAznF.jpg',1,'FFF'),(9,1,'Servicios',5,'servicios-inicio.jpg',2,'FAECDF');
/*!40000 ALTER TABLE `seccion_texto_foto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social`
--

DROP TABLE IF EXISTS `social`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social` (
  `idsocial` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `imagen` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `direccion` varchar(512) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `posicion` int(11) DEFAULT NULL,
  PRIMARY KEY (`idsocial`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social`
--

LOCK TABLES `social` WRITE;
/*!40000 ALTER TABLE `social` DISABLE KEYS */;
INSERT INTO `social` VALUES (1,'Facebook','icono-facebook_2TFMP3G.jpg','https://facebook.com',1),(2,'Instagram','icono-instagram_5A4T7jv.jpg','https://instagram.com',2);
/*!40000 ALTER TABLE `social` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `texto_contacto`
--

DROP TABLE IF EXISTS `texto_contacto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `texto_contacto` (
  `idtexto` int(11) NOT NULL AUTO_INCREMENT,
  `ididioma` int(11) NOT NULL,
  `idcontacto` int(11) NOT NULL,
  `titulo` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`idtexto`),
  KEY `fk_texto_contacto_idioma1_idx` (`ididioma`),
  KEY `fk_texto_contacto_contacto1_idx` (`idcontacto`),
  CONSTRAINT `fk_texto_contacto_contacto1` FOREIGN KEY (`idcontacto`) REFERENCES `contacto` (`idcontacto`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_texto_contacto_idioma1` FOREIGN KEY (`ididioma`) REFERENCES `idioma` (`ididioma`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `texto_contacto`
--

LOCK TABLES `texto_contacto` WRITE;
/*!40000 ALTER TABLE `texto_contacto` DISABLE KEYS */;
INSERT INTO `texto_contacto` VALUES (1,1,1,'Contacto'),(2,2,1,'Contacto');
/*!40000 ALTER TABLE `texto_contacto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `texto_foto_fila`
--

DROP TABLE IF EXISTS `texto_foto_fila`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `texto_foto_fila` (
  `idtexto` int(11) NOT NULL AUTO_INCREMENT,
  `ididioma` int(11) NOT NULL,
  `idfoto` int(11) NOT NULL,
  `texto` varchar(64) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`idtexto`),
  KEY `fk_seccion_foto_foto_texto_idioma1_idx` (`ididioma`),
  KEY `fk_idioma_foto_fila_foto_fila1_idx` (`idfoto`),
  CONSTRAINT `fk_idioma_foto_fila_foto_fila1` FOREIGN KEY (`idfoto`) REFERENCES `foto_fila` (`idfoto`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_seccion_foto_foto_texto_idioma1` FOREIGN KEY (`ididioma`) REFERENCES `idioma` (`ididioma`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `texto_foto_fila`
--

LOCK TABLES `texto_foto_fila` WRITE;
/*!40000 ALTER TABLE `texto_foto_fila` DISABLE KEYS */;
INSERT INTO `texto_foto_fila` VALUES (9,1,2,'Habitación Matrimonial'),(10,2,2,'Double Room'),(11,1,3,'Habitación Doble'),(12,2,3,'Twin Room'),(13,1,4,'Habitación Doble'),(14,2,4,'Twin Room'),(15,1,5,'Habitación Triple'),(16,2,5,'Triple Room'),(17,1,6,'Vereda Interior'),(18,2,6,'Inner Sidewalk'),(19,1,7,'Jardines'),(20,2,7,'Gardens'),(21,1,8,'Comedor'),(22,2,8,'Dining Room'),(23,1,9,'Ave'),(24,2,9,'Bird'),(25,1,10,'Balcones'),(26,2,10,'Balconies'),(27,1,11,'Arboles Frutales'),(28,2,11,'Fruit Trees');
/*!40000 ALTER TABLE `texto_foto_fila` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `texto_imagen`
--

DROP TABLE IF EXISTS `texto_imagen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `texto_imagen` (
  `idtexto` int(11) NOT NULL AUTO_INCREMENT,
  `ididioma` int(11) NOT NULL,
  `idimagen` int(11) NOT NULL,
  `texto` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`idtexto`),
  KEY `fk_imagen_inicio_string_imagen_inicio1_idx` (`idimagen`),
  KEY `fk_imagen_inicio_string_idioma1_idx` (`ididioma`),
  CONSTRAINT `fk_imagen_inicio_string_idioma1` FOREIGN KEY (`ididioma`) REFERENCES `idioma` (`ididioma`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_imagen_inicio_string_imagen_inicio1` FOREIGN KEY (`idimagen`) REFERENCES `imagen_seccion_carrusel` (`idimagen`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `texto_imagen`
--

LOCK TABLES `texto_imagen` WRITE;
/*!40000 ALTER TABLE `texto_imagen` DISABLE KEYS */;
INSERT INTO `texto_imagen` VALUES (5,1,4,'vive una experiencia andina'),(6,2,4,'experience the andes'),(7,1,5,'relájate en el valle sagrado'),(8,2,5,'relax in the sacred valley'),(9,1,6,'Machu Picchu'),(10,2,6,'Machu Picchu'),(11,1,7,'Maras Moray'),(12,2,7,'Maras Moray');
/*!40000 ALTER TABLE `texto_imagen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `texto_opcion`
--

DROP TABLE IF EXISTS `texto_opcion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `texto_opcion` (
  `idtexto` int(11) NOT NULL AUTO_INCREMENT,
  `idopcion` int(11) NOT NULL,
  `ididioma` int(11) NOT NULL,
  `titulo` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `direccion` varchar(512) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`idtexto`),
  KEY `fk_opcion_texto_opcion1_idx` (`idopcion`),
  KEY `fk_opcion_texto_idioma1_idx` (`ididioma`),
  CONSTRAINT `fk_opcion_texto_idioma1` FOREIGN KEY (`ididioma`) REFERENCES `idioma` (`ididioma`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_opcion_texto_opcion1` FOREIGN KEY (`idopcion`) REFERENCES `opcion` (`idopcion`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `texto_opcion`
--

LOCK TABLES `texto_opcion` WRITE;
/*!40000 ALTER TABLE `texto_opcion` DISABLE KEYS */;
INSERT INTO `texto_opcion` VALUES (1,1,1,'Inicio',''),(2,1,2,'Home',''),(3,2,1,'Quienes Somos','quienes-somos'),(4,2,2,'Who We Are','who-we-are'),(5,3,1,'Instalaciones','instalaciones'),(6,3,2,'Facilities','facilities'),(7,4,1,'Tours','tours'),(8,4,2,'Tours','tours'),(9,5,1,'Servicios','servicios'),(10,5,2,'Services','services'),(11,6,1,'Contacto','contacto'),(12,6,2,'Contact','contact');
/*!40000 ALTER TABLE `texto_opcion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `texto_parametro`
--

DROP TABLE IF EXISTS `texto_parametro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `texto_parametro` (
  `idtexto` int(11) NOT NULL AUTO_INCREMENT,
  `idparametro` int(11) NOT NULL,
  `ididioma` int(11) NOT NULL,
  `copyright` varchar(128) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `titulosocial` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`idtexto`),
  KEY `fk_texto_parametro_parametro1_idx` (`idparametro`),
  KEY `fk_texto_parametro_idioma1_idx` (`ididioma`),
  CONSTRAINT `fk_texto_parametro_idioma1` FOREIGN KEY (`ididioma`) REFERENCES `idioma` (`ididioma`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_texto_parametro_parametro1` FOREIGN KEY (`idparametro`) REFERENCES `parametro` (`idparametro`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `texto_parametro`
--

LOCK TABLES `texto_parametro` WRITE;
/*!40000 ALTER TABLE `texto_parametro` DISABLE KEYS */;
INSERT INTO `texto_parametro` VALUES (1,1,1,'© 2019 Luma Rumi. Todos los derechos reservados.','Síganos'),(2,1,2,'© 2019 Luma Rumi. All rights reserved.','Follow us');
/*!40000 ALTER TABLE `texto_parametro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `texto_seccion_carrusel`
--

DROP TABLE IF EXISTS `texto_seccion_carrusel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `texto_seccion_carrusel` (
  `idtexto` int(11) NOT NULL AUTO_INCREMENT,
  `idseccion` int(11) NOT NULL,
  `ididioma` int(11) NOT NULL,
  `titulo` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`idtexto`),
  KEY `fk_texto_seccion_carrusel_seccion_carrusel1_idx` (`idseccion`),
  KEY `fk_texto_seccion_carrusel_idioma1_idx` (`ididioma`),
  CONSTRAINT `fk_texto_seccion_carrusel_idioma1` FOREIGN KEY (`ididioma`) REFERENCES `idioma` (`ididioma`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_texto_seccion_carrusel_seccion_carrusel1` FOREIGN KEY (`idseccion`) REFERENCES `seccion_carrusel` (`idseccion`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `texto_seccion_carrusel`
--

LOCK TABLES `texto_seccion_carrusel` WRITE;
/*!40000 ALTER TABLE `texto_seccion_carrusel` DISABLE KEYS */;
INSERT INTO `texto_seccion_carrusel` VALUES (1,2,1,'Sin título'),(2,2,2,'No title'),(3,3,1,'Caminatas y tours'),(4,3,2,'Tours and walks');
/*!40000 ALTER TABLE `texto_seccion_carrusel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `texto_seccion_foto`
--

DROP TABLE IF EXISTS `texto_seccion_foto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `texto_seccion_foto` (
  `idtexto` int(11) NOT NULL AUTO_INCREMENT,
  `idseccion` int(11) NOT NULL,
  `ididioma` int(11) NOT NULL,
  `titulo` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`idtexto`),
  KEY `fk_texto_seccion_foot_seccion_foto1_idx` (`idseccion`),
  KEY `fk_texto_seccion_foto_idioma1_idx` (`ididioma`),
  CONSTRAINT `fk_texto_seccion_foot_seccion_foto1` FOREIGN KEY (`idseccion`) REFERENCES `seccion_foto` (`idseccion`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_texto_seccion_foto_idioma1` FOREIGN KEY (`ididioma`) REFERENCES `idioma` (`ididioma`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `texto_seccion_foto`
--

LOCK TABLES `texto_seccion_foto` WRITE;
/*!40000 ALTER TABLE `texto_seccion_foto` DISABLE KEYS */;
INSERT INTO `texto_seccion_foto` VALUES (1,6,1,'Cuartos y Ambientes'),(2,6,2,'Rooms and Facilities');
/*!40000 ALTER TABLE `texto_seccion_foto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `texto_seccion_texto_foto`
--

DROP TABLE IF EXISTS `texto_seccion_texto_foto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `texto_seccion_texto_foto` (
  `idtexto` int(11) NOT NULL AUTO_INCREMENT,
  `idseccion` int(11) NOT NULL,
  `ididioma` int(11) NOT NULL,
  `texto` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`idtexto`),
  KEY `fk_seccion_texto_foto_texto_seccion_texto_foto1_idx` (`idseccion`),
  KEY `fk_seccion_texto_foto_texto_idioma1_idx` (`ididioma`),
  CONSTRAINT `fk_seccion_texto_foto_texto_idioma1` FOREIGN KEY (`ididioma`) REFERENCES `idioma` (`ididioma`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_seccion_texto_foto_texto_seccion_texto_foto1` FOREIGN KEY (`idseccion`) REFERENCES `seccion_texto_foto` (`idseccion`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `texto_seccion_texto_foto`
--

LOCK TABLES `texto_seccion_texto_foto` WRITE;
/*!40000 ALTER TABLE `texto_seccion_texto_foto` DISABLE KEYS */;
INSERT INTO `texto_seccion_texto_foto` VALUES (1,8,1,'## Quienes Somos\r\n\r\nA los pies nevado Chicón, en el Valle Sagrado del Urubamba encontrarás nuestro hotel.\r\n\r\nSentirás la belleza y la calma del lugar y el olor al campo donde podrás relajarte practicando las actividades que más te gustan.\r\n\r\nEmpieza tu día respirando aire puro, en medio de la naturaleza. Intégrate con los árboles y flores, las  montañas bajo el cielo azul, el sol y al anochecer, la luna.'),(2,8,2,'## About us\r\n\r\nYou will find our hotel at the foot of the snowy Chicón mountain, in the Sacred Valley of the Urubamba.\r\n\r\nFeel the beauty, calm and fresh smell of the countryside where you can relax practicing your preferred activities.\r\n\r\nStart your day breathing pure air in the midst of nature. Integrate with the trees and flowers,  mountains under  blue sky, the sun and in the evening, the moon.'),(3,9,1,'# Servicios\r\n\r\nLuna Rumi te espera para que en la tranquilidad del Valle puedas, solo o acompañado, practicar Yoga, Tai Chi, Chi kung, stretching o realizar talleres de meditación, mindfullnes, retiros espirituales entre otras actividades.'),(4,9,2,'# Services\r\n\r\nLuna Rumi awaits so that you can, in the Valley quiet , alone or accompanied, practice Yoga, Tai Chi, Chi Kung, stretching or meditation workshops, mindfullnes exercises, spiritual retreats or our other activities.');
/*!40000 ALTER TABLE `texto_seccion_texto_foto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-15 14:58:25
