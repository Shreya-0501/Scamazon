
# Scamazon

## Overview
Scamazon is a mobile app that uses HTML and CSS for frontend and SQL for backend, it is a tool that connects customers and vendors for easy buying and selling, where customers can buy products in one click!

- Website consists of mainly 2 divisions
  - Customer:
    - Display of orders
    - Search for new products

  - Vendor:
    - Your Items:
      - Add items
      - Display items


- Refer to the UI_connect_backend.png document for the diagram that shows how UI is connected to the backend using http requests and how backend connects to the db using Mysql.connector

- Refer to website_tree.png for flow of the website

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

- Refer to the flowchart.pptx, website_tree.png to see the flow of frontend


## Backend

-  Databases with pictures (SQL)
	- Vendors
		- Can upload pictures, prod description
		- Your Items

	- Customers
		- Can search (with queries)
		- Customers can see prev/your orders
	
### API end points

- Verification of username and password:
	- Input: Username and password
	- Output : Proceeds to the next page if all the details are valid, else displays the same page with error
	- Function : Verifies the username and password with the details in database

- Search for products:
	- Input: product name/tag 
	- Output : All the products related to the search query are displayed
	- Function : Searches for the product in the database that match with the search query

- Add a new product (vendor) : 
	- Input: All details of the product and its picture
	- Output : The new product is added to My catalog (vendor)
	- Function : Adds the new product to the database

- Add a new Customer/Vendor : 
	- Input: All details of the customer/vendor
	- Output : If all the details are valid (username is unique..) proceeds to the login page, else displays the same page with error messsage
	- Function : Adds the new customer/vendor to the database

**DB connectors**

Mysql.connector

## Database

### Tables

- Vendor table

Stores the Username, password, and the Vendor ID of the vendor

	- Vendor ID -> PK
	- Username
	- Password

- Prod table

Has the details of all the products in the database

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
 
Stores the Username, password, and the Customer ID of the customer
	
	- Customer ID -> PK
	- Username
	- Password

- Order History

Has details of all previous orders of the customer

	- Order ID -> PK
	- Customer ID -> FK
	- Prod ID -> FK
	- Date






