from transformers import AutoTokenizer, AutoModelForCausalLM
import torch



device = "cuda" if torch.cuda.is_available() else "cpu"


model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"


tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)


def generate_answer(triples, question):

    context = "\n".join([f"- {h} {r} {t}." for h, r, t in triples])
    prompt = f"Context:\n{context}\n\nQ: {question}\nA:"

    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    output = model.generate(inputs["input_ids"], max_new_tokens=100, do_sample=True)

    answer = tokenizer.decode(output[0], skip_special_tokens=True)
    return answer.split("A:")[-1].strip()
