from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
path_out = './editedimg'

for filename in os.listdir(path):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(path, filename)
        img = Image.open(img_path)
        
        # Perform image processing operations here
        edit = img.filter(ImageFilter.SHARPEN).convert("L")
        factor = 1.5
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(factor)
        blur_radius = 10  # Adjust this value for the desired blur effect
        edit = edit.filter(ImageFilter.GaussianBlur(blur_radius))#blurimg
        
        # Save the edited image
        clean_name = os.path.splitext(filename)[0]
        edited_filename = f"{clean_name}_edited.jpg"
        edited_path = os.path.join(path_out, edited_filename)
        edit.save(edited_path)

        print(f"Saved edited image: {edited_filename}")

    else:
        print(f"Skipping non-JPEG/JPG/PNG file: {filename}")

