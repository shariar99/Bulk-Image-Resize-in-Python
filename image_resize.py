from PIL import Image
import os

import PIL 

def resize_images(input_folder, output_folder, max_width, max_height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        if os.path.isfile(input_path):
          
            img = Image.open(input_path)

           
            original_width, original_height = img.size

            aspect_ratio = original_width / original_height
            new_width = min(original_width, max_width)
            new_height = int(new_width / aspect_ratio)

         
            if new_height > max_height:
                new_height = max_height
                new_width = int(new_height * aspect_ratio)

           
            resized_img = img.resize((new_width, new_height), PIL.Image.Resampling.LANCZOS)



            resized_img.save(output_path)
            print(f"{input_path} -> {output_path}")

if __name__ == "__main__":
   
    input_folder = "path/to/input/folder"  # Replace with the path to your input folder
    output_folder = "path/to/output/folder"  # Replace with the path to your output folder
    max_width = 32  
    max_height = 32  

    resize_images(input_folder, output_folder, max_width, max_height) 
