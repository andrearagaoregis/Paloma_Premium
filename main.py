import streamlit as st
from paloma_premium.config import Config
from paloma_premium.database import DatabaseService
from paloma_premium.chat_service import ChatService
from paloma_premium.ui_service import UiService, save_persistent_data

def main():
    st.set_page_config(
        page_title="Paloma Premium",
        page_icon="💋",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    # ... (restante do seu código main, exatamente igual, só mudando imports)
    # Lembre de ajustar todos os imports relativos, e chamadas de classe/função

if __name__ == "__main__":
    main()
