"""Câu thần chú khi API có vấn đề — in ra terminal + hiện trên popup đổi nhà cung cấp (pick-provider.sh).

  from spells import spell; spell("openai", "credit")   →  "Credit OpenAI cháy rồi, gọi hồn đứa khác thôi 👻"
  python3 _tools/spells.py openai credit                 (in 1 câu, dùng từ shell)

kind: credit | key | timeout | manual (user tự đọc thần chú để đổi key / nhà cung cấp).
Thêm câu mới: thêm vào SPECIAL (riêng từng nhà) hoặc GENERIC ({P} = tên nhà cung cấp).
"""
import random, sys

NAMES = {"openai": "OpenAI", "gemini": "Gemini", "fal": "fal.ai", "replicate": "Replicate", "cloudflare": "Cloudflare",
         "pollinations": "Pollinations", "huggingface": "Hugging Face", "elevenlabs": "ElevenLabs",
         "topview": "TopView", "higgsfield": "Higgsfield"}

SPECIAL = {
    ("openai", "credit"): ["Credit OpenAI cháy rồi, gọi hồn đứa khác thôi 👻"],
    ("openai", "key"): ["Key OpenAI hết linh rồi, thắp nhang thay key mới 🕯️"],
    ("gemini", "credit"): ["Gemini hết đạn, chuối Nano Banana cũng hết luôn 🍌"],
    ("fal", "credit"): ["fal.ai rụng như lá mùa thu vì hết tiền 🍂"],
    ("replicate", "credit"): ["Replicate hết credit, không nhân bản nổi nữa 🧬"],
    ("cloudflare", "credit"): ["Cloudflare hết suất cơm free hôm nay, mai quay lại nha ☁️"],
    ("pollinations", "credit"): ["Ong Pollinations hết phấn rồi, bay đi nhà khác thôi 🐝"],
    ("huggingface", "credit"): ["Hugging Face tháng này ôm hết nổi rồi 🤗"],
    ("elevenlabs", "credit"): ["ElevenLabs hết hơi, giọng ai cũng khàn rồi 🎙️"],
    ("topview", "credit"): ["TopView hết vé, avatar đình công 🎬"],
    ("higgsfield", "credit"): ["Higgsfield hết xu, máy quay tắt đèn 🎥"],
}
GENERIC = {
    "credit": ["Credit {P} cháy rồi, gọi hồn đứa khác thôi 👻", "{P} cạn ví rồi, ví mình cũng cạn, gọi hồn nhà free đi 🪦",
               "{P} đòi tiền điện, mình dọn sang nhà khác thôi 💸"],
    "key": ["Key {P} hết linh rồi, thắp nhang thay key mới 🕯️", "{P} không nhận mặt mình nữa, đưa key mới cho nó nhớ lại 🔑",
            "Bùa key {P} hết hiệu lực, vẽ bùa mới thôi 📜"],
    "timeout": ["{P} đang ngủ đông, gọi 3 lần không dậy, gọi hồn đứa khác 😴", "{P} đứng hình rồi, cho nó nghỉ, đổi người gánh 🐢",
                "Mạng tới {P} như rùa bò, gọi hồn nhà khác cho nhanh 🛜"],
    "noref": ["{P} không nhìn được ảnh mẫu, nhân vật dễ lạc hồn, gọi nhà khác có mắt 👀",
              "{P} mù ảnh tham chiếu, vẽ là sai mặt liền, đổi nhà thôi 🫥"],
    "manual": ["Triệu hồi nhà cung cấp mới 🔮", "Thắp nhang, gọi hồn provider khác 🕯️", "Đổi bùa, đổi key, đổi vận 🧧"],
}


def spell(provider, kind):
    p = NAMES.get(provider) or (provider or "API").split(":")[-1]  # "custom:together" → "together"
    return random.choice(SPECIAL.get((provider, kind)) or GENERIC.get(kind) or GENERIC["manual"]).format(P=p)


if __name__ == "__main__":
    for _s in (sys.stdout,):
        if hasattr(_s, "reconfigure"): _s.reconfigure(encoding="utf-8")
    print(spell(sys.argv[1] if len(sys.argv) > 1 else "", sys.argv[2] if len(sys.argv) > 2 else "manual"))
