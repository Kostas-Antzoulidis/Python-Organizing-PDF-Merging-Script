Simple python script that takes a folder containing image files that have names starting with '00', '01', or '02', creates three new subfolders within the original folder, named '00', '01', and '02' and
distributes the files into these subfolders based on their filename prefixes ('00' files go into '00' folder, etc.).For each subfolder ('00', '01', '02'), the script merges these images into a single PDF for each subfolder (order of images in the PDF matches the alphabetical or numerical order of the filenames). The PDF is named after the subfolder (e.g., '00.pdf', '01.pdf', '02.pdf').

This script uses the Pillow library for image processing and the FPDF library for creating PDFs. Ensure your image files have the extensions ".jpg" or ".png".
if you dont have them run these commands before executing:
  pip install Pillow
  pip install fpdf

To run the script, clone the repository and simply run "python .\Organizing_PDFMerging_Script.py". 
Provided inside are 2 foldiers: 
  sampleImages   -> Contains 10 image files to test the script on.
  testDir        -> Default directory to run script in.

You can change the default directory inside the script file by following the commented instructions.
The results of the script will be inside the testDir. If you want to try it again, simply erase everything from testDir and copy-paste the images provided in sampleImages in the testDir and run again(or provide other .jpg or .png photos)
