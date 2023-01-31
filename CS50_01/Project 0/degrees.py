import csv
import sys
from pathlib import Path
import util

mypath = Path(r"C:\Users\212628255\Documents\Knowledge\CS50s - Search\degrees\small")

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])  # fill sets
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    # if len(sys.argv) > 2:
    #     sys.exit("Usage: python degrees.py [directory]")
    #
    # directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    directory = mypath
    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))

    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    # solve
    path = shortest_path(source, target)

    # show results
    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    solution = list()
    explored = set()

    solution_found = False
    empty = False

    start = Node(state=source, parent=None, action=None)
    frontier = QueueFrontier()
    frontier.add(start)

    while not solution_found:
        if frontier.empty():
            solution_found = True
            empty = True
            continue

        # Choose a node from frontier
        node = frontier.remove()

        # If node is the target, then we have a solution
        if node.state == target:
            solution_found = True
            while node.parent is not None:
                pid, mid = node.state, node.action
                solution.append((mid, pid))
                node = node.parent
            solution.reverse()

        # Mark node as explored
        explored.add(node)
        neighbors = neighbors_for_person(node.state)

        for neighbor in neighbors:
            child = Node(state=neighbor[1], action=neighbor[0], parent=node)
            # Add neighbor to frontier
            frontier.add(child)

            # If any child node from neighbors is the target, then we have a solution
            if child.state == target:
                solution_found = True
                while child.parent is not None:
                    pid, mid = child.state, child.action
                    solution.append((mid, pid))
                    child = child.parent
                solution.reverse()

    if solution_found:
        if empty:
            return None
        return solution



def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:    # check in keys
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]



if __name__ == "__main__":
    main()
"""
Loading data...
Data loaded.
names[name] = id
kevin bacon {'102'}
tom cruise {'129', '9999'}
cary elwes {'144'}
tom hanks {'158'}
mandy patinkin {'1597'}
dustin hoffman {'163'}
chris sarandon {'1697'}
demi moore {'193'}
jack nicholson {'197'}
bill paxton {'200'}
sally field {'398'}
valeria golino {'420'}
gerald r. molen {'596520'}
gary sinise {'641'}
robin wright {'705'}
emma watson {'914612'}

people[id] = name: , birth: , movies: (movie_id)
102 {'name': 'Kevin Bacon', 'birth': '1958', 'movies': {'112384', '104257'}}
129 {'name': 'Tom Cruise', 'birth': '1962', 'movies': {'95953', '104257'}}
144 {'name': 'Cary Elwes', 'birth': '1962', 'movies': {'93779'}}
158 {'name': 'Tom Hanks', 'birth': '1956', 'movies': {'109830', '112384'}}
1597 {'name': 'Mandy Patinkin', 'birth': '1952', 'movies': {'93779'}}
163 {'name': 'Dustin Hoffman', 'birth': '1937', 'movies': {'95953'}}
1697 {'name': 'Chris Sarandon', 'birth': '1942', 'movies': {'93779'}}
193 {'name': 'Demi Moore', 'birth': '1962', 'movies': {'104257'}}
197 {'name': 'Jack Nicholson', 'birth': '1937', 'movies': {'104257'}}
200 {'name': 'Bill Paxton', 'birth': '1955', 'movies': {'112384'}}
398 {'name': 'Sally Field', 'birth': '1946', 'movies': {'109830'}}
420 {'name': 'Valeria Golino', 'birth': '1965', 'movies': {'95953'}}
596520 {'name': 'Gerald R. Molen', 'birth': '1935', 'movies': {'95953'}}
641 {'name': 'Gary Sinise', 'birth': '1955', 'movies': {'109830', '112384'}}
705 {'name': 'Robin Wright', 'birth': '1966', 'movies': {'109830', '93779'}}
914612 {'name': 'Emma Watson', 'birth': '1990', 'movies': set()}
9999 {'name': 'Tom Cruise', 'birth': '1900', 'movies': set()}

movies[id] = title: , year: ' stars: (people_id)
112384 {'title': 'Apollo 13', 'year': '1995', 'stars': {'200', '158', '641', '102'}}
104257 {'title': 'A Few Good Men', 'year': '1992', 'stars': {'193', '129', '197', '102'}}
109830 {'title': 'Forrest Gump', 'year': '1994', 'stars': {'398', '705', '158', '641'}}
93779 {'title': 'The Princess Bride', 'year': '1987', 'stars': {'144', '1697', '1597', '705'}}
95953 {'title': 'Rain Man', 'year': '1988', 'stars': {'420', '596520', '129', '163'}}
Name: sally field
Name: kevin bacon
2 degrees of separation.
1: Sally Field and Gary Sinise starred in Forrest Gump
2: Gary Sinise and Kevin Bacon starred in Apollo 13
"""