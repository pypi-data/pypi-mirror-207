class neural:
    def __init__(self, x, y, x_size, y_size, binary_exit, epochs):
        from keras.models import Sequential
        from keras.layers import Dense
        model = Sequential()

        if binary_exit:
            model.add(Dense(100, input_dim=x_size, activation='relu'))
            model.add(Dense(100, activation='relu'))
            model.add(Dense(y_size, activation='sigmoid'))
        if not binary_exit:
            model.add(Dense(1, input_dim=x_size))

        model.compile(loss='binary_crossentropy' if binary_exit else 'mean_squared_error',
                      optimizer='adam' if binary_exit else 'sgd',
                      metrics=['accuracy'])

        model.fit(x, y, epochs=epochs, verbose=False)

        self.model = model
    def get(self, request):
        return self.model.predict(request)