import numpy as np
import tifffile
import matplotlib.pyplot as plt

# Load 3D TIFF image
def load_tiff(file_path):
    return tifffile.imread(file_path)

# Initialize global variables
keypoints = []  # List to store the keypoints
current_slice = 0  # Current slice index

# Function to update the displayed image
def update_display(image):
    plt.imshow(image[current_slice, :, :], cmap="gray")
    plt.title(f"Slice {current_slice + 1}/{image.shape[0]}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.colorbar()

# Function to handle mouse clicks
def onclick(event):
    if event.xdata and event.ydata:
        x, y = int(event.xdata), int(event.ydata)
        z = current_slice
        keypoints.append((z, y, x))
        print(f"Keypoint added: (Z={z}, Y={y}, X={x})")
        plt.scatter(x, y, color='red', s=10)
        plt.draw()

# Function to handle keyboard events for navigation
def onkeypress(event, image):
    global current_slice

    if event.key == "up":
        current_slice = min(current_slice + 1, image.shape[0] - 1)
    elif event.key == "down":
        current_slice = max(current_slice - 1, 0)

    plt.clf()
    update_display(image)
    plt.draw()

# Main function
def main():
    file_path = input("Enter the path to the TIFF file: ")
    image = load_tiff(file_path)

    global current_slice
    current_slice = 0

    fig, ax = plt.subplots()
    update_display(image)

    # Connect events
    fig.canvas.mpl_connect("button_press_event", onclick)
    fig.canvas.mpl_connect("key_press_event", lambda event: onkeypress(event, image))

    print("Instructions:")
    print("- Use the mouse to click on keypoints (red dots will appear).")
    print("- Use the UP/DOWN arrow keys to navigate between slices.")
    print("- Close the plot window when finished.")

    plt.show()

    # Save keypoints
    save_path = input("Enter the path to save the keypoints (e.g., keypoints.npy): ")
    np.save(save_path, np.array(keypoints))
    print(f"Keypoints saved to {save_path}")

if __name__ == "__main__":
    main()
