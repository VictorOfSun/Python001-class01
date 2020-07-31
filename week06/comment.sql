-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- 主机： 127.0.0.1:3306
-- 生成日期： 2020-07-31 08:17:48
-- 服务器版本： 10.4.10-MariaDB
-- PHP 版本： 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `test`
--

-- --------------------------------------------------------

--
-- 表的结构 `comment`
--

DROP TABLE IF EXISTS `comment`;
CREATE TABLE IF NOT EXISTS `comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(500) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL COMMENT '内容',
  `star` int(5) DEFAULT NULL COMMENT '星级',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `comment`
--

INSERT INTO `comment` (`id`, `content`, `star`) VALUES
(1, '乔诺兰真大手！！！要剧情有剧情要大叔有大叔要耍酷有耍酷要JQ有JQ要反转有反转要AI有AI要voice porn有voice porn，现在连啃绝版书的狗都有了！！！还有什么是夕阳红二人组不行的？', 5),
(2, 'Jim Caviezel那个奄奄一息的发声真的听多了会神经衰弱。。。', 2),
(3, '值得你整晚都不睡觉，偶尔更一集都不敢随便找个时间看的良心之作。', 5),
(4, 'You are being watched. 你正在被做成表。', 4),
(5, '【CBS】机器宝宝快去帮特工爸爸把宅总爹地救回来！脑残粉想给十颗星啊！', 5),
(6, 'AI美死！一家四口美死！富豪包养特工拯救世界第二季！', 5),
(7, 'every saint has past (宅总), every sinner has future.（李四叔）在汤不热上看到的。。。。', 4),
(8, '二位演员太招人喜欢了', 4),
(9, '壮哉美利坚夕阳红！！', 5),
(10, '渐入佳境。。。有几集很惊艳，也有差池，但甩其他烂尾无力的美剧几条街了。 故事的立意起于想象力，但却是靠扎实的细节支撑的，很棒。', 4),
(11, '最可怜的莫过于空壳公司里每天输入一堆「乱码」的员工，眼睛累坏了吧。迷妹当如Root，萌宠当如Machine，忠犬当如Reese。配角好评，单集故事风格各异，主线剧情悬疑有余，多赞的剧本啊！', 5),
(12, '比之首季质量起伏增大,短板扎眼,动人起来又妙不可言,中盘维持了11集的稳定.总体较前作低迷.开始把不住人情与正义的平衡是个重症,规避或直面总得选一条,别再妥协敷衍或让角色对问题视而不见甚至OOC伺候了.编剧团或需要就理念等基准点重建共识.存在格调迥异于整体的集数,均尝试成功.舒适音画基本得以保持', 4),
(13, '五好家庭诞生~~', 5),
(14, '比前季水准更高，不光主线全面铺开牛逼至极，宅总的经历虐心得一塌糊涂，单集的个案也精彩多了，还有Facebook梗！越看越觉得几乎每个人都生活在不断的抉择和过去和悔恨的阴影之下，都失去过某些人某些东西，甚至Root都有死去的童年好友。这解释了他们的选择，也让他们联结得更紧密。', 4),
(15, '【A－】可以看出乔纳森的剧作野心绝对不仅仅只局限于“单元剧”上面，很明显，他也意识到一味以单元剧的形式磨合主线的模式是会被观众所厌烦的。所以这一季诺兰弟尝试了许多新鲜套路：一二集的营救行动；第十集到第十三集的“入狱—越狱—控制—反控制”的主线大事件；第十六集的主观视角转换（同时终于引出了肖大锤这个角色）；第十七集的“暴雪山庄”经典模式；还有最后两集各种精彩绝伦的反转。乔纳森诺兰凭借第二季证明了自己在主流商业剧集的高超的编剧能力。', 5),
(16, '我对相杀百合组的爱正式超越夕阳红！总之，夕阳红已经变成妥妥儿的人肉背景。这剧别名叫：孩子们都很好 吧。', 5),
(17, '这就是爱~', 5),
(18, '高科技和罪犯悬疑动作揶揄糅合在一起 要不好看也不容易', 5),
(20, '又看一遍，又看哭好几回这种丢脸事一定不能说出去，嗯', 5);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
