class Movie:
    def __init__(self, title, director, cast, length, rating=-1):
        self.title = title
        self.director = director
        self.cast = cast
        self.length = length
        self.rating = rating

    def __str__(self):
        return 'Movie title=' + self.title + '\ndirector=' + self.director + '\n'

    def get_info(self):
        return "Title: {} Director: {} Cast: {} Length: {}" .format(self.title, self.director, self.cast, self.length)

class DLL_Node:
    def __init__(self, prev, data , next):
        self.data = data
        self.prev = prev
        self.next = next

class Pyflix:
    def __init__(self):
        self.head = DLL_Node(None, None, None)
        self.tail = DLL_Node(self.head, None, None)
        #self.head.next = self.tail
        self.size = 0
        self.current = self.head

    def __str__(self):
        l_ist = ''
        data_node = self.head.next
        while data_node != self.tail :
            if data_node == self.current:
                pointer = "--> {} {} \n" .format(data_node.data.title, data_node.data.director)
            else:
                pointer = "{} {} \n" .format(data_node.data.title, data_node.data.director)
            l_ist += pointer
            data_node = data_node.next
        return l_ist

    def add_movie(self, movie):
        new_node = DLL_Node(self.tail.prev, movie, self.tail)
        new_node.prev.next = new_node
        self.tail.prev = new_node
        self.size += 1

    def get_current(self):
        print(self.current.data)

    def next_movie(self):
        if self.current.next == self.tail and self.size > 0:
            self.current = self.head.next
        elif self.size > 0:
            self.current = self.current.next

    def prev_movie(self):
        if self.current.prev == self.head and self.size > 0:
            self.current = self.tail.prev
        elif self.size > 0:
            self.current = self.head.next

    def reset(self):
        self.current = self.head

    def rate(self):
        if self.current != self.head:
            user_rating = int(input("Rating: "))
            self.current.data.rating = user_rating
            print("Rating is {}".format(user_rating))
        else:
            print("NO MOVIE SELECTED")

    def info(self):
        return self.current.data.get_info()

    def remove_current(self):
        if self.current != self.head:
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.size -= 1
            self.next_movie()

    def length(self):
        return self.size

    def search(self, word):
        save_current = self.current
        counter = 0
        while counter < self.size:
            if self.current != self.head:
                if (word in self.current.data.title) or (word in self.current.data.director) or (word in self.current.data.cast):
                    self.info()

                counter += 1
            self.next_movie()
        self.current = save_current
        print("No movie")


movie_list = Pyflix()
Movie1 = Movie("El Camino", "Vince Gilligan", "Aaron Paul", 122)
Movie2 = Movie("Joker", "Todd Philips", "Joaquin Phoenix", 122)
Movie3 = Movie("Midsommar", "An Aster", "Florence Pugh", 138)
movie_list.add_movie(Movie1)
movie_list.add_movie(Movie2)
movie_list.add_movie(Movie3)

print(movie_list)
movie_list.next_movie()
movie_list.get_current()
movie_list.next_movie()
movie_list.get_current()
movie_list.rate()
movie_list.prev_movie()
movie_list.remove_current()
print(movie_list)
movie_list.get_current()
Movie4 = Movie("Hustlers", "Lorene Scafaria", "Constance Wu, Jennifer Lopez", 110)
movie_list.add_movie(Movie4)
movie_list.next_movie()
movie_list.next_movie()
movie_list.info()
print(movie_list)



