INSERT INTO @final_table
    SELECT *, CURRENT_DATE() as fecrutina 
    FROM @source_table