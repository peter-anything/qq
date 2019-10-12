CREATE TABLE IF NOT EXISTS `User`(
   `id` INT AUTO_INCREMENT,
   `qq_id` INT,
   `username` VARCHAR(64),
   `nickname` VARCHAR(64),
   `password` VARCHAR(128),
   `mobile` VARCHAR(16),
   `email` VARCHAR(64),
   `avatar` VARCHAR(128),
   `address` VARCHAR(128),
   `age` TINYINT(3),
   `sex` TINYINT(1),
   `created_at` TIMESTAMP,
   `updated_at` TIMESTAMP,
   PRIMARY KEY ( `id` )
);