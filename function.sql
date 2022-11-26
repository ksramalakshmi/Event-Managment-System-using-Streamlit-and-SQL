DELIMITER $$
CREATE FUNCTION TOTAL_SALES(total INTEGER)
RETURNS INTEGER
DETERMINISTIC
BEGIN
	RETURN (TOTAL * 400);
END
$$
DELIMITER ;	

SELECT EVENT_NAME, TOTAL_SALES(TABLE4.TOTAL_ATTENDEES) FROM TABLE4;