from keras.layers import Dense
from keras.models import Sequential, load_model
class ezneural:
    def __init__(self, x=[1], y=[2], x_size=1, y_size=1, binary_exit=False, epochs = 150):
        self.x = x
        self.y = y
        self.x_size = x_size
        self.y_size = y_size
        self.binary_exit = binary_exit
        self.epochs = epochs
    def create_model(self):
        model = Sequential()

        if self.binary_exit:
            model.add(Dense(100, input_dim=self.x_size, activation='relu'))
            model.add(Dense(100, activation='relu'))
            model.add(Dense(self.y_size, activation='sigmoid'))
        if not self.binary_exit:
            model.add(Dense(1, input_dim=self.x_size))

        model.compile(loss='binary_crossentropy' if self.binary_exit else 'mean_squared_error',
                      optimizer='adam' if self.binary_exit else 'sgd',
                      metrics=['accuracy'])

        model.fit(self.x, self.y, epochs=self.epochs, verbose=False)

        self.model = model
    def get(self, request):
        return self.model.predict(request)
    def save_to_file(self, file_name):
        self.model.save(file_name+'.h5')
    def load_from_file(self, file_name):
        self.model = load_model(file_name+'.h5')