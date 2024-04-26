-- Query to rank country origins of bands by the number of (non-unique) fans
SELECT origin, COUNT(*) as nb_fans
FROM bands
GROUP BY origin
ORDER BY nb_fans DESC;

