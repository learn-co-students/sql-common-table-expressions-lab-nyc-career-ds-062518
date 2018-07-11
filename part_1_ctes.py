def use_cte_to_determine_average_sale():
    return """
    WITH average_sales AS (
    SELECT AVG(amount) FROM sales)
    SELECT * from average_sales;
    """

def select_all_above_average_sales():
    return """
    WITH average_sales AS (SELECT AVG(amount) AS benchmark FROM sales)
    SELECT * from sales WHERE amount > (SELECT benchmark FROM average_sales);
    """
