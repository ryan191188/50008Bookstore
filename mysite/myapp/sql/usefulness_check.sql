DELIMITER $$
CREATE PROCEDURE check_usefulness(IN score int(11), IN loginName varchar(64), IN userBeingRated VARCHAR(64))
BEGIN
    IF score < 0 OR score > 3 THEN
		SIGNAL SQLSTATE '45002'
			SET MESSAGE_TEXT = 'check constraint on myapp_usefulness.score failed';
    END IF;
    
    IF loginName = userBeingRated THEN
		SIGNAL SQLSTATE '45003'
			SET MESSAGE_TEXT = 'check constraint on myapp_usefulness.loginName/userBeingRated failed';
    END IF;
END$$

DELIMITER ;

-- before insert
DELIMITER $$
CREATE TRIGGER usefulness_before_insert BEFORE INSERT ON myapp_usefulness
FOR EACH ROW
BEGIN
    CALL check_usefulness(new.score, new.loginName, new.userBeingRated);
END$$   

DELIMITER ;

-- before update
DELIMITER $$
CREATE TRIGGER usefulness_before_update BEFORE UPDATE ON myapp_usefulness
FOR EACH ROW
BEGIN
    CALL check_usefulness(new.score, new.loginName, new.userBeingRated);
END$$
   
DELIMITER ;

########error score shld be > 2#########