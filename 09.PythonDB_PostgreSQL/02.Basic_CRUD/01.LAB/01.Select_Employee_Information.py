SELECT
	id,
	CONCAT(first_name, ' ', last_name) as "Full name",
	job_title as "Job title"
FROM employees;