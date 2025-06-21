"""Module for checking robots.txt permissions."""

from urllib import parse, robotparser

AGENT = "Savy"
URL = "https://www.thegradcafe.com/survey/"

PARSER = robotparser.RobotFileParser(URL)
PARSER.set_url(parse.urljoin(URL, "robots.txt"))
PARSER.read()

if PARSER.can_fetch(AGENT, URL):
    print(f"{AGENT} is allowed to access {URL}")
