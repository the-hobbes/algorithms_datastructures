"""Simple resizable array."""

class ArrayList(object):

	def __init__(self):
		self.max_size = 5
		self.current_size = 0
		self.latest_index = None
		self.array = [None] * self.max_size

	def insert(self, data):
		if self.latest_index is None:
			self.latest_index = 0
		else:
			self.latest_index += 1
		self.array[self.latest_index] = data

		# Double the size if needed.
		self.current_size += 1
		if self.current_size + 1 == self.max_size:
			self.resize()

	def resize(self):
		self.max_size = self.max_size * 2
		new_array = [None] * self.max_size
		for i in range(0, len(self.array)):
			new_array[i] = self.array[i]
		self.array = new_array

	def get(self, index):
		return self.array[index]


def main():
	al = ArrayList()
	assert al.current_size == 0
	assert al.max_size == 5
	al.insert(1)
	al.insert(2)
	al.insert(3)
	al.insert(4)
	al.insert(5)
	assert al.get(4) == 5
	assert al.current_size == 5
	assert al.max_size == 10


if __name__ == '__main__':
	main()