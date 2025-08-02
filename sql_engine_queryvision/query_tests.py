from sql_runner import run_query
from tabulate import tabulate

test_queries = [
    "SELECT * FROM Customer LIMIT 5;",
    "SELECT Country, COUNT(*) FROM Customer GROUP BY Country ORDER BY COUNT(*) DESC;",
    "SELECT * FROM Invoice WHERE Total>20;",
    "SELECT * FROM BrokenTable;", #only to trigger an error
]

for i,q in enumerate(test_queries):
    print(f"\n Running Query {i+1}:\n{q}")
    result = run_query(q)

    if hasattr(result, 'to_markdown'):
        print(tabulate(result, headers = 'keys', tablefmt = 'grid'))
    else:
        print(result) #print errors as plain text