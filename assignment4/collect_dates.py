import re
from typing import Tuple

## -- Task 3 (IN3110 optional, IN4110 required) -- ##

# create array with all names of months
month_names = [
    "jan",
    "feb",
    "mar",
    "apr",
    "may",
    "jun",
    "jul",
    "aug",
    "sep",
    "oct",
    "nov",
    "dec",
]

...


def get_date_patterns() -> Tuple[str, str, str]:
    """Return strings containing regex pattern for year, month, day
    arguments:
        None
    return:
        year, month, day (tuple): Containing regular expression patterns for each field
    """

    # Regex to capture days, months and years with numbers

    jan = r"\b[jJ]an(?:uary)?\b"
    feb = r"\b[fF]eb(?:ruary)?\b"
    mar = r"\b[mM]ar(?:ch)?\b"
    apr = r"\b[aA]pr(?:il)?\b"
    may = r"\b[mM]ay\b"
    jun = r"\b[jJ]un(?:e)?\b"
    jul = r"\b[jJ]ul(?:y)?\b"
    aug = r"\b[aA]aug(?:ust)?\b"
    sep = r"\b[sS]ep(?:tember)?\b"
    oct = r"\b[oO]ct(?:ober)?\b"
    nov = r"\b[nN]ov(?:ember)?\b"
    dec = r"\b[dD]ec(?:ember)?\b"

    iso_month_format = r"\b(?:0\d|1[0-2])\b"

    # year should accept a 4-digit number between at least 1000-2029
    year = r"(?P<year>(?:1\d\d\d|20[0-2]\d))"
    # month should accept month names or month numbers
    month = rf"(?P<month>(?:{jan}|{feb}|{mar}|{apr}|{may}|{jun}|{jul}|{aug}|{sep}|{oct}|{nov}|{dec}))"
    # day should be a number, which may or may not be zero-padded
    day = r"(?P<day>0[1-9]\b|[1-9]\b|[1-2]\d\b|3[0-1]\b)"

    return year, month, day


def convert_month(s: str) -> str:
    """Converts a string month to number (e.g. 'September' -> '09'.

    You don't need to use this function,
    but you may find it useful.

    arguments:
        month_name (str) : month name
    returns:
        month_number (str) : month number as zero-padded string
    """
    # If already digit do nothing
    if s.isdigit():
        return zero_pad(s)

    # Convert to number as string
    for i in range(len(month_names)):
        if s.lower().startswith(month_names[i]):
            return zero_pad(str(i + 1))


def zero_pad(n: str):
    """zero-pad a number string

    turns '2' into '02'

    You don't need to use this function,
    but you may find it useful.
    """
    if n.isdigit():
        if int(n) < 10:
            return f"0{int(n)}"
        else:
            return n
    else:
        raise ValueError("Attempting to zero pad a non digit string")


def find_dates(text: str, output: str = None) -> list:
    """Finds all dates in a text using reg ex

    arguments:
        text (string): A string containing html text from a website
    return:
        results (list): A list with all the dates found
    """
    year, month, day = get_date_patterns()
    iso_month_format = r"(?P<month>(?:\b(?:0\d|1[0-2])\b))"

    # Date on format YYYY/MM/DD - ISO
    ISO = rf"{year}-{iso_month_format}-{day}"

    # Date on format DD/MM/YYYY
    DMY = rf"{day}\s{month}\s{year}"

    # Date on format MM/DD/YYYY
    MDY = rf"{month}\s{day}[,]?\s{year}"

    # Date on format YYYY/MM/DD
    YMD = rf"{year}\s{month}\s{day}"

    # list with all supported formats
    formats = [ISO, DMY, MDY, YMD]
    dates = []

    # find all dates in any format in text
    for f in formats:
        pat = re.compile(f, flags=re.IGNORECASE)
        for m in pat.finditer(text):
            g = m.groupdict()
            dates.append(f"{g['year']}/{convert_month(g['month'])}/{zero_pad(g['day'])}")

    # Write to file if wanted
    if output:
        print(f"Writing to: {output}")
        with open(output, "w") as f:
            f.write("\n".join(dates))
    return dates
