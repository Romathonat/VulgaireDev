-- MySQL dump 10.13  Distrib 5.7.20, for Linux (x86_64)
--
-- Host: localhost    Database: vulgairedev
-- ------------------------------------------------------
-- Server version	5.7.20

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
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add site',2,'add_site'),(5,'Can change site',2,'change_site'),(6,'Can delete site',2,'delete_site'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add group',4,'add_group'),(11,'Can change group',4,'change_group'),(12,'Can delete group',4,'delete_group'),(13,'Can add user',5,'add_user'),(14,'Can change user',5,'change_user'),(15,'Can delete user',5,'delete_user'),(16,'Can add content type',6,'add_contenttype'),(17,'Can change content type',6,'change_contenttype'),(18,'Can delete content type',6,'delete_contenttype'),(19,'Can add session',7,'add_session'),(20,'Can change session',7,'change_session'),(21,'Can delete session',7,'delete_session'),(22,'Can add article',8,'add_article'),(23,'Can change article',8,'change_article'),(24,'Can delete article',8,'delete_article'),(25,'Can add categorie',9,'add_categorie'),(26,'Can change categorie',9,'change_categorie'),(27,'Can delete categorie',9,'delete_categorie');
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
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$24000$dGoeKHOo0XCB$zLxVHBSPBGy51uMcPCQgucSa+pMWXnfw5soNsaXiZtU=','2019-08-03 22:58:11.313906',1,'adminVulgaireDev','','','romain.mathonat@gmail.com',1,1,'2017-12-21 14:29:55.134617'),(2,'pbkdf2_sha256$24000$M6X97rzOkUdW$UsVyUreJa6PBjEaQGbm3kDL2Bys2eOSdXx0gwmUJGw8=',NULL,0,'VulgaireDev','','','',0,1,'2017-12-21 14:32:03.961709'),(3,'pbkdf2_sha256$24000$LsgTfWwNpxuu$RmvaylNoCCuzfFEKKi8B/+ubrWrsUyt0rxqnPo/7sNI=',NULL,0,'Haalford','','','',0,1,'2017-12-21 14:36:19.622805'),(4,'pbkdf2_sha256$24000$FInyuV2TY4Yt$WYe0Q5ISm1JPGo0RQNJk0fpQCSghhiriHn7ZgTWfTOU=',NULL,0,'Draedixe','','','',0,1,'2017-12-21 14:46:32.720287');
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
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_article`
--

DROP TABLE IF EXISTS `blog_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titre` varchar(100) NOT NULL,
  `slug` varchar(100) NOT NULL,
  `preview` longtext NOT NULL,
  `urlGitHub` varchar(200) DEFAULT NULL,
  `publie` tinyint(1) NOT NULL,
  `date` datetime(6) NOT NULL,
  `auteur_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_article_auteur_id_762d9f93_fk_auth_user_id` (`auteur_id`),
  KEY `blog_article_2dbcba41` (`slug`),
  CONSTRAINT `blog_article_auteur_id_762d9f93_fk_auth_user_id` FOREIGN KEY (`auteur_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_article`
--

LOCK TABLES `blog_article` WRITE;
/*!40000 ALTER TABLE `blog_article` DISABLE KEYS */;
INSERT INTO `blog_article` VALUES (1,'pow(2,n) | 2 << n','2-puissance-n','En info on entend souvent parler de 2^n, parfois sans explications claires. On va essayer de débroussailler le sujet, et de comprendre avec quelques exemples.','pow_2n/pow_2n.md',1,'2015-11-14 20:10:04.000000',2),(2,'Combat de Poule','combat-de-poule','Dans le sport, avant les phases dites finales d\'une compétition, on a droit aux phases de poule. Mais combien de combats sont organisés par poule ? C\'est ce qu\'on va expliquer aujourd\'hui.','combat_poules/combat_poules.md',1,'2015-12-05 14:01:50.000000',2),(3,'La somme maximale de nombres consécutifs dans un tableau','max-nombre-consecutif','Vous disposez d\'un tableau contenant des nombres, positifs ou négatifs. On vous donne 2 nombres A et B. Quelle est la somme maximale d\'éléments consécutifs commençant par A et finissant par B (compris) qui est maximale ?','max_array/max_array.md',1,'2016-02-06 14:42:23.000000',2),(4,'Enigme: La bouteille empoisonnée','bouteille-empoisonnee','Vous êtes roi, et préparez votre mariage qui a lieu demain. Vous disposez d\'autant de serviteurs que vous le désirez, et possédez 1000 bouteilles de vin pour le festin de demain. On vous apprend qu\'une des bouteilles parmis les 1000 est empoisonnée, et provoque la mort en moins de 24h, et ce quelle que soit la quantité absorbée. Quel est le nombre minimal de serviteurs que vous devez mobiliser afin de pouvoir isoler de manière certaine la bouteille empoisonée ?','bouteille_poison/bouteille_poison.md',1,'2016-04-17 22:12:29.000000',2),(5,'Enigme: La ronde des chapeaux','Ronde-des-chapeaux','Je vous propose la petite énigme suivante :\r\n\r\nDans une salle sans miroir se trouvent N personnes. Chacune de ces personnes porte sur la tête un chapeau coloré et peut voir la couleur des chapeaux des autres personnes. Par contre, une personne ne peut pas connaitre la couleur de son chapeau.\r\n\r\nOn sait qu\'il existe N couleurs de chapeau différentes. Attention, plusieurs personnes peuvent avoir un chapeau de même couleur sur la tête! Ainsi, une couleur de chapeau qui existe peut ne pas être portée. (Il n\'y a pas de bijection entre les couleurs et les personnes).\r\n\r\nAu bout d\'un certain temps, les N personnes vont annoncer simultanément une couleur. Quelle stratégie doivent-elles mettre en place pour qu\'au moins l\'une d\'entre elle annonce la couleur de son chapeau?','ronde_chapeau/ronde_chapeau.md',1,'2016-05-08 13:36:19.000000',3),(6,'OCCInterface and ExploREST','occinterface-exploREST','OCCInterface and ExploREST are part of the result of my work this summer. Check it out !','OCCInterface/OCCInterface.md',1,'2016-09-02 09:21:16.000000',2),(7,'Disqus comments and article submission','disqus-comments-article-submission','A quick article to explain two new functionalities of vulgairedev.','commentsArticlModif/commentsArticModifs.md',1,'2016-09-16 20:35:59.000000',2),(8,'Numérique et éducation','numerique-education','Parlons un peu du passage au numérique dans l\'éducation. Il y a deux-trois points qui me titillent que je voudrais partager.','passageNumerique/passageNumerique.md',1,'2016-10-28 14:22:58.000000',2),(9,'Introduction to caffe','caffe-introduction','Today, an article about caffe, a framework for convolutional neural network (machine learning). Caffe is quite famous, but its documentation is terrific. In this tutorial we will train a model, and use the python interface to ask the Neural Network to classify an image.','caffeIntroduction/caffeIntroduction.md',1,'2016-11-07 16:03:47.000000',2),(10,'Faces detection with caffe','faces-detection-caffe','This is a project I worked on recently : detecting faces on an image thanks to machine learning (using caffe for CNN).','CNNarticle/CNNarticle.md',1,'2016-11-20 15:47:14.000000',2),(11,'Eight Queens Puzzle','eightQueensPuzzle','You have a chessboard of 8*8 square. You have 8 queens. Your goal is to place the 8 queens on the board, without any of them threatening another one. A queen is threaten if she is on the same row, or the same column, or the same diagonal of another queen (like in the rules of chess).','eightQueensPuzzle/eightQueens.md',1,'2016-12-31 11:17:09.000000',2),(12,'Faux positifs','faux-positifs','En statistique et en machine learning, on utilise souvent la notion de \"faux positifs\", \"vrai positifs\", rappel, précision ... Nous allons expliquer ces concepts aujourd\'hui.','fauxPositifs/fauxPositifs.md',1,'2017-02-10 14:57:25.000000',2),(13,'Les problemes P, NP','problemesP_NP','Nous allons parler des problèmes P, NP, NP-Complet et NP-Difficile. Ce sont des notions de base en informatique en tant que \"science\".','NPProblemes/NPProblemes.md',1,'2017-03-10 11:00:41.000000',2),(14,'Introduction à la DP','intro_dp','Dynamic Programming. Ou programmation dynamique en français. C\'est une technique de résolution de problèmes, qui peut être un peu compliquée à comprendre, mais nous allons essayer de nous en sortir avec un exemple qu\'on qualifie de \"pas trop dur\".','intro_DP/intro_DP.md',1,'2017-05-11 14:42:01.000000',2),(15,'Intro de l\'intro à la DP','intro_intro_dp','Le dernier article concernant la programmation dynamique començait avec un exemple un peu trop compliqué. Ici on va en faire un plus simple avec la suite de Fibonacci, ce sera plus facile pour comprendre.','intro_de_intro_DP/intro_de_intro_DP.md',1,'2017-05-15 14:28:16.000000',2),(16,'Docker: a post to my past self','docker-post-to-my-past-self','TL;DR I used Docker during last months. I write down here what I would have liked to know when beginning using it, what you can do with it and some tricks you need to be aware of.','docker/docker.md',1,'2017-11-01 14:28:16.000000',2),(17,'Résumé de statistiques/probabilités','resume-statistique','Je suis en train de faire les cours du MIT sur les probabilités/statisitques (ici). Le titre officiel est \"Introduction aux probabilités et statistiques\", mais le cours est tout de même assez complet je trouve, donc je fais un résumé ici (ce n\'est pas un vrai cours suffisamment, donc si vous ne connaissez pas un minimum, ça risque d\'être un peu dur).','statistiques/statistiques.md',1,'2017-11-07 14:28:16.000000',2),(18,'Résumé de statistiques bayesiennes','statistiques-bayesienne','Comme l\'article sur les probabilités, il s\'agit ici d\'un résumé de cours du MIT trouvable ici sur leur site.','statistiques_bayesienne/stat_bayes.md',1,'2017-11-15 14:28:16.000000',2),(19,'Tuto: déploiement d\'un projet Django','deploiement-django','Aujourd\'hui un article bien plus conséquent. Un tuto pour être précis.\r\n\r\nLe déploiement d\'un projet django n\'est pas forcement une partie de plaisir la première fois. On va expliquer comment faire ici, en s\'efforçant d\'être clair, parce que les informations présentes sur le web sont parfois confuses.\r\n\r\nEt ça me servira de mémo.','deploy_django/deploy_django.md',1,'2015-12-20 14:28:16.000000',2),(20,'L\'utilisation des opérateurs bit à bit','operateurs-bit-a-bit','Vous voyez parfois du code du style \"x & 1\"\r\n\r\nsans comprendre ce qu\'il fait ?\r\n\r\nVous voulez apprendre deux ou trois trucs pour être \"plus proche de votre ordinateur\"?\r\n\r\nSuivez le guide avec ce premier article proposé par Draedixe !','operateur_bit/operateur_bit.md',1,'2016-01-04 14:28:16.000000',4),(21,'Les Chiffres','les-chiffres','Presque tout le monde connaît \"les chiffres et les lettres\", cette émission où les participants ont un QI presque 2 fois supérieur à celui des participants des ch\'tis à Mykonos, et qui gagnent pourtant bien moins de 2 fois ce que ces derniers récoltent grâce à leur talent ... d\'existence.','chiffres/chiffres.md',1,'2016-01-11 14:28:16.000000',2),(22,'Combien de zones dans ce cercle ?','nombre-de-partitions-cercle','On dispose d\'un cercle dans lequel un nombre n de points ont été disposés le long de son périmètre. Les points sont ensuite reliés deux à deux, comme sur la figure ci-contre, ce qui génère une figure géométrique.\r\n\r\nCombien existe-t-il de zones ?','zones_cercle/zones_cercle.md',1,'2016-02-08 14:28:16.000000',2),(23,'A Priori Implementation','apriori','In this notebook, we will implement the algorithm of the Apriori algorithm as described in \"Fast algorithms for mining association rules\", Rakesh Agrawal, Ramakrishnan Srikant.','apriori/apriori.ipynb',1,'2018-01-26 22:55:18.000000',2),(24,'Compter les sous-séquences','compter-sous-seq','Après quelques temps d\'inactivité, je reviens avec une nouvelle programmation dynamique.','number_subsequences/number_subsequences.md',1,'2018-07-10 22:55:18.000000',2),(25,'L\'énigme des deux enfants','enigme-enfants','Je suis tombé sur l\'énigme des deux enfants, proposé par science4all.','deux-enfants/deux-enfants.md',1,'2019-02-07 12:20:09.000000',2),(26,'SAX: Piecewise Aggregate Approximation','paa','We have a series of n numbers that we want to divide into w slots. We want to compute the mean of each slot, how do we proceed when n is not divisible by w ? This is called a Piecewise Aggregate Approximation (PAA).','paa/paa.md',1,'2019-03-21 14:25:18.000000',2);
/*!40000 ALTER TABLE `blog_article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_article_categorie`
--

DROP TABLE IF EXISTS `blog_article_categorie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_article_categorie` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `article_id` int(11) NOT NULL,
  `categorie_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `blog_article_categorie_article_id_69a7a01f_uniq` (`article_id`,`categorie_id`),
  KEY `blog_article_categori_categorie_id_f7839d5d_fk_blog_categorie_id` (`categorie_id`),
  CONSTRAINT `blog_article_categori_categorie_id_f7839d5d_fk_blog_categorie_id` FOREIGN KEY (`categorie_id`) REFERENCES `blog_categorie` (`id`),
  CONSTRAINT `blog_article_categorie_article_id_09003486_fk_blog_article_id` FOREIGN KEY (`article_id`) REFERENCES `blog_article` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_article_categorie`
--

LOCK TABLES `blog_article_categorie` WRITE;
/*!40000 ALTER TABLE `blog_article_categorie` DISABLE KEYS */;
INSERT INTO `blog_article_categorie` VALUES (1,1,5),(2,2,5),(3,3,4),(4,4,5),(5,5,5),(6,6,3),(7,7,3),(8,8,1),(9,9,3),(10,10,3),(11,10,4),(12,11,4),(13,12,5),(14,13,4),(15,13,5),(16,14,4),(17,14,5),(18,15,4),(19,15,5),(20,16,2),(21,17,5),(22,18,5),(23,19,2),(24,20,3),(25,21,4),(26,21,5),(27,22,5),(28,23,3),(29,24,4),(30,25,5),(31,26,5);
/*!40000 ALTER TABLE `blog_article_categorie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_categorie`
--

DROP TABLE IF EXISTS `blog_categorie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_categorie` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(30) NOT NULL,
  `couleur` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_categorie`
--

LOCK TABLES `blog_categorie` WRITE;
/*!40000 ALTER TABLE `blog_categorie` DISABLE KEYS */;
INSERT INTO `blog_categorie` VALUES (1,'Divers','rgb(255,188,121)'),(2,'Systeme','rgb(200,200,200)'),(3,'Developpement','rgb(218,151,143)'),(4,'Algorithmique','rgb(192,255,248)'),(5,'\"Maths\"','rgb(255,188,121)');
/*!40000 ALTER TABLE `blog_categorie` ENABLE KEYS */;
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
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2017-12-21 14:30:31.735564','1','Divers',1,'Ajout.',9,1),(2,'2017-12-21 14:30:44.627230','2','Systeme',1,'Ajout.',9,1),(3,'2017-12-21 14:31:01.769406','3','Developpement',1,'Ajout.',9,1),(4,'2017-12-21 14:31:18.387186','4','Algorithmique',1,'Ajout.',9,1),(5,'2017-12-21 14:31:34.297676','5','\"Maths\"',1,'Ajout.',9,1),(6,'2017-12-21 14:32:03.987256','2','VulgaireDev',1,'Ajout.',5,1),(7,'2017-12-21 14:32:55.862778','1','pow(2,n) | 2 << n',1,'Ajout.',8,1),(8,'2017-12-21 14:33:51.888692','2','Combat de Poule',1,'Ajout.',8,1),(9,'2017-12-21 14:34:27.286812','3','La somme maximale de nombres consécutifs dans un tableau',1,'Ajout.',8,1),(10,'2017-12-21 14:35:04.848240','4','Enigme: La bouteille empoisonnée',1,'Ajout.',8,1),(11,'2017-12-21 14:36:02.954099','5','Enigme: La ronde des chapeaux',1,'Ajout.',8,1),(12,'2017-12-21 14:36:19.648786','3','Haalford',1,'Ajout.',5,1),(13,'2017-12-21 14:36:27.277753','5','Enigme: La ronde des chapeaux',2,'Modification de auteur.',8,1),(14,'2017-12-21 14:37:20.877210','6','OCCInterface and ExploREST',1,'Ajout.',8,1),(15,'2017-12-21 14:37:50.909171','7','Disqus comments and article submission',1,'Ajout.',8,1),(16,'2017-12-21 14:38:29.644488','8','Numérique et éducation',1,'Ajout.',8,1),(17,'2017-12-21 14:39:01.115513','9','Introduction to caffe',1,'Ajout.',8,1),(18,'2017-12-21 14:39:36.662043','10','Faces detection with caffe',1,'Ajout.',8,1),(19,'2017-12-21 14:40:16.581266','11','Eight Queens Puzzle',1,'Ajout.',8,1),(20,'2017-12-21 14:40:53.388706','12','Faux positifs',1,'Ajout.',8,1),(21,'2017-12-21 14:41:33.435419','13','Les problemes P, NP',1,'Ajout.',8,1),(22,'2017-12-21 14:42:05.817335','14','Introduction à la DP',1,'Ajout.',8,1),(23,'2017-12-21 14:42:52.834350','15','Intro de l\'intro à la DP',1,'Ajout.',8,1),(24,'2017-12-21 14:43:31.504267','16','Docker: a post to my past self',1,'Ajout.',8,1),(25,'2017-12-21 14:44:07.557002','17','Résumé de statistiques/probabilités',1,'Ajout.',8,1),(26,'2017-12-21 14:45:10.103128','18','Résumé de statistiques bayesiennes',1,'Ajout.',8,1),(27,'2017-12-21 14:45:42.862264','19','Tuto: déploiement d\'un projet Django',1,'Ajout.',8,1),(28,'2017-12-21 14:46:20.851585','20','L\'utilisation des opérateurs bit à bit',1,'Ajout.',8,1),(29,'2017-12-21 14:46:32.745129','4','Draedixe',1,'Ajout.',5,1),(30,'2017-12-21 14:46:39.787219','20','L\'utilisation des opérateurs bit à bit',2,'Modification de auteur.',8,1),(31,'2017-12-21 14:47:13.991313','21','Les Chiffres',1,'Ajout.',8,1),(32,'2017-12-21 14:47:53.326034','22','Combien de zones dans ce cercle ?',1,'Ajout.',8,1),(33,'2019-08-03 22:59:35.114311','23','A Priori Implementation',1,'Ajout.',8,1),(34,'2019-08-03 23:00:28.633248','23','A Priori Implementation',2,'Modification de urlGitHub.',8,1),(35,'2019-08-03 23:02:31.302733','24','Compter les sous-séquences',1,'Ajout.',8,1),(36,'2019-08-03 23:04:24.082631','25','L\'énigme des deux enfants',1,'Ajout.',8,1),(37,'2019-08-03 23:05:57.858791','26','SAX: Piecewise Aggregate Approximation',1,'Ajout.',8,1),(38,'2019-08-03 23:14:56.351145','24','Compter les sous-séquences',2,'Aucun champ modifié.',8,1);
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
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(4,'auth','group'),(3,'auth','permission'),(5,'auth','user'),(8,'blog','article'),(9,'blog','categorie'),(6,'contenttypes','contenttype'),(7,'sessions','session'),(2,'sites','site');
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
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-12-21 14:28:14.283380'),(2,'auth','0001_initial','2017-12-21 14:28:14.830624'),(3,'admin','0001_initial','2017-12-21 14:28:14.969334'),(4,'admin','0002_logentry_remove_auto_add','2017-12-21 14:28:15.003321'),(5,'contenttypes','0002_remove_content_type_name','2017-12-21 14:28:15.113669'),(6,'auth','0002_alter_permission_name_max_length','2017-12-21 14:28:15.153736'),(7,'auth','0003_alter_user_email_max_length','2017-12-21 14:28:15.177727'),(8,'auth','0004_alter_user_username_opts','2017-12-21 14:28:15.197840'),(9,'auth','0005_alter_user_last_login_null','2017-12-21 14:28:15.237823'),(10,'auth','0006_require_contenttypes_0002','2017-12-21 14:28:15.242401'),(11,'auth','0007_alter_validators_add_error_messages','2017-12-21 14:28:15.253946'),(12,'blog','0001_initial','2017-12-21 14:28:15.526412'),(13,'sessions','0001_initial','2017-12-21 14:28:15.581695'),(14,'sites','0001_initial','2017-12-21 14:28:15.617743'),(15,'sites','0002_alter_domain_unique','2017-12-21 14:28:15.656086');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('k7dpvflf1i7q36zqg3kht4vihhgd4p27','ODA4MGRiYTBmM2RjNWVkMDZjMWZhNDA2NDdmNGVmN2ZjZWU4NmRjYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NjNiZGIxNzQ2NTkwOWU3NTBmMjJmY2FmN2YyOGVmMGEyMTI1NjhjIn0=','2018-01-04 14:30:06.098105'),('tu5vb7kgt39slteby16e5onh8yrxo75t','YjJlZWU3YjExZGZhYWJmNDkxMTA5NzhiYzdjMDNhYTYyYWE3NDJjYzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNjYzYmRiMTc0NjU5MDllNzUwZjIyZmNhZjdmMjhlZjBhMjEyNTY4YyIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2019-08-17 22:58:11.329187');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-04  0:30:01
