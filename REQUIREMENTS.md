### Functional Requirements
- Login
- Logout
- Create account
- Delete account
- User profiles
- Users can add pictures for items they are selling
- Users can post listing
- Users can save items for later
- Users can view their saved items
- The user should be able to search for specific listings
- The user should be able to filter their search based on different parameters
- The user should be able to sort their search based on different parameters
- Users can add listing to cart
- Users can view their cart
- Users can check out

### Non-Functional Requirements
- The website should work on both desktop and mobile
- Users can stay signed into their account
- Website should show most popular on homescreen

### Use Cases
1. Users can add picture for item they are selling
  	- **Pre-condition:** User has an account and is logged in

  	- **Trigger:** User clicks "Upload Image" when on Selling page

  	- **Primary Sequence:**
	   1. Website prompts user to upload photo
	   2. User uploads photo they want
	   3. Website saves photo to item being listed 

  	- **Primary Postconditions:** Users can see photo of item that is sold on its listing page
  
 	 - **Alternative Sequence:**
  	   1. User tries to upload non compatible file as photo
    	   - Website displays error message to customer
    	   - Website prompts user to upload compatible file

2. Users can save items for later
  	- **Pre-Condition:** User has an account and is logged in

  	- **Trigger:** User clicks on "Save to Wishlist" on item listing

  	- **Primary Sequence:**
    	1. Website saves item to user's "Wishlist" items
    	2. Website redirects user to their Wishlist page  

  	- **Primary Postconditions:** Users can see their saved items on their profile 

3. The user should be able to search for specific listings
	- **Pre-condition:** None
	
	- **Trigger:** The user selects the search button or presses enter when the text box is in focus
	
	- **Primary Sequence:**
	  1. The user optionally enters text into the search text box
	  2. The system checks all listings for matching queries
	  3. The website displays matching listings if any
	
	- **Primary Postconditions:** The website displays any matching listings 
	
	- **Alternate Sequence:**
	  1. The user enters invalid text into the text field
	  2. The user is prompted to edit their query

4. The user should be able to post a listing to sell a chicken
	- **Pre-condition:** The user has an account and is logged in
	
	- **Trigger:** The user clicks 'New Listing'
	
	- **Primary Sequence:**
      1. The user fills out the information about their chicken (name, price, description, image)
      2. User submits their listing by clicking 'Publish Listing'

	- **Primary Postconditions:** Users are able to view this listing
	
	- **Alternate Sequence:**
	  1. The user doesn't fill out required fields
	  2. The user is prompted to fill in the information about their chicken

5. Users are able to check out
    - **Pre-condition:** The user has an account, is logged in, and has item(s) in their cart
	
    - **Trigger:** User clicks on "Checkout" 
	
    - **Primary Sequence:**
      1. User fills out their shipping and payment information
      2. User submits their order
	  
    - **Primary Postconditions:** Users able to see confirmation that their order has been placed
   
    - **Alternate Sequence:**
      1. The user doesn't fill out required fields
      2. The user is prompted to fill in the information about their shipping address and/or payment information
      
6. Users can add listing to cart
    - **Pre-condition:** The user has an account and is logged in 

    - **Trigger:** User clicks on 'Add to Cart' on certain listing page

    - **Primary Sequence:** 
      1. Website adds that listing to their cart
      2. Website redirects user to their Cart page
	 
	- **Primary Postconditions:** Users are able to view all their items in their cart page
	
