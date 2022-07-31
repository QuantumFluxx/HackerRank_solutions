-- Contest Leaderboard
-- https://www.hackerrank.com/challenges/contest-leaderboard/problem

SELECT
  hackers.hacker_id,
  hackers.name,
  SUM(scores.max_score)
FROM
  (
    SELECT
      hacker_id,
      challenge_id,
      MAX(score) AS max_score
    FROM
      submissions
    GROUP BY
      challenge_id,
      hacker_id
  ) AS scores
  INNER JOIN hackers ON scores.hacker_id = hackers.hacker_id
GROUP BY
  hackers.hacker_id,
  hackers.name
HAVING
  sum(scores.max_score) > 0
ORDER BY
  SUM(scores.max_score) DESC,
  hackers.hacker_id ASC;
