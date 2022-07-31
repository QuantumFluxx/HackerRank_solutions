-- Draw The Triangle 2
-- https://www.hackerrank.com/challenges/draw-the-triangle-2/problem

SELECT RPAD('*', 2 * LEVEL - 1, ' *')
FROM DUAL CONNECT BY LEVEL <= 20;