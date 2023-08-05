import random


class pBool:
    def __init__(self, credibility: float) -> None:
        '''
        Parameters
        ----------
        credibility: float (between 0 and 1)
            the degree of credibility
            0: False, 1: True
        '''
        if isinstance(credibility, (int, float)):
            if 0 <= credibility <= 1:
                self.credibility = credibility
            else:
                raise ValueError("credibility must be between 0 and 1")
        else:
            raise TypeError("\"credibility\" must be float")
        
        self.is_fixed = False
        self.flag = self.get()
        
    def __str__(self) -> str:
        return str(self.get())

    def __eq__(self, other: object) -> bool:
        return other == self.get()
    
    def __ne__(self, other: object) -> bool:
        return other != self.get()
    

    def get(self, true=True, false=False) -> bool:
        '''get bool by credibility
        Parameters
        ----------
        true: Any
            the value you want to return if flag is true
        false: Any
            the value you want to return if flag is false
        '''
        if not self.is_fixed:
            self.flag = random.random() <= self.credibility
        
        return true if self.flag else false
    

    def fix(self) -> None:
        self.is_fixed = True


    def unfix(self) -> None:
        self.is_fixed = False

        
# constant
falser = pBool(0.25)
grey = pBool(0.5)
truer = pBool(0.75)