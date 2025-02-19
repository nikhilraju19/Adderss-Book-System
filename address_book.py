from logging_config import logger


class Contact:
    """
    This class contains the inbuilt functions to get the contact details of a person
    """
    def __init__(self, first_name, last_name, city, state, zip_code, mobile_number, email_id):
        """
        Description:
            This function is a constructor that gets contact details of a person
        Parameters:
            self: self refers to the instance of the class
            first_name: first name of the person
            last_name: last name of the person
            city: city of residence
            state: state of residence
            zip_code: zip code of area
            mobile_number: mobile_number of the person
            email_id: email id of the person
        Return:
            None
        """ 
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.mobile_number = mobile_number
        self.email_id = email_id
        
    def __str__(self):
        """
        Description:
            This function controls what should be returned when the class object is represented as a string.
        Parameters:
            self: self refers to the instance of the class
        Return:
            None
        """ 
        return (f"Name: {self.first_name} {self.last_name}\n"
                f"Address: {self.city}, {self.state} - {self.zip_code}\n"
                f"Contact Details: Mobile - {self.mobile_number}, Email - {self.email_id}\n")
        
class MyContacts:
    """
    This class contains the functions for the multiple operations of the my contacts
    """
    def __init__(self):
        """
        Description:
            It is a constructor that initializes empty contacts list upon object creation
        Parameters:
            self: self refers to the instance of the class
        Return:
            None
        """ 
        self.contacts = []
        
    def add_contact(self, contact):
        """
        Description:
            This function is used to add a contact in the my contacts
        Parameters:
            self: self refers to the instance of the class
            contact: contact that needed to add in my contacts
        Return:
            bool: True if contact is added successfully in the my contacts, False otherwise
        """ 
        if contact is not None:
            self.contacts.append(contact)
            logger.info(f"{contact.first_name} {contact.last_name} added to my contacts")
            return True
        logger.warning("Failed to add contact")
        return False

    def display_contacts(self):
        """
        Description:
            This function is used to display contacts present in my contacts
        Parameters:
            self: self refers to the instance of the class
        Return:
            None
        """ 
        if not self.contacts:
            logger.warning("No contacts available to display.")
            print("No contacts in my contacts")
        else:
            print("Displaying contacts present in My Contacts:")
            for contact in self.contacts:
                print(f"{contact}")
    
    def edit_contact(self, first_name, last_name):
        """
        Description:
            This function is used to edit a contact in the my contacts
        Parameters:
            self: self refers to the instance of the class
            first_name: first name that needed to edit a contact
            last_name: last name that needed to edit a contact
        Return:
            bool: True if contact is edited successfully in the my contacts, False otherwise
        """ 
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                print("Editing contact. Leave blank to keep existing value.")
                contact.city = input(f"Enter new city ({contact.city}): ") or contact.city
                contact.state = input(f"Enter new state ({contact.state}): ") or contact.state
                contact.zip_code = input(f"Enter new zip code ({contact.zip_code}): ") or contact.zip_code
                contact.mobile_number = input(f"Enter new mobile number ({contact.mobile_number}): ") or contact.mobile_number
                contact.email_id = input(f"Enter new email id ({contact.email_id}): ") or contact.email_id
                logger.info(f"{first_name} {last_name} - Contact updated successfully")
                print(f"{first_name} {last_name} - Contact updated successfully")
                return True
        logger.warning("Contact not found.")
        print("Contact not found. Please try again.")
        return False
       
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
                print("Invalid Input: Mobile number should be numeric and it must be exactly 10 digits")
        while True:
            email_id = input("Enter email id: ")
            if '@' in email_id or '.' in email_id:
                break
            else:
                logger.warning("Invalid Email id format")
                print("Invalid Email id format")
                
    except KeyboardInterrupt:
        logger.error("Process interrupted by user.")
        print("Process interrupted by user. Exiting...")
        exit(1)
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"Unexpected error occured: {e}")
        return None
    
    # if all the variables are non empty it creates contact otherwise it returns None
    if all([first_name, last_name, city, state, zip_code, mobile_number, email_id]):
        contact = Contact(first_name, last_name, city, state, zip_code, mobile_number, email_id)
        logger.info(f"{first_name} {last_name} - Contact created successfully")
        print(f"{first_name} {last_name} - Contact created successfully")
        return contact
    else:
        logger.warning("Failed to create contact. Please enter correct details in all the fields")
        print("Failed to create contact. Please try again.")
        return None
    
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
    my_contacts = MyContacts()
    while True:
        try:
            print("\nAdress Book Menu: ")
            print("1. Create a new contact")
            print("2. Display Contacts")
            print("3. Edit a contact")
            print("4. Exit")
            
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                contact = create_contact()
                my_contacts.add_contact(contact)
            elif choice == 2:
                my_contacts.display_contacts()
            elif choice == 3:
                first_name = input("Enter the first name of the contact to edit: ")
                last_name = input("Enter the last name of the contact to edit: ")
                my_contacts.edit_contact(first_name, last_name)    
            elif choice == 4:
                logger.info("Exiting My Contacts System")
                print("Exiting My Contacts System")
                break
            else:
                logger.warning("Invalid choice. Please enter a valid choice.")
                print("Invalid choice. Please try again.")

        except KeyboardInterrupt:
            logger.error("Process interrupted by user.")
            print("Process interrupted by user. Exiting...")
            exit(1)
        
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            print(f"Unexpected error occured: {e}")
            return None

if __name__ == "__main__":
    main()