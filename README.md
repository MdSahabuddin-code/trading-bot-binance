This project follows a modular architecture separating CLI, validation, and API layers for maintainability.



## Sample Output
### Market Order

--- ORDER REQUEST ---
BTCUSDT BUY MARKET 0.01 None

--- ORDER SUCCESS ---
Order ID: 13096967235
Status: FILLED
Executed Qty: 0.0100
Avg Price: 78532.600000


### Limit Order
--- ORDER REQUEST ---
BTCUSDT SELL LIMIT 0.01 90000

--- ORDER SUCCESS ---
Order ID: 13096970000
Status: NEW
Executed Qty: 0.0000
Avg Price: 0.00
