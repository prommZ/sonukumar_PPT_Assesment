import azure.functions as func
import logging

app = func.FunctionApp()

@app.blob_trigger(
    arg_name="myblob",
    path="blobprocessor/{name}",
    connection="storageeventdemo123_STORAGE"
)
@app.cosmos_db_output(
    arg_name="outputDocument",
    database_name="FileDB",
    container_name="Files",
    connection="musstorage5_STORAGE"
)
def blob_trigger(myblob: func.InputStream, outputDocument: func.Out[dict]):

    logging.info(
        f"Python blob trigger function processed blob "
        f"Name: {myblob.name} "
        f"Blob Size: {myblob.length} bytes"
    )

    file_name = myblob.name.split('/')[-1]

    outputDocument.set({
        "id": file_name,
        "filename": file_name,
        "size": myblob.length
    })