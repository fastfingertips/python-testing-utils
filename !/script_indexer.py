from fastapi import FastAPI, HTTPException
import uvicorn

# Create a FastAPI instance
app = FastAPI()

# Define a list of script names
scripts = ["script1", "script2", "script3"]

def script_name_to_index(name, scripts):
    """
    Converts a script name to its corresponding index in the scripts list.
    
    Args:
    name (str): The script name to be converted.
    scripts (list): List of available script names.
    
    Returns:
    int: The index of the script in the scripts list.
    
    Raises:
    HTTPException: If the provided script name is not in the list.
    """
    normalized_name = name.lower()
    normalized_scripts = [script.lower() for script in scripts]

    try:
        return normalized_scripts.index(normalized_name)
    except Exception as e:
        # Raise an HTTPException with a 422 status code and a detail message
        raise HTTPException(status_code=422, detail="Invalid script name") from e

@app.get("/scripts/{script_name}")
def script_index(script_name: str):
    """
    Endpoint to retrieve the index of a script based on its name.
    
    Args:
    script_name (str): The name of the script.
    
    Returns:
    dict: A dictionary containing the script name and its index.
    
    Raises:
    HTTPException: If an invalid script name is provided.
    """
    try:
        # Call the script_name_to_index function to get the index
        index = script_name_to_index(script_name, scripts)
        return {"name": script_name, "index": index}
    except HTTPException as e:
        # Re-raise the HTTPException to maintain proper error handling
        raise e

# Run the application using uvicorn when executed directly
if __name__ == "__main__":
    print("Scripts:", scripts)
    uvicorn.run(app, host="localhost", port=32100)