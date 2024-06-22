import streamlit as st
from PyPDF2 import PdfMerger
import io

# Título da aplicação
st.title("Unificador de PDFs")

# Instruções para o usuário
st.write("Selecione os arquivos PDF que você deseja unificar:")

# Carregando arquivos PDF
uploaded_files = st.file_uploader("Escolha os arquivos PDF", accept_multiple_files=True, type="pdf")

# Botão para iniciar a unificação dos PDFs
if st.button("Unificar PDFs"):
    if uploaded_files:
        merger = PdfMerger()
        for uploaded_file in uploaded_files:
            # Adiciona cada PDF ao merger
            merger.append(uploaded_file)

        # Cria um buffer em memória para o PDF mesclado
        pdf_buffer = io.BytesIO()
        merger.write(pdf_buffer)
        merger.close()

        # Move o buffer para o início
        pdf_buffer.seek(0)

        # Gera um link para download
        st.success("PDFs unificados com sucesso!")
        st.download_button(
            label="Baixar arquivo unificado",
            data=pdf_buffer,
            file_name="completoUnificado.pdf",
            mime="application/pdf"
        )
    else:
        st.error("Por favor, carregue pelo menos um arquivo PDF.")
