# LegalEase AI

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/LegalEaseAI.git
   cd LegalEaseAI
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

4. Add your AI71 API key:

   - Open `src/ai71_api.py` and replace `"PUT_YOUR_API_KEY_HERE"` with your actual API key.

5. Run the Streamlit application:
   ```sh
   streamlit run src/main.py
   ```

## Usage

Upload a legal document (PDF, DOCX, or TXT) and click "Summarize Document" to get the summary.
