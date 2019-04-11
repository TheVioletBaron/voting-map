"""
Casey Edmonds-Estes
Project 4
11/13/18
"""

class Region:
    """
    A region (represented by a list of long/lat coordinates) along with
    republican, democrat, and other vote counts.
    """

    def __init__(self, coords, r_votes, d_votes, o_votes):
        self.coords = coords
        self.republican_votes = r_votes
        self.democrat_votes = d_votes
        self.other_votes = o_votes

    def lats(self):
        "Return a list of the latitudes of all the coordinates in the region"
        return [i[1] for i in self.coords]
        
    
    def longs(self):
        "Return a list of the longitudes of all the coordinates in the region"
        return [i[0] for i in self.coords]

    def min_lat(self):
        "Return the minimum latitude of the region"
        return min(self.lats())
    
    def min_long(self):
        "Return the minimum longitude of the region"
        return min(self.longs())
    
    def max_lat(self):
        "Return the maximum latitude of the region"
        return max(self.lats())
    
    def max_long(self):
        "Return the maximum longitude of the region"
        return max(self.longs())

    def plurality(self):
        """return 'REPUBLICAN','DEMOCRAT', or 'OTHER'
        depending on plurality of votes
        Breakes ties randomly"""

        #Tiebreaker section
        from random import randint
        if self.republican_votes == (self.democrat_votes and self.other_votes):
            breaker = random.randint(1,3)
            if breaker == 1:
                return 'REPUBLICAN'
            elif breaker == 2:
                return 'DEMOCRAT'
            else:
                return 'OTHER'
        if self.republican_votes == self.democrat_votes:
            breaker = random.randint(1,2)
            if breaker == 1:
                return 'REPUBLICAN'
            else:
                return "DEMOCRAT"
        if self.republican_votes == self.other_votes:
            breaker = random.randint(1,2)
            if breaker == 1:
                return 'REPUBLICAN'
            else:
                return "OTHER"
        if self.other_votes == self.democrat_votes:
            breaker = random.randint(1,2)
            if breaker == 1:
                return 'OTHER'
            else:
                return "DEMOCRAT"

        #regular section
        if self.republican_votes > (self.democrat_votes and self.other_votes):
            return 'REPUBLICAN'
        elif self.democrat_votes > (self.republican_votes and self.other_votes):
            return 'DEMOCRAT'
        else:
            return 'OTHER'
        
    def total_votes(self):
        "The total number of votes cast in this region"
        return self.republican_votes + self.democrat_votes + self.other_votes

    def republican_percentage(self):
        "The precentage of republication votes cast in this region"
        return self.republican_votes/(self.democrat_votes + self.republican_votes + self.other_votes) 
        
    def democrat_percentage(self):
        "The precentage of democrat votes cast in this region"
        return self.democrat_votes/(self.democrat_votes + self.republican_votes + self.other_votes)

    def other_percentage(self):
        "The precentage of other votes cast in this region"
        return self.other_votes/(self.democrat_votes + self.republican_votes + self.other_votes)


