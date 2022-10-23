import re
from urllib.parse import urljoin

## -- Task 2 -- ##


def find_urls(
    html: str,
    base_url: str = "https://en.wikipedia.org",
    output: str = None,
) -> set:
    """Find all the url links in a html text using regex
    Arguments:
        html (str): html string to parse
    Returns:
        urls (set) : set with all the urls found in html text
    """
    # create and compile regular expression(s)

    # 1. find all the anchor tags, then
    # 2. find the urls href attributes
    urls = set()
    anchor_tag = re.compile(r"<a[^>]+>", flags=re.IGNORECASE)
    url_pat = re.compile(r'href="([^"^#]+)', flags=re.IGNORECASE)

    protocol = base_url.split("/")[0]
    for a_tag in anchor_tag.findall(html):
        url = url_pat.search(a_tag)
        if url:
            url = url.group(1)
            if url.startswith("//") and base_url:
                urls.add(protocol + url)
            elif url.startswith("/") and base_url:
                urls.add(base_url + url)
            else:
                urls.add(url)

    # Write to file if requested
    if output:
        print(f"Writing to: {output}")
        with open(output, "w") as f:
            f.write("\n".join(urls))

    return urls


def find_articles(html: str, output=None) -> set:
    """Finds all the wiki articles inside a html text. Make call to find urls, and filter
    arguments:
        - html (str) : the html text to parse
    returns:
        - (set) : a set with urls to all the articles found
    """
    urls = "\n".join(find_urls(html))
    pattern = re.compile("https://[a-z]*.*wikipedia.org(?:/wiki/[^:]*$|$)", flags=re.IGNORECASE | re.MULTILINE)
    articles = set(pattern.findall(urls))

    # Write to file if wanted
    if output:
        print(f"Writing to: {output}")
        with open(output, "w") as f:
            f.write("\n".join(articles))
    return articles


## Regex example
def find_img_src(html: str):
    """Find all src attributes of img tags in an HTML string

    Args:
        html (str): A string containing some HTML.

    Returns:
        src_set (set): A set of strings containing image URLs

    The set contains every found src attibute of an img tag in the given HTML.
    """
    # img_pat finds all the <img alt="..." src="..."> snippets
    # this finds <img and collects everything up to the closing '>'
    img_pat = re.compile(r"<img[^>]+>", flags=re.IGNORECASE)
    # src finds the text between quotes of the `src` attribute
    src_pat = re.compile(r'src="([^"]+)"', flags=re.IGNORECASE)
    src_set = set()
    # first, find all the img tags
    for img_tag in img_pat.findall(html):
        # then, find the src attribute of the img, if any
        src = src_pat.find(img_tag)
        src_set.add(src)
    return src_set
