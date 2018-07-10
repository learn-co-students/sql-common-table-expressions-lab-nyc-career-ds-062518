def cte_deletes_duplicates():
    return """WITH min_id AS
    (SELECT sale_id, MIN(id) as minimum_id FROM sales GROUP BY sale_id)
    DELETE FROM sales
    WHERE id NOT IN (SELECT minimum_id FROM min_id);"""

def correct_above_avg_sales():
    return """WITH average_sales
    AS (SELECT AVG(amount) FROM sales)
    SELECT locations.city, sales.date_of_sale, sales.amount
    FROM locations JOIN sales ON
    locations.id = sales.location_id
    WHERE sales.amount > (SELECT * FROM average_sales);
    """
