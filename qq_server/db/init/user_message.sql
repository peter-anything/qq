CREATE TABLE IF NOT EXISTS `UserMessage`(
   `user_id` INT,
   `message_id` INT,
   `created_at` TIMESTAMP,
   `updated_at` TIMESTAMP,
   PRIMARY KEY (`user_id`, `message_id`)
);