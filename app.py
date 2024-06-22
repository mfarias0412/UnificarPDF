import streamlit as st
from PyPDF2 import PdfMerger

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
            merger.append(uploaded_file)

        # Escrever o arquivo PDF mesclado
        output_path = "completoUnificado.pdf"
        with open(output_path, "wb") as output_file:
            merger.write(output_file)

        merger.close()

        # Exibir mensagem de sucesso e link para download
        st.success(f"PDFs unificados com sucesso!")
        st.markdown(f"[Baixar arquivo unificado](./{output_path})")
    else:
        st.error("Por favor, carregue pelo menos um arquivo PDF.")
