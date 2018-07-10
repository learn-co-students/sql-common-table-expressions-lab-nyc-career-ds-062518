def cte_deletes_duplicates():
    return """WITH delete_dup AS (SELECT min(sale_id) AS min_id FROM sales
        GROUP BY sale_id)
        DELETE from sales WHERE sales.id not in (SELECT min_id FROM delete_dup);
            """

def correct_above_avg_sales():
    return """WITH average_sales AS (SELECT AVG(amount) As avg_amount FROM sales)
            SELECT locations.city, sales.date_of_sale, sales.amount FROM sales
            JOIN locations ON locations.id = sales.location_id
            WHERE amount > (SELECT avg_amount FROM average_sales);"""
