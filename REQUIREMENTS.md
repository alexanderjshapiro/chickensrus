### Functional Requirements
- User profiles
- Users can view all items sellers are currently selling 
- Users can add pictures for items they are selling
- Users can save items for later
- The user should be able to search for specific listings
- The user should be able to filter their search based on different parameters
- The user should be able to sort their search based on different parameters
- The user should be able to choose how their chicken is sold, e.g. auction, auction with reserve, fixed price
- The user can open up more information on a current listing
- The user verifies their bidding on a listing

### Non-Functional Requirements
- The website should work on both desktop and mobile
- Notifications should be sent to buyers interested in a chicken whose auction is ending soon
- Users can stay signed into their account
- Website can save payment method

### Use Cases
1. Users can add pictures for items they are selling
  - **Pre-condition:** User has an account and is logged in

  - **Trigger:** User clicks "Add pictures" when on Selling page

  - **Primary Sequence:**
    1. Website prompts user to upload photos
    2. User uploads photos they want
    3. Website saves photos to item being listed 

  **Primary Postconditions:** Users can see photos of item that is sold
  
  **Alternative Sequence:**
  1. User tries to upload non compatible file as photo
    - Website displays error message to customer
    - Website prompts user to upload compatible file

2. Users can save items for later
  - **Pre-Condition:** User has an account and is logged in

  - **Trigger:** User clicks on "Save for Later" on item listing

  - **Primary Sequence:**
    1. Website saves item to user's "Saved" items
    2. Website displays message saying item has been saved  

  - **Primary Postconditions:** Users can see their saved items on their profile ## Requirements

3. The user should be able to search for specific listings
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

4. The user should be able to choose how their chicken is sold, e.g. auction, auction with reserve, fixed price
   - **Pre-condition:** The user is logged in and is creating a listing
	
	- **Trigger:** The user creates a listing
	
	- **Primary Sequence:**
	  1. The user selects if they want to create an auction, or sell at a fixed price
	  2. The user selects an optional reserve price and a duration if they select an auction, or a price if they select fixed price
	
	- **Primary Postconditions:** The user is allowed to continue creating their listing 
	
	- **Alternate Sequence:**
	  1. The user enters invalid input into the duration field
	  2. The user is prompted to edit the duration

7. The user can open up more information on a current listing
	- **Pre-condition:** None

	- **Trigger:** User clicks "More Info" on a listing

	- **Primary Sequence:**
	  1. A box opens up with any extra information or details the seller wanted to provide

	- **Primary Postcondition:**  Users can see additional information the seller gave
	
	- **Alternate Sequence:**
	  1. No extra information was given, so the box is empty

8.  The user verifies their bidding on a listing
	- **Pre-condition:** The user is signed in

	- **Trigger:** User clicks on "Bid" on a listing

	- **Primary Sequence:** 
	  1. User is prompted to verify their bidding via a "Proceed" button
	  2. User clicks on button

	- **Primary Postconditions:** Website displays a message saying "Bidding Received"

	- **Alternate Sequence:**
	  1. The user doesn't have a payment method saved
	  2. User is prompted to update their payment method


