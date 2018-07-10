def cte_deletes_duplicates():
    return """WITH min_id AS
                (SELECT sale_id, MIN(id) AS
                minimum_id FROM sales GROUP BY sale_id)
                DELETE FROM sales
                WHERE id NOT IN (SELECT minimum_id FROM min_id);"""

def correct_above_avg_sales():
    return """WITH average_sales AS
                (SELECT AVG(amount) AS avg_sales FROM sales)
                SELECT city, date_of_sale, amount FROM sales
                JOIN locations ON locations.id = location_id
                WHERE amount > (SELECT * FROM average_sales);"""
