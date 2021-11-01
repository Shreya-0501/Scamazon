
# Scamazon

## Overview
Scamazon is a mobile app that uses HTML and CSS for frontend and SQL for backend, it is a tool that connects customers and vendors for easy buying and selling, where customers can buy products in one click!

- Website consists of mainly 2 divisions
  - Customer:
    - Just display of orders
    - Search for new products

  - Vendor:
    - Your Items:
      - Add items
      - Display items

## Frontend design

- First page : choose
	- **Vendor Login**
		- Username
		- Password

	- **Customer login**
		- Username
		- Password

### Vendor UI

Pages: 
- **Your Items**: (Default)
	- Lists your items
		- Add new Prod 

- **Add Items**:
	- Fill the details of Prod table

### Customer UI

Pages:
- **Search**: (Default)
	- Search bar
	- Filters ( color, brand, vendor, price range )
	- Sort:
		- Price ASC
		- Price DSC
		- Relevance : Default

- **Your orders**
	- Lists your orders

**DB connectors**
Mysql.connector

## Backend design

-  Databases with pictures (SQL)
	- Vendors
		- Can upload pictures, prod description
		- Your Items

	- Customers
		- Can search (with queries)
		- Customers can see prev/your orders
	
### Tables

- Vendor table
	- Vendor ID -> PK
	- Username
	- Password

- Prod table
	- Prod ID
	- **Prod photo**
	- Prod price
	- Prod name (1st  priority)
	- Prod category
		- Sports
		- Electronics
		- Kitchen
		- Clothing
		- Books
	- Vendor ID -> FK
	- Tags (2nd Priority)

- Customer Table
	- Customer ID -> PK
	- Username
	- Password

- Order History
	- Order ID -> PK
	- Customer ID -> FK
	- Prod ID -> FK
	- Date






