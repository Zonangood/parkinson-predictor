import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from predict import predict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins for now, consider restricting to specific origins in production
origins = ["*"]

# Configure the CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the endpoint for handling file uploads
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    try:
        uploads_dir = "uploads"
        if not os.path.exists(uploads_dir):
            os.makedirs(uploads_dir)
        
        # Sanitize file name to prevent directory traversal attacks
        file_name = file.filename.replace("/", "_")
        file_location = os.path.abspath(os.path.join(uploads_dir, file_name))

        # Save the uploaded file to disk
        with open(file_location, "wb") as file_object:
            file_object.write(file.file.read())

        # Perform prediction on the uploaded file
        result = predict(file_location)

        # Return the filename and prediction result
        return {"filename": file.filename, "result": result}

    except Exception as e:
        # Log the error for debugging purposes
        app.logger.error(f"Error occurred during file upload: {e}")
        # Return an error response
        return JSONResponse(status_code=500, content={"error": "An error occurred during file upload"})


# Define a root endpoint for testing purposes
@app.get("/")
async def root():
    return { "message" : "Welcome to the Parkinson's diagnosis API" }
import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from predict import predict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins for now, consider restricting to specific origins in production
origins = ["*"]

# Configure the CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the endpoint for handling file uploads
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    try:
        uploads_dir = "uploads"
        if not os.path.exists(uploads_dir):
            os.makedirs(uploads_dir)
        
        # Sanitize file name to prevent directory traversal attacks
        file_name = file.filename.replace("/", "_")
        file_location = os.path.abspath(os.path.join(uploads_dir, file_name))

        # Save the uploaded file to disk
        with open(file_location, "wb") as file_object:
            file_object.write(file.file.read())

        # Perform prediction on the uploaded file
        result = predict(file_location)

        # Return the filename and prediction result
        return {"filename": file.filename, "result": result}

    except Exception as e:
        # Log the error for debugging purposes
        app.logger.error(f"Error occurred during file upload: {e}")
        # Return an error response
        return JSONResponse(status_code=500, content={"error": "An error occurred during file upload"})


# Define a root endpoint for testing purposes
@app.get("/")
async def root():
    return { "message" : "Welcome to the Parkinson's diagnosis API" }
