import requests
from bs4 import BeautifulSoup
import re

URL = "https://appbrewery.github.io/Zillow-Clone/"


class ZillowDataManager:

    def __init__(self):
        self.response = requests.get(url=URL)
        self.soup = BeautifulSoup(self.response.content, "html.parser")
        self.links = []
        self.prices = []
        self.addresses = []

    def extract_dollar_amount(self, string):
        """
        Extracts the dollar amount from a string, including the dollar sign and number.

        Args:
            string (str): The input string containing a dollar amount.

        Returns:
            str: The dollar amount including the dollar sign and number (e.g., "$2,810" or "$2,450").
                 If no dollar amount is found, returns None.

        This function uses a regular expression to search for a dollar sign ($) followed by one or more digits (0-9)
        and/or commas (,). The regular expression pattern is r'\$([\d,]+)'. The parentheses create a capturing group,
        which allows the function to retrieve the matched text (the dollar amount) using match.group(1).
        """
        match = re.search(r'\$([\d,]+)', string)
        if match:
            return match.group(1)
        else:
            return None

    def property_data(self):
        link_elements = self.soup.find_all(class_="property-card-link")
        for link_element in link_elements:
            link = link_element.get("href")
            self.links.append(link)
        price_elements = self.soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
        for price_element in price_elements:
            price = price_element.getText()
            self.prices.append(self.extract_dollar_amount(price))
        address_elements = self.soup.find_all(class_="StyledPropertyCardDataArea-anchor")
        for addr_element in address_elements:
            self.addresses.append(addr_element.text.strip())
