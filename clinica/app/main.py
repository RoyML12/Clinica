from fastapi import FastAPI

from app.routers import paciente_router
from app.routers import doctor_router
from app.routers import cita_router
from app.routers import receta_router

app = FastAPI(title="API Clinica")

app.include_router(paciente_router.router)
app.include_router(doctor_router.router)
app.include_router(cita_router.router)
app.include_router(receta_router.router)


@app.get("/")
def root():
    return {"message": "API Clinica funcionando"}