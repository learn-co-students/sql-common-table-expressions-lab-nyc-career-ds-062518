def use_cte_to_determine_average_sale():
    return """WITH average_sales AS (SELECT AVG(amount) from sales)
    SELECT * from average_sales;"""

def select_all_above_average_sales():
    return """SELECT * from sales WHERE amount > (SELECT AVG(amount) from sales);"""
