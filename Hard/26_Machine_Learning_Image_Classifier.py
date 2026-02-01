from tensorflow import keras
import numpy as np
from PIL import Image

class ImageClassifier:
    def __init__(self):
        self.model = None
        self.load_or_train_model()

    def load_or_train_model(self):
        try:
            self.model = keras.models.load_model('mnist_model.h5')
            print("Model loaded from file.")
        except:
            print("Training new model...")
            self.train_model()

    def train_model(self):
        # Load MNIST dataset
        (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

        # Preprocess data
        x_train = x_train.astype('float32') / 255.0
        x_test = x_test.astype('float32') / 255.0
        x_train = x_train.reshape((x_train.shape[0], 28, 28, 1))
        x_test = x_test.reshape((x_test.shape[0], 28, 28, 1))

        # Build model
        self.model = keras.Sequential([
            keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
            keras.layers.MaxPooling2D((2, 2)),
            keras.layers.Conv2D(64, (3, 3), activation='relu'),
            keras.layers.MaxPooling2D((2, 2)),
            keras.layers.Flatten(),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(10, activation='softmax')
        ])

        # Compile model
        self.model.compile(optimizer='adam',
                          loss='sparse_categorical_crossentropy',
                          metrics=['accuracy'])

        # Train model
        self.model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

        # Save model
        self.model.save('mnist_model.h5')
        print("Model trained and saved.")

    def preprocess_image(self, image_path):
        # Load and preprocess image
        img = Image.open(image_path).convert('L')  # Convert to grayscale
        img = img.resize((28, 28))
        img_array = np.array(img)
        img_array = img_array.astype('float32') / 255.0
        img_array = img_array.reshape((1, 28, 28, 1))
        return img_array

    def classify_image(self, image_path):
        if self.model is None:
            print("Model not loaded.")
            return None

        img_array = self.preprocess_image(image_path)
        prediction = self.model.predict(img_array)
        predicted_class = np.argmax(prediction)
        confidence = np.max(prediction)

        return predicted_class, confidence

    def test_accuracy(self):
        if self.model is None:
            print("Model not loaded.")
            return

        (_, _), (x_test, y_test) = keras.datasets.mnist.load_data()
        x_test = x_test.astype('float32') / 255.0
        x_test = x_test.reshape((x_test.shape[0], 28, 28, 1))

        test_loss, test_acc = self.model.evaluate(x_test, y_test, verbose=2)
        print(f"Test accuracy: {test_acc}")

def main():
    classifier = ImageClassifier()

    print("Image Classifier for Handwritten Digits (MNIST)")
    print("Commands:")
    print("1. Test model accuracy")
    print("2. Classify an image (provide path to 28x28 grayscale image)")
    print("3. Exit")

    while True:
        choice = input("Enter choice: ")

        if choice == "1":
            classifier.test_accuracy()
        elif choice == "2":
            image_path = input("Enter image path: ")
            try:
                predicted_class, confidence = classifier.classify_image(image_path)
                print(f"Predicted digit: {predicted_class}")
                print(f"Confidence: {confidence:.2%}")
            except Exception as e:
                print(f"Error classifying image: {e}")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()