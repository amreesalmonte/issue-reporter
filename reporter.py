# uses the github API to watch for new issues
import requests

def userInput():
    # takes in user input of repository name and owner and returns it

    
    repoName = input("Repository name: ")
    repoOwner = input("Repository owner: ")

    return repoName, repoOwner

def verify(repoName, repoOwner):
    # verifies if the repository exists
    # repoName, repoOwner - string

    repo = "https://api.github.com/repos/" + repoOwner + "/" + repoName + "/issues" # /:owner/:repo/issues

    request = requests.get(repo, {"state" : "all"}) # default response obtained are open issues need to specify all
    response = request.json()

    if "message" in response:
        print("There was a problem accessing the repository")
        quit()
    else:
        return response

def parseData(response):
    # parses through the json file and extracts issue title and id
    # returns a separate list of open issues and closed issues
    # reponse - list type that contains response from request

    openIssues = []
    closedIssues = []
    if response != []:  # empty means no issues in repo
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

    print("\n{:}".format("OPEN ISSUES"))
    # table formatting
    print("-" * 78) 
    print("|{:^15}|{:^60}|".format("id", "title")) # character limit for issue titles in github is 60
    print("-" * 78) 
    for issue in openIssues:
        id = str(issue[0])
        title = issue[1]
        print("|{:^15}|{:^60}|".format(id, title))
    print("-" * 78) 
    print("TOTAL NUMBER OF OPEN ISSUES:", len(openIssues))

    print("\n{:}".format("CLOSED ISSUES"))
    # table formatting
    print("-" * 78) 
    print("|{:^15}|{:^60}|".format("id", "title"))
    print("-" * 78) 
    for issue in closedIssues:
        id = str(issue[0])
        title = issue[1]
        print("|{:^15}|{:^60}|".format(id, title))
    print("-" * 78) 
    print("TOTAL NUMBER OF CLOSED ISSUES:", len(closedIssues), " \n")

def main():

    repoName, repoOwner = userInput()
    response = verify(repoName, repoOwner)

    openIssues, closedIssues = parseData(response)
    formatOutput(openIssues, closedIssues)

if __name__ == "__main__":
    main()  