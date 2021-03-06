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


	def __init__(self, capacity=10, load=0.9):
		# Total capacity of the table.
		# Referrs to how many 'buckets' there are in the hash table.
		self.capacity = capacity
		# How loaded is the hash table (current capacity / total capacity).
		# This is used to determine when a resize should happen. Defaults to
		# 90% loaded to trigger a resize, by default 9 elements.
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
			head = self.slots[picked_slot]  # head of the linked list in the slot.
			new_node = self._HashEntry(key, value)
			head.insert(new_node)

		# We resize the hash table if it is too loaded.
		self.current_capacity += 1
		current_load = float(self.current_capacity) / float(self.capacity)
		if current_load >= self.load:
			self.resize()

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

	def resize(self):
		# Double capacity if hash table is too loaded.
		new_capacity = self.capacity * 2
		new_slots = [None] * new_capacity
		# Compute new hashes for all items into the new slots.
		# 1) Loop through each slot.
		for slot_index in range(0, len(self.slots)):
			current_head = self.slots[slot_index]
			while current_head:
				# 2) Loop through each node in the linked list in the slot, and
				# rehash it.
				hashed_key = hash(current_head.key)
				new_slot = hashed_key % self.current_capacity
				# TODO: factor out this code, shared with insert.
				if not new_slots[new_slot]:
					self.slots[new_slot] = self._HashEntry(current_head.key, current_head.value)
				else:
					head = self.slots[new_slot]
					new_node = self._HashEntry(current_head.key, current_head.value)
					head.insert(new_node)
				current_head = current_head.next

		self.slots = new_slot
		self.capacity = new_capacity

	def delete(self, key):
		# TODO: Implement this.
		raise NotImplementedError

def main():
	ht = HashTable()
	ht.insert("a", 1)
	ht.insert("b", 2)
	assert ht.retrieve("a") == 1
	ht.insert("c", 3)
	ht.insert("d", 4)
	ht.insert("e", 5)
	ht.insert("f", 6)
	ht.insert("g", 7)
	ht.insert("h", 8)
	assert ht.current_capacity == 8.0
	assert ht.capacity == 10
	ht.insert("i", 9)
	assert ht.capacity == 20
	

if __name__ == '__main__':
	main()
		