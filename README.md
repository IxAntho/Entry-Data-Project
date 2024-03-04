# Zillow Form Data Entry

This project is designed to extract data from a Zillow clone website listing webpage and automatically fill out a Google Form with the
extracted information. It uses Python and the Selenium library to interact with the web browser and automate the form
submission process.

## File Structure
- **main.py:** The main entry point of the application, responsible for instantiating and running the required classes.
- **form_data_entry.py:** Contains the FormDataEntry class, which handles the interaction with the Google Form and form submission process.
- **zillow_data_manager.py:** Contains the ZillowDataManager class, which scrapes the Zillow listing webpage and extracts the relevant property data.