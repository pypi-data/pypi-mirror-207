# 数据库

```mysql
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for location_boundary
-- ----------------------------
DROP TABLE IF EXISTS `location_boundary`;
CREATE TABLE `location_boundary`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `boundary_list` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '边界线列表',
  `name` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '名称',
  `created_at` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for location_location
-- ----------------------------
DROP TABLE IF EXISTS `location_location`;
CREATE TABLE `location_location`  (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '站名',
  `region_code` bigint(18) NULL DEFAULT NULL COMMENT '区站号',
  `address` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '站址',
  `longitude` decimal(10, 6) NULL DEFAULT NULL COMMENT '经度',
  `latitude` decimal(10, 6) NULL DEFAULT NULL COMMENT '纬度',
  `group_id` int(11) NOT NULL DEFAULT 0 COMMENT '分组ID',
  `user_id` int(11) NOT NULL DEFAULT 0 COMMENT '用户ID',
  `by_user_id` int(11) NOT NULL DEFAULT 0 COMMENT '填报用户ID',
  `updated_at` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0),
  `created_at` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  `is_delete` tinyint(2) NOT NULL COMMENT '是否删除',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `code`(`region_code`) USING BTREE,
  INDEX `lng`(`longitude`) USING BTREE,
  INDEX `lat`(`latitude`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 231 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '气象站信息' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for location_region
-- ----------------------------
DROP TABLE IF EXISTS `location_region`;
CREATE TABLE `location_region`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` bigint(16) NOT NULL COMMENT '行政区划代码',
  `level` int(1) NOT NULL DEFAULT 0 COMMENT '类型: 0国家或者未填写 1-省 直辖市   2-市  3-区县',
  `p_code` bigint(16) NOT NULL DEFAULT 0 COMMENT '父级行政区划代码',
  `name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '名称',
  `is_delete` tinyint(4) NOT NULL DEFAULT 0 COMMENT '0',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `complex_code`(`p_code`, `code`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3222 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;

```

# 使用

1.使用之前注意需要配置redis服务

