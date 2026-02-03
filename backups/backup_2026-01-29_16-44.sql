-- MySQL dump 10.13  Distrib 8.0.44, for Linux (x86_64)
--
-- Host: localhost    Database: ratmer
-- ------------------------------------------------------
-- Server version	8.0.44

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `num_T` varchar(100) NOT NULL,
  `data_prth` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `Salary` int NOT NULL,
  `Job` varchar(100) NOT NULL,
  `nots` varchar(500) NOT NULL,
  `image_path` varchar(100) NOT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'emaad','+79038745893','07/04/1995','montagnkov 1',4500,'охрана','Наблюдение в аудиториях и общежитиях обязательно.','uploads/emaad-DT2026-01-07-T-15-45.jpg',1),(2,'johnny depp','0034215567','07/04/1995','Краснодар, ул. Зиповская, д. 5',4000,'охрана','good','uploads/johnny depp-DT2026-01-09-T-17-29.png',1),(3,'andre','+79038745893','07/04/1996','krasondar,moscovskaea122',5500,'Network Technician','good','uploads/andre-DT2026-01-12-T-09-12.jpg',1),(4,'Иван Сергеевич Петров','+7 918 345-67-89','15.04.1995','Россия, г. Краснодар, ул. Красная, д. 120, кв. 45',4000,'Системный администратор','Опыт работы 4 года, ответственный, умеет работать в команде.','uploads/Иван Сергеевич Петров-DT2026-01-25-T-08-26.jpg',1);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `list_points_checkd`
--

DROP TABLE IF EXISTS `list_points_checkd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `list_points_checkd` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_check_point` int NOT NULL,
  `dataD` date NOT NULL DEFAULT (curdate()),
  `timeD` time NOT NULL DEFAULT (curtime()),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `list_points_checkd`
--

LOCK TABLES `list_points_checkd` WRITE;
/*!40000 ALTER TABLE `list_points_checkd` DISABLE KEYS */;
INSERT INTO `list_points_checkd` VALUES (1,5,'2026-01-09','12:42:28'),(2,5,'2026-01-09','12:42:48'),(3,5,'2026-01-09','13:42:18'),(4,5,'2026-01-12','07:56:07'),(5,6,'2026-01-17','07:45:16'),(6,3,'2026-01-17','08:18:34'),(7,2,'2026-01-17','08:18:51'),(8,1,'2026-01-17','08:19:14'),(9,1,'2026-01-17','08:19:14'),(10,5,'2026-01-17','08:19:36'),(11,6,'2026-01-22','14:12:50'),(12,6,'2026-01-25','08:35:23');
/*!40000 ALTER TABLE `list_points_checkd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `points_chick`
--

DROP TABLE IF EXISTS `points_chick`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `points_chick` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_project` int NOT NULL,
  `name_point` varchar(100) NOT NULL,
  `Coordinates` varchar(100) NOT NULL,
  `id_entry_emp` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `points_chick`
--

LOCK TABLES `points_chick` WRITE;
/*!40000 ALTER TABLE `points_chick` DISABLE KEYS */;
INSERT INTO `points_chick` VALUES (1,1,'приход н4','45.059217, 38.962773','admin aaa'),(2,2,'приход н4','45.059217, 38.962773','admin aaa'),(3,2,'главни приход','45.059217, 38.962773','admin aaa'),(4,2,'3 floor sectoin miting','45.059217, 38.962773','admin aaa'),(5,2,'entry1','45.059217, 38.962773','admin aaa'),(6,2,'from contener','45.059217, 38.962773','admin aaa'),(7,4,'приход н4re44','45.050438, 38.958060','admin aaa');
/*!40000 ALTER TABLE `points_chick` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_guards`
--

DROP TABLE IF EXISTS `project_guards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_guards` (
  `id` int NOT NULL AUTO_INCREMENT,
  `project_id` int DEFAULT NULL,
  `project_name` varchar(100) NOT NULL,
  `employee_id` int DEFAULT NULL,
  `employee_name` varchar(100) NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date NOT NULL,
  `emp` varchar(100) NOT NULL,
  `nots` varchar(500) NOT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `fk_pg_emp` (`employee_id`),
  KEY `fk_pg_proj` (`project_id`),
  CONSTRAINT `fk_pg_emp` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`id`),
  CONSTRAINT `fk_pg_proj` FOREIGN KEY (`project_id`) REFERENCES `projuct` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_guards`
--

LOCK TABLES `project_guards` WRITE;
/*!40000 ALTER TABLE `project_guards` DISABLE KEYS */;
INSERT INTO `project_guards` VALUES (1,1,'mfatins',1,'emaad','2026-01-09','2026-01-09','admin aaa','sdfv',1),(2,2,'vvv',1,'emaad','2026-01-09','2026-01-09','admin aaa','good from docker',1),(3,2,'vvv',2,'johnny depp','2026-01-09','2026-01-09','admin aaa','good from docker',1),(4,3,'Српска Кафана',3,'andre','2026-01-12','2026-01-12','admin aaa','tike for sylry emplyee',1),(5,3,'Српска Кафана',1,'emaad','2026-01-12','2026-01-12','admin aaa','trying',1),(6,4,'Каскад',1,'emaad','2026-01-12','2026-01-12','admin aaa','Доступна подсветка района, города или области после поиска организации на сайте. Есть возможность просмотра улиц на картах.\r\n\r\nДоступен поиск как по географическим объектам (адресам, улицам, городам, регионам и странам), так и по организациям. На картах имеется возможность измерять расстояние, прокладывать маршруты и просматривать панорамы улиц.',1),(7,5,'ЖК «Северный Парк»',4,'Иван Сергеевич Петров','2026-01-25','2026-01-25','admin hussen','Охранник закреплён за данным объектом на постоянной основе,',1);
/*!40000 ALTER TABLE `project_guards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projuct`
--

DROP TABLE IF EXISTS `projuct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projuct` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `Coordinates` varchar(100) NOT NULL,
  `q_person` int NOT NULL,
  `ses_work` varchar(100) NOT NULL,
  `start_time_work` varchar(100) NOT NULL,
  `sum_of_proj` int NOT NULL,
  `pers_of_proj` varchar(100) NOT NULL,
  `n_phone` varchar(100) NOT NULL,
  `sel_emp` int NOT NULL,
  `nots` varchar(500) NOT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projuct`
--

LOCK TABLES `projuct` WRITE;
/*!40000 ALTER TABLE `projuct` DISABLE KEYS */;
INSERT INTO `projuct` VALUES (1,'mfatins','Краснодар, ул. Зиповская, д. 5','45.060934, 39.001527',5,'24','00:00',250000,'andry','+79948125674',4700,'Наблюдение в аудиториях и общежитиях обязательно.',1),(2,'vvv','montagnkov 1','45.060934, 39.001527',7,'12','00:00',490000,'Дмитрий Егоров','9568831556',4700,'no thing for naw',1),(3,'Српска Кафана','улица Монтажников, 1, Фестивальный микрорайон, Краснодар','45.059122, 38.962788',4,'17','14:15',400000,'Дмитрий Егоров','+79948125674',4500,'Наблюдение в аудиториях и общежитиях обязательно.',1),(4,'Каскад','улица Монтажников, 1, Фестивальный микрорайон, Краснодар,','45.059071, 38.962540',4,'12','22:00',500000,'andry','79786543210',5000,'Яндекс Карты — поисково-информационная картографическая служба Яндекса. Открыта в 2004 году. Есть поиск по карте, информация о пробках, отслеживание городского транспорта, прокладка маршрутов и панорамы улиц крупных и других городов[',1),(5,'ЖК «Северный Парк»','Россия, г. Краснодар, ул. Российская, д. 267','45.0578, 38.9753',6,'12','08:00',450000,'Алексей Викторович Смирнов','+7 961 432-18-55',5000,'Объект с видеонаблюдением, требуется опыт работы от 1 года.',1);
/*!40000 ALTER TABLE `projuct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salary_history`
--

DROP TABLE IF EXISTS `salary_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salary_history` (
  `id` int NOT NULL AUTO_INCREMENT,
  `emp_id` int NOT NULL,
  `project_id` int NOT NULL,
  `pay_method` varchar(100) NOT NULL,
  `pay_for` varchar(100) NOT NULL,
  `sum` int NOT NULL,
  `data_entry_clerk_id` varchar(150) DEFAULT NULL,
  `process_supervisor_id` int DEFAULT NULL,
  `responsible_emp_id` varchar(150) DEFAULT NULL,
  `nots` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `done_or_not` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salary_history`
--

LOCK TABLES `salary_history` WRITE;
/*!40000 ALTER TABLE `salary_history` DISABLE KEYS */;
INSERT INTO `salary_history` VALUES (1,1,2,'зарплата','2026-01',10000,'admin aaa',NULL,NULL,'srg',0),(2,2,2,'аванс','2026-01',4700,'admin aaa',NULL,NULL,'nurm',0),(3,3,3,'аванс','2026-01',4500,'admin aaa',NULL,NULL,'nurm',0),(4,1,4,'аванс','2026-01',5000,'admin aaa',NULL,NULL,' dfe',0),(5,1,4,'зарплата','2026-01',5000,'admin aaa',NULL,NULL,'jhv',0),(6,1,4,'аванс','2026-01',7000,'admin aaa',NULL,NULL,'Può un cantautore rappresentare un territorio? Esiste una città che suona come una canzone? Ma un cantautore è un poeta?\r\nSe ha senso porsi queste domande, la vita e l’opera di Fabrizio De André ne sono la risposta. Con circa quarant’anni di carriera, quattordici album più singoli e varie antologie, scrivendo canzoni e melodie che sono entrate nel cuore di tutti, Fabrizio De André – Faber – per gli amici, ha un posto di diritto nella tradizione letteraria italiana. La cura estrema che ha sempre dedicato al testo e l’accuratezza delle rime e degli accordi ne fanno uno dei più grandi poeti del ‘900 italiano.\r\n\r\nParlare di Fabrizio De André per noi è come parlare della Liguria: rischieremmo di non concludere mai l’argomento, di consumare tutta la batteria del tuo smartphone. Così abbiamo deciso di concentrarci in pochi concetti chiave tratti dalle sue canzoni, lasciandoti il piacere di approfondire tu stesso la sua conoscenza con la sua musica.',0);
/*!40000 ALTER TABLE `salary_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `role` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'aaa','1111','admin'),(2,'bbb','dY5IEb','supadmin'),(4,'emaad','UgSWIU','emp'),(5,'hussen','CQAbaS','admin');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `work_shifts`
--

DROP TABLE IF EXISTS `work_shifts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `work_shifts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `employee_id_input` int NOT NULL,
  `project_id_input` int NOT NULL,
  `start_day` date NOT NULL,
  `start_time` time NOT NULL,
  `end_day` date NOT NULL,
  `end_time` time NOT NULL,
  `file_path` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `work_shifts`
--

LOCK TABLES `work_shifts` WRITE;
/*!40000 ALTER TABLE `work_shifts` DISABLE KEYS */;
INSERT INTO `work_shifts` VALUES (1,1,2,'2026-01-09','00:12:00','2026-01-09','12:12:00','obxod/id1-DT2026-01-09-T-12-02.jpg'),(2,2,2,'2026-01-10','00:00:00','2026-01-10','12:00:00','obxod/id2-DT2026-01-09-T-17-31.jpg'),(3,2,2,'2026-01-12','00:00:00','2026-01-12','12:00:00','obxod/id2-DT2026-01-12-T-08-07.jpg'),(4,3,3,'2026-01-13','13:15:00','2026-01-13','01:15:00','obxod/id3-DT2026-01-12-T-09-17.jpg'),(5,3,3,'2026-01-12','14:15:00','2026-01-13','07:15:00','obxod/id3-DT2026-01-12-T-11-08.jpg'),(6,1,4,'2026-01-13','22:00:00','2026-01-14','10:00:00','obxod/id1-DT2026-01-12-T-11-47.jpg'),(7,1,2,'2026-01-15','00:00:00','2026-01-15','12:00:00','obxod/id1-DT2026-01-15-T-11-34.jpg'),(8,1,2,'2026-01-17','00:00:00','2026-01-17','00:00:00','obxod/id1-DT2026-01-17-T-09-19.jpg'),(9,2,2,'2026-01-23','00:00:00','2026-01-23','12:00:00','obxod/id2-DT2026-01-22-T-11-58.jpg'),(10,3,3,'2026-01-22','14:15:00','2026-01-23','07:15:00','obxod/id3-DT2026-01-22-T-14-12.jpg'),(11,4,5,'2026-01-25','08:00:00','2026-01-25','20:00:00','obxod/id4-DT2026-01-25-T-08-39.jpg');
/*!40000 ALTER TABLE `work_shifts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-01-29 13:44:05
