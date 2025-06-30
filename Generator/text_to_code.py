from transformers import pipeline

def generate_code(prompt):
    try:
        generator = pipeline("text-generation", model="Salesforce/codegen-350M-multi")
        code = generator(prompt, max_length=200, do_sample=True)[0]['generated_text']
        return code
    except Exception as e:
        return f"Code generation failed: {e}"
