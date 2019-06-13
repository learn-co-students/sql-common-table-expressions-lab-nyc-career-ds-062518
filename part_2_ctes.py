def cte_deletes_duplicates():
    return """WITH dupe AS
                (SELECT sale_id, min(id) as min FROM sales GROUP BY sale_id)
                DELETE FROM sales
                WHERE id NOT IN (SELECT min from dupe);"""

def correct_above_avg_sales():
    return """WITH average_sales AS
     (SELECT AVG(amount) as avg FROM sales)
     SELECT locations.city, sales.date_of_sale, sales.amount FROM sales JOIN locations
     ON locations.id = sales.location_id
     WHERE amount > (SELECT avg from average_sales);"""
