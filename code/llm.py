import pandas as pd
import maritalk

def pergunta_llm(pergunta):
    model = maritalk.MariTalk(
        key="100088405894968274443$48d83f597eed3dac55ca7ab70e8d6d46628784d793046bf36006985b4d18354e",
        model="sabia-2-medium"  # No momento, suportamos os modelos sabia-2-medium e sabia-2-small
    )

    messages = [
        {"role": "user", "content": f"{pergunta}"},
    ]

    resposta = model.generate(
        messages,
        do_sample=True,
        max_tokens=200,
        temperature=0.7,
        top_p=0.95)["answer"]

    return resposta
def update_dataset(df: pd.DataFrame, pergunta, resposta, classe):
    novo_registro = {'Pergunta': pergunta, 'Resposta': resposta, 'LGPD': classe}
    df = df._append(novo_registro, ignore_index = True)
    df.to_csv('../dataset/dataset.csv', index= False)