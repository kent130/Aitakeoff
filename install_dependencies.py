import subprocess

# List of required packages
packages = ["openai", "pytesseract", "pdf2image", "requests", "pandas", "streamlit"]

# Install each package
for package in packages:
    subprocess.check_call(["pip", "install", package])

print("All required modules are installed successfully!")
