/*
 Navicat Premium Data Transfer

 Source Server         : phpmystudy
 Source Server Type    : MySQL
 Source Server Version : 50726
 Source Host           : localhost:3306

 Target Server Type    : MySQL
 Target Server Version : 50726
 File Encoding         : 65001

 Date: 27/04/2021 11:57:13
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `admin_admin_log`;
CREATE TABLE `admin_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `method` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `uid` int(11) NULL DEFAULT NULL,
  `url` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `desc` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL,
  `ip` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `user_agent` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL,
  `create_time` datetime(0) NULL DEFAULT NULL,
  `success` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1267 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;


-- ----------------------------
-- Table structure for admin_measure_data
-- ----------------------------
DROP TABLE IF EXISTS `admin_measure_data`;
CREATE TABLE `admin_measure_data`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `coord_xyz` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `measure_address` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `measure_status` int(11) NULL DEFAULT NULL,
  `measure_info` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `create_time` datetime(0) NULL DEFAULT NULL,
  `update_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;


-- ----------------------------
-- Table structure for admin_photo
-- ----------------------------
DROP TABLE IF EXISTS `admin_photo`;
CREATE TABLE `admin_photo`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `measure_data_id` int(11),
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `href` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL,
  `mime` char(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `size` char(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `shape` char(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `create_time` datetime(0) NULL DEFAULT NULL,
  `update_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin_photo
-- ----------------------------
--  INSERT INTO `admin_photo` VALUES (
    --  3, 'name.png', '', 'image/png', '2204', '2021-03-19 18:53:02');
--  INSERT INTO `admin_photo` VALUES (
    --  17, 'name.jpg', '', 'image/png', '94211', '2021-04-01 23:39:41');


-- ----------------------------
-- Table structure for admin_detection_data
-- ----------------------------
DROP TABLE IF EXISTS `admin_detection_data`;
CREATE TABLE `admin_detection_data`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `photo_id` int(11),
  `result_str` varchar(512) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `create_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;



-- ----------------------------
-- Table structure for admin_power
-- ----------------------------
DROP TABLE IF EXISTS `admin_power`;
CREATE TABLE `admin_power`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '权限编号',
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '权限名称',
  `type` varchar(1) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '权限类型',
  `code` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '权限标识',
  `url` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '权限路径',
  `parent_id` varchar(19) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '父类编号',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `enable` int(11) NULL DEFAULT NULL COMMENT '是否开启',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 48 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin_power
-- ----------------------------

INSERT INTO `admin_power` VALUES (
    3,  '用户管理', '1', 'admin:user:main',   '/admin/user/',  '3',  NULL, NULL, 1);
INSERT INTO `admin_power` VALUES (
    22, '用户增加', '2', 'admin:user:add',    '',              '3',  NULL, NULL, 1);
INSERT INTO `admin_power` VALUES (
    23, '用户编辑', '2', 'admin:user:edit',   '',              '3',  NULL, NULL, 1);
INSERT INTO `admin_power` VALUES (
    24, '用户删除', '2', 'admin:user:remove', '',              '3',  NULL, NULL, 1);


INSERT INTO `admin_power` VALUES (
    4,  '权限管理', '1', 'admin:power:main',  '/admin/power/', '4',  NULL, NULL, 1);
INSERT INTO `admin_power` VALUES (
    21, '权限增加', '2', 'admin:power:add',   '',              '4',  NULL, NULL, 1);
INSERT INTO `admin_power` VALUES (
    25, '权限编辑', '2', 'admin:power:edit',  '',              '4',  NULL, NULL, 1);
INSERT INTO `admin_power` VALUES (
    26, '用户删除', '2', 'admin:power:remove', '',             '4',  NULL, NULL, 1);


INSERT INTO `admin_power` VALUES (
    9,  '角色管理', '1', 'admin:role:main',   '/admin/role/',  '9',  NULL, NULL, 1);
INSERT INTO `admin_power` VALUES (
    27, '用户增加', '2', 'admin:role:add',    '',              '9',  NULL, NULL, 1);
INSERT INTO `admin_power` VALUES (
    28, '角色编辑', '2', 'admin:role:edit',   '',              '9',  NULL, NULL, 1);
INSERT INTO `admin_power` VALUES (
    29, '角色删除', '2', 'admin:role:remove', '',              '9',  NULL, NULL, 1);
INSERT INTO `admin_power` VALUES (
    30, '角色授权', '2', 'admin:role:power',  '',              '9',  NULL, NULL, 1);


INSERT INTO `admin_power` VALUES (
    13, '日志管理', '1', 'admin:log:index',   '/admin/log/',   '13',  NULL, NULL, 1);


INSERT INTO `admin_power` VALUES (
    18, '图片上传', '1',  'admin:file:main',  '/admin/file/',  '18', NULL, NULL, 1);
INSERT INTO `admin_power` VALUES (
    31, '图片增加', '2', 'admin:file:add',    '',              '18', NULL, NULL, 1);
INSERT INTO `admin_power` VALUES (
    32, '图片删除', '2', 'admin:file:delete', '',              '18', NULL, NULL, 1);


--  INSERT INTO `admin_power` VALUES (
    --  44, '数据字典', '1', 'admin:dict:main', '/admin/dict',     '44',  NULL, NULL, 1);
--  INSERT INTO `admin_power` VALUES (
    --  45, '字典增加', '2', 'admin:dict:add',  '',                '44', NULL, NULL, 1);
--  INSERT INTO `admin_power` VALUES (
    --  46, '字典修改', '2', 'admin:dict:edit', '',                '44', NULL, NULL, 1);
--  INSERT INTO `admin_power` VALUES (
    --  47, '字典删除', '2', 'admin:dict:remove', '',              '44', NULL, NULL, 1);

-- ----------------------------
-- Table structure for admin_role
-- ----------------------------
DROP TABLE IF EXISTS `admin_role`;
CREATE TABLE `admin_role`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '角色ID',
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '角色名称',
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '角色标识',
  `remark` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '备注',
  `details` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '详情',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `enable` int(11) NULL DEFAULT NULL COMMENT '是否启用',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin_role
-- ----------------------------
INSERT INTO `admin_role` VALUES (
    1, '管理员', 'admin', NULL, 'admin', NULL, NULL, 1);
INSERT INTO `admin_role` VALUES (
    2, '普通用户', 'common', NULL, 'read only', NULL, NULL, 1);

-- ----------------------------
-- Table structure for admin_role_power
-- ----------------------------
DROP TABLE IF EXISTS `admin_role_power`;
CREATE TABLE `admin_role_power`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '标识',
  `power_id` int(11) NULL DEFAULT NULL COMMENT '用户编号',
  `role_id` int(11) NULL DEFAULT NULL COMMENT '角色编号',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `power_id`(`power_id`) USING BTREE,
  INDEX `role_id`(`role_id`) USING BTREE,
  CONSTRAINT `admin_role_power_ibfk_1` FOREIGN KEY (`power_id`) REFERENCES `admin_power` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `admin_role_power_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `admin_role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 212 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin_role_power
-- ----------------------------

INSERT INTO `admin_role_power` VALUES (164, 13, 2);
INSERT INTO `admin_role_power` VALUES (193, 13, 1);

INSERT INTO `admin_role_power` VALUES (160, 3, 2);
INSERT INTO `admin_role_power` VALUES (189, 3, 1);
INSERT INTO `admin_role_power` VALUES (197, 22, 1);
INSERT INTO `admin_role_power` VALUES (198, 23, 1);
INSERT INTO `admin_role_power` VALUES (199, 24, 1);

INSERT INTO `admin_role_power` VALUES (161, 4, 2);
INSERT INTO `admin_role_power` VALUES (190, 4, 1);
INSERT INTO `admin_role_power` VALUES (196, 21, 1);
INSERT INTO `admin_role_power` VALUES (200, 25, 1);
INSERT INTO `admin_role_power` VALUES (201, 26, 1);

INSERT INTO `admin_role_power` VALUES (162, 9, 2);
INSERT INTO `admin_role_power` VALUES (191, 9, 1);
INSERT INTO `admin_role_power` VALUES (202, 27, 1);
INSERT INTO `admin_role_power` VALUES (203, 28, 1);
INSERT INTO `admin_role_power` VALUES (204, 29, 1);
INSERT INTO `admin_role_power` VALUES (205, 30, 1);

INSERT INTO `admin_role_power` VALUES (166, 18, 2);
INSERT INTO `admin_role_power` VALUES (195, 18, 1);
INSERT INTO `admin_role_power` VALUES (206, 31, 1);
INSERT INTO `admin_role_power` VALUES (207, 32, 1);

-- ----------------------------
-- Table structure for admin_user
-- ----------------------------
DROP TABLE IF EXISTS `admin_user`;
CREATE TABLE `admin_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `username` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '用户名',
  `password_hash` varchar(128) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '哈希密码',
  `create_at` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_at` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `enable` int(11) NULL DEFAULT NULL COMMENT '启用',
  `realname` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '真实名字',
  `remark` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '备注',
  `avatar` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '头像',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin_user
-- ----------------------------
INSERT INTO `admin_user` VALUES (
    1, 'admin',
    'pbkdf2:sha256:150000$d6llBPnx$a745958a0eb53726425d6bd0e6017ebd88ba7d104f138ccc98bd62d53ed968df',
    '2021-10-30 03:35:00', '2021-10-30 03:35:00',
    1, '超级管理', '', '');

-- ----------------------------
-- Table structure for admin_user_role
-- ----------------------------
DROP TABLE IF EXISTS `admin_user_role`;
CREATE TABLE `admin_user_role`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '标识',
  `user_id` int(11) NULL DEFAULT NULL COMMENT '用户编号',
  `role_id` int(11) NULL DEFAULT NULL COMMENT '角色编号',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `role_id`(`role_id`) USING BTREE,
  INDEX `user_id`(`user_id`) USING BTREE,
  CONSTRAINT `admin_user_role_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `admin_role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `admin_user_role_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `admin_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin_user_role
-- ----------------------------
INSERT INTO `admin_user_role` VALUES (14, 1, 1);

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
/* DROP TABLE IF EXISTS `alembic_version`; */
/* CREATE TABLE `alembic_version`  ( */
  /* `version_num` varchar(32) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL, */
  /* PRIMARY KEY (`version_num`) USING BTREE */
/* ) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = DYNAMIC; */

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
--  INSERT INTO `alembic_version` VALUES ('ec21e19825ff');

SET FOREIGN_KEY_CHECKS = 1;

