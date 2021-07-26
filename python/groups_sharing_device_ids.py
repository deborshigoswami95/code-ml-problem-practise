"""
class Account:
    def __init__(self, account_id, device_ids):
        self.account_id = account_id
        self.device_ids = device_ids
        
    # code for pretty printing
    def __repr__(self):
        return "Account(account_id='{}', device_ids={})".format(self.account_id, self.device_ids)

example_accounts=[
    Account(account_id="alice@gogoo.com", device_ids=[1, 2]),
    Account(account_id="betty@gogoo.com", device_ids=[3]),
    Account(account_id="a@gogoo.com", device_ids=[1, 4]),
    Account(account_id="daniel@gogoo.com", device_ids=[5, 6]),
    Account(account_id="erica.watson@gogoo.com", device_ids=[7, 8]),
    Account(account_id="e.w@gogoo.com", device_ids=[7, 9]),
    Account(account_id="e.watson@gogoo.com", device_ids=[9, 10]),
    Account(account_id="fred.hampton@gogoo.com", device_ids=[11, 12]),
    Account(account_id="f.h@gogoo.com", device_ids=[13, 14]),
    Account(account_id="f.hampton@gogoo.com", device_ids=[11, 13])
 ]

**** QUESTION ****

Given above is a list of accounts and the device id's associated with those accounts,
  1. Implement an algorithm to find the largest group of people who share one or more device id's
      Ans: This can be implemented using Depth First Search that finds all the connected components of a graph where each account is a node
      
  2. Write unit tests for this algorithm and package it in a python file neatly
  
  
Example output is given below
"""


# Example output:

# grouped_accounts = [
#     ["alice@icloud.com", "a@icloud.com"],
#     ["betty@icloud.com"], 
#     ["daniel@icloud.com"],
#     ["erica.watson@icloud.com", "e.w@icloud.com", "e.watson@icloud.com"],
#     ["fred.hampton@icloud.com", "f.h@icloud.com", "f.hampton@icloud.com"]
# ]
