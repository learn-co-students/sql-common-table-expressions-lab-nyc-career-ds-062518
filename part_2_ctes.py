def cte_deletes_duplicates():
    return """WITH minimum_id AS(SELECT MIN(id) FROM sales GROUP BY sale_id) DELETE FROM sales WHERE id NOT IN minimum_id;"""

def correct_above_avg_sales():
    #cte_deletes_duplicates()
    return """SELECT locations.city, sales.date_of_sale, sales.amount FROM sales INNER JOIN locations ON sales.location_id = locations.id WHERE sales.amount > (SELECT AVG(amount) FROM sales);"""
