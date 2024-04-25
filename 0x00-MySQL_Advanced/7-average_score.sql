-- Create Stored Procedure
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_count INT;

    -- Calculate total score and count of corrections for the user
    SELECT SUM(score), COUNT(*) INTO total_score, total_count
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate average score and update user's average_score attribute
    IF total_count > 0 THEN
        UPDATE users
        SET average_score = total_score / total_count
        WHERE id = user_id;
    END IF;
END;
//
DELIMITER ;

