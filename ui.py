from chatbot import generate_response  # Ensure this is correctly imported from chatbot.py
import gradio as gr
from datetime import datetime
from deep_translator import GoogleTranslator  # Import Google Translate API wrapper

# Company & Creator Information
COMPANY_NAME = "Nestlé HR Assistant"
CREATOR_NAME = "UI Designed by Uday Bhadauria"

# Store username globally
user_name = ""
theme_mode = "light"  # Default theme is Light Mode

# Language mapping for Google Translator
LANGUAGE_CODES = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Hindi": "hi",
    "Chinese": "zh-CN",
    "Arabic": "ar",
}

# Function to store username
def set_username(name):
    global user_name
    user_name = name
    return f"Welcome, {name}! You can now ask your HR questions."

# Function to translate responses
def translate_response(response, target_language):
    if target_language == "English":
        return response  # No translation needed
    
    try:
        lang_code = LANGUAGE_CODES.get(target_language, "en")  # Default to English if not found
        translator = GoogleTranslator(source="en", target=lang_code)  # Set source as English
        return translator.translate(response)
    except Exception as e:
        return f"⚠️ Translation error: {str(e)}"

# Chatbot function
def chatbot_interface(query, target_language):
    global user_name
    if not user_name:
        return "Please enter your name first before asking a question."

    response = generate_response(query)  # Get chatbot response
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Append user name & timestamp
    final_response = f"{user_name}, please find the response: {response} \n\n📅 {timestamp}"

    # Translate response
    translated_response = translate_response(final_response, target_language)
    return translated_response

# Function to toggle theme mode
def toggle_theme():
    global theme_mode
    theme_mode = "dark" if theme_mode == "light" else "light"
    return f"Theme switched to {theme_mode.capitalize()} Mode"

# List of languages for translation
LANGUAGES = list(LANGUAGE_CODES.keys())

# Gradio Interface with Light Orange Background
with gr.Blocks(css=".gradio-container {background-color: #FFDAB9}") as iface:  # Light Orange Color
    gr.HTML(f"""
    <div style="text-align: center;">
        <h1>🤖 {COMPANY_NAME}</h1>
        <h3>AI-Powered HR Chatbot</h3>
        <p>Welcome to <b>{COMPANY_NAME}</b>, your virtual HR assistant.<br>Type your question below and get instant responses!</p>
        <hr>
        <p><b>{CREATOR_NAME}</b></p>
    </div>
    """)

    # Theme Toggle Button
    theme_status = gr.Textbox(label="Current Theme", value="Light Mode", interactive=False)
    theme_toggle_btn = gr.Button("Toggle Theme")

    # Username Input Section
    with gr.Row():
        name_input = gr.Textbox(label="Enter Your Name:", placeholder="Type your name here...")
        name_submit_btn = gr.Button("Set Name")

    name_output = gr.Textbox(label="User Status", interactive=False)

    # Chat Section
    with gr.Row():
        with gr.Column():
            user_input = gr.Textbox(label="Ask your HR Question:", placeholder="e.g. What are the company working hours?")
            submit_btn = gr.Button("Get Answer", variant="primary")

        with gr.Column():
            output_text = gr.Textbox(label="Chatbot Response", interactive=False)

    # Language Selector Dropdown
    language_selector = gr.Dropdown(label="Select Language", choices=LANGUAGES, value="English")

    # Predefined Question Buttons (Fixed!)
    with gr.Row():
        predefined_btn1 = gr.Button("Company Working Hours")
        predefined_btn2 = gr.Button("Leave Policy")

    # Button Click Actions
    name_submit_btn.click(set_username, inputs=name_input, outputs=name_output)
    submit_btn.click(chatbot_interface, inputs=[user_input, language_selector], outputs=output_text)
    theme_toggle_btn.click(toggle_theme, outputs=theme_status)

    # **✅ Fix: Properly Pass Language Selector as Input**
    predefined_btn1.click(chatbot_interface, inputs=[gr.Textbox(value="Company Working Hours", visible=False), language_selector], outputs=output_text)
    predefined_btn2.click(chatbot_interface, inputs=[gr.Textbox(value="Leave Policy", visible=False), language_selector], outputs=output_text)

# Launch the Gradio interface
iface.launch(share=True)
