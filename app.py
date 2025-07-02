from fastapi import FastAPI
from contextlib import asynccontextmanager

# Impor fungsi dan router Anda
from src.controllers.user_controller import route as user_router
from src.controllers.auth_controller import auth_route as auth_router
from src.db.database import create_tabels
from src.utils.cloudinary_config import setup_cloudinary

# Definisikan lifespan manager untuk menangani event startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Menjalankan kode startup saat aplikasi dimulai.
    """
    print("🚀 Server starting up...")
    # Panggil fungsi setup di sini
    create_tabels()
    setup_cloudinary()
    yield
    # Kode setelah yield akan berjalan saat shutdown (jika ada)
    print("🔌 Server shutting down...")


# Inisialisasi aplikasi FastAPI dengan lifespan
app = FastAPI(
    title="Peminjaman Buku API",
    description="API untuk layanan peminjaman buku.",
    version="1.0.0",
    lifespan=lifespan
)

# Daftarkan router Anda
app.include_router(user_router, prefix="/api", tags=["Users"])
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

@app.get("/")
def root():
    """
    Endpoint root untuk memeriksa apakah server berjalan.
    """
    return {"message": "Welcome to the FastAPI CRUD API"}