DELIMITER $$
CREATE PROCEDURE check_format(IN format char(9))
BEGIN
    IF format <> 'paperback' OR format <> 'hardcover' THEN
		SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'check constraint on myapp_book.format failed';
    END IF;
END$$

DELIMITER ;

-- before insert
DELIMITER $$
CREATE TRIGGER book_before_insert BEFORE INSERT ON myapp_book
FOR EACH ROW
BEGIN
    CALL check_format(new.format);
END$$   

DELIMITER ; 

-- before update
DELIMITER $$
CREATE TRIGGER book_before_update BEFORE UPDATE ON myapp_book
FOR EACH ROW
BEGIN
    CALL check_format(new.format);
END$$
   
DELIMITER ;