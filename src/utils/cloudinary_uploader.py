# src/utils/cloudinary_uploader.py
from fastapi import UploadFile, HTTPException
import cloudinary.uploader

def upload_image(file: UploadFile, folder: str) -> dict:
    """
    Uploads an image file to a specified folder in Cloudinary.

    :param file: The file to upload (from a FastAPI request).
    :param folder: The destination folder in Cloudinary.
    :return: A dictionary containing the 'public_id' and 'secure_url' of the uploaded image.
    """
    try:
        # Upload the file and get the result
        upload_result = cloudinary.uploader.upload(
            file.file,
            folder=folder,
            resource_type="image"
        )
        
        # Extract the necessary information
        secure_url = upload_result.get("secure_url")
        public_id = upload_result.get("public_id")
        
        if not all([secure_url, public_id]):
            raise HTTPException(status_code=500, detail="Cloudinary did not return required information.")
            
        return {"public_id": public_id, "url": secure_url}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during file upload: {e}")


def delete_image(public_id: str):
    """
    Deletes an image from Cloudinary using its public_id.

    :param public_id: The public_id of the image to delete.
    :return: The result dictionary from Cloudinary.
    """
    try:
        # Delete the image
        delete_result = cloudinary.uploader.destroy(public_id)
        
        # The result for a successful deletion is typically {'result': 'ok'}
        if delete_result.get("result") != "ok":
            # This case handles if Cloudinary says not found, etc.
             raise HTTPException(status_code=404, detail=f"Image with public_id '{public_id}' not found or could not be deleted.")

        return delete_result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during file deletion: {e}")