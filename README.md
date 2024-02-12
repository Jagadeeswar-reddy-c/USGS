# Automated USGS Satellite Image Downloads

## Overview:
This project aims to streamline the process of acquiring satellite imagery from the United States Geological Survey (USGS) by automating the download procedure. The USGS provides valuable satellite data that can be utilized for various applications such as environmental monitoring, land cover analysis, and change detection. Automating the image download process enhances efficiency and ensures timely access to up-to-date satellite data.

## Key Features:
Automated Retrieval: Effortlessly fetch satellite images from USGS servers without manual intervention.

Customizable Parameters: Tailor your image requests by specifying parameters such as date range, geographic coordinates, and sensor type.

Scheduled Downloads: Set up periodic downloads to keep your dataset updated with the latest satellite imagery automatically.

Data Integrity: Verify and ensure the integrity of downloaded data through checksums and error handling mechanisms.

Documentation: Comprehensive documentation to guide users on installation, configuration, and usage of the automated download script.

## Usage:
Installation:

```bash
git clone https://github.com/Jagadeeswar-reddy-c/USGS.git
cd automated-usgs-image-downloads
pip install -r requirements.txt
```

## Configuration:

Edit the Python file (Main.py) to set your USGS credentials and customize download parameters.
```bash
# Main.py

# user for input
username = "" # Example: name@gmail.com
password = "" # Example: ********(paswword)

# Specify paths
path_csv = ""  # Example: /home/user/Desktop/location
dst_path = ""  # Example: /home/user/Desktop/location/data

```

Please replace the input prompts accordingly based on your specific use case. This script allows users to input their GitHub username, password, path for CSV files, and the destination path for downloaded files when running the script.

## Run the Script:
```bash
python Main.py
```
