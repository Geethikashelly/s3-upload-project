import os
import shutil

def upload_to_s3_simulator(file_path, bucket_name):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    os.makedirs(bucket_name, exist_ok=True)
    shutil.copy(file_path, bucket_name)
    print(f"File '{file_path}' uploaded successfully to '{bucket_name}'.")

if __name__ == "__main__":
    file_to_upload = "example.txt"
    simulated_bucket = "simulated_s3_bucket"
    upload_to_s3_simulator(file_to_upload, simulated_bucket)
