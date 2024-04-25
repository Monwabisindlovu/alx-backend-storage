-- Create a temporary table to store the counts of fans per country
CREATE TEMPORARY TABLE fan_counts AS
SELECT origin, COUNT(*) AS nb_fans
FROM metal_bands
GROUP BY origin;

-- Select the country origins and their corresponding fan counts, ordered by fan count
SELECT origin, nb_fans
FROM fan_counts
ORDER BY nb_fans DESC;

