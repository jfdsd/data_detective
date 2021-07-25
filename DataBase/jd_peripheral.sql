/*
 Navicat Premium Data Transfer

 Source Server         : wade
 Source Server Type    : MySQL
 Source Server Version : 80025
 Source Host           : localhost:3306
 Source Schema         : jd_peripheral

 Target Server Type    : MySQL
 Target Server Version : 80025
 File Encoding         : 65001

 Date: 25/07/2021 03:01:48
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for attention
-- ----------------------------
DROP TABLE IF EXISTS `attention`;
CREATE TABLE `attention`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `jd_price` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `jd_id` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `good` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `middle_time` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `poor_time` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of attention
-- ----------------------------
INSERT INTO `attention` VALUES (1, '金士顿（Kingston）32GB USB3.0 U盘 DT100G3 黑色 滑盖设计 时尚便利', '34.90', '854803', '0%', '2021-07-21 12:25:14', '2021-07-25 00:20:39');
INSERT INTO `attention` VALUES (4, '西部数据(WD) 2TB USB3.0 移动硬盘 Elements 新元素系列2.5英寸 大容量 快速传输 轻薄便携', '419.00', '6772447', '0%', '2021-07-22 18:43:08', '2021-07-24 21:17:41');
INSERT INTO `attention` VALUES (7, '闪迪(SanDisk)64GB USB3.0 U盘 CZ73酷铄 银色 读速150MB/s 金属外壳 内含安全加密软件', '52.90', '2145498', '0%', '2021-07-24 21:42:22', '2021-07-24 13:27:51');

-- ----------------------------
-- Table structure for jd_ranking
-- ----------------------------
DROP TABLE IF EXISTS `jd_ranking`;
CREATE TABLE `jd_ranking`  (
  `id` int(0) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `jd_price` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `jd_id` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `good` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of jd_ranking
-- ----------------------------
INSERT INTO `jd_ranking` VALUES (1, '公牛（BULL）新国标分控插座/插线板/插排/排插/接线板/拖线板 GN-B3043  4位分控全长1.8米 独立开关', '35.90', '3693877', '0%');
INSERT INTO `jd_ranking` VALUES (2, '西部数据(WD) 2TB USB3.0 移动硬盘 Elements SE 新元素系列2.5英寸 大容量 快速传输 便携 商务办公', '429.00', '7764263', '0%');
INSERT INTO `jd_ranking` VALUES (3, '金士顿（Kingston）32GB USB3.0 U盘 DT100G3 黑色 滑盖设计 时尚便利', '34.90', '854803', '0%');
INSERT INTO `jd_ranking` VALUES (4, '闪迪(SanDisk)64GB USB3.0 U盘 CZ73酷铄 银色 读速150MB/s 金属外壳 内含安全加密软件', '52.90', '2145498', '0%');
INSERT INTO `jd_ranking` VALUES (5, '公牛（BULL）新国标插座/插线板/插排/排插/接线板/拖线板 4位总控全长1.8米 GN-B3220', '25.90', '100018301402', '0%');
INSERT INTO `jd_ranking` VALUES (6, '西部数据(WD) 2TB USB3.0 移动硬盘 Elements 新元素系列2.5英寸 大容量 快速传输 轻薄便携', '419.00', '6772447', '0%');
INSERT INTO `jd_ranking` VALUES (7, '罗技（Logitech）M220 轻音鼠标 无线鼠标 办公鼠标 对称鼠标 带无线微型接收器 灰黑色', '79.00', '3290987', '0%');
INSERT INTO `jd_ranking` VALUES (8, '罗技（Logitech）MK275 键鼠套装 无线键鼠套装 办公键鼠套装 全尺寸 黑蓝色 带无线2.4G接收器', '119.00', '2291748', '0%');
INSERT INTO `jd_ranking` VALUES (9, '公牛（BULL）新国标分控插座/插线板/插排/排插/接线板/拖线板 GN-B3043  4位分控全长3米 独立开关', '43.90', '4124952', '0%');
INSERT INTO `jd_ranking` VALUES (10, '小米 无线键鼠套装 简洁轻薄 全尺寸104键键盘 舒适鼠标 2.4G无线传输 电脑办公套装', '99.00', '100010548644', '0%');
INSERT INTO `jd_ranking` VALUES (11, '雷蛇(Razer) 蝰蛇标准版 鼠标 有线鼠标 游戏鼠标 人体工程学 电竞 黑色 6400DPI lol吃鸡神器cf', '129.00', '8141909', '0%');
INSERT INTO `jd_ranking` VALUES (12, '小米无线鼠标 Lite 2.4GHz无线传输 办公鼠标 黑色', '39.00', '100005554605', '0%');
INSERT INTO `jd_ranking` VALUES (13, '罗技（G）G502 HERO主宰者有线鼠标 游戏鼠标 HERO引擎 RGB鼠标 电竞鼠标 25600DPI', '349.00', '100001691967', '0%');
INSERT INTO `jd_ranking` VALUES (14, '金士顿（Kingston）32GB USB3.2 Gen 1 U盘 DTX 时尚设计 轻巧便携', '26.90', '100008550229', '0%');
INSERT INTO `jd_ranking` VALUES (15, '东芝(TOSHIBA) 2TB 移动硬盘 新小黑A3 USB3.0 2.5英寸 商务黑 兼容Mac 轻薄便携 稳定耐用 高速传输 爆款', '409.00', '6461421', '0%');
INSERT INTO `jd_ranking` VALUES (16, '罗技（Logitech）M330轻音鼠标 无线鼠标 办公鼠标 右手鼠标 带无线微型接收器 黑色', '109.00', '3290993', '0%');
INSERT INTO `jd_ranking` VALUES (17, '戴尔（DELL）MS116 有线鼠标 商务办公经典对称有线USB接口即插即用鼠标（黑色）', '22.90', '2136538', '0%');
INSERT INTO `jd_ranking` VALUES (18, '希捷(Seagate) 移动硬盘 2TB USB3.0 简 2.5英寸 高速 轻薄 便携 兼容PS4', '419.00', '100006464203', '0%');
INSERT INTO `jd_ranking` VALUES (19, '金士顿（Kingston）128GB USB3.0 U盘 DT100G3 读速130MB/s 黑色 滑盖设计 时尚便利', '90.00', '2109922', '0%');
INSERT INTO `jd_ranking` VALUES (20, '金士顿（Kingston）64GB USB3.0 U盘 DT100G3 黑色 滑盖设计 时尚便利', '49.90', '854802', '0%');
INSERT INTO `jd_ranking` VALUES (21, '公牛（BULL）转换插头/品字形一转三插座/无线转换插座/电源转换器 适用卧室、厨房 3位分控插座 GN-96033', '40.50', '100000479987', '0%');
INSERT INTO `jd_ranking` VALUES (22, '爱国者（aigo）64GB USB3.0 U盘 U330金属旋转系列 银色 快速传输 出色出众', '39.90', '5869754', '0%');
INSERT INTO `jd_ranking` VALUES (23, '西部数据(WD) 1TB USB3.0 移动硬盘 Elements SE 新元素系列2.5英寸 快速传输 便携 商务办公', '329.00', '7536981', '0%');
INSERT INTO `jd_ranking` VALUES (24, '小米（MI）米家新国标USB插座/插线板/插排/排插/拖线板/插板/接线板 3USB接口+3孔位  总控 全长1.8米  白色', '49.00', '4354506', '0%');
INSERT INTO `jd_ranking` VALUES (25, '公牛（BULL）插座/插线板/插排/排插/接线板/拖线板 4位分控全长5米 GN-B3043', '52.90', '100009508517', '0%');
INSERT INTO `jd_ranking` VALUES (26, '西部数据(WD) 2TB USB3.0 移动硬盘 My Passport随行版 2.5英寸 黑色 大容量 高速 加密 自动备份 兼容Mac', '439.00', '100007341458', '0%');
INSERT INTO `jd_ranking` VALUES (27, '罗技（Logitech）MK120 键鼠套装 有线键鼠套装 办公键鼠套装 电脑键盘 笔记本键盘 联想全尺寸 黑色', '89.00', '584300', '0%');
INSERT INTO `jd_ranking` VALUES (28, '雷柏（Rapoo） V500PRO 机械键盘 有线键盘 游戏键盘 104键混光键盘 吃鸡键盘 电脑键盘 黑色 黑轴', '119.00', '5028795', '0%');
INSERT INTO `jd_ranking` VALUES (29, '绿联 HDMI线2.0版 4K数字高清线 2米 3D视频线工程级 笔记本电脑机顶盒连接电视投影仪显示器数据连接线', '29.90', '1233214', '0%');
INSERT INTO `jd_ranking` VALUES (30, '惠普（HP）真机械手感键盘鼠标套装游戏有线背光电竞吃鸡笔记本台式电脑外设办公键鼠朋克网吧三件套 K500黑色彩光【经典版】', '59.90', '66424479811', '0%');
INSERT INTO `jd_ranking` VALUES (31, '绿联USB蓝牙适配器4.0发射器兼容5.0音频接收器aptx免驱 PC台式机笔记本电脑接手机无线蓝牙耳机音响鼠标键盘', '35.00', '3252898', '0%');
INSERT INTO `jd_ranking` VALUES (32, '罗技（Logitech）MK345 无线键鼠套装 防泼溅 时尚高效', '169.00', '1241897', '0%');
INSERT INTO `jd_ranking` VALUES (33, '绿联USB3.0分线器 高速4口扩展坞 HUB集线器 USB拓展坞笔记本电脑转接头一拖多接口转换器转接头延长线50985', '59.00', '100002408530', '0%');
INSERT INTO `jd_ranking` VALUES (34, '得力(deli)耐磨办公游戏鼠标垫 办公用品 黑色3692', '9.50', '1013024', '0%');
INSERT INTO `jd_ranking` VALUES (35, '山泽(SAMZHE)HDMI线2.0版 电脑电视4K视频高清线 投影仪数据连接线 1.5米 15SH8', '16.90', '5160398', '0%');
INSERT INTO `jd_ranking` VALUES (36, '绿联 手机无线投屏器 4K高清hdmi音视频同屏传输器 适用苹果安卓华为手机电脑接电视显示器投影仪线', '179.00', '100016161814', '0%');
INSERT INTO `jd_ranking` VALUES (37, '绿联 HDMI转VGA线转换器  高清转接头适配器 笔记本电脑机顶盒子连电视显示器PPT投影仪线 黑色', '29.90', '55563238198', '0%');
INSERT INTO `jd_ranking` VALUES (38, 'Wacom和冠数位板 手绘板 手写板 写字板 绘画板 绘图板 电子绘板 电脑绘图板  CTL-672/K2-F', '509.00', '6011419', '0%');
INSERT INTO `jd_ranking` VALUES (39, '高漫1060pro 数位板可连接手机手绘板电脑绘画板手写板写字板电子绘图板', '136.00', '4536314', '0%');
INSERT INTO `jd_ranking` VALUES (40, '小米液晶小黑板 10英寸 儿童画板 写字演算手写绘画涂鸦 电子画板', '49.00', '100008566572', '0%');
INSERT INTO `jd_ranking` VALUES (41, 'TP-LINK USB蓝牙适配器4.0发射器兼容5.0蓝牙接收器免驱动 PC台式机笔记本电脑手机无线蓝牙耳机鼠标键盘音箱', '35.00', '100008797693', '0%');
INSERT INTO `jd_ranking` VALUES (42, '绿联 USB转千兆网口3.0分线器 笔记本外置有线网卡转换器扩展坞 适用苹果华为电脑拓展坞HUB集线器RJ45转接头', '99.00', '100017354742', '0%');
INSERT INTO `jd_ranking` VALUES (43, '得力(deli)舒适耐磨树脂鼠标垫 办公游戏鼠标垫 280*220mm 黑色2227', '25.00', '100002535736', '0%');
INSERT INTO `jd_ranking` VALUES (44, '绿联 Type-C移动硬盘盒2.5英寸USB3.0 SATA串口笔记本台式外置壳固态机械ssd硬盘 USB款', '39.90', '12948837247', '0%');
INSERT INTO `jd_ranking` VALUES (45, '小米液晶小黑板 13.5英寸 儿童画板 写字演算手写绘画涂鸦 电子画板', '89.00', '100004879541', '0%');
INSERT INTO `jd_ranking` VALUES (46, '绿联USB3.0分线器 高速4口拓展坞 USB集线器HUB扩展坞 笔记本电脑一拖四多接口转换器转接头延长线1.5米30221', '65.00', '2304689', '0%');
INSERT INTO `jd_ranking` VALUES (47, '小米米家液晶小黑板 20英寸 儿童画板 写字演算手写绘画涂鸦 电子画板', '139.00', '100016138236', '0%');
INSERT INTO `jd_ranking` VALUES (48, '联想（Lenovo）A601 USB分线器 高速3.0接口转换器 4口USB扩展坞 转接头 HUB集线器 USB延长线 笔记本 台式机/0.25米', '46.70', '100005457634', '0%');
INSERT INTO `jd_ranking` VALUES (49, '联想 USB3.0转千兆网口转RJ45有线网卡扩展坞转接头笔记本电脑USB3.0*3分线器 小新拯救者拓展坞 F1-U03', '99.00', '100018111588', '0%');
INSERT INTO `jd_ranking` VALUES (50, '绿联（UGREEN）USB分线器2.0 4口HUB集线器扩展坞 笔记本电脑一拖四转换器多接口延长线带电源口 黑1米 20277', '25.90', '100004806754', '0%');
INSERT INTO `jd_ranking` VALUES (51, '得力(deli)耐磨办公游戏鼠标垫 办公用品 黑色3691', '9.90', '1013999', '0%');
INSERT INTO `jd_ranking` VALUES (52, '赛睿 (SteelSeries) QcK Heavy M 黑色 6mm厚度 FPS游戏专用 移动定位精准 电竞游戏鼠标垫', '69.00', '265102', '0%');
INSERT INTO `jd_ranking` VALUES (53, '高漫M6数位板可连接手机手绘板 电脑绘图板电子绘画板智能手写板', '168.00', '48354769095', '0%');
INSERT INTO `jd_ranking` VALUES (54, '绿联 M.2 NVMe移动硬盘盒 Type-C3.1接口SSD固态硬盘盒子笔记本电脑M2全铝外置盒  10902', '119.00', '100015801178', '0%');
INSERT INTO `jd_ranking` VALUES (55, '灵蛇（LINGSHE）鼠标垫 家用办公游戏鼠标垫 办公鼠标垫小号 精密包边防滑可水洗P01黑色', '3.90', '4062692', '0%');
INSERT INTO `jd_ranking` VALUES (56, '得力(deli) 快捷键鼠标垫 800*300*3mm 快捷键大全大号鼠标垫 锁边加厚办公电脑键盘桌垫 83004', '29.90', '100016323972', '0%');
INSERT INTO `jd_ranking` VALUES (57, '联想（Lenovo）移动硬盘盒 2.5英寸USB3.0 SATA串口笔记本电脑外置壳固态机械ssd硬盘盒 K01-A', '35.90', '100021539104', '0%');
INSERT INTO `jd_ranking` VALUES (58, '绿联（UGREEN）移动硬盘盒2.5英寸 USB3.0机械固态SSD外置硬盘盒壳 SATA串口笔记本电脑外接硬盘盒子', '49.00', '100006491672', '0%');
INSERT INTO `jd_ranking` VALUES (59, '绿联 移动硬盘盒底座2.5/3.5英寸 USB3.0台式机笔记本电脑外接SATA串口机械固态ssd硬盘盒子外置硬盘座50740', '99.00', '100014961322', '0%');
INSERT INTO `jd_ranking` VALUES (60, '绿联（UGREEN）硬盘盒底座2.5/3.5英寸 USB3.0台式笔记本SATA串口机械固态ssd外置硬盘盒子 双盘位50742', '149.00', '100014988528', '0%');

SET FOREIGN_KEY_CHECKS = 1;
