import streamlit as st


# Initialize session state variables if they don't exist
if 'initial_render' not in st.session_state:
    st.session_state.initial_render = True
if 'doctor' not in st.session_state:
    st.session_state.doctor = False
if 'patient' not in st.session_state:
    st.session_state.patient = False

def set_patient_mode():
    st.session_state.patient = True
    st.session_state.doctor = False
    st.session_state.initial_render = False

def set_doctor_mode():
    st.session_state.doctor = True
    st.session_state.patient = False
    st.session_state.initial_render = False

# Page configuration
st.set_page_config(page_title="Clickable Boxes")

# Custom CSS to style the boxes
st.markdown("""
    <style>
    .box-container {
        background-color: transparent;
        border-radius: 10px;
        padding: 30px;
        margin: 10px 0;
        cursor: pointer;
        transition: all 0.3s ease;
        border: 1px #a2a2a2 solid;
    }
    .box-header {
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 15px;
        color: red;
        transition: color 0.3s ease;
    }
    .box-description {
        font-size: 18px;
        color: #fff;
        line-height: 1.5;
        transition: color 0.3s ease;
    }
    </style>
    """, unsafe_allow_html=True)

# Main interface
if st.session_state.initial_render:
    col1, col2 = st.columns([1, 1])

    # First Box - For Patients
    with col1:
        if st.button("For Individual Patients", key="patient_button", use_container_width=True, on_click=set_patient_mode):
            pass

        st.markdown("""
            <div class="box-container">
                <div class="box-description">
                    Diagonose your disease and generate a prescription
                    with medications for that before consulting a doctor. 
                </div>
            </div>
        """, unsafe_allow_html=True)

    # Second Box - For Doctors
    with col2:
        if st.button("For Doctors", key="doctor_button", use_container_width=True, on_click=set_doctor_mode):
            pass

        st.markdown("""
            <div class="box-container">
                <div class="box-description">
                    Get a Differential Diagonosis for the Patient profile
                    along with probable medications.
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div class="box-header">
            Do not consume any medicine prescribed by the ai without consulting a doctor.
        </div>
    """, unsafe_allow_html=True)

# Handle different states
elif st.session_state.patient:
    # Initialize session states
    if "form_submitted" not in st.session_state:
        st.session_state.form_submitted = False

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "patient_data" not in st.session_state:
        st.session_state.patient_data = {}

    # Title
    st.title("DOCTOR-AI Chat")

    # Function to handle form submission
    def submit_form():
        st.session_state.patient_data = {
            "name": st.session_state.name,
            "age": st.session_state.age,
            "gender": st.session_state.gender,
            "phone": st.session_state.phone,
            "email": st.session_state.email,
            "blood_group": st.session_state.blood_group,
            "symptoms": st.session_state.symptoms,
            "medical_history": st.session_state.medical_history,
            "medications": st.session_state.medications,
            "allergies": st.session_state.allergies
        }
        st.session_state.form_submitted = True

    # Show form if not submitted
    if not st.session_state.form_submitted:
        st.markdown("### Please fill in your details")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.text_input("Full Name", key="name")
            st.number_input("Age", min_value=0, max_value=120, key="age")
            st.selectbox("Gender", ["Select", "Male", "Female", "Other"], key="gender")
            
        with col2:
            st.text_input("Phone Number", key="phone", placeholder="optional")
            st.text_input("Email", key="email", placeholder="optional")
            st.selectbox("Blood Group", ["Select", "A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"], key="blood_group")
        
        st.markdown("### Medical Information")
        st.text_area("Current Symptoms", key="symptoms")
        st.text_area("Medical History", key="medical_history", placeholder="optional")
        st.text_area("Current Medications", key="medications", placeholder="optional")
        st.text_area("Known Allergies", key="allergies", placeholder="optional")
        
        if st.button("Continue to Chat"):
            # Basic validation
            if (st.session_state.name and 
                st.session_state.age > 0 and 
                st.session_state.gender != "Select" and 
                st.session_state.blood_group != "Select"):
                submit_form()
                st.rerun()
            else:
                st.error("Please fill in all required fields.")

    # Show chat interface after form submission
    else:
        # Patient Details Expander
        with st.expander("Patient Details", expanded=False):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Full Name:** {st.session_state.patient_data['name']}")
                st.markdown(f"**Age:** {st.session_state.patient_data['age']} years")
                st.markdown(f"**Gender:** {st.session_state.patient_data['gender']}")
            with col2:
                st.markdown(f"**Phone Number:** {st.session_state.patient_data['phone']}")
                st.markdown(f"**Email:** {st.session_state.patient_data['email']}")
                st.markdown(f"**Blood Group:** {st.session_state.patient_data['blood_group']}")

        # Patient Issues Expander
        with st.expander("Patient Issues", expanded=False):
            st.markdown("**Current Symptoms:**")
            st.text(st.session_state.patient_data['symptoms'])
            
            st.markdown("**Medical History:**")
            st.text(st.session_state.patient_data['medical_history'])
            
            st.markdown("**Current Medications:**")
            st.text(st.session_state.patient_data['medications'])
            
            st.markdown("**Known Allergies:**")
            st.text(st.session_state.patient_data['allergies'])

        # Chat Interface
        st.markdown("### Chat with Medical Assistant")
        st.markdown("---")

        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input
        if prompt := st.chat_input("Type your message here..."):
            # Display user message
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Simulate AI response (replace this with actual AI integration)
            ai_response = f"I understand your concern about '{prompt}'. This is a placeholder response. In a real implementation, this would be connected to a medical AI model that can provide appropriate medical guidance while noting that it's not a replacement for professional medical advice."
            
            # Display assistant response
            with st.chat_message("assistant"):
                st.markdown(ai_response)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": ai_response})

        # Add disclaimer at the bottom
        st.markdown("---")
        st.markdown("*Disclaimer: This is a demonstration medical chat assistant. Please consult with a qualified healthcare professional for actual medical advice.*")


elif st.session_state.doctor:
    st.title("Doctor Interface")
    if st.button("Back to Home"):
        st.session_state.initial_render = True
        st.session_state.doctor = False
        st.rerun()