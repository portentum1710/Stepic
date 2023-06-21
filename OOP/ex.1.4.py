#             ПОДВИГ 4
# class MediaPlayer:
#     def open(self, file):
#         self.filename = file
#
#     def play(self):
#         print('Воспроизведение', self.filename)
#
#
# media1 = MediaPlayer()
# media1.open("filemedia1")
# media1.play()
#
# media2 = MediaPlayer()
# media2.open("filemedia2")
# media2.play()
# __________________________________________________________
#               ПОДВИГ 5

class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        sort_lst = []
        for i in self.data:
            if Graph.LIMIT_Y[0] <= i <= Graph.LIMIT_Y[-1]:
                sort_lst.append(str(i))
        print(" ".join(sort_lst))


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()


