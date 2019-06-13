def cte_deletes_duplicates():
    return """WITH minimums AS (SELECT MIN(id) AS minimum_id FROM sales GROUP BY sale_id) DELETE FROM sales WHERE sales.id not in (SELECT minimum_id FROM minimums);"""

def correct_above_avg_sales():
    return """ WITH average_sales AS (SELECT AVG(amount) as average FROM sales) SELECT locations.city, sales.date_of_sale, sales.amount FROM sales JOIN locations ON sales.location_id = locations.id WHERE amount > (SELECT average FROM average_sales);


    """
