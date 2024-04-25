-- Rank country origins of bands by the number of (non-unique) fans
-- and store the result in the 'tmp_res' file
SELECT origin, COUNT(*) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

-- Note: The result will be stored in the 'tmp_res' file.
