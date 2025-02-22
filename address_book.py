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
            It returns the contact details of a person.
        """ 
        return (f"Name: {self.first_name} {self.last_name}\n"
                f"Address: {self.city}, {self.state} - {self.zip_code}\n"
                f"Contact Details: Mobile - {self.mobile_number}, Email - {self.email_id}\n")
        
class MyContacts:
    """
    This class contains the functions of multiple operations for my contacts
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
        
    def contact_exists(self, first_name, last_name):
        """
        Description:
            This function is used to check whether a contact is already exist or not
        Parameters:
            self: self refers to the instance of the class
            first_name: first name to check if is already in contacts or not
            last_name: last name to check if is already in contacts or not
        Return:
            boool: True if contact exist, False otherwise
        """ 
        return any(contact.first_name == first_name and contact.last_name == last_name for contact in self.contacts)
  
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
        if len(self.contacts) == 0:
            logger.warning("No contacts available to display.")
            print("No contacts available to display")
        else:
            print("Displaying contacts present in My Contacts:")
            for index, contact in enumerate(self.contacts, start = 1):
                print(f"Contact {index}:")
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
        logger.warning("Contact not found to edit.")
        print("Contact not found to edit.")
        return False

    def delete_contact(self, first_name, last_name):
        """
        Description:
            This function is used to delete a contact in the my contacts
        Parameters:
            self: self refers to the instance of the class
            first_name: first name that needed to delete a contact
            last_name: last name that needed to delete a contact
        Return:
            bool: True if contact is edited successfully in the my contacts, False otherwise
        """
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                self.contacts.remove(contact)
                logger.info(f"{first_name} {last_name} - Contact deleted successfully")
                print(f"{first_name} {last_name} - Contact deleted successfully")
                return True
        logger.warning("Contact not found to delete.")
        print("Contact not found to delete.")
        return False
    
    def sort_by_name(self):
        """
        Description:
            This function is used to sorts the contacts in the address book alphabetically name.
        Parameters:
            self: self refers to the instance of this class.
        Return:
            bool: True if contacts are sorted alphabetically, False otherwise
        """
        if self.contacts:
            self.contacts.sort(key=lambda contact: (contact.first_name.lower(), contact.last_name.lower()))
            logger.info(f"Contacts sorted alphabetically by name")
            print(f"Contacts sorted alphabetically by name.")
            return True
        else:
            logger.warning(f"No contacts to sort in Address book.")
            print(f"No contacts to sort in Address book.")
            return False
        
    def sort_by_state(self):
        """
        Description:
            This function is used to sorts the contacts in the address book alphabetically name.
        Parameters:
            self: self refers to the instance of this class.
        Return:
            bool: True if contacts are sorted alphabetically, False otherwise
        """
        if self.contacts:
            self.contacts.sort(key=lambda contact: (contact.state.lower()))
            logger.info(f"Contacts sorted alphabetically by state")
            print(f"Contacts sorted alphabetically by state.")
            return True
        else:
            logger.warning(f"No contacts to sort in Address book.")
            print(f"No contacts to sort in Address book.")
            return False
    
class AddressBookSystem():
    """
    This class contains the functions of mutliple operations for Address Book System
    """
    def __init__(self):
        """
        Description:
            It is a constructor that initializes empty address books dictionary upon object creation
        Parameters:
            self: self refers to the instance of the class
        Return:
            None
        """ 
        self.address_books = {}
        self.city_dict = {}
        self.state_dict = {}
        
    def add_address_book(self, name):
        """
        Description:
            This functions is used to know whether a address book is already exist or not, if not then add it.
        Parameters:
            self: self refers to the instance of the class
            name: name of the address book
        Return:
            bool: True if address book not exists, False otherwise
        """ 
        if name not in self.address_books:
            self.address_books[name] = MyContacts()
            logger.info(f"Address Book {name} - Created Successfully")
            print(f"Address Book {name} - Created Successfully")
            return True
        else:
            logger.warning(f"Address Book {name} already exists")
            print(f"Address Book {name} already exists")
            return False
        
    def get_address_book(self, name):
        """
        Description:
            This functions is used to get the details of the address book
        Parameters:
            self: self refers to the instance of the class
            name: name of the address book
        Return:
            address book details
        """
        return self.address_books.get(name)

    def update_city_dict(self):
        """
        Description:
            This functions is used to append all the contacts present in a given city
        Parameters:
            self: self refers to the instance of the class
        Return:
            None
        """
        self.city_dict.clear()
        for book in self.address_books.values():
            for contact in book.contacts:
                city_lower = contact.city.lower()
                if city_lower not in self.city_dict:
                    self.city_dict[city_lower] = []
                self.city_dict[city_lower].append(contact)

    def search_by_city(self, city):
        """
        Description:
            This functions is used to get the details of the persons present in a given city
        Parameters:
            self: self refers to the instance of the class
            city: city to search people
        Return:
            contact details of a person present in a given city
        """
        city_lower = city.lower()
        if city_lower in self.city_dict:
            print(f"Contacts found in city {city}:")
            for contact in self.city_dict[city_lower]:
                print(contact)
        else:
            logger.warning(f"No contacts found in city {city}.")
            print(f"No contacts found in city {city}.")
            
    def update_state_dict(self):
        """
        Description:
            This functions is used to append all the contacts present in a given state
        Parameters:
            self: self refers to the instance of the class
        Return:
            None
        """
        self.state_dict.clear()
        for book in self.address_books.values():
            for contact in book.contacts:
                state_lower = contact.state.lower()
                if state_lower not in self.state_dict:
                    self.state_dict[state_lower] = []
                self.state_dict[state_lower].append(contact)

    def search_by_state(self, state):
        """
        Description:
            This functions is used to get the details of the persons present in a given state
        Parameters:
            self: self refers to the instance of the class
            state: state to search people
        Return:
            contact details of a person present in a given state
        """
        state_lower = state.lower()
        if state_lower in self.state_dict:
            print(f"Contacts found in state {state}:")
            for contact in self.state_dict[state_lower]:
                print(contact)
        else:
            logger.warning(f"No contacts found in state {state}.")
            print(f"No contacts found in state {state}.")
            
    def count_by_city(self, city):
        """
        Description:
            This function is used to display the number of contacts in a given city.
        Parameters:
            self: self refers to the instance of the class
            city: The city name to get the count
        Return:
            None
        """
        city_lower = city.lower()
        if city_lower in self.city_dict:
            count = len(self.city_dict[city_lower])
            print(f"Number of contacts in {city}: {count} persons")
        else:
            logger.warning(f"No contacts found in city {city}.")
            print(f"No contacts found in city {city}.")
            
def create_contact(address_book):
    """
	Description:
		This function is used to create a new contact
	Parameters:
        None
	Return:
		contact details of a person if present, None otherwise
    """
    while True:     
        try:
            first_name = input("\nEnter the contact's first name : ")
            last_name = input("Enter the contact's last name: ")
            city = input("Enter name of the city: ")
            state = input("Enter name of the state: ")
            while True: 
                zip_code = input("Enter zip code: ")
                if zip_code.isdigit() and len(zip_code) == 6:
                    break 
                else:
                    logger.warning("Zip code should be numeric and it should be valid")
                    print("Invalid Input: Zip code should be numeric and it should be valid")
            while True:
                mobile_number = input("Enter mobile number: ")
                if mobile_number.isdigit() and len(mobile_number) == 10:
                    break
                else:
                    logger.warning("Mobile number should be numeric and it must be exactly 10 digits")
                    print("Invalid Input: Mobile number should be numeric and it must be exactly 10 digits")
            while True:
                email_id = input("Enter email id: ")
                if '@' in email_id and '.' in email_id:
                    break
                else:
                    logger.warning("Invalid Email id format")
                    print("Invalid Email id format")
            if address_book.contact_exists(first_name, last_name):
                logger.warning(f"{first_name} {last_name} - Contact already exists.")
                print(f"{first_name} {last_name} - Contact already exists.")
                print("Please enter a new contact.")
                continue
                    
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
            address_book.add_contact(contact)
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
    system = AddressBookSystem()
    while True:
        try:
            print("\nAddress Book System Menu: ")
            print("1. Create a new Address Book")
            print("2. Create a new contact in Address Book")
            print("3. Display contacts in Address Book")
            print("4. Edit a contact in Address Book")
            print("5. Delete a contact in Address Book")
            print("6. Search for a person by city across Address Books")
            print("7. Search for a person by state across Address Books")
            print("8. Get count of contacts in a city")
            print("9. Sort contacts in Address Book alphabetically by name")
            print("10. Sort contacts in Address Book alphabetically by state")
            print("11. Exit")
            
            choice = int(input("\nPlease select a number from Address Book System Menu: "))
            
            if choice == 1:
                name = input("Enter Address Book name: ")
                system.add_address_book(name)
                
            elif choice == 2:
                name  = input("Enter Address Book name to create a new contact: ")
                if name in system.address_books:
                    while True:
                        number_of_persons = input(f"Enter the number of persons to be added in {name} contacts: ")
                        if number_of_persons.isdigit():
                            number_of_persons = int(number_of_persons)
                            if number_of_persons > 0:
                                break
                            else:
                                logger.warning("Number of persons should be greater than zero")
                                print("Number of persons should be greater than zero")
                        else:
                            logger.warning("Invalid Input: Please enter integers only")
                            print("Invalid Input: Please enter integers only")
                    book = system.get_address_book(name)
                    for _ in range(number_of_persons):
                        contact = create_contact(book)
                        if contact:
                                logger.info(f"{contact.first_name} {contact.last_name} - Contact added to {name} contacts")
                                print(f"{contact.first_name} {contact.last_name} - Contact added to {name} contacts")
                    system.update_city_dict()
                    system.update_state_dict()
                else:
                    logger.warning(f"Address book {name} doesn't exist.")
                    print(f"Address book {name} doesn't exist.")
                    
            elif choice == 3:
                name  = input("Enter Address Book name to display contacts: ")
                if name in system.address_books:
                    book = system.get_address_book(name)
                    if book:
                        book.display_contacts()
                    else:
                        logger.warning(f"No contacts to display in Address book {name}.")
                        print(f"No contacts to display in Address book {name}.")
                else:
                    logger.warning(f"Address book {name} doesn't exist.")
                    print(f"Address book {name} doesn't exist.")
                    
            elif choice == 4:
                name  = input("Enter Address Book name to edit a contact: ")
                if name in system.address_books:
                    book = system.get_address_book(name)
                    if book and book.contacts:
                        first_name = input("Enter the first name of the contact to edit: ")
                        last_name = input("Enter the last name of the contact to edit: ")
                        book.edit_contact(first_name, last_name)
                        system.update_city_dict()
                        system.update_state_dict()
                    else:
                        logger.warning(f"No contacts to edit in Address book {name}.")
                        print(f"No contacts to edit in Address book {name}.")
                else:
                    logger.warning(f"Address book {name} doesn't exist.")
                    print(f"Address book {name} doesn't exist.")
                    
            elif choice == 5:
                name  = input("Enter Address Book name to delete a contact: ")
                if name in system.address_books:
                    book = system.get_address_book(name)
                    if book and book.contacts:
                        first_name = input("Enter the first name of the contact to delete: ")
                        last_name = input("Enter the last name of the contact to delete: ")
                        book.delete_contact(first_name, last_name)
                        system.update_city_dict()
                        system.update_state_dict()
                    else:
                        logger.warning(f"No contacts to delete in Address book {name}.")
                        print(f"No contacts to delete in Address book {name}.")
                else:
                    logger.warning(f"Address book {name} doesn't exist.")
                    print(f"Address book {name} doesn't exist.")                
            
            elif choice == 6:
                city = input("Enter city name to search for contacts: ")
                system.search_by_city(city)
                
            elif choice == 7:
                state = input("Enter state name to search for contacts: ")
                system.search_by_state(state)
                
            elif choice == 8:
                city = input("Enter city name to count contacts: ")
                system.count_by_city(city)
                
            elif choice == 9:
                book_name = input("Enter Address Book name to sort contacts by name: ")
                if book_name in system.address_books:
                    book = system.get_address_book(book_name)
                    book.sort_by_name()
                else:
                    logger.warning(f"Address book {book_name} does not exist.")
                    print(f"Address book {book_name} does not exist.")
                    
            elif choice == 10:
                book_name = input("Enter Address Book name to sort contacts by state: ")
                if book_name in system.address_books:
                    book = system.get_address_book(book_name)
                    book.sort_by_state()
                else:
                    logger.warning(f"Address book {book_name} does not exist.")
                    print(f"Address book {book_name} does not exist.")

            elif choice == 11:
                logger.info("Exiting Address Book System")
                print("Exiting Address Book System")
                break
            else:
                logger.warning("Invalid choice. Please choose a valid option from Address Book System Menu.")
                print("Invalid choice. Please choose a valid option from Address Book System Menu.")

        except KeyboardInterrupt:
            logger.error("Process interrupted by user.")
            print("Process interrupted by user. Exiting...")
            exit(1)
        
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            print(f"Unexpected error occured: {e}")


if __name__ == "__main__":
    main()