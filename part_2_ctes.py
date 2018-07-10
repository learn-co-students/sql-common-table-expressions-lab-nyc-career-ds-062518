def cte_deletes_duplicates():
    return """
            WITH minimum_id AS (SELECT sale_id, MIN(id) AS min_id FROM sales GROUP BY sale_id)
            DELETE FROM sales WHERE id NOT IN (SELECT min_id FROM minimum_id);
            """

def correct_above_avg_sales():
    return """
            WITH average_sales AS (SELECT AVG(amount) FROM sales)
            SELECT locations.city, sales.date_of_sale, sales.amount FROM sales JOIN locations ON sales.location_id = locations.id WHERE amount > (SELECT * FROM average_sales);
            """
