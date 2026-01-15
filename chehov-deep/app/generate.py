from openai import AsyncOpenAI
from confiq import AI_TOKEN
client = AsyncOpenAI(
  base_url = "https://openrouter.ai/api/v1",
  api_key = AI_TOKEN)

async def ai_generate(text: str):
  completion = await client.chat.completions.create(
    model="deepseek/deepseek-v3.2-exp",
    messages=[
      {
        "role": "user",
        "content": text + "Сгенерируй ответ в формате диалога, имитируя стиль переписки А.П. Чехова. Обязательные элементы ответа: Используй вежливую форму обращения («милостивый государь/государыня», «уважаемый») Применяй характерные чеховские речевые обороты («как известно», «между прочим», «не могу не отметить») Включи в текст тонкий юмор и иронию Добавь психологическую глубину, размышления о жизни Используй литературную речь конца XIX века Включи описание бытовых деталей Добавь элементы подтекста Избегай современных слов и выражений. текст не более 100 слов"
      }
    ]
  )
  print(completion)
  return completion.choices[0].message.content