-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema ItemDatabase
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ItemDatabase
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ItemDatabase` DEFAULT CHARACTER SET utf8 ;
USE `ItemDatabase` ;

-- -----------------------------------------------------
-- Table `ItemDatabase`.`Item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ItemDatabase`.`Item` (
  `ITEM_ID` INT UNSIGNED NOT NULL,
  `Category` VARCHAR(45) NOT NULL,
  `Color` VARCHAR(45) NOT NULL,
  `Size` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ITEM_ID`),
  UNIQUE INDEX `ITEM_ID_UNIQUE` (`ITEM_ID` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ItemDatabase`.`Person`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ItemDatabase`.`Person` (
  `email` VARCHAR(45) NOT NULL,
  `Given_Name` VARCHAR(45) NOT NULL,
  `Surname` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`email`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ItemDatabase`.`Person_has_Item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ItemDatabase`.`Person_has_Item` (
  `Status` VARCHAR(6) NOT NULL,
  `Person_email` VARCHAR(45) NOT NULL,
  `Person_Has_ID` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`Person_email`, `Person_Has_ID`),
  INDEX `fk_Person_has_Item_Person1_idx` (`Person_email` ASC) VISIBLE,
  INDEX `fk_Person_has_Item_Item1_idx` (`Person_Has_ID` ASC) VISIBLE,
  CONSTRAINT `fk_Person_has_Item_Person1`
    FOREIGN KEY (`Person_email`)
    REFERENCES `ItemDatabase`.`Person` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Person_has_Item_Item1`
    FOREIGN KEY (`Person_Has_ID`)
    REFERENCES `ItemDatabase`.`Item` (`ITEM_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ItemDatabase`.`Lost_and_Found`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ItemDatabase`.`Lost_and_Found` (
  `Specific_ITEM_ID` INT UNSIGNED NOT NULL,
  `Lost_Date` DATE NOT NULL,
  `Last_Seen` MEDIUMTEXT NOT NULL,
  `Claimed` TINYINT NULL,
  `Found_Date` DATE NULL,
  `Found_Location` VARCHAR(45) NULL,
  `Image` VARCHAR(45) NULL,
  `Person_has_Lost_Item` VARCHAR(45) NOT NULL,
  `Person_has_Found_Item` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Specific_ITEM_ID`, `Person_has_Lost_Item`, `Person_has_Found_Item`),
  INDEX `fk_Lost_and_Found_Person_has_Item1_idx` (`Person_has_Lost_Item` ASC) VISIBLE,
  INDEX `fk_Lost_and_Found_Person_has_Item2_idx` (`Person_has_Found_Item` ASC) VISIBLE,
  CONSTRAINT `fk_Lost_and_Found_Person_has_Item1`
    FOREIGN KEY (`Person_has_Lost_Item`)
    REFERENCES `ItemDatabase`.`Person_has_Item` (`Person_email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Lost_and_Found_Person_has_Item2`
    FOREIGN KEY (`Person_has_Found_Item`)
    REFERENCES `ItemDatabase`.`Person_has_Item` (`Person_email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ItemDatabase`.`Earphone`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ItemDatabase`.`Earphone` (
  `Brand` VARCHAR(45) NOT NULL,
  `Earphones_Item_ITEM_ID` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`Earphones_Item_ITEM_ID`),
  CONSTRAINT `fk_Earphone_Item1`
    FOREIGN KEY (`Earphones_Item_ITEM_ID`)
    REFERENCES `ItemDatabase`.`Item` (`ITEM_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ItemDatabase`.`Campus_Card`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ItemDatabase`.`Campus_Card` (
  `Matr_Number` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `CampusCard_Item_ITEM_ID` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`CampusCard_Item_ITEM_ID`),
  CONSTRAINT `fk_Campus_Card_Item1`
    FOREIGN KEY (`CampusCard_Item_ITEM_ID`)
    REFERENCES `ItemDatabase`.`Item` (`ITEM_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ItemDatabase`.`Keys`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ItemDatabase`.`Keys` (
  `Room_Number` VARCHAR(45) NOT NULL,
  `College` VARCHAR(45) NOT NULL,
  `Attached_Item_Description` VARCHAR(75) NULL,
  `Keys_Item_ITEM_ID` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`Keys_Item_ITEM_ID`),
  CONSTRAINT `fk_Keys_Item1`
    FOREIGN KEY (`Keys_Item_ITEM_ID`)
    REFERENCES `ItemDatabase`.`Item` (`ITEM_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ItemDatabase`.`Moderator`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ItemDatabase`.`Moderator` (
  `Person_email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Person_email`),
  CONSTRAINT `fk_Moderator_Person1`
    FOREIGN KEY (`Person_email`)
    REFERENCES `ItemDatabase`.`Person` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ItemDatabase`.`Moderator_Moderates_Lost_and_Found`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ItemDatabase`.`Moderator_Moderates_Lost_and_Found` (
  `Moderator_Person_email` VARCHAR(45) NOT NULL,
  `Lost_and_Found_Specific_ITEM_ID` INT UNSIGNED NOT NULL,
  `Reason` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Moderator_Person_email`, `Lost_and_Found_Specific_ITEM_ID`),
  INDEX `fk_Moderator_has_Lost and Found_Lost and Found1_idx` (`Lost_and_Found_Specific_ITEM_ID` ASC) VISIBLE,
  INDEX `fk_Moderator_has_Lost and Found_Moderator1_idx` (`Moderator_Person_email` ASC) VISIBLE,
  CONSTRAINT `fk_Moderator_has_Lost and Found_Moderator1`
    FOREIGN KEY (`Moderator_Person_email`)
    REFERENCES `ItemDatabase`.`Moderator` (`Person_email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Moderator_has_Lost and Found_Lost and Found1`
    FOREIGN KEY (`Lost_and_Found_Specific_ITEM_ID`)
    REFERENCES `ItemDatabase`.`Lost_and_Found` (`Specific_ITEM_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ItemDatabase`.`Clothes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ItemDatabase`.`Clothes` (
  `Clothes_ITEM_ID` INT UNSIGNED NOT NULL,
  `Color` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Clothes_ITEM_ID`),
  CONSTRAINT `fk_Clothes_Item1`
    FOREIGN KEY (`Clothes_ITEM_ID`)
    REFERENCES `ItemDatabase`.`Item` (`ITEM_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ItemDatabase`.`Pant`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ItemDatabase`.`Pant` (
  `Pant_Type` VARCHAR(45) NOT NULL,
  `Clothes_Pant_ITEM_ID` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`Clothes_Pant_ITEM_ID`),
  CONSTRAINT `fk_Pant_Clothes1`
    FOREIGN KEY (`Clothes_Pant_ITEM_ID`)
    REFERENCES `ItemDatabase`.`Clothes` (`Clothes_ITEM_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ItemDatabase`.`Shirt`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ItemDatabase`.`Shirt` (
  `Shirt_Type` VARCHAR(45) NOT NULL,
  `Clothes_Shirt_ITEM_ID` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`Clothes_Shirt_ITEM_ID`),
  CONSTRAINT `fk_Shirt_Clothes1`
    FOREIGN KEY (`Clothes_Shirt_ITEM_ID`)
    REFERENCES `ItemDatabase`.`Clothes` (`Clothes_ITEM_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
