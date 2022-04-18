## Requirements

### Functional Requirements
- The user should be able to search for specific listings
- The user should be able to filter their search based on different parameters
- The user should be able to sort their search based on different parameters
- The user should be able to choose how their chicken is sold, e.g. auction, auction with reserve, fixed price

### Non-Functional Requirements
- The website should work on both desktop and mobile
- Notifications should be sent to buyers interested in a chicken whose auction is ending soon

### Use Cases
1. The user should be able to search for specific listings
	- **Pre-condition:** None
	
	- **Trigger:** The user selects the search button or presses enter when the text box is in focus
	
	- **Primary Sequence:**
	  1. The user optionally enters text into the search text box
	  2. The system checks all listings for matching queries
	  3. The website displayes matching listings if any
	
	- **Primary Postconditions:** The website displays any matching listings 
	
	- **Alternate Sequence:**
	  1. The user enters invalid text into the text field
	  2. The user is prompted to edit their query

2. The user should be able to choose how their chicken is sold, e.g. auction, auction with reserve, fixed price
   - **Pre-condition:** The user is logged in and is creating a listing
	
	- **Trigger:** The user creates a listing
	
	- **Primary Sequence:**
	  1. The user selects if they want to create an auction, or sell at a fixed price
	  2. The user selects an optional reserve price and a duration if they select an auction, or a price if they select fixed price
	
	- **Primary Postconditions:** The user is allowed to continue creating their listing 
	
	- **Alternate Sequence:**
	  1. The user enters invalid input into the duration field
	  2. The user is prompted to edit the duration
