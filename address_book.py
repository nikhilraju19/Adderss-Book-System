from logging_config import logger


def create_contact():
    """
	Description:
		This function is used to create a new contact
	Parameters:
        None
	Return:
		contact details of a person if present, None otherwise
    """
    try:
        first_name = input("Enter the contact's first name : ")
        last_name = input("Enter the contact's last name: ")
        city = input("Enter name of the city: ")
        state = input("Enter name of the state: ")
        while True: 
            zip_code = input("Enter zip code: ")
            if zip_code.isdigit():
                break 
            else:
                logger.warning("Zip code should be numeric")
                print("Invalid Input: Zip code should be numeric")
        while True:
            mobile_number = input("Enter mobile number: ")
            if mobile_number.isdigit() and len(mobile_number) == 10:
                break
            else:
                logger.warning("Mobile number should be numeric and it must be exactly 10 digits")
                print("Mobile number should be numeric and it must be exactly 10 digits")
        while True:
            email_id = input("Enter email id: ")
            if '@' in email_id or '.' in email_id:
                break
            else:
                print("Invalid Email id format")
                
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
        logger.error("Process interrupted by user.")
        exit(1)
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"Unexpected error occured: {e}")
        return None
    
    # if all the variables are non empty it creates contact otherwise it returns None
    if all([first_name, last_name, city, state, zip_code, mobile_number, email_id]):
        contact = {
            "first_name": first_name,
            "last_name": last_name,
            "city": city,
            "state": state,
            "zip_code": zip_code,
            "mobile_number": mobile_number,
            "email_id": email_id
        }
        logger.info(f"{first_name} {last_name} - Contact created successfully ")
        return contact
    else:
        logger.warning("Failed to create contact. Please enter correct details in all the fields")
        return None

def add_contact(my_contacts, contact):
    """
	Description:
		This function is used to add a contact in the my_contacts
	Parameters:
        my_contacts: my contacts contains all the contacts at one place
        contact: contact that needed to add in my contacts
	Return:
		bool: True if contact is added successfully in the my contacts, False otherwise
    """ 
    if contact:
        my_contacts.append(contact)
        logger.info(f"{contact['first_name']} {contact['last_name']} added to my contacts")
        return True
    logger.warning("Failed to add contact.")
    return False
    
def display_contacts(my_contacts):
    """
	Description:
		This function is used to display contacts present in my contacts
	Parameters:
        my_contacts: my_contacts is to display contacts present in them
	Return:
		None
    """ 
    if not my_contacts:
        logger.warning("To display contact details please add a contact first")
        print("No contacts in my contacts")
    else:
        print("\nDisplaying contacts in my contacts:")
        for contact in my_contacts:
            print(f"Name: {contact['first_name']} {contact['last_name']}")
            print(f"Address: {contact['city']}, {contact['state']} - {contact['zip_code']}")
            print(f"Contact Details: Mobile number - {contact['mobile_number']}, Email id - {contact['email_id']}\n")

def main():
    """
	Description:
		This function calls all necessary sub-functions to perform the intended operations 
   		of the program. It serves as the entry point when the script is run.
	Parameters:
		None
	Return:
		None
    """
    my_contacts = []
    contact = create_contact()
    add_contact(my_contacts, contact)
    display_contacts(my_contacts)


if __name__ == "__main__":
    main()