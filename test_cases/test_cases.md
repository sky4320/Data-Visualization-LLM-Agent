# LLM Test Scenarios for SQL Generation

## Happy Path
- **Prompt:** Show 5 customers' name.
- **Expected SQL:** SELECT FirstName, LastName FROM Customer LIMIT 5;
- **Result:** Passed.

!(image/Happy.png)

## Complex Scenario
- **Prompt:** Find the names of customers who have spent more than $10 total.
- **Expected SQL:** SELECT FirstName, LastName
                    FROM Customer
                    WHERE CustomerId IN (
                        SELECT CustomerId
                        FROM Invoice
                        GROUP BY CustomerId
                        HAVING SUM(Total) > Id
                    )
- **Result** Passed. The generated SQL matches the expected query and correctly filters customers who spent more than $10 in total.

!(image/Complex.png)

## Negative Scenario
- **Prompt:** Displaying the rating for each album.
- **Observation:** The LLM returned a query that attempted to calculate "rating" using invoice prices, even though there is no `Rating` column in the schema and no defined logic for calculating it.
- **Result:** Passed.
- **Recommendation:** Prompt should be reworded with clear criteria or definitions for "rating", or be avoided unless such a metric is explicitly available in the dataset.

!(image/Negative.png)




