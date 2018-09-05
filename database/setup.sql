CREATE SCHEMA `pixel`
  DEFAULT CHARACTER SET utf8
  COLLATE utf8_unicode_ci;

CREATE TABLE `pixel`.`events` (
  `id`         INT          NOT NULL AUTO_INCREMENT,
  `event_name` VARCHAR(255) NOT NULL,
  `timestamp`  TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `client`     VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC)
);

ALTER TABLE `pixel`.`events`
  ADD COLUMN `value` VARCHAR(255) NULL
  AFTER `client`;

ALTER TABLE `pixel`.`events`
  ADD COLUMN `ip` VARCHAR(255) NULL
  AFTER `value`;
