import firebase_admin
from firebase_admin import credentials, firestore

# 서비스 계정 키로 인증
cred = credentials.Certificate("serviceAccountKey.json")

# Firebase 앱 초기화 (중복 초기화 방지)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Firestore 클라이언트 생성
db = firestore.client()
