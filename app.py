from fastapi import FastAPI;
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routes.usuariosRoutes import appUsuario

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las URLs
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

app.include_router(appUsuario)

#levantar el servidor
if __name__ == "__main__":
     uvicorn.run( 'app:app', host='0.0.0.0', port=4000, reload=True)