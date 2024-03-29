SET @hour := -1;

SELECT
    (@hour := @hour + 1) AS HOUR, 
    (
        SELECT COUNT(DATETIME) AS COUNT
        FROM ANIMAL_OUTS 
        WHERE HOUR(DATETIME) = @hour 
    )
FROM ANIMAL_OUTS
WHERE @hour < 23;