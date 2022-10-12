import json

import tqdm
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer_en2vi = AutoTokenizer.from_pretrained("vinai/vinai-translate-en2vi", src_lang="en_XX")
model_en2vi = AutoModelForSeq2SeqLM.from_pretrained("vinai/vinai-translate-en2vi")


def translate_en2vi(en_text: str) -> str:
    input_ids = tokenizer_en2vi(en_text, return_tensors="pt").input_ids
    output_ids = model_en2vi.generate(
        input_ids,
        do_sample=True,
        top_k=100,
        top_p=0.8,
        decoder_start_token_id=tokenizer_en2vi.lang_code_to_id["vi_VN"],
        num_return_sequences=1,
    )
    vi_text = tokenizer_en2vi.batch_decode(output_ids, skip_special_tokens=True)
    vi_text = " ".join(vi_text)
    return vi_text


# en_text = "I haven't been to a public gym before. When I exercise in a private space, I feel more comfortable."
# print(translate_en2vi(en_text))
#
# en_text = "i haven't been to a public gym before when i exercise in a private space i feel more comfortable"
# print(translate_en2vi(en_text))

data_path = r"C:\Users\admin\Downloads\region_descriptions.json\region_descriptions.json"
data = json.loads(open(data_path, 'r', encoding='utf-8').read())
for item in tqdm.tqdm(data):
    for region in item['regions']:
        txt = region['phrase']
        trans = translate_en2vi(txt)
        region['phrase'] = trans
save_data_path = r'F:\project\python\image_caption\convert_data\vi_region_descriptions.json'
open(save_data_path,'w', encoding='utf-8').write(json.dumps(data))
