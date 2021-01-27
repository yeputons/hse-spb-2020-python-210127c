def solve(table_orders, table_customers):
    pass
    

"""
OrderID,CustomerName,OrderDate
10308,Ana Trujillo Emparedados y helados,1996-09-18
"""
print(solve(
"""
+---------+------------+------------+
| OrderID | CustomerID | OrderDate  |
| 10308   | 2          | 1996-09-18 |
| 10309   | 37         | 1996-09-19 |
| 10310   | 77         | 1996-09-20 |
+---------+------------+------------+
""",
"""
+------------+-------------------------------------+----------------+---------+
| CustomerID |  CustomerName                       | ContactName    | Country |
| 1          |  Alfreds Futterkiste                | Maria Anders   | Germany |
| 2          |  Ana Trujillo Emparedados y helados | Ana Trujillo   | Mexico  |
| 3          |  Antonio Moreno Taquería            | Antonio Moreno | Mexico  |
+------------+-------------------------------------+----------------+---------+
"""))
