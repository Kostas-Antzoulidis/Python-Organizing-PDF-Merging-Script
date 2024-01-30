# Organizing-PDFMerging-script by Konstantinos Antzoulidis
# *to change destination foldier go to the bottom of the screen and see relevant comment*

# ---FOR DIRECTORY INSTRUCTIONS---
import os
# ---FOR IMAGE PROCESSING---
from PIL import Image
# ---FOR PDF PROCESSING---
from fpdf import FPDF

# ---FUNCTION FOR ORGANIZING IMAGES TO SUBFOLDIERS---
def organize_files(input_folder):
    try:
        # Creating subfolders '00', '01', '02'.
        for i in range(3):
            subfolder = os.path.join(input_folder, f"{i:02d}")
            os.makedirs(subfolder, exist_ok=True)

        # ---Moving files of target directory to corresponding subfolders based on filename prefix.---
        for filename in os.listdir(input_folder):
            # ---Working with .jpg and .png images---
            if filename.endswith(".jpg") or filename.endswith(".png"):
                # ---Calculating destination foldier---
                prefix = filename[:2]
                subfolder_path = os.path.join(input_folder, prefix)
                file_path = os.path.join(input_folder, filename)
                destination_path = os.path.join(subfolder_path, filename)

                if os.path.exists(subfolder_path):
                    os.rename(file_path, destination_path)
                else:
                    print(f"Error: Subfolder {prefix} does not exist for file {filename}")

    except Exception as e:
        print(f"Error during file organization: {e}")


# ---FUNCTION FOR MERGING IMAGES TO PDF AND OUTPUTTING SAID PDF FILE---
def merge_images_to_pdf(input_folder):
    try:
        for subfolder in os.listdir(input_folder):
            subfolder_path = os.path.join(input_folder, subfolder)
            if os.path.isdir(subfolder_path):
                # ---Naming and creating PDF---
                pdf_filename = os.path.join(input_folder, f"{subfolder}.pdf")
                pdf = FPDF()
                
                # ---Getting image files in alphabetical order---
                image_files = sorted([f for f in os.listdir(subfolder_path) if f.endswith(".jpg") or f.endswith(".png")])
                
                # ---Adding to PDF---
                for image_file in image_files:
                    image_path = os.path.join(subfolder_path, image_file)
                    pdf.add_page()
                    pdf.image(image_path, 0, 0, 210, 297)  # Assuming A4 size

                # ---Outputting pdf---
                pdf.output(pdf_filename, "F")
                
    except Exception as e:
        print(f"Error during PDF merging: {e}")


# ---Default input foldier when you run the program is ./testDir within the foldier this file is in---
if __name__ == "__main__":
    # ---Change input foldier by changing this---
    input_folder = "./testDir"
    
    # ---Organizing files into subfolders---
    organize_files(input_folder)
    
    # ---Merging images into PDFs for each subfolder---
    merge_images_to_pdf(input_folder)