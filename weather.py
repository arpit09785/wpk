import numpy as np
import pickle
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open('D:/internship/SAV files/ParkinsonsSVM.sav', 'rb'))

def heart_disease_prediction(input_data):
    # Convert input data to numpy array and reshape
    input_data_as_array = np.asarray(input_data, dtype=float)
    input_data_reshaped = input_data_as_array.reshape(1, -1)

    # Make prediction
    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 1:
        return 'The person has Parkinson.'
    else:
        return 'The person does not have Parkinson.'

def main():
    # Title
    st.title('Parkinson Prediction Web App')

    # Input fields 		
    name = st.text_input('Name')		
    fo = st.text_input('MDVP:Fo(Hz)')
    fhi = st.text_input('MDVP:Fhi(Hz)')
    flo = st.text_input('MDVP:Flo(Hz)')
    jitter_percent = st.text_input('MDVP:Jitter(%)')
    jitter_abs = st.text_input('MDVP:Jitter(Abs)')
    rap = st.text_input('MDVP:RAP')
    ppq = st.text_input('MDVP:PPQ')
    ddp = st.text_input('Jitter:DDP')
    shimmer = st.text_input('MDVP:Shimmer')
    shimmer_db = st.text_input('MDVP:Shimmer(dB)')
    apq3 = st.text_input('Shimmer:APQ3')
    apq5 = st.text_input('Shimmer:APQ5')
    apq = st.text_input('MDVP:APQ')
    dda = st.text_input('Shimmer:DDA')
    nhr = st.text_input('NHR')
    hnr = st.text_input('HNR')
    rpde = st.text_input('RPDE')
    dfa = st.text_input('DFA')
    spread1 = st.text_input('spread1')
    spread2 = st.text_input('spread2')
    d2 = st.text_input('D2')
    ppe = st.text_input('PPE')

    # Prediction result
    diagnosis = ''

    if st.button('Parkinsons Test Report'):
        try:
            # Convert all inputs to float before passing to model
            input_data = [float(name), float(fo), float(fhi), float(flo),
              float(jitter_percent), float(jitter_abs), float(rap),
              float(ppq), float(ddp), float(shimmer),
              float(shimmer_db), float(apq3), float(apq5),
              float(apq), float(dda), float(nhr),
              float(hnr), float(rpde), float(dfa),
              float(spread1), float(spread2), float(d2),
              float(ppe)]
            
            diagnosis = heart_disease_prediction(input_data)
        except ValueError:
            diagnosis = "⚠️ Please enter valid numeric values in all fields."

        st.success(diagnosis)

if _name_ == '_main_':
    main()