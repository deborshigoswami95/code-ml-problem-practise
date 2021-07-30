"""
  https://leetcode.com/problems/lru-cache/

"""


class Node:
    def __init__(self, val=0, key=None):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache=dict()
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head
        self.capacity=capacity
        

    def get(self, key: int) -> int:
        # if key exists then return val and pull to head
        if key in self.cache:
            p=self.cache[key].prev
            n=self.cache[key].next
            p.next=n
            n.prev=p  
            
            current_first = self.head.next
            self.head.next=self.cache[key]
            self.cache[key].prev=self.head
            self.cache[key].next=current_first
            current_first.prev=self.cache[key]
            return self.cache[key].val
        # if key does not exist then return -1
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        # if key exists then update value & pull to head
        if key in self.cache:
            self.cache[key].val=value
            p=self.cache[key].prev
            n=self.cache[key].next
            p.next=n
            n.prev=p 
            current_first = self.head.next
            self.head.next=self.cache[key]
            self.cache[key].prev=self.head
            self.cache[key].next=current_first
            current_first.prev=self.cache[key]
            
            
        # elif key does not exist and capacity reached then, put at head and delete last key
        elif key not in self.cache and self.capacity==0:
            
            self.cache[key]=Node(value, key)
            current_first=self.head.next
            self.head.next=self.cache[key]
            self.cache[key].prev=self.head
            self.cache[key].next=current_first
            current_first.prev=self.cache[key]
            
            
            current_last=self.tail.prev
            self.tail.prev = current_last.prev
            current_last.prev.next=self.tail
            self.cache.pop(current_last.key)
            

        # else decrement capacity by 1 and put at head
        else:
            
            self.capacity-=1
            
            self.cache[key]=Node(value, key)
            current_first=self.head.next
            self.head.next=self.cache[key]
            self.cache[key].prev=self.head
            self.cache[key].next=current_first
            current_first.prev=self.cache[key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
