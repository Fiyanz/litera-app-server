import cloudinary
import os
from dotenv import load_dotenv

def setup_cloudinary():
    """
    Loads environment variables and configures the Cloudinary SDK.
    This should be called once when the application starts.
    """
    # Load environment variables from a .env file
    load_dotenv()
    
    cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME")
    api_key = os.getenv("CLOUDINARY_API_KEY")
    api_secret = os.getenv("CLOUDINARY_API_SECRET")

    if not all([cloud_name, api_key, api_secret]):
        raise ValueError("Cloudinary environment variables are not fully set.")

    cloudinary.config(
        cloud_name=cloud_name,
        api_key=api_key,
        api_secret=api_secret,
        secure=True
    )
    print("Cloudinary configuration successful.")