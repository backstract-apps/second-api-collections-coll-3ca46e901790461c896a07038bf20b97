from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - second-api-collections-coll-3ca46e901790461c896a07038bf20b97',debug=False,docs_url='/modest-sammet-1670b9cac36311efacee0242ac12000392/docs',openapi_url='/modest-sammet-1670b9cac36311efacee0242ac12000392/openapi.json')

app.include_router(router, prefix='/modest-sammet-1670b9cac36311efacee0242ac12000392/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()