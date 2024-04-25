-- Create a stored procedure ComputeAverageScoreForUser
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN p_user_id INT
)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_projects INT;

    -- Calculate the total score and total number of projects for the user
    SELECT SUM(score), COUNT(DISTINCT project_id)
    INTO total_score, total_projects
    FROM corrections
    WHERE user_id = p_user_id;

    -- Calculate the average score and update the users table
    IF total_projects > 0 THEN
        UPDATE users
        SET average_score = total_score / total_projects
        WHERE id = p_user_id;
    ELSE
        UPDATE users
        SET average_score = 0
        WHERE id = p_user_id;
    END IF;
END;
//
DELIMITER ;

