-- Ollivander's Inventory
-- https://www.hackerrank.com/challenges/harry-potter-and-wands/problem

SELECT
(
    SELECT w1.id FROM wands AS w1
    inner JOIN wands_property AS p1
    ON w1.code = p1.code
    WHERE p1.age=wands_property.age 
    AND w1.coins_needed=min(wands.coins_needed)
),

wands_property.age, min(wands.coins_needed), wands.power

FROM wands

INNER JOIN wands_property
ON wands.code = wands_property.code

WHERE wands_property.is_evil=0

GROUP BY wands.power DESC, wands_property.age DESC