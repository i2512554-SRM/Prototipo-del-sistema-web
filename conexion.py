import os
from supabase import create_client
from dotenv import load_dotenv

class ConexionSupabase:
    def __init__(self):
        load_dotenv()
        self.url = os.getenv("SUPABASE_URL")
        self.apikey = os.getenv("SUPABASE_APIKEY")

        if not self.url or not self.apikey:
            raise Exception("Error: variables de entorno no configuradas")

    def conectar(self):
        return create_client(self.url, self.apikey)
