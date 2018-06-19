class HashTable(object):
	"""Simple implementation of a hash table."""


	class _HashEntry(object):
		"""A small linked list implementation to avoid collisions."""
		def __init__(self, key, value):
			self.key = key
			self.value = value
			self.next = None
			self.head = None

		def search(self, value):
			current = self.head
			while current:
				if current.value == value:
					return current
				current = current.next
			return None

		def insert(self, node):
			# If there's a node in the ll with a duplicate key, update
			# its value.
			dupe_key_node = self.search(node.value)
			if dupe_key_node:
				dupe_key_node.value = node.value
				return
			# Otherwise, insert a new node.
			# new_head -> old_head -> next...
			old_head = self.head
			self.head = node
			self.head.next = old_head


	def __init__(self, capacity=10, load=0.0):
		# Total capacity of the table.
		# Referrs to how many 'buckets' there are in the hash table.
		self.capacity = capacity
		# How loaded is the hash table (current capacity / total capacity).
		# This is used to determine when a resize should happen.
		self.load = load
		# How many items are in the hash table right now
		self.current_capacity = 0
		# The list represents the buckets.
		self.slots = [None] * self.capacity

	def insert(self, key, value):
		hashed_key = hash(key)
		# Choose a location to store the value in.
		picked_slot = hashed_key % self.capacity
		if not self.slots[picked_slot]:
			self.slots[picked_slot] = self._HashEntry(key, value)
		else:
			# Otherwise, we need to insert a new node into the linked list
			# that exists in the slot.
			head = self.slots[0]  # head of the linked list in the slot.
			new_node = self._HashEntry(key, value)
			head.insert(new_node)

	def retrieve(self, key):
		# Hash the key to the right slot, and search the linked list there.
		hashed_key = hash(key)
		picked_slot = hashed_key % self.capacity
		if self.slots[picked_slot]:
			head = self.slots[picked_slot]
			if head.key == key:
				return head.value
			else:
				found_key = head.search(key)
				return found_key.value
		return None

def main():
	ht = HashTable()
	ht.insert("a", 1)
	ht.insert("b", 2)
	assert ht.retrieve("a") == 1

if __name__ == '__main__':
	main()
		