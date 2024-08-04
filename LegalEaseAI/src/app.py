import streamlit as st
from file_reader import read_file
from document_analysis import summarize_document
from legal_categorization import categorize_document
from key_terms_extraction import extract_key_terms
from actionable_insights import get_actionable_insights
from collaborative_annotations import save_annotation, get_annotations

st.set_page_config(
    page_title="LegalEase AI",
    page_icon=":gavel:",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f6;
    }
    .sidebar .sidebar-content {
        background-color: #ffffff;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        padding: 1rem;
        display: flex;
        flex-direction: column;
    }
    .sidebar .sidebar-content a {
        text-decoration: none;
    }
    .stButton button {
        background-color: #005b96;
        color: white;
        border-radius: 8px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s, transform 0.3s;
    }
    .stButton button:hover {
        background-color: #003f6c;
        transform: scale(1.05);
    }
    .card {
        background-color: #ffffff;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        padding: 1rem;
        margin-bottom: 1rem;
        transition: box-shadow 0.3s, transform 0.3s;
    }
    .card:hover {
        box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.3);
        transform: scale(1.02);
    }
    .card-header {
        font-weight: bold;
        font-size: 1.25rem;
        color: #005b96;
        margin-bottom: 0.5rem;
    }
    .card-content {
        color: #333;
    }
    .stTextInput textarea {
        border-radius: 8px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }
    .highlight {
        background-color: #e0f7fa;
        border-left: 5px solid #005b96;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.title("LegalEase AI")
st.sidebar.subheader("Features")
st.sidebar.write("Explore our advanced legal document analysis tools:")

features = {
    "Document Summary": "Summarize your document to get a concise overview.",
    "Categorize Document": "Automatically categorize the document into legal types.",
    "Extract Key Terms": "Extract and highlight key legal terms and phrases.",
    "Actionable Insights": "Get actionable recommendations based on document content.",
    "Collaborative Annotations": "Annotate and comment on specific parts of the document."
}

selected_feature = st.sidebar.selectbox("Choose a feature:", list(features.keys()))

st.title("LegalEase AI 📜")
st.write("Upload a legal document to get detailed insights.")

uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", "docx"])

if uploaded_file is not None:
    try:
        text = read_file(uploaded_file)
        st.write("Document content:")
        st.text_area("Document Text", text, height=250)
    except ValueError as e:
        st.error(str(e))
        st.stop()

    st.subheader(features[selected_feature])
    
    if selected_feature == "Document Summary":
        if st.button("Summarize Document"):
            with st.spinner('Generating summary...'):
                summary = summarize_document(text)
                st.markdown(f'''
                <div class="card highlight">
                    <div class="card-header">Summary Result</div>
                    <div class="card-content">{summary}</div>
                </div>
                ''', unsafe_allow_html=True)

    elif selected_feature == "Categorize Document":
        if st.button("Categorize Document"):
            with st.spinner('Categorizing document...'):
                category = categorize_document(text)
                st.markdown(f'''
                <div class="card highlight">
                    <div class="card-header">Document Category</div>
                    <div class="card-content">{category}</div>
                </div>
                ''', unsafe_allow_html=True)

    elif selected_feature == "Extract Key Terms":
        if st.button("Extract Key Terms"):
            with st.spinner('Extracting key terms...'):
                key_terms = extract_key_terms(text)
                st.markdown(f'''
                <div class="card highlight">
                    <div class="card-header">Key Legal Terms</div>
                    <div class="card-content">{key_terms}</div>
                </div>
                ''', unsafe_allow_html=True)

    elif selected_feature == "Actionable Insights":
        if st.button("Get Actionable Insights"):
            with st.spinner('Generating insights...'):
                insights = get_actionable_insights(text)
                st.markdown(f'''
                <div class="card highlight">
                    <div class="card-header">Actionable Insights</div>
                    <div class="card-content">{insights}</div>
                </div>
                ''', unsafe_allow_html=True)

    elif selected_feature == "Collaborative Annotations":
        st.subheader("Collaborative Annotations ✏️")
        annotation_text = st.text_area("Add your annotation:", height=100)
        if st.button("Save Annotation"):
            save_annotation("document_1", {"annotation": annotation_text})  # Using a placeholder document ID
            st.success("Annotation saved!")
        
        annotations = get_annotations("document_1")
        st.write("Existing Annotations:")
        for annotation in annotations:
            st.markdown(f'''
            <div class="card highlight">
                <div class="card-content">📝 {annotation['annotation']}</div>
            </div>
            ''', unsafe_allow_html=True)
