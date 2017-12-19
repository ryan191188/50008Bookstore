DELIMITER $$
CREATE PROCEDURE check_feedback_score(IN score int(11))
BEGIN
    IF score < 0 OR score > 10 THEN
		SIGNAL SQLSTATE '45001'
			SET MESSAGE_TEXT = 'check constraint on myapp_feedback.score failed';
    END IF;
END$$

DELIMITER ;

-- before insert
DELIMITER $$
CREATE TRIGGER feedback_before_insert BEFORE INSERT ON myapp_feedback
FOR EACH ROW
BEGIN
    CALL check_feedback_score(new.score);
END$$   

DELIMITER ;

-- before update
DELIMITER $$
CREATE TRIGGER feedback_before_update BEFORE UPDATE ON myapp_feedback
FOR EACH ROW
BEGIN
    CALL check_feedback_score(new.score);
END$$
   
DELIMITER ;