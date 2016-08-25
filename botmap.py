# botmap.py
# Python 3.5


"""
@vin_robot is my telegram bot; telegram.me/vin_robot
Python script to track the mapping between command and response
Telegrom bot will use this mapping to determine relevant response
"""

# Utility library, relative with respect to the calling script
from UTILS.find_my_public_ip import get_ip
from UTILS.get_forex_rate import get_GBP_INR_rate

# List of predefined questions and responses for raspberry pi
commands = {
    "/hi": "hi there",
    "/hello": "How are you doing today?",
    "/ping": "Pong",
    "/ip": get_ip(),  # get external IP address
    "/gbp": get_GBP_INR_rate()  # Get today's exchange rate
}
