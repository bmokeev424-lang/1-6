
SELECT * FROM maintenance_request ORDER BY priority;

SELECT status, COUNT(*) FROM maintenance_request GROUP BY status;

SELECT * FROM equipment
WHERE id NOT IN (
    SELECT equipment_id FROM maintenance_request
    WHERE status IN ('new', 'in_progress')
);

SELECT equipment_id, COUNT(*) AS cnt
FROM maintenance_request
GROUP BY equipment_id
ORDER BY cnt DESC
LIMIT 5;