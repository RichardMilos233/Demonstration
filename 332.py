# You are given a list of airline tickets where 
# tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. 
# Reconstruct the itinerary in order and return it.

# All of the tickets belong to a man who departs from "JFK", thus, 
# the itinerary must begin with "JFK". 
# If there are multiple valid itineraries, 
# you should return the itinerary that has the smallest lexical order when read as a single string.

# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

import heapq
from collections import defaultdict

class Solution:
    def __init__(self):
         self.current = "JFK"
         self.reachable = defaultdict(list)

    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        for t in tickets:
            heapq.heappush(self.reachable[t[0]], t[1])
        
        itenerary = self.dfs(tickets, [])
        return itenerary
    
    def dfs(self, tickets, itenerary):
        current = self.current
        itenerary.append(current)
        nexts = self.reachable[current]
        tickets_copy = tickets.copy()
        itenerary_copy = itenerary.copy()
        print(f"current: {current}, itenerary: {itenerary}\ntickets: {tickets}\n")
        while tickets_copy:
            for next in nexts:
                self.reachable[current].remove(next)
                t = [current, next]
                tickets.remove(t)
                self.current = next
                itenerary = self.dfs(tickets, itenerary)
                if not tickets:
                    return itenerary
                tickets = tickets_copy
                itenerary = itenerary_copy
                self.current = current
                heapq.heappush(self.reachable[current], next)
            return itenerary
        return itenerary


tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","JFK"],["ATL","AAA"],["AAA","ATL"],["ATL","BBB"],["BBB","ATL"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","JFK"],["ATL","AAA"],["AAA","ATL"],["ATL","BBB"],["BBB","ATL"],["ATL","CCC"],["CCC","ATL"]]
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","JFK"],["ATL","AAA"],["AAA","ATL"],["ATL","BBB"],["BBB","ATL"],["ATL","DDD"],["DDD","ATL"],["ATL","EEE"],["EEE","ATL"],["ATL","FFF"],["FFF","ATL"],["ATL","GGG"],["GGG","ATL"],["ATL","HHH"],["HHH","ATL"],["ATL","III"],["III","ATL"],["ATL","JJJ"],["JJJ","ATL"],["ATL","KKK"],["KKK","ATL"],["ATL","LLL"],["LLL","ATL"],["ATL","MMM"],["MMM","ATL"],["ATL","NNN"],["NNN","ATL"]]

solution = Solution()

ans = solution.findItinerary(tickets)
print(ans)