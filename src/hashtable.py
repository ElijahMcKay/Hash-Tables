# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    # defining for clarity
    def __str__(self):
        return f"({self.key}, {self.value})"

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # turn key into integer index
        index = self._hash_mod(key)

        # creating list_node var
        new_node = LinkedPair(key, value)

        current_node = self.storage[index]

        # if this key/val pair exists, handle collision
        if current_node is not None:
            # print(f"Collision at {index}")
            # if item key is the same, overwrite value
            if current_node.key == key:
                current_node.value = value
                
                return current_node
            # in the case that the keys don't match
            else:
                # loop over the linked list until we're at the last node
                while current_node.next is not None:
                    # iterate current_node
                    current_node = current_node.next

                    # if keys match, overwrite
                    if current_node.key == key:
                        current_node.value = value

                        return current_node
                    
                # after while loop, add new_node as the final item       
                current_node.next = new_node

        # if there is no collision
        elif current_node is None:
            self.storage[index] = new_node

            return self.storage[index]





    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        # making var for current node
        current_node = self.storage[index]
        next_node = self.storage[index].next


        # print(self.storage)
        if current_node is None and current_node.key is not key:
            print(f"Key {key} not found")

            return None
        # if current_node.next == None (only 1 item in the LL)
        elif current_node.next is None and current_node.key == key:
            # make sure to delete the value in the actual array, not just current_node
            self.storage[index] = None

            return current_node
            
        # shouldn't have gotten to this point if there was only 1 LL in node
        while next_node is not None:
            
            # if there is a match, delete the node in that position
            if next_node.key == key:
                # switching the pointers to skip over the item to delete
                current_node.next = next_node.next
                # deleted_node = next_node
                # next_node = None

                return
            
            # if not, iterate to the next node
            current_node = next_node
            next_node = next_node.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        current_node = self.storage[index]

        # not using next_node here because there may just be 1 node in LL and we want the loop to work for that too
        while current_node:

            if current_node.key == key:
                return current_node.value
            
            #iterate to continue the loop if the iteration wasn't a match
            current_node = current_node.next

        # if we finish the loop and don't find the key, return None
        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_list = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        for item in old_list:
            current_node = item
            # print('currnode', current_node)
            # for every node in each item in old list, insert it into new doubled list
            while current_node is not None:
                self.insert(current_node.key, current_node.value)

                current_node = current_node.next

        # print(self.storage)
        return self.storage




if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
