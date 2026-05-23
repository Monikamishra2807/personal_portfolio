import os, mimetypes, requests
class SupabaseStorageService:
    def __init__(self):
        self.base_url = os.getenv('SUPABASE_URL', '').rstrip('/')
        self.api_key = os.getenv('SUPABASE_KEY', '')
        self.bucket = os.getenv('SUPABASE_BUCKET', 'portfolio-media')
        self.public = os.getenv('SUPABASE_PUBLIC_BUCKET', 'true').lower() == 'true'
    @property
    def headers(self):
        return {'apikey': self.api_key, 'Authorization': f'Bearer {self.api_key}'}
    def upload(self, file_obj, path):
        url = f"{self.base_url}/storage/v1/object/{self.bucket}/{path}"
        content_type = mimetypes.guess_type(path)[0] or 'application/octet-stream'
        resp = requests.post(url, headers={**self.headers, 'Content-Type': content_type, 'x-upsert': 'true'}, data=file_obj.read(), timeout=30)
        resp.raise_for_status()
        return self.get_public_url(path) if self.public else path
    def get_public_url(self, path):
        return f"{self.base_url}/storage/v1/object/public/{self.bucket}/{path}"
