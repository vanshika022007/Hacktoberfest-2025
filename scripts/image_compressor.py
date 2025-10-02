from PIL import Image
import os

def compress_image(input_path, output_path, quality=70):
    """
    Compress a single image and save it.
    
    :param input_path: Path to the original image
    :param output_path: Path to save compressed image
    :param quality: Compression quality (1-95), lower means smaller file
    """
    try:
        with Image.open(input_path) as img:
            img.save(output_path, "JPEG", optimize=True, quality=quality)
            print(f"Compressed: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Error compressing {input_path}: {e}")

def compress_folder(folder_path, output_folder, quality=70):
    """
    Compress all images in a folder.
    
    :param folder_path: Path to input folder
    :param output_folder: Path to save compressed images
    :param quality: Compression quality (1-95)
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(folder_path):
        input_file = os.path.join(folder_path, filename)
        output_file = os.path.join(output_folder, filename)

        if os.path.isfile(input_file):
            # Only process common image formats
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                compress_image(input_file, output_file, quality)

if __name__ == "__main__":
    # Example usage:
    # Compress a single image
    # compress_image("input.jpg", "compressed.jpg", quality=70)
    
    # Compress all images in a folder
    compress_folder("images", "compressed_images", quality=60)
