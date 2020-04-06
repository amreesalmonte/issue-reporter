# uses the github API to watch for new issues
import requests

def parseData(response):
    # parses through the json file and extracts issue title and id
    # returns a separate list of open issues and closed issues
    # reponse - list type that contains response from request

    openIssues = []
    closedIssues = []
    for issue in response:
        data = (issue["id"], issue["title"])
        if issue["state"] == "closed":
            closedIssues.append(data)
        else:
            openIssues.append(data)
 
    return openIssues, closedIssues

def formatOutput(openIssues, closedIssues):
    # formats and outputs results in terminal
    # openIssues - list of tuples formatted as (id, title) that contain open issues in the repo
    # closedIssues - list of tuples formatted as (id, title) that contain closed issues in the repo

    print("\n{:^60}".format("OPEN ISSUES"))
    #table formatting
    print("-" * 70) 
    print("|{:^15}|{:^60}|".format("id", "title"))
    print("-" * 75) 
    for issue in openIssues:
        id = str(issue[0])
        title = issue[1]
        print("|{:^15}|{:^60}|".format(id, title))
    print("TOTAL NUMBER OF OPEN ISSUES:", len(openIssues))

    print("\n{:^60}".format("CLOSED ISSUES"))
    #table formatting
    print("-" * 70) 
    print("|{:^15}|{:^60}|".format("id", "title"))
    print("-" * 75) 
    for issue in closedIssues:
        id = str(issue[0])
        title = issue[1]
        print("|{:^15}|{:^60}|".format(id, title))
    print("TOTAL NUMBER OF CLOSED ISSUES:", len(closedIssues))

def main():

    repo = "https://api.github.com/repos/omxhealth/a-a-interview/issues" #/repos/:owner/:repo/issues
    request = requests.get(repo, {"state" : "all"}) #default response obtained are open issues need to specify all
    response = request.json()

    openIssues, closedIssues = parseData(response)
    formatOutput(openIssues, closedIssues)

if __name__ == "__main__":
    main()  