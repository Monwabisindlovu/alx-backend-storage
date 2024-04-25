-- SQL script to list all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, (2022 - MIN(formed)) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
GROUP BY band_name
ORDER BY lifespan DESC;

