# mailmap_py2.py
# Python 3.5

"""
Python script to track the mapping between subject and response
Raspberry pi will use this mapping file to determine relevant response
"""

# Utility library, relative with respect to the calling script
from UTILS.find_my_public_ip_py2 import get_ip
from UTILS.get_forex_rate_py2 import get_GBP_INR_rate

# List of predefined questions and responses for raspberry pi
mail_map = {
    "hi": "hi there",
    "test": "Roger",
    "where are you": get_ip(),  # get external IP address
    "what is the rate": get_GBP_INR_rate()  # Get today's exchange rate
}
