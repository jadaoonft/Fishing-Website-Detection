import re
from urllib.parse import urlparse


def extract_url_features(url):

    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    parsed = urlparse(url)

    hostname = parsed.netloc
    path = parsed.path

    features = [
        len(url),
        len(hostname),
        url.count("."),
        url.count("-"),
        url.count("@"),
        url.count("?"),
        url.count("="),
        url.count("/"),
        url.count("%"),
        sum(c.isdigit() for c in url),
        int(url.startswith("https://")),
        int("@" in url),
        int("-" in hostname),
        int(len(url) > 75),
        int(re.search(r"\d+\.\d+\.\d+\.\d+", hostname) is not None),
    ]

    return features


def get_reasons(url):

    reasons = []

    if len(url) > 75:
        reasons.append("URL is unusually long")

    if "@" in url:
        reasons.append("Contains @ symbol")

    if "-" in urlparse(url if "://" in url else "http://" + url).netloc:
        reasons.append("Domain contains hyphen")

    if not url.startswith("https://"):
        reasons.append("HTTPS is not used")

    if url.count(".") > 3:
        reasons.append("Many subdomain/dot components")

    if sum(c.isdigit() for c in url) > 5:
        reasons.append("Contains many digits")

    if not reasons:
        reasons.append("No major suspicious URL patterns detected")

    return reasons