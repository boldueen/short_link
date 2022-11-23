from pathlib import Path

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from api.metadata import tags
from api.api import root_router

BASE_PATH = Path(__file__).resolve().parent


app = FastAPI(title="link shorts test", openapi_tag=tags)

origins = ['*']
favicon_path = f'{BASE_PATH}/favicon.ico'


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(root_router)

@app.get("/", status_code=200)
async def root():
    return "Fuck You!"

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)




if __name__ == "__main__":
    # debug only
    print(BASE_PATH)
    import uvicorn
    uvicorn.run(
            'main:app',
            host="0.0.0.0", 
            port=8001, 
            reload=True,
            )

    