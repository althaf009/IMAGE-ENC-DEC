from PIL import Image
import numpy as np
import argparse

def encrypt_image(image_path, output_path, key):
    # Open image
    image = Image.open(image_path)
    pixels = np.array(image)

    # Perform encryption (example: XOR with key)
    key = key % 256  # Ensure key is in range 0-255
    encrypted_pixels = (pixels + key) % 256

    # Save encrypted image
    encrypted_image = Image.fromarray(encrypted_pixels.astype(np.uint8))
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    # Open encrypted image
    encrypted_image = Image.open(image_path)
    encrypted_pixels = np.array(encrypted_image)

    # Perform decryption (example: XOR with key)
    key = key % 256  # Ensure key is in range 0-255
    decrypted_pixels = (encrypted_pixels - key) % 256

    # Save decrypted image
    decrypted_image = Image.fromarray(decrypted_pixels.astype(np.uint8))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encrypt or decrypt an image.")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode of operation")
    parser.add_argument("input", help="Input image path")
    parser.add_argument("output", help="Output image path")
    parser.add_argument("key", type=int, help="Encryption/Decryption key (integer)")

    args = parser.parse_args()

    if args.mode == "encrypt":
        encrypt_image(args.input, args.output, args.key)
    elif args.mode == "decrypt":
        decrypt_image(args.input, args.output, args.key)
