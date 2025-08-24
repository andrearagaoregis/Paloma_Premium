import streamlit as st
import time
import random
import json
import uuid
from .config import Config
from .database import PersistentState, save_persistent_data, get_user_id

def load_persistent_data():
    user_id = get_user_id()
    db = PersistentState()
    saved_data = db.load_state(user_id) or {}
    for key, value in saved_data.items():
        if key not in st.session_state:
            st.session_state[key] = value

def save_persistent_data():
    user_id = get_user_id()
    db = PersistentState()
    persistent_keys = [
        'age_verified', 'messages', 'request_count',
        'connection_complete', 'chat_started', 'audio_sent',
        'current_page', 'show_vip_offer', 'session_id',
        'last_cta_time'
    ]
    new_data = {key: st.session_state.get(key) for key in persistent_keys if key in st.session_state}
    saved_data = db.load_state(user_id) or {}
    if new_data != saved_data:
        db.save_state(user_id, new_data)

def get_user_id():
    if 'user_id' not in st.session_state:
        user_id = st.query_params.get('uid', [None])[0]
        if not user_id:
            user_id = str(uuid.uuid4())
            st.query_params['uid'] = user_id
        st.session_state.user_id = user_id
    return st.session_state.user_id

# ... Aqui, preserve todas as funções de UI, Sidebar, Gallery, Chat, etc,
# exatamente como estão no seu código original.
# (Devido ao tamanho, você pode simplesmente copiar e colar o conteúdo
# das funções do seu código original para cá, apenas alterando imports se necessário.)

# Exemplo (apenas assinatura da função, corpo igual seu original):
# def show_status_effect(container, status_type):
#     ... # igual seu código

# def show_call_effect():
#     ... # igual seu código

# def age_verification():
#     ... # igual seu código

# def setup_sidebar():
#     ... # igual seu código

# def show_gallery_page(conn):
#     ... # igual seu código

# def chat_shortcuts():
#     ... # igual seu código

# def enhanced_chat_ui(conn):
#     ... # igual seu código
