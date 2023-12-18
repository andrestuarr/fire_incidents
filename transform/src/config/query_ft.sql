CREATE OR REPLACE TABLE @final_table AS
    SELECT *, CONCAT(SUBSTR(incident_date, 1, 4),SUBSTR(incident_date, 6,2)) as codmes 
    FROM @source_table