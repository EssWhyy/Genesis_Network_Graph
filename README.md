# Genesis_Network_Graph
## A Simple Character Network Graph (Gephi)

A small project I did on network graphs using Gephi.

Gephi is a data visualisation software which can map out a network graph given an input list of nodes (a name, and an integer which defines how big the node is) and edges (two nodes, and an integer, which shows how strong the connection is between the two nodes)

Using Python 3, I first highlight main characters in each of the 1500+ verses/rows in the bible book Genesis, along with counting the total times a character is mentioned, using count_characters.py.

Following which I use the itertools combination module in count_connections.py to count edges/the number of times 2 characters are mentioned in each verse. (I have to assign each name with an ASCII symbol within the excel sheet due to a built-in restriction for Gephi)

From there I input the nodes and edges datasets into Gephi, and adjusted the position and colours of the nodes based on their position in the story and relations with other characters.

*More info on how to use Gephi can be found here: https://gephi.org/users/quick-start/*

