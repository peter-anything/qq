CREATE TABLE IF NOT EXISTS `Message`(
   `id` INT AUTO_INCREMENT,
   `message` VARCHAR(1024),
   `created_at` TIMESTAMP,
   `updated_at` TIMESTAMP,
   PRIMARY KEY ( `id` )
);