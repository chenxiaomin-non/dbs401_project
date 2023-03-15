import api 
import uvicorn
import db_call

if __name__ == "__main__":
    db_call.create_table_if_not_exists()
    uvicorn.run(api.app, host="localhost", port=8000)
    