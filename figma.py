import streamlit as st
import openai
from config import OPENAI_API_KEY, FIGMA_API_KEY
openai.api_key = OPENAI_API_KEY

# Function to generate Angular code with GPT-3
def generate_angular(components):
  prompt = f"Generate Angular code for these components: {components}"
  
  response = openai.Completion.create(
    engine="text-davinci-002", 
    prompt=prompt,
    max_tokens=500
  )

  return response.choices[0].text

st.title("Figma to Angular Converter")

# File upload
figma_file = st.file_uploader("Upload Figma file") 

if figma_file:

  # Get components from Figma
  components = get_figma_components(figma_file.name)

  # Generate Angular code
  code = generate_angular(components)

  # Display code output
  st.code(code, language='typescript')

  # Download button
  st.download_button(
    label='Download Angular code',
    data=code,
    file_name='output.component.ts'
  )

else:
  st.info("Upload a Figma file to get started")
