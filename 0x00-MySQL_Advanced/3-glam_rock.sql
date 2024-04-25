-- and display the band_name and lifespan (in years until 2022)
SELECT
    band_name,
    IFNULL(YEAR(2022) - CAST(SUBSTRING_INDEX(splitted, '-', 1) AS UNSIGNED), 0) AS lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', styles) > 0
ORDER BY lifespan DESC, band_name;
