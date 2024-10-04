-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
-- SELECT
--     COUNT(*) AS a
-- FROM
--     assignments
-- WHERE
--     grade == 'A'
-- GROUP BY
--     teacher_id
-- ORDER BY
--     a DESC;
WITH graded_assignments AS (
    SELECT teacher_id, COUNT(*) AS graded_counter
    FROM assignments
    WHERE state == 'GRADED'
    GROUP BY teacher_id
), max_grade_assignments AS (
    SELECT teacher_id
    FROM graded_assignments
    ORDER BY graded_counter DESC
    LIMIT 1
) 
SELECT COUNT(*) AS a
 FROM assignments
 WHERE teacher_id == (SELECT teacher_id from max_grade_assignments) AND grade == 'A';