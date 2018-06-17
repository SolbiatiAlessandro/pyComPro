import urllib2
import argparse
import time
from bs4 import BeautifulSoup

accepted_color_div1 = set(["user-orange","user-violet","user-legendary","user-red"])
accepted_color_div2 = set(["user-blue", "user-cyan"])

def parsepage(html, _problem, div):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find("table", {"class": "status-frame-datatable"})
    res = []
    for row in range(1,100,2):
        try:
            language = table.contents[row].contents[9].text[10:-6]
            if language == "Python 3" or language == "Python 2":
                if div == 1:
                    color = table.contents[row].contents[5].contents[1].get('class')[1] in accepted_color_div1
                elif div == 2:
                    color = table.contents[row].contents[5].contents[1].get('class')[1] in accepted_color_div2
                else:
                    color = 1
                problem = table.contents[row].contents[7].text[19:20] == _problem
                verdict = table.contents[row].contents[11].text[1:-1] == "Accepted"
                if(color and problem and verdict):
                    res.append(table.contents[row].contents[1].contents[1].get('href'))
        except:
            print("error at row :"+str(row))
    return res


def writeurls(f, _urls):
    for _url in _urls:
        f.write("<a class='cflink' href='https://codeforces.com"+str(_url)+"'>"+str(_url[-8:])+"</a>\n")


def main():
    parser = argparse.ArgumentParser(description='Automatically find good solution for cf contest')
    parser.add_argument('contest_number', type=int,
                        help=':number of the contest e.g. 988')
    parser.add_argument('problem_number', type=str,
                        help=':number of the problem e.g. A')
    parser.add_argument('div', type=int, help=':1 (div1) or 2 (div2) contest')
    """
    parser.
    add_argument('--sum', dest='accumulate', action='store_const',
                       const=sum, default=max,
                       help='sum the integers (default: find the max)')
    """
    args = parser.parse_args()

    f = open("./contest/"+str(args.contest_number) + "/"+str(args.problem_number)+".html", "w")
    init = "<style>.cflink{padding: 8px;box-shadow: 0px 0px 8px grey;background: aliceblue;line-height: 40px;}</style><p>This is a list of all the python AC submission from high-ranking users to <b>contest "+str(args.contest_number)+"</b> for the <b>problem "+str(args.problem_number)+"</p>"

    f.write(init)

    html = urllib2.urlopen("http://codeforces.com/contest/"+str(args.contest_number)+"/status/page/1?order=BY_JUDGED_DESC").read()
    _urls = parsepage(html,args.problem_number,args.div)
    writeurls(f,_urls)

    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.findAll("span", {"class": "page-index"})[-1]["pageindex"]


    for page in range(2,int(pages)):
        print("request : "+str(page)+"/"+pages+" | approx. time left : "+str(((int(pages)-page)*0.5)/60)+" mins")
        html = urllib2.urlopen(
            "http://codeforces.com/contest/" + str(args.contest_number) + "/status/page/"+str(page)+"?order=BY_JUDGED_DESC").read()
        _urls = parsepage(html,args.problem_number,args.div)
        writeurls(f, _urls)
        time.sleep(0.5)


main()

