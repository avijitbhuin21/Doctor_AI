```Generated with AI```
# DOCTOR-AI README

## Overview

DOCTOR-AI is a medical assistant web application built using **Streamlit** that helps individuals and doctors with diagnostic assistance. The platform allows patients to input their symptoms and medical history to receive a preliminary diagnosis and prescription suggestions, while doctors can use the tool to get differential diagnoses based on patient data. The application is designed to help users by providing a base level of medical insight, but it is essential to consult a healthcare professional for accurate and reliable medical advice.

## Features

- **Patient Mode**: Patients can input personal information, symptoms, medical history, and current medications. The system will analyze the data and provide a preliminary diagnosis with suggested medications.
- **Doctor Mode**: Doctors can input patient data and upload medical reports to receive differential diagnoses and additional suggestions for treatment or next steps.
- **Chat Interface**: An interactive chat interface powered by AI allows users to ask medical questions, receive responses, and get diagnostic insights based on the input data.
- **File Upload**: Doctors can upload medical reports (PDFs, images, Word documents) for further analysis, which enhances diagnosis suggestions.
- **Medical Disclaimer**: All AI-generated advice comes with a disclaimer that it should not replace professional medical consultation.

## Try it Here
**https://doctor-ai-by-avijit.streamlit.app/**

## Prerequisites

Before running the application, ensure the following requirements are met:

- Python 3.x
- Streamlit
- pandas
- io
- External helper functions (located in `utils.py`)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/doctor-ai.git
   cd doctor-ai
   ```

2. **Install dependencies**:
   Install the required libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   After the installation is complete, you can run the app using Streamlit:
   ```bash
   streamlit run app.py
   ```

## Application Workflow

### 1. **Patient Mode**
   - **Step 1**: Upon starting the app, patients are prompted to fill in their personal and medical information, including:
     - Name, Age, Gender, Height, Weight, Blood Group
     - Symptoms, Medical History, Current Medications, Extra Details
   - **Step 2**: Once the form is filled, patients can submit the data, which is analyzed by the AI assistant to provide a preliminary diagnosis.
   - **Step 3**: The patient can interact with the AI assistant via the chat interface to clarify symptoms and receive additional information.
   - **Step 4**: The AI provides a diagnosis based on the input data and the conversation.

### 2. **Doctor Mode**
   - **Step 1**: Doctors can input patient information similar to patients but with a broader focus, including the ability to upload medical reports for a more in-depth diagnosis.
   - **Step 2**: Doctors will receive a differential diagnosis based on the patient's data, which helps in understanding possible conditions and treatment recommendations.
   - **Step 3**: The platform analyzes uploaded files (e.g., PDFs, images, etc.) and incorporates them into the diagnosis process.
   - **Step 4**: The doctor receives the diagnosis result, which may include suggestions for further investigation.

### 3. **Interactive Chat**
   - The chat interface allows for continuous interaction between the user (patient or doctor) and the AI assistant, making the diagnostic process more dynamic.
   - The chat history is maintained, so users can refer to earlier exchanges during the consultation.

## Code Structure

The app consists of the following key components:

- **`app.py`**: Main Streamlit app containing all the page logic, patient and doctor mode handling, and UI elements.
- **`utils.py`**: Helper functions for processing patient data, generating diagnoses, and interacting with the medical AI model.
- **`requirements.txt`**: Python dependencies for the project (Streamlit, pandas, etc.).
- **`assets/`**: Folder containing any images or other static resources for the app.

## UI/UX Design

- The app uses **Streamlit**'s simple but powerful UI components, including text inputs, buttons, text areas, and file uploaders.
- The design is minimalistic but functional, with a clear separation between the patient and doctor modes.
- Custom CSS is used to enhance the appearance of the interface, making it more user-friendly and visually appealing.

## Known Issues and Limitations

- **Accuracy**: The AI-generated diagnoses are based on a simple set of rules and are not a substitute for professional medical evaluation.
- **File Upload Limitations**: Depending on the file size, there may be limits on the types and sizes of reports that can be uploaded.
- **Performance**: The performance of the app may be affected by the complexity of the input data and the AI's response time.

## Future Enhancements

- **Advanced AI Models**: The system can be integrated with more advanced machine learning models for better diagnostic accuracy.
- **Database Integration**: Storing user and patient data for analysis and improving AI responses.
- **Mobile Compatibility**: Optimizing the app for mobile use for broader accessibility.
- **Real-time Consultations**: Adding video and audio capabilities for real-time doctor-patient consultations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

*Disclaimer: The AI assistant provided by DOCTOR-AI is for educational and informational purposes only. The generated diagnoses should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or another qualified health provider with any questions you may have regarding a medical condition.*
