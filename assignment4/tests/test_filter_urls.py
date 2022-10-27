import pytest
from filter_urls import find_articles, find_urls
from requesting_urls import get_html

# Test some random urls


def test_find_urls():
    html = """
    <a href="#fragment-only">anchor link</a>
    <a id="some-id" href="/relative/path#fragment">relative link</a>
    <a href="//other.host/same-protocol">same-protocol link</a>
    <a href="https://example.com">absolute URL</a>
    """
    urls = find_urls(html, base_url="https://en.wikipedia.org")
    assert urls == {
        "https://en.wikipedia.org/relative/path",
        "https://other.host/same-protocol",
        "https://example.com",
    }


def test_find_urls_output(tmpdir):
    html = """
    <a href="#fragment-only">anchor link</a>
    <a id="some-id" href="/relative/path#fragment">relative link</a>
    <a href="//other.host/same-protocol">same-protocol link</a>
    <a href="https://example.com">absolute URL</a>
    """
    dest = tmpdir.join("output.txt")
    urls = find_urls(html, base_url="https://en.wikipedia.org", output=str(dest))

    assert dest.exists()  # assert output file was created

    with dest.open() as f:
        written_output = f.read()

    url_list = written_output.split("\n")
    assert set(url_list) == {
        "https://en.wikipedia.org/relative/path",
        "https://other.host/same-protocol",
        "https://example.com",
    }


@pytest.mark.parametrize(
    "url, links",
    [
        ("https://en.wikipedia.org/wiki/Nobel_Prize", ["x"]),
        ("https://en.wikipedia.org/wiki/Bundesliga", ["x"]),
        (
            "https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup",
            ["x"],
        ),
    ],
)
def test_find_urls_pages(url, links):

    html = get_html(url)
    urls = find_urls(html)
    assert isinstance(urls, set)
    # print(urls)
    for url in urls:
        # make sure we've got full URLs
        assert not url.startswith("/")
        assert not url.startswith("#")
        assert " " not in url
        assert "://" in url
    # for link in links:
    #     assert link in urls


@pytest.mark.parametrize(
    "url, expected, not_expected",
    [
        (
            "https://en.wikipedia.org/wiki/Nobel_Prize",
            [
                "https://en.wikipedia.org/wiki/Nobel_Prize_in_Physics",
                "https://en.wikipedia.org/wiki/Laureate",
                "https://bcl.wikipedia.org/wiki/Nobel_Prize",
                "https://or.wikipedia.org/wiki/%E0%AC%A8%E0%AD%8B%E0%AC%AC%E0%AD%87%E0%AC%B2_%E0%AC%AA%E0%AD%81%E0%AC%B0%E0%AC%B8%E0%AD%8D%E0%AC%95%E0%AC%BE%E0%AC%B0",
            ],
            [
                "https://www.nobelprize.org/prizes/facts/facts-on-the-nobel-prize-in-physiology-or-medicine",
                "https://en.wikipedia.org/wiki/File:AlfredNobel_adjusted.jpg",
            ],
        ),
        (
            "https://en.wikipedia.org/wiki/Bundesliga",
            [
                "https://en.wikipedia.org/wiki/German_football_league_system",
                "https://tt.wikipedia.org/wiki/Bundesliga",
                "https://en.wikipedia.org/wiki/Altona,_Hamburg",
            ],
            [
                "http://www.weltfussball.de/zuschauer/bundesliga-2010-2011/1/",
                "https://en.wikipedia.org/wiki/Wikipedia:Contact_us",
            ],
        ),
        (
            "https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup",
            [
                "https://en.wikipedia.org/wiki/International_Ski_Federation",
                "https://en.wikipedia.org/wiki/Hahnenkamm,_Kitzb%C3%BChel",
                "https://en.wikipedia.org/wiki/Henrik_Kristoffersen",
            ],
            [
                "https://www.fis-ski.com/DB/general/results.html?sectorcode=AL&amp;raceid=100063",
                "https://en.wikipedia.org/w/index.php?title=2019%E2%80%9320_FIS_Alpine_Ski_World_Cup&amp;action=edit&amp;section=2",
                "https://en.wikipedia.org/wiki/Special:RecentChanges",
            ],
        ),
    ],
)
def test_find_articles(url, expected, not_expected):
    html = get_html(url)
    articles = find_articles(html)
    assert isinstance(articles, set)
    assert len(articles) > 10
    for article in articles:
        assert "://" in article
        proto, _, rest = article.partition("://")
        hostname, _, path = rest.partition("/")
        assert hostname.endswith("wikipedia.org"), f"Not a wikipedia link: {article}"
        assert path.startswith("wiki/"), f"Not a wikipedia article: {article}"

    # check expected articles are present
    for article in expected:
        assert article in articles
    # check certain urls are left out. E.g. namespaces in wiki and other websites
    for non_article in not_expected:
        assert non_article not in articles


def test_find_articles_output(tmpdir):
    html = """
    <a href="#fragment-only">anchor link</a>
    <a id="some-id" href="/wiki/relative/path#fragment">relative link</a>
    <a href="//other.host/same-protocol">same-protocol link</a>
    <a href="https://example.com">absolute URL</a>
    <a href="/wiki/other_path">other relative path</a>
    <a href="/wiki/path/File:img.jpg">File namespace</a>
    <a href="/w/index.php?cc">index path</a>
    """

    dest = tmpdir.join("output.txt")
    articles = find_articles(html, output=str(dest))

    assert dest.exists()  # assert output file was created

    with dest.open() as f:
        written_output = f.read()

    url_list = written_output.split("\n")
    assert set(url_list) == {
        "https://en.wikipedia.org/wiki/relative/path",
        "https://en.wikipedia.org/wiki/other_path",
    }
