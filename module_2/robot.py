from urllib import parse, robotparser

agent = "Savy"
url = "https://www.thegradcafe.com/survey/"

parser = robotparser.RobotFileParser(url)
parser.set_url(parse.urljoin(url, "robots.txt"))
parser.read()

if parser.can_fetch(agent, url):
    print(f"{agent} is allowed to access {url}")