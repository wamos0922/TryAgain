# ======================================================================
# File: mycats/demo.py (Sample Usage Repository)
# 
# Demonstrates library usage with templates and manual input, including 
# step-by-step previews.
# ======================================================================
import os 
from PIL import Image

# Helper function to safely get a float input from the user.
def get_float_input(prompt: str, default_value: float) -> float:
    while True:
        try:
            user_input = input(f"{prompt} (Default: {default_value:.2f}): ")
            if not user_input:
                return default_value
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")

# Create Dummy Image
def create_dummy_image(filename="sample_input.png"):
    """Creates a basic image if no input file exists for testing."""
    if not os.path.exists(filename):
        print(f"--- Creating a dummy image: {filename} ---")
        img = Image.new('RGB', (300, 200), color='#6A5ACD')
        img.save(filename)
# --- Library Imports ---
try:
    from ossimg.proc import ( 
        load_image, 
        adjust_brightness, 
        adjust_saturation, 
        adjust_sharpness, 
        adjust_shadows,
        apply_golden_hour,
        apply_gritty_contrast,
        apply_pastel_matte,
        # Import the new manual edit sequence function
        process_manual_edits 
    )
except ImportError:
    print("FATAL ERROR: Library 'ossimg' not found. Please run 'pip3 install -e .' in the ossimg folder.")
    exit(1)


# --- MANUAL EDIT LOGIC (Collects Input, Runs Process, Saves Previews) ---





# --- MAIN ENTRY POINT ---

