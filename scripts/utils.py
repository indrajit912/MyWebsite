# Some utility functions
#
# Author: Indrajit Ghosh
#
# Date: Nov 15, 2023
#

import base64
from datetime import datetime, timedelta, timezone

def convert_zip_to_base64(file_path):
    """
    Convert a ZIP file to a base64-encoded data URL.

    Parameters:
    - file_path (str): The path to the ZIP file.

    Returns:
    str: The base64-encoded data URL for the ZIP file.
    """
    with open(file_path, "rb") as file:
        zip_data = file.read()
        base64_data = base64.b64encode(zip_data).decode('utf-8')
        return f"data:application/zip;base64,{base64_data}"


def convert_utc_to_ist(utc_datetime_str):
    """
    Convert a UTC datetime string to Indian Standard Time (IST) format.

    Args:
        utc_datetime_str (str): A string representing a UTC datetime in the format '%Y-%m-%d %H:%M:%S'.

    Returns:
        str: A string representing the datetime in IST format, e.g., 'Dec 13, 2023 07:06 AM IST'.

    Example:
        >>> convert_utc_to_ist('2023-12-13 07:06:16')
        'Dec 13, 2023 07:06 AM IST'
    """
    # Convert string to datetime object
    utc_datetime = datetime.strptime(utc_datetime_str, "%Y-%m-%d %H:%M:%S")

    # Define UTC and IST timezones
    utc_timezone = timezone.utc
    ist_timezone = timezone(timedelta(hours=5, minutes=30))

    # Convert UTC datetime to IST
    ist_datetime = utc_datetime.replace(tzinfo=utc_timezone).astimezone(ist_timezone)

    # Format datetime in the desired string format
    formatted_datetime = ist_datetime.strftime("%b %d, %Y %I:%M %p IST")

    return formatted_datetime