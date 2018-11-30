def cte_deletes_duplicates():
    return """WITH duplicates AS ( SELECT MIN(id) AS minimum_id  FROM sales GROUP BY sale_id)
    DELETE FROM sales  WHERE  id NOT IN (SELECT minimum_id FROM duplicates);
    """

def correct_above_avg_sales():
    return """ WITH average_sales AS ( SELECT AVG(amount) AS avg_sale_calc FROM sales)
    SELECT locations.city, sales.date_of_sale,sales.amount FROM sales JOIN locations on locations.id = sales.location_id WHERE amount > (SELECT avg_sale_calc from average_sales);
    """
