# Voice Profile — [TÊN NHÂN VẬT]

> Dùng file này khi viết voice direction cho ElevenLabs (VO — Claude gen sau "ok 4D") hoặc chọn giọng TopView TTS (UGC — người dùng tự gen theo thẻ).

---

## Core Voice Spec

```yaml
Name: [Tên nhân vật]
Language: English (US)
Accent: [American neutral / Southern / NYC / etc.]
Gender: [Female / Male]
Age feel: [Early 30s / Mid 40s / etc.]
```

---

## Delivery Style

**Pace:** `[Slow / Moderate / Fast]` — ~`[120–150]` wpm  
**Energy level:** `[1–10]` — `[7/10: Enthusiastic nhưng không hype]`  
**Warmth:** `[1–10]` — `[8/10: Warm, like talking to a friend]`

**Characteristic delivery patterns:**
- [VD: Nhấn mạnh key words bằng cách slow down, không raise pitch]
- [VD: Hay dùng pause 0.5s trước khi nói điều quan trọng]
- [VD: Tone đi xuống ở cuối câu — confident, không uptalk]

---

## Filler Words & Natural Speech Patterns

> Thêm vào script để VO ElevenLabs / TopView TTS nghe tự nhiên hơn

```
OK to include:
- "Honestly, ..."
- "I mean, ..."
- "Like, ..."
- "You know what I mean?"
- Brief pause + "Yeah."
- "I was like, wait, this is actually working"

Avoid:
- "Um", "Uh" nhiều lần liên tiếp
- Trailing off cuối câu không rõ ý
```

---

## Voice Direction (ElevenLabs VO / chọn giọng TopView TTS)

```
Voice: Natural American female voice, early 30s, warm and conversational.
Moderate pace (~140 wpm). Genuine enthusiasm — NOT infomercial energy.
Occasional natural pauses. Slight vocal warmth, not breathy.
```

---

## Sample Lines (để test voice consistency)

Dùng những câu này để test nếu switch tool hoặc sau thời gian dài không dùng nhân vật này:

1. *"Okay so I've been using this for about three weeks now, and I genuinely wasn't expecting it to work this fast."*
2. *"Like, I know everyone says that, but hear me out."*
3. *"My skin just... looks different. And I'm someone who's tried everything."*
