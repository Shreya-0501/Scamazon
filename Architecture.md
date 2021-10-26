
# Scamazon

- Native app/ mobile app (front end -> kivy/react)
  - Customer:
    - Just display of orders

  - Vendor:
    - Your Items:
      - Icons for delete on each prod
      - Edit prod info on each prod

- Middleware

-  Databases with pictures (SQL)
	- Vendors
		- Can upload pictures, prod description
		- Your Items

	- Customers
		- Can search (with queries)
		- Customers can see prev/your orders

## Tables

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



## Designing UI

- First page : choose
	- Vendor Login
		- Username
		- Password

	- Customer login
		- Username
		- Password

### Vendor UI

Pages: 
- Your Items: Default
	- Lists your items
		- Edit Prod info
		- Delete Prod

- Add Items:
	- Fill the details of Prod table

### Customer UI

Pages:
- Search: (Default)
	- Search bar
	- Filters ( color, brand, vendor, price range )
	- Sort:
		- Price ASC
		- Price DSC
		- Relevance : Default

- Your orders
	- Lists your orders

