class Collection:
    """
    A collection of...something.
    
    The responsibility of Collection is to keep and provide information
    about itself. It has convenience methods for adding, removing, and
    getting items within the collection by group name.\n
    This can be used either as a template for a more specific class, or
    as a "rich variable".
    
    Attributes:
        _collection (dict): a dictionary of items
            {key: group_name, value: a list of items}
    """

    def __init__(self):
        """
        Constructs a new Collection
        """
        self._collection = {}

    def add_item(self, group, item):
        """
        Adds the given item to the given group.
        
        Args:
            group (string): the name of the group
            item (any): the item to add
        """
        if not group in self._collection.keys():
            self._collection[group] = []
        
        if not item in self._collection[group]:
            self._collection[group].append(item)

    def get_items(self, group):
        """
        Gets the items in the given group.
        
        Args:
            group (string): the name of the group
            
        Returns:
            List: the items in the group
        """
        results = []
        if group in self._collection.keys():
            results = self._collection[group].copy()
        return results

    def get_all_items(self):
        """
        Gets all of the items in the Collection.
        
        Returns:
            List: all of the items in the Collection
        """
        results = []
        for group in self._collection:
            results.extend(self._collection[group])
        return results

    def get_first_item(self, group):
        """
        Gets the first item in the given group.
        
        Args:
            group (string): the name of the group
        """
        result = None
        if group in self._collection.keys():
            result = self._collection[group][0]
        return result

    def remove_item(self, group, item):
        """
        Removes an item from the given group.
        
        Args:
            group (string): the name of the group
            item (any): the item to remove
        """
        if group in self._collection:
            self._collection[group].remove(item)

    def remove_group(self, group):
        """
        Removes an entire group
        
        Args:
            group (string): the name of the group
        """
        if group in self._collection:
            del self._collection[group]
