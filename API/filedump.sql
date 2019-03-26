-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: portofolio
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2

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
-- Table structure for table `Product`
--

DROP TABLE IF EXISTS `Product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `url_image` varchar(255) DEFAULT NULL,
  `seller` varchar(255) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `vendor` varchar(100) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `processor` varchar(255) DEFAULT NULL,
  `ram` varchar(255) DEFAULT NULL,
  `memory` varchar(255) DEFAULT NULL,
  `camera` varchar(255) DEFAULT NULL,
  `other_description` varchar(255) DEFAULT NULL,
  `stock` int(11) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `seller_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Product`
--

LOCK TABLES `Product` WRITE;
/*!40000 ALTER TABLE `Product` DISABLE KEYS */;
INSERT INTO `Product` VALUES (1,'https://static.toiimg.com/photo/64171591/Samsung-Galaxy-S10.jpg','benzema','new','sony','sony xperia z3',1000000,'snapdragon 820','ram 2GB','memory 16GB','23 MP','size 5 inc',5,'malang',6),(6,'https://www.91-img.com/pictures/132400-v11-xiaomi-redmi-note-7-mobile-phone-large-1.jpg','dzinsyah2','second','xiaomi','xiaomi redmi note 4',1500000,'snapdragon 660','ram 3GB','memory 32GB','13 MP','size 5 inc',6,'sidoarjo',4),(7,'https://www.91-img.com/pictures/sony-xperia-xz-premium-mobile-phone-large-1.jpg','dzinsyah2','second','sony',' sony xperia xz',1500000,'snapdragon 825','ram 3GB','memory 32GB','13 MP','size 5 inc',7,'sidoarjo',4),(9,'https://www.91-img.com/pictures/126466-v10-samsung-galaxy-a6-mobile-phone-large-1.jpg','benzema','deadsd','clkd','vfv',9832748,'kjvfjd','v','j','k','j',90,'kj',6),(10,'https://static.toiimg.com/thumb/msid-63271013,width-220,resizemode-4/Sony-Xperia-XZ-Pro.jpg','benzema','second','sony',' sony xperia xz',9500000,'snapdragon 825','ram 3GB','memory 32GB','13 MP','size 5 inc',5,'sidoarjo',6),(14,'http://www.91-img.com/pictures/samsung-galaxy-s7-mobile-phone-large-1.jpg','dzinsyah','n','n','n',8,'k','kk','k','k','kk',88,'kk',1),(15,'https://www.91-img.com/pictures/111232-v1-samsung-galaxy-note-8-mobile-phone-large-1.jpg','benzema','new','samsung','samsung note 8',5000000,'snapdragon 845','4gb','64gb','12 mp','layar 5 inc',10,'malang',6),(16,'https://www.91-img.com/pictures/131238-v4-realme-3-mobile-phone-large-1.jpg','alterra','new','realme','realme3',2000000,'helio 70','4GB','64GB','13 MP','layar 10 inc',10,'surabaya',29);
/*!40000 ALTER TABLE `Product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cart` (
  `cart_id` int(11) NOT NULL AUTO_INCREMENT,
  `urlimage` varchar(200) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `product_name` varchar(200) DEFAULT NULL,
  `qty` int(11) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`cart_id`),
  UNIQUE KEY `cart_id` (`cart_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
INSERT INTO `cart` VALUES (2,'https://www.91-img.com/pictures/132400-v11-xiaomi-redmi-note-7-mobile-phone-large-1.jpg',6,6,'xiaomi redmi note 4',2,3000000,'2019-03-26 17:21:38','2019-03-26 17:21:38'),(3,'https://www.91-img.com/pictures/sony-xperia-xz-premium-mobile-phone-large-1.jpg',7,6,' sony xperia xz',3,4500000,'2019-03-26 17:22:04','2019-03-26 17:22:04');
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback` (
  `fb_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `feedback` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`fb_id`),
  UNIQUE KEY `fb_id` (`fb_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
INSERT INTO `feedback` VALUES (2,6,'dzinsyah@alphatech.com','pelayanan sangat cepat!'),(3,6,'benzema@alphatech.com','pelayanan sangat cepat!'),(4,6,'benzema@alphatech.com','pelayanan kkurang memuaskan!');
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transaction` (
  `tr_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `fullname` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `address` varchar(1000) DEFAULT NULL,
  `total_qty` int(11) DEFAULT NULL,
  `total_price` int(11) DEFAULT NULL,
  `payment_method` varchar(200) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`tr_id`),
  UNIQUE KEY `tr_id` (`tr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction`
--

LOCK TABLES `transaction` WRITE;
/*!40000 ALTER TABLE `transaction` DISABLE KEYS */;
INSERT INTO `transaction` VALUES (1,6,'karim benzema','benzema@gmail.com','malang',6,7000000,'alfamart','waiting for payment','2019-03-24 10:50:34','2019-03-24 10:50:34'),(2,6,'karim benzema','benzema@gmail.com','malang',6,7000000,'alfamart','waiting for payment','2019-03-24 10:51:30','2019-03-24 10:51:30');
/*!40000 ALTER TABLE `transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(200) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `telephone` varchar(100) DEFAULT NULL,
  `status_admin` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'dzinsyah','dzinsyah@alphatech.id','bismillah','tumpang','1578643287347','admin'),(3,'dzinsyah1','dzinsyah1@alphatech.id','bismillah','tumpang','085258721899','admin'),(4,'dzinsyah2','dzinsyah2@alphatech.id','bismillah','tumpang','085258721899','seller'),(6,'benzema','budi@alphatech.com','bismillah','malangg','0852587218999','seller'),(7,'ronaldo','ronaldo@alphatech.id','bismillah','malang','085258721899','seller'),(8,'adi','adi@alphatech.id','bismillah','malang','085258721899','seller'),(11,'adi1','addii@alphatech.id','bismillah','malang','085258721899','seller'),(12,NULL,NULL,NULL,NULL,NULL,'seller'),(13,NULL,NULL,NULL,NULL,NULL,'seller'),(15,'adi2','addiiii@alphatech.id','bismillah','malang','085258721899','seller'),(16,'dzidsin','jfdasfnj@klmvdkv.vom','bjncdkj','kjdsnnlksam','987598435','seller'),(17,'dzinsyah5','dzinsyah3@gmail.com','bismillah','tumpang','08988883338','seller'),(21,'dzinsyah55','dzinsyah111@gmail.com','bismillah','tumpang','08988883338','seller'),(22,'alta','alta@gmail.com','bismillah','malang','0893298838333','seller'),(24,'saya','saya@gmail.com','bismillah','malang','089777888999','seller'),(26,'aw','awas@gmail.skm','bismillah','malang','09887474','seller'),(28,'aq','aq@gmail.com','bismillah','malalng','987598435','seller'),(29,'alterra','alterra@alphatech.id','bismillah','jalan tidar','089777788899','seller');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-26 17:37:22
